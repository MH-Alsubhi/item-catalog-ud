from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import datetime
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



# Create fake categories
# Category1 = Category(name="Interpreted Programming Languages",desc ='An interpreted language is a programming language for which most of its implementations execute instructions directly, without previously compiling a program into machine-language instructions. The interpreter executes the program directly, translating each statement into a sequence of one or more subroutines already compiled into machine code. (Wikipedia)'
#                      )
# session.add(Category1)
# session.commit()

Category2 = Category(name="Functional Programming Languages",
                      desc='Functional programming languages define every computation as a mathematical evaluation. They focus on the application of functions. Many of the functional programming languages are bound to mathematical calculations.')
session.add(Category2)
session.commit()



print ("Your database has been populated with fake data!")