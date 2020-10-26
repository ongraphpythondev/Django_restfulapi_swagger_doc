# Django_restfulapi_swagger_doc

# Swagger

Swagger is in essence an Interface Description Language for describing RESTful APIs expressed using JSON. Swagger is used together with a set of open-source software tools to design, build, document, and use RESTful web services. Swagger includes automated documentation, code generation, and test-case generation

## Prerequisites:

You will need the following programmes properly installed on your computer.

* [Python](https://www.python.org/) 3.6+

* Virtual Environment

To install virtual environment on your system use:
```bash
apt-get install python3-venv
```

## Installation and Running :

```bash
git clone https://github.com/ongraphpythondev/Django_restfulapi_swagger_doc.git

cd Django_restfulapi_swagger_doc

python3 -m venv venv

source venv/bin/activate

# Install required packages for the project to run
pip install -r requirements.txt

python manage.py migrate

python manage.py runserver

```

Open Browser and Type http://127.0.0.1:8000
