This project was done by **Andrea Pedrosa**, as part of the in course assessment(ICA) for **Software for Digital Innovation**

This GUI application was built using `Python Tkinter` GUI framework and other supporting Python packages pandas, numpy, etc. the list can be found in the requirements.txt file.

`How to launch this GUI application:`
The necessary software tools, packages and their respective versions used for this project need to be installed first. This project supports **Python version 3 upwards**


###### Installation ######

1. ***Python*** :
    To install `python` visit https://www.python.org/downloads/ and download a python interpreter compatible with your device (**Python 3** `is advisable for all users`). For ***Mac*** the in built one is not recommended update to **Python 3**.

2. ***Packages used*** :
    To install the packages used and their respective version which is located in the requirements.txt file. Open the project folder in **Command Prompt** and paste or type the following command `python -m pip install -r requirements.txt`. For **Mac Users** use `python3 -m pip install -r requirements.txt`.

If successfully installed the next step will be to run the application


###### Start the application ######

Open the project folder in **Command Prompt** and type or paste this command `python -m Index`. For **Mac Users** use `python3 -m Index`, this will start the GUI application ![GUI Interface](this should contain an image of the gui interface).


###### Available Visualisations ######

The GUI can be used to check the following visualisations

`Covid -  `

1. Areas with highest cases on a given day
2. %Change in daily cases
3. Areas with high cases on a given month
4. Comparison of two areas

`Stop and Search - `

1. Compare two areas stop and search that resulted in arrest
2. Outcome of stop and search
3. Gender
4. Stop and search result by Age Range that resulted in A no further action disposal
5. Stop and search result by Ethnicity


###### How to run test (Unit and Functional) ######

The `TDD (Testing Driven Development)` paradigm was applied in this project. The unit and functional tests are contained in the **test_Index.py** file. 
*** Before attempting to run tests for the application, all the packages mentioned above must be installed ***

The steps listed below demonstrate how to run the functional tests used for this project and determine the application's test coverage:

1. Run **test_Index.py** file. Open the project folder in **Command Prompt** and type `python -m test_app`. For **Mac** type `python3 -m test_app`, this runs all the test for the GUI application.

2. To check for test coverage, Open the project folder in **Command Prompt** 
    1. We need to first run the tests with coverage, type or paste this command in terminal `python -m coverage run -m unittest discover`. For **Mac** use `python3 -m coverage run -m unittest discover`, this runs all the test for the GUI application and calculates the coverage.
    
    2. To report the coverage in **Command Prompt** type or paste this command `python -m coverage report -m`. For **Mac** use `python3 -m coverage report -m`, this shows the coverage of the tests.



The full details of the Blackbox testing(functional and non-functional) was discussed in the report. Thanks 🙏
