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
    return render_template('category/categories.html',categories = categories)


# add new category
@app.route('/categories/new',methods=['GET','POST'])
def new_category():
    if request.method == 'POST':
        new_category = Category(name=request.form['name'],desc = request.form['desc'])
        session.add(new_category)
        session.commit()
        return redirect(url_for('list_categories'))
    else:
        return render_template('category/new.html')


# edit category
@app.route('/categories/<path:category_name>/edit',methods=['GET','POST'])
def edit_category(category_name):
    edited_category = session.query(Category).filter_by(name=category_name).one()
    if request.method == 'POST':
        edited_category.name = request.form['name']
        edit_category.desc = request.form['desc']
        return redirect(url_for('list_categories'))
    else:
        return render_template('category/edit.html',category = edited_category)


# delete category
@app.route('/categories/<path:category_name>/delete',methods=['GET','POST'])
def delete_category():
    return "delete form will be here"


# //ITEMS ROUTES//

# list all items in category 
@app.route('/categories/<path:category_name>/items')
def list_items():
    return render_template('partials/header.html')


# add new item
@app.route('/categories/new',methods=['GET','POST'])
def new_item():
    return render_template('categories/new.html')


# edit item
@app.route('/items/<path:category_name>/<path:item_name>/edit',methods=['GET','POST'])
def edit_item():
    return render_template('categories/edit.html')


# delete item
@app.route('/items/<path:category_name>/<path:item_name>',methods=['GET','POST'])
def delete_item():
    return "delete form will be here"




if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)