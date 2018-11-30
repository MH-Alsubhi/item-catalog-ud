from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import datetime
import json
from db_setup import *

engine = create_engine('sqlite:///catalog.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()


data = json.loads(open('data.json', 'r').read())
for entry in data['categories']:
    added_category = Category(
        name=entry['name'], desc=entry['desc'], user_id=entry['user_id'])
    session.add(added_category)
    session.commit()
    print('category {} added'.format(entry['name']))
    for item in entry['items']:
        added_item = Item(name=item['name'],
                    desc=item['desc'], category_id=item['category_id'], user_id=item['user_id'])
        session.add(added_item)
        session.commit()
        print('item {} added'.format(item['name']))
        print('all data entered successfully')