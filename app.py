#!/usr/bin/env python
from flask import Flask, render_template, request, redirect
from flask import url_for, make_response, flash, session as login_session
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db_setup import Base, Category, Item, User
from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
from functools import wraps
import random
import string
import httplib2
import json
import requests


app = Flask(__name__)


engine = create_engine('sqlite:///catalog.db?check_same_thread=False')
Base.metadata.bind = engine


DBSession = sessionmaker(bind=engine)
session = DBSession()


# is_logged middleware
def is_loggedin(f):
    '''Checks to see whether a user is logged in'''
    @wraps(f)
    def check(*args, **kwargs):
        if 'email' not in login_session:
            flash('Please login first')
            return redirect('/login')
        return f(*args, **kwargs)
    return check


# // AUTH ROUTES //
# login
CLIENT_ID = json.loads(
    open('client_secrets.json', 'r').read())['web']['client_id']

# inject session in all tamplates


@app.context_processor
def inject_session_in_all_templates():
    return dict(login_session=login_session)


@app.route('/login')
def login():
    state = ''.join(random.choice(string.ascii_uppercase + string.digits)
                    for x in range(32))
    login_session['state'] = state
    return render_template('auth/login.html', STATE=state)


# Gconnect route
@app.route('/gconnect', methods=['POST'])
def gconnect():
    # Validate state token
    if request.args.get('state') != login_session['state']:
        response = make_response(json.dumps('Invalid state parameter.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    # Obtain authorization code
    code = request.data

    try:
        # Upgrade the authorization code into a credentials object
        oauth_flow = flow_from_clientsecrets('client_secrets.json', scope='')
        oauth_flow.redirect_uri = 'postmessage'
        credentials = oauth_flow.step2_exchange(code)
    except FlowExchangeError:
        response = make_response(
            json.dumps('Failed to upgrade the authorization code.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    # Check that the access token is valid.
    access_token = credentials.access_token
    url = ('https://www.googleapis.com/oauth2/v1/tokeninfo?access_token=%s'
           % access_token)
    h = httplib2.Http()
    result = json.loads(h.request(url, 'GET')[1])

    # If there was an error in the access token info, abort.
    if result.get('error') is not None:
        response = make_response(json.dumps(result.get('error')), 500)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Verify that the access token is used for the intended user.
    gplus_id = credentials.id_token['sub']
    if result['user_id'] != gplus_id:
        response = make_response(
            json.dumps("Token's user ID doesn't match given user ID."), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Verify that the access token is valid for this app.
    if result['issued_to'] != CLIENT_ID:
        response = make_response(
            json.dumps("Token's client ID does not match app's."), 401)
        print("Token's client ID does not match app's.")
        response.headers['Content-Type'] = 'application/json'
        return response

    stored_access_token = login_session.get('access_token')
    stored_gplus_id = login_session.get('gplus_id')
    if stored_access_token is not None and gplus_id == stored_gplus_id:
        response = make_response(json.dumps(
            'Current user is already connected.'),
            200)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Store the access token in the session for later use.
    login_session['access_token'] = credentials.access_token
    login_session['gplus_id'] = gplus_id

    # Get user info
    userinfo_url = "https://www.googleapis.com/oauth2/v1/userinfo"
    params = {'access_token': credentials.access_token, 'alt': 'json'}
    answer = requests.get(userinfo_url, params=params)

    data = answer.json()
    login_session['email'] = data['email']
    return redirect(url_for('signup'))


# complete signup after auth with googleapis
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    # check if user already in db
    exists = session.query(User).filter_by(
        email=login_session['email']).scalar()
    if request.method == 'POST':
        if request.form['name']:
            new_user = User(name=request.form['name'],
                            email=login_session['email'])
            session.add(new_user)
            session.commit()
            login_session['name'] = new_user.name
            login_session['user_id'] = new_user.id
            flash('Signed up successfully welcome {}'.format(new_user.name))
            return redirect(url_for('list_categories'))
        else:
            flash('Signup failed, there is no name')
            return redirect(url_for('list_categories'))

    # if user already in db
    if exists:
        # get user
        user = session.query(User).filter_by(
            email=login_session['email']).one()
        login_session['name'] = user.name
        login_session['user_id'] = user.id
        flash('Welcome back  {}'.format(user.name))
        return redirect(url_for('list_categories'))
    else:
        # if not direct to signup
        return render_template('auth/signup.html')


@app.route('/gdisconnect')
def gdisconnect():
    # Only disconnect a connected user.
    access_token = login_session.get('access_token')
    if access_token is None:
        response = make_response(
            json.dumps('Current user not connected.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    url = 'https://accounts.google.com/o/oauth2/revoke?token=%s' % access_token
    h = httplib2.Http()
    result = h.request(url, 'GET')[0]
    if result['status'] == '200':
        # Reset the user's sesson.
        del login_session['access_token']
        del login_session['gplus_id']
        del login_session['email']
        del login_session['name']
        del login_session['user_id']

    flash("You are logged out successfully")
    return redirect(url_for('list_categories'))


# //CATEGORIES ROUTES//
# list all categories route


@app.route('/')
@app.route('/categories')
def list_categories():
    categories = session.query(Category).all()
    return render_template('category/categories.html', categories=categories)


# add new category
@app.route('/categories/new', methods=['GET', 'POST'])
@is_loggedin
def new_category():
    if request.method == 'POST':
        if request.form['name'] and request.form['desc']:
            new_category = Category(
                name=request.form['name'],
                desc=request.form['desc'],
                user_id=login_session['user_id'])
            session.add(new_category)
            session.commit()
            flash('Category {} successfully added'.format(new_category.name))
            return redirect(url_for('list_categories'))
        else:
          flash('Category not added, there is no name or description !')
          return redirect(url_for('list_categories'))  
    else:
        return render_template('category/new.html')


# edit category
@app.route('/categories/<path:category_name>/edit', methods=['GET', 'POST'])
@is_loggedin
def edit_category(category_name):
    edited_category = session.query(
        Category).filter_by(name=category_name).one()
    if request.method == 'POST':
        if request.form['name'] and request.form['desc']:
            if edited_category.user_id != login_session['user_id']:
                return 'You are not authorized to edit this category'
            edited_category.name = request.form['name']
            edit_category.desc = request.form['desc']
            session.add(edited_category)
            session.commit()
            flash('Category {} successfully edited'.format(edited_category.name))
            return redirect(url_for('list_categories'))
        else:
            flash('Category not edited, there is no name or description !')
            return redirect(url_for('list_categories')) 
    else:
        return render_template('category/edit.html', category=edited_category)


# delete category
@app.route('/categories/<path:category_name>/delete', methods=['GET', 'POST'])
@is_loggedin
def delete_category(category_name):
    deleted_category = session.query(
        Category).filter_by(name=category_name).one()
    if request.method == 'POST':
        if deleted_category.user_id != login_session['user_id']:
            return 'You are not authorized to delete this category'
        session.delete(deleted_category)
        session.commit()
        flash('Category {} successfully deleted'.format(deleted_category.name))
        return redirect(url_for('list_categories'))

    else:
        return render_template('category/delete.html', category=deleted_category)


# //ITEMS ROUTES//
# list all items in category
@app.route('/categories/<path:category_name>/items')
def list_items(category_name):
    category = session.query(Category).filter_by(name=category_name).one()
    items = session.query(Item).filter_by(category_id=category.id).all()
    return render_template('item/items.html', category=category, items=items)


# add new item
@app.route('/categories/<path:category_name>/items/new', methods=['GET', 'POST'])
@is_loggedin
def new_item(category_name):
    category = session.query(Category).filter_by(name=category_name).one()
    categories = session.query(Category).all()
    if request.method == 'POST':
        if request.form['name'] and request.form['desc']:
            new_item = Item(
                name=request.form['name'], desc=request.form['desc'], category_id=category.id, user_id=login_session['user_id'])
            session.add(new_item)
            session.commit()
            flash('Item {} successfully added'.format(new_item.name))
            return redirect(url_for('list_items', category_name=category_name))
        else:
            flash('Item not added, there is no name or description !')
            return redirect(url_for('list_items', category_name=category_name)) 
    else:
        return render_template('item/new.html', categories=categories, category=category)


# edit item
@app.route('/items/<path:category_name>/<path:item_name>/edit', methods=['GET', 'POST'])
@is_loggedin
def edit_item(category_name, item_name):
    category = session.query(Category).filter_by(name=category_name).one()
    categories = session.query(Category).all()
    edited_item = session.query(Item).filter_by(name=item_name).one()
    if request.method == 'POST':
        if request.form['name'] and request.form['desc']:
            if edited_item.user_id != login_session['user_id']:
                return 'You are not authorized to edit this item'
            edited_item.name = request.form['name']
            edited_item.desc = request.form['desc']
            edited_item.category_id = request.form['category_id']
            session.add(edited_item)
            session.commit()
            flash('Item {} successfully edited'.format(edited_item.name))
            return redirect(url_for('list_items', category_name=category.name))
        else:
            flash('Item not edited, there is no name or description !')
            return redirect(url_for('list_items', category_name=category_name)) 
    else:
        return render_template('item/edit.html', item=edited_item, categories=categories, category=category)

# show item


@app.route('/items/<path:category_name>/<path:item_name>/show')
def show_item(category_name, item_name):
    category = session.query(Category).filter_by(name=category_name).one()
    item = session.query(Item).filter_by(name=item_name).one()
    return render_template('item/show.html', item=item, category=category)


# delete item
@app.route('/items/<path:category_name>/<path:item_name>', methods=['GET', 'POST'])
@is_loggedin
def delete_item(category_name, item_name):
    category = session.query(Category).filter_by(name=category_name).one()
    deleted_item = session.query(Item).filter_by(name=item_name).one()
    if request.method == 'POST':
        if deleted_item.user_id != login_session['user_id']:
            return 'You are not authorized to delete this item'
        session.delete(deleted_item)
        session.commit()
        flash('Item {} successfully edited'.format(deleted_item.name))
        return redirect(url_for('list_items', category_name=category.name))
    else:
        return render_template('item/delete.html', item=deleted_item, category=category)


# // JSON endpoints
# API V1

# categories names list only
@app.route('/api/v1/categories')
def categories_json():
    categories = session.query(Category).all()
    categories_dict = [i.serialize for i in categories]
    return json.dumps(categories_dict)


# categories names with items list
@app.route('/api/v1/categories/items')
def categories_items_json():
    categories = session.query(Category).all()
    category_dict = [c.serialize for c in categories]
    for c in range(len(category_dict)):
        items = [i.serialize for i in session.query(Item).filter_by(
            category_id=category_dict[c]["id"]).all()]
        if items:
            category_dict[c]["Items"] = items
    return json.dumps(category_dict)

# single category info


@app.route('/api/v1/categories/<int:category_id>')
def category_json(category_id):
    category = session.query(Category).filter_by(id=category_id).one()
    category_json = category.serialize
    return json.dumps(category_json)

# single category info with items


@app.route('/api/v1/categories/<int:category_id>/items')
def category_items_json(category_id):
    category = session.query(Category).filter_by(id=category_id).one()
    category_dict = [category.serialize]
    for c in range(len(category_dict)):
        items = [i.serialize for i in session.query(Item).filter_by(
            category_id=category_dict[c]["id"]).all()]
        if items:
            category_dict[c]["Items"] = items
    return json.dumps(category_dict)


# single item info
@app.route('/api/v1/categories/<int:category_id>/items/<int:item_id>')
def item_json(category_id, item_id):
    category = session.query(Category).filter_by(id=category_id).one()
    item = session.query(Item).filter_by(
        category_id=category_id, id=item_id).one()
    category_dict = [category.serialize]
    for c in range(len(category_dict)):
        items = [i.serialize for i in session.query(Item).filter_by(
            category_id=category_dict[c]["id"]).all()]
        if items:
            category_dict[c]["Items"] = items
    return json.dumps(category_dict)


if __name__ == '__main__':
    app.debug = True
    app.secret_key = 'super_secret_key'
    app.run(host='0.0.0.0', port=5000)
