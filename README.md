# Item catalog project 
## Item catalog is an application that provides a list of items within a variety of categories as well as provide a user registration and authentication system. Registered users will have the ability to post, edit and delete their own items.
### For this project i will list programming languages and divided them into categories.



### Instructions:-
 1. Clone or direct download [item-catalog-ud](https://github.com/MH-Alsubhi/item-catalog-ud) repository.
 2. Cd to app folder using `cd/item-catalog-ud`.
 3. Run `pip install -r requirements.txt` to install all requirement.
 4. Get [credentials](https://developers.google.com/identity/protocols/OpenIDConnect#getcredentials) from google, follow the guide and add `http://localhost:5000` to 'Authorized JavaScript origins' and `http://localhost:5000/login` , `http://localhost:5000/gconnect` to Authorized redirect URIs, then download credentials(client_secrets) as `json` file.
 5. Rename downloaded file to `client_secrets.json` and place it inside app folder `item-catalog-ud`.
 6. Run `python db_setup.py` command to create database.
 7. Run `python db_seeder.py` command to fill database with starter data.
 8. Run `python app.py` to start the app.
 9. Visit `localhost:5000` in your browser. 
 
 
 ### API V1 endpoints:-
 - `/api/v1/categories` 
 Expected response :-
```
[

-   {
    
    -   id:  1,
        
    -   name:  "Interpreted Programming Languages",
        
    -   desc:  "An interpreted language is a programming language for which most of its implementations execute instructions directly, without previously compiling a program into machine-language instructions. The interpreter executes the program directly, translating each statement into a sequence of one or more subroutines already compiled into machine code. (Wikipedia)"
        
    
    },
    
-   {
    
    -   id:  2,
        
    -   name:  "Functional Programming Languages",
        
    -   desc:  "Functional programming languages define every computation as a mathematical evaluation. They focus on the application of functions. Many of the functional programming languages are bound to mathematical calculations."
        
    
    },
    
-   {
    
    -   id:  3,
        
    -   name:  "Compiled Programming Languages",
        
    -   desc:  "A compiled language is a programming language whose implementations are typically compilers (translators that generate machine code from source code), and not interpreters (step-by-step executors of source code, where no pre-runtime translation takes place). (Wikipedia)"
        
    
    }
    

]
```


 - `/api/v1/categories/items`
 Expected response :-
 ```
[

-   {
    
    -   id:  1,
        
    -   name:  "Interpreted Programming Languages",
        
    -   desc:  "An interpreted language is a programming language for which most of its implementations execute instructions directly, without previously compiling a program into machine-language instructions. The interpreter executes the program directly, translating each statement into a sequence of one or more subroutines already compiled into machine code. (Wikipedia)",
        
    -   Items:
        
        [
        
        -   {
            
            -   id:  1,
                
            -   name:  "APL",
                
            -   desc:  "Named after the book A Programming Language (Iverson, Kenneth E., 1962), APL is an array programming language. It can work simultaneously on multiple arrays of data. It is interpretive, interactive and a functional programming language."
                
            
            },
            
        -   {
            
            -   id:  2,
                
            -   name:  "BASIC",
                
            -   desc:  "Developed by John George Kemeny and Thomas Eugene Kurtz at Dartmouth in 1964, it is an acronym for Beginnerâ€™s All-purpose Symbolic Instruction Code. It was designed with the intent of giving the non-science people an access to computers."
                
            
            },
            
        -   {
            
            -   id:  3,
                
            -   name:  "Eiffel",
                
            -   desc:  "It is an object-oriented programming language that is ISO-standardized and used to develop extensible and reusable software. It is a development platform for many industries such as finance, aerospace and video gaming."
                
            
            },
            
        -   {
            
            -   id:  4,
                
            -   name:  "Forth",
                
            -   desc:  "It is a structured imperative programming language, which bases its implementation on stacks. It supports an interactive execution of commands as well as the compilation of sequences of commands."
                
            
            },
            
        -   {
            
            -   id:  5,
                
            -   name:  "Game Maker Language",
                
            -   desc:  "It is an interpreted computer programming language intended to be used in cooperation with Game Maker, an application for game creation. Mark Overmars, a Dutch computer scientist, designed this language."
                
            
            },
            
        -   {
            
            -   id:  6,
                
            -   name:  "Frink",
                
            -   desc:  "Developed by Alan Eliasen and named after Professor John Frink, a popular fictional character. It is based on the Java Virtual Machine and focuses on science and engineering. Its striking feature is that it tracks the units of measure through all the calculations that enables quantities to contain their units of measurement."
                
            
            },
            
        -   {
            
            -   id:  7,
                
            -   name:  "ICI",
                
            -   desc:  "Designed by Tim Long in 1992, ICI is a general purpose interpreted computer programming language. It supports dynamic typing, flexible data types and other language constructs similar to C."
                
            
            },
            
        -   {
            
            -   id:  8,
                
            -   name:  "J",
                
            -   desc:  "Ken Iverson and Roger Hui developed this programming language that requires only the basic ASCII character set. It is an array programming language that works well with mathematical and statistical operations."
                
            
            },
            
        -   {
            
            -   id:  9,
                
            -   name:  "Lisp",
                
            -   desc:  "Lisp is the second-oldest high-level programming language in widespread use today. The name Lisp is derived from â€˜List Processing Languageâ€™. One of the important data structures that Lisp supports is linked list. Lisp programs deal with source code as a data structure."
                
            
            }
            
        
        ]
        
    
    },
    
-   {
    
    -   id:  2,
        
    -   name:  "Functional Programming Languages",
        
    -   desc:  "Functional programming languages define every computation as a mathematical evaluation. They focus on the application of functions. Many of the functional programming languages are bound to mathematical calculations.",
        
    -   Items:
        
        [
        
        -   {
            
            -   id:  10,
                
            -   name:  "Charity",
                
            -   desc:  "It is a purely functional, not-Turing-complete language, which means that all its programs are guaranteed to terminate. Charity was designed at the University of Calgary, a public University in Canada."
                
            
            },
            
        -   {
            
            -   id:  11,
                
            -   name:  "Clean",
                
            -   desc:  "It is a purely functional programming language that supports portability across platforms, automatic garbage collection, multiple data structures and referential transparency, which means that a function with a given input will always give the same output"
                
            
            },
            
        -   {
            
            -   id:  12,
                
            -   name:  "Curry",
                
            -   desc:  "It is a functional logic programming language that implements functional and logic programming as well as constraint programming, wherein the relationships between variables are stated in the form of constraints"
                
            
            }
            
        
        ]
        
    
    },
    
-   {
    
    -   id:  3,
        
    -   name:  "Compiled Programming Languages",
        
    -   desc:  "A compiled language is a programming language whose implementations are typically compilers (translators that generate machine code from source code), and not interpreters (step-by-step executors of source code, where no pre-runtime translation takes place). (Wikipedia)",
        
    -   Items:
        
        [
        
        -   {
            
            -   id:  13,
                
            -   name:  "Ada",
                
            -   desc:  "It is a statically typed, structured, imperative programming language that is based on Pascal. A team of CII Honeywell Bull that was led by Jean Ichbiah developed Ada. The Ada compilers are validated for mission-critical systems. Ada is an internationally standardized computer programming language."
                
            
            }
            
        
        ]
        
    
    }
    

]
```

- `/api/v1/categories/<int:category_id>`
Expected response :-
```
{

-   id:  1,
    
-   name:  "Interpreted Programming Languages",
    
-   desc:  "An interpreted language is a programming language for which most of its implementations execute instructions directly, without previously compiling a program into machine-language instructions. The interpreter executes the program directly, translating each statement into a sequence of one or more subroutines already compiled into machine code. (Wikipedia)"
    

}
```


- `/api/v1/categories/<int:category_id>/items`
Expected response :-
```
[

-   {
    
    -   id:  1,
        
    -   name:  "Interpreted Programming Languages",
        
    -   desc:  "An interpreted language is a programming language for which most of its implementations execute instructions directly, without previously compiling a program into machine-language instructions. The interpreter executes the program directly, translating each statement into a sequence of one or more subroutines already compiled into machine code. (Wikipedia)",
        
    -   Items:
        
        [
        
        -   {
            
            -   id:  1,
                
            -   name:  "APL",
                
            -   desc:  "Named after the book A Programming Language (Iverson, Kenneth E., 1962), APL is an array programming language. It can work simultaneously on multiple arrays of data. It is interpretive, interactive and a functional programming language."
                
            
            },
            
        -   {
            
            -   id:  2,
                
            -   name:  "BASIC",
                
            -   desc:  "Developed by John George Kemeny and Thomas Eugene Kurtz at Dartmouth in 1964, it is an acronym for Beginnerâ€™s All-purpose Symbolic Instruction Code. It was designed with the intent of giving the non-science people an access to computers."
                
            
            },
            
        -   {
            
            -   id:  3,
                
            -   name:  "Eiffel",
                
            -   desc:  "It is an object-oriented programming language that is ISO-standardized and used to develop extensible and reusable software. It is a development platform for many industries such as finance, aerospace and video gaming."
                
            
            },
            
        -   {
            
            -   id:  4,
                
            -   name:  "Forth",
                
            -   desc:  "It is a structured imperative programming language, which bases its implementation on stacks. It supports an interactive execution of commands as well as the compilation of sequences of commands."
                
            
            },
            
        -   {
            
            -   id:  5,
                
            -   name:  "Game Maker Language",
                
            -   desc:  "It is an interpreted computer programming language intended to be used in cooperation with Game Maker, an application for game creation. Mark Overmars, a Dutch computer scientist, designed this language."
                
            
            },
            
        -   {
            
            -   id:  6,
                
            -   name:  "Frink",
                
            -   desc:  "Developed by Alan Eliasen and named after Professor John Frink, a popular fictional character. It is based on the Java Virtual Machine and focuses on science and engineering. Its striking feature is that it tracks the units of measure through all the calculations that enables quantities to contain their units of measurement."
                
            
            },
            
        -   {
            
            -   id:  7,
                
            -   name:  "ICI",
                
            -   desc:  "Designed by Tim Long in 1992, ICI is a general purpose interpreted computer programming language. It supports dynamic typing, flexible data types and other language constructs similar to C."
                
            
            },
            
        -   {
            
            -   id:  8,
                
            -   name:  "J",
                
            -   desc:  "Ken Iverson and Roger Hui developed this programming language that requires only the basic ASCII character set. It is an array programming language that works well with mathematical and statistical operations."
                
            
            },
            
        -   {
            
            -   id:  9,
                
            -   name:  "Lisp",
                
            -   desc:  "Lisp is the second-oldest high-level programming language in widespread use today. The name Lisp is derived from â€˜List Processing Languageâ€™. One of the important data structures that Lisp supports is linked list. Lisp programs deal with source code as a data structure."
                
            
            }
            
        
        ]
        
    
    }
    

]
```

- `/api/v1/categories/<int:category_id>/items/<int:item_id>`
Expected response :-
```
[

-   {
    
    -   id:  1,
        
    -   name:  "Interpreted Programming Languages",
        
    -   desc:  "An interpreted language is a programming language for which most of its implementations execute instructions directly, without previously compiling a program into machine-language instructions. The interpreter executes the program directly, translating each statement into a sequence of one or more subroutines already compiled into machine code. (Wikipedia)",
        
    -   Items:
        
        [
        
        -   {
            
            -   id:  1,
                
            -   name:  "APL",
                
            -   desc:  "Named after the book A Programming Language (Iverson, Kenneth E., 1962), APL is an array programming language. It can work simultaneously on multiple arrays of data. It is interpretive, interactive and a functional programming language."
                
            
            },
            
        -   {
            
            -   id:  2,
                
            -   name:  "BASIC",
                
            -   desc:  "Developed by John George Kemeny and Thomas Eugene Kurtz at Dartmouth in 1964, it is an acronym for Beginnerâ€™s All-purpose Symbolic Instruction Code. It was designed with the intent of giving the non-science people an access to computers."
                
            
            },
            
        -   {
            
            -   id:  3,
                
            -   name:  "Eiffel",
                
            -   desc:  "It is an object-oriented programming language that is ISO-standardized and used to develop extensible and reusable software. It is a development platform for many industries such as finance, aerospace and video gaming."
                
            
            },
            
        -   {
            
            -   id:  4,
                
            -   name:  "Forth",
                
            -   desc:  "It is a structured imperative programming language, which bases its implementation on stacks. It supports an interactive execution of commands as well as the compilation of sequences of commands."
                
            
            },
            
        -   {
            
            -   id:  5,
                
            -   name:  "Game Maker Language",
                
            -   desc:  "It is an interpreted computer programming language intended to be used in cooperation with Game Maker, an application for game creation. Mark Overmars, a Dutch computer scientist, designed this language."
                
            
            },
            
        -   {
            
            -   id:  6,
                
            -   name:  "Frink",
                
            -   desc:  "Developed by Alan Eliasen and named after Professor John Frink, a popular fictional character. It is based on the Java Virtual Machine and focuses on science and engineering. Its striking feature is that it tracks the units of measure through all the calculations that enables quantities to contain their units of measurement."
                
            
            },
            
        -   {
            
            -   id:  7,
                
            -   name:  "ICI",
                
            -   desc:  "Designed by Tim Long in 1992, ICI is a general purpose interpreted computer programming language. It supports dynamic typing, flexible data types and other language constructs similar to C."
                
            
            },
            
        -   {
            
            -   id:  8,
                
            -   name:  "J",
                
            -   desc:  "Ken Iverson and Roger Hui developed this programming language that requires only the basic ASCII character set. It is an array programming language that works well with mathematical and statistical operations."
                
            
            },
            
        -   {
            
            -   id:  9,
                
            -   name:  "Lisp",
                
            -   desc:  "Lisp is the second-oldest high-level programming language in widespread use today. The name Lisp is derived from â€˜List Processing Languageâ€™. One of the important data structures that Lisp supports is linked list. Lisp programs deal with source code as a data structure."
                
            
            }
            
        
        ]
        
    
    }
    

]
```

### Future plans:-

 - [ ] Limiting api calls.
 - [x] Improve UI.
 - ~~[ ] Add sign-in using Facebook.~~
 - [ ] Document api using [Postman](https://www.getpostman.com/).
 - [x] Deploy app to linux server.
