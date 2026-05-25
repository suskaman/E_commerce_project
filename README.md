# About the project "E_commerce_project"
## Description:
Project "E_commerce_project"

## Installation:
1. Clone the repository:

```
git clone https://github.com/suskaman/E_commerce_project.git
```

2. Install requirements:

```
   pip install -r requirements.txt
```
3. Change git remote url to avoid accidental pushes to base project:
```
git remote set-url origin github_username/repo_name
git remote -v # confirm the changes
```
## Usage example
This application is under developing

## logging
The project write a logs into directory 'logs'.
* The default log level is DEBUG for all of them.
* Format for console: [YYYY-MM-DD HH:mm:ss] | levelname | funcName | name | message
* Format for file: [YYYY-MM-DD HH:mm:ss] | levelname | name | filename:lineno | funcName | message


## Testing of a modules
All code of this project are testing on the package **'tests'**.
Module **conftest.py** has a fixtures for test modules.

* There are tests for the module **'catalog.py'** in the module **'test_catalog.py'**.
A correct work of classes **'Product'** and **'Category'** is checked with **'pytest.fixture'**.
For more information look at the **tests/test_catalog.py**

* There are tests for the module **'utils.py'** in the module **'test_utils.py'**.
A correct work of functions **'get_category_from_json'** and **'get_product_from_json'** is checked for type and emptiness.
For more information look at the **tests/test_utils.py**


**For start tests use this command in the terminal**:
```
pytest tests
```

## License
Distributed under the Unlicense License. See License.txt for more information