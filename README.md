# ImportEngine

Let's take a minute to lay the groundwork for our strategy object importer:

Review the file structure and organization of the skeleton code we've provided.
Create a new ImporterInterface abstract class:
This class should implement a can_ingest class method which decides if a file is compatible with the importer.
A parse abstract class method signature which we will realize and fully complete in the children classes that implement the ImporterInterface.


Before implementing our code, we need to install the python-docx library to work with word documents in Python. This library requires a new version of a Python helper module called setuptools. To install the updated helper and the docx library, run:


pip install -U setuptools
pip install python-docx 
Then, we're ready to implement our first strategy object:

Create a new DocxImporter class that inherits ImporterInterface.
Implement the parse method that uses the python-docx library to read import data from a docx file.
Import and use your importer in the run.py file.


Before implementing our code, we need to install the pandas library to work with csv files in python by running:


pip install pandas
Then, we're ready to implement our first strategy object:

Create a new CSVImporter class that inherits ImporterInterface.
Implement the parse method that uses the pandas library to read import data from a csv file.
Import and use your importer in the run.py file


Encapsulation can make our software easy to work with. Refactor your code to:

Include a new Importer class that will encapsulate the CSVImporter and DocxImporter classes. It should realize the ImporterInterface.
Write a parse method that makes a decision for which importer to use based on filetype.
Refactor run.py to consume the Importer class!
