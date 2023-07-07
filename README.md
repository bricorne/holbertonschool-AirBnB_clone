<p align="center">
  <img src="https://github.com/bricorne/holbertonschool-AirBnB_clone/assets/124582867/76c9d1b9-4265-4073-8534-fb088aeb8c5d">
</p>

<h1> AirBnB Clone - The Console</h1>
Creation of a command interpreter in Python using the cmd module, in order to manage the Back-End part. This is the first step towards building your first full web application : The AirBnB Clone.

<h2> Description of the project</h2></p>

-  Put in place a parent class (called BaseModel) to take care of the initialization, serialization and deserialization of your future intances
-  Create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
-  Create all classes used for AirBnB (User, State, City, Place…) that inherit from BaseModel
-  Create the first abstracted storage engine of the project: File storage.
-  Create all unittests to validate all our classes and storage engin.

<h2> What's a command interpreter ?</h2></p>
A command interpreter allows the user to interact with a program using commands in the form of text lines.

-  Create a new object (ex: a new user; a new place...)
-  Retrieve an object in a file, a database etc...
-  Do operations on objects (count, compute stats, etc...)
-  Update attributes of an object
-  Destroy an object

<h2> Execution</h2></p>
Your shell should work like this in interactive mode:

```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```
But also in non-interactive mode: (like the Shell project in C)

```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```

<h2> What we should learn from this project</h2></p>

- How to create a Python package
- How to create a command interpreter in Python using the cmd module
- What is Unit testing and how to implement it in a large project
- How to serialize and deserialize a Class
- How to write and read a JSON file
- How to manage datetime
- What is an UUID
- What is *args and how to use it
- What is **kwargs and how to use it
- How to handle named arguments in a function

<h3> Python Package</h3>
A python package is a collection of modules. Modules that are related to each other are mainly put in the same package. When a module from an external package is required in a program, that package can be imported and its modules can be put to use.
A package is a directory of Python modules that contains an additional __init__.py file, which distinguishes a package from a directory that is supposed to contain multiple Python scripts. Packages can be nested to multiple depths if each corresponding directory contains its own __init__.py file.

<h3> Unit Tests</h3>
Unit testing is a software testing method by which individual units of source code—sets of one or more computer program modules together with associated control data, usage procedures, and operating procedures—are tested to determine whether they are fit for use.

Unit tests must also pass in non-interactive mode: `$ echo "python3 -m unittest discover tests" | bash`

<h3> Serialize & Deserialize</h3>
Serialization is the process of converting a data object a combination of code and data represented within a region of data storage into a series of bytes that saves the state of the object in an easily transmittable form. In this project, we convert the python object to JSON format.

Deserialization is the process of reconstructing a data structure or object from a series of bytes or a string in order to instantiate the object for consumption. Here, the convertion of the JSON format back to python object.

<h3> Write & Read JSON File</h3>
<img src="https://github.com/bricorne/holbertonschool-AirBnB_clone/assets/124582867/0eea4d51-7552-456c-8cf9-77d727d51014">

<h2>Authors</h2></p>

Brice Poitevineau - [@bricorne](https://github.com/bricorne)<br>

Nicolas De Sousa - [@Nico-dsa](https://github.com/Nico-dsa)<br> 
