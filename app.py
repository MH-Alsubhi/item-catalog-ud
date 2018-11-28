from flask import Flask, render_template, request, redirect, jsonify, url_for
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db_setup import Base, Category, Item


app = Flask(__name__)


engine = create_engine('sqlite:///catalog.db')
Base.metadata.bind = engine


DBSession = sessionmaker(bind=engine)
session = DBSession()


# //CATEGORIES ROUTES// 
# list all categories route 
@app.route('/')
@app.route('/categories')
def list_categories():
    return render_template('category/categories.html')


# add new category
@app.route('/categories/new',methods=['GET','POST'])
def new_category():
    return render_template('item/items.html')


# edit category
@app.route('/categories/<path:category_name>/edit',methods=['GET','POST'])
def edit_category():
    return render_template('categories/edit.html')


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