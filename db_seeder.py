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




# Category1 = Category(name="Interpreted Programming Languages",desc ='An interpreted language is a programming language for which most of its implementations execute instructions directly, without previously compiling a program into machine-language instructions. The interpreter executes the program directly, translating each statement into a sequence of one or more subroutines already compiled into machine code. (Wikipedia)'
#                      )
# session.add(Category1)
# session.commit()

# Category2 = Category(name="Functional Programming Languages",
#                       desc='Functional programming languages define every computation as a mathematical evaluation. They focus on the application of functions. Many of the functional programming languages are bound to mathematical calculations.')
# session.add(Category2)
# session.commit()

# item_1 = Item(name="APL",
#                       desc='Named after the book A Programming Language (Iverson, Kenneth E., 1962), APL is an array programming language. It can work simultaneously on multiple arrays of data. It is interpretive, interactive and a functional programming language.', category_id = 1)
# session.add(item_1)
# session.commit()

# item_2 = Item(name="AutoIt",
#                       desc='It is a freeware automation language for Microsoft Windows. It’s main intent is to create automation scripts that can be used for the execution of certain repetitive tasks on Windows.', category_id = 1)
# session.add(item_2)
# session.commit()

# item_3 = Item(name="BASIC",
#                       desc='Developed by John George Kemeny and Thomas Eugene Kurtz at Dartmouth in 1964, it is an acronym for Beginner’s All-purpose Symbolic Instruction Code. It was designed with the intent of giving the non-science people an access to computers.', category_id = 1)
# session.add(item_3)
# session.commit()



print ("Your database has been populated with fake data!")