Click Example Application
=========================

Description
-----------

This repository shows the implementation of CLI application based on the framework click (https://github.com/pallets/click).
The implemented sample application provides a rudimentary GIT like command line interface with the commands 'greetings' and 'whoami'.
This example shows some basic capabilities of the click framework.

I implemented also some simple unit tests. These unit tests show how you can test your click application.

In order to show you a possible documentation approach the folder 'docs' contains a Sphinx based documentation of the sample application.
 

How To Install This Example
---------------------------
```
virtualenv -p /usr/bin/python3 venv && source venv/bin/activate

git clone https://github.com/h3nr1-g/Click-Example.git click-demo

cd click-demo && python setup.py install
```

How To Run The Unit Tests
-------------------------
```
cd tests

py.test -v
```

How To Build The Documentation
------------------------------
```
cd docs

make clean && make html

cd _build/html

x-www-browser index.html
```