from flask import Flask, render_template, request, redirect, jsonify, url_for
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db_setup import Base, Category, Item


app = Flask(__name__)


engine = create_engine('sqlite:///catalog.db?check_same_thread=False')
Base.metadata.bind = engine


DBSession = sessionmaker(bind=engine)
session = DBSession()


# //CATEGORIES ROUTES//
# list all categories route
@app.route('/')
@app.route('/categories')
def list_categories():
    categories = session.query(Category).all()
    return render_template('category/categories.html', categories=categories)


# add new category
@app.route('/categories/new', methods=['GET', 'POST'])
def new_category():
    if request.method == 'POST':
        new_category = Category(
            name=request.form['name'], desc=request.form['desc'])
        session.add(new_category)
        session.commit()
        return redirect(url_for('list_categories'))
    else:
        return render_template('category/new.html')


# edit category
@app.route('/categories/<path:category_name>/edit', methods=['GET', 'POST'])
def edit_category(category_name):
    edited_category = session.query(
        Category).filter_by(name=category_name).one()
    if request.method == 'POST':
        edited_category.name = request.form['name']
        edit_category.desc = request.form['desc']
        session.add(edited_category)
        session.commit()
        return redirect(url_for('list_categories'))
    else:
        return render_template('category/edit.html', category=edited_category)


# delete category
@app.route('/categories/<path:category_name>/delete', methods=['GET', 'POST'])
def delete_category(category_name):
    deleted_category = session.query(
        Category).filter_by(name=category_name).one()
    if request.method == 'POST':
        session.delete(deleted_category)
        session.commit
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
def new_item(category_name):
    category = session.query(Category).filter_by(name=category_name).one()
    categories = session.query(Category).all()
    if request.method == 'POST':
        new_item = Item(
            name=request.form['name'], desc=request.form['desc'], category_id=category.id)
        session.add(new_item)
        session.commit()
        return redirect(url_for('list_items', category_name=category_name))
    else:
        return render_template('item/new.html', categories=categories, category=category)


# edit item
@app.route('/items/<path:category_name>/<path:item_name>/edit', methods=['GET', 'POST'])
def edit_item(category_name, item_name):
    category = session.query(Category).filter_by(name=category_name).one()
    categories = session.query(Category).all()
    edited_item = session.query(Item).filter_by(name=item_name).one()
    if request.method == 'POST':
        edited_item.name = request.form['name']
        edited_item.desc = request.form['desc']
        edited_item.category_id = request.form['category_id']
        session.add(edited_item)
        session.commit()
        return redirect(url_for('list_items', category_name=category.name))
    else:
        return render_template('item/edit.html', item=edited_item, categories=categories, category=category)

#  show item


@app.route('/items/<path:category_name>/<path:item_name>/show')
def show_item(category_name, item_name):
    category = session.query(Category).filter_by(name=category_name).one()
    item = session.query(Item).filter_by(name=item_name).one()
    return render_template('item/show.html', item=item, category=category)


# delete item
@app.route('/items/<path:category_name>/<path:item_name>', methods=['GET', 'POST'])
def delete_item(category_name, item_name):
    category = session.query(Category).filter_by(name=category_name).one()
    deleted_item = session.query(Item).filter_by(name=item_name).one()
    if request.method == 'POST':
        session.delete(deleted_item)
        session.commit()
        return redirect(url_for('list_items', category_name=category.name))
    else:
        return render_template('item/delete.html',item=deleted_item, category=category)


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
