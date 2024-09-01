import pandas as pd
import pytest
import warnings
from Helper.Widgets import TkLabel, TkMenuDropdown
from Helper.ListOfMonths import ListOfMonths
from Helper.Regions import AllRegions
from Helper.ListOfMonths import ListOfMonths
from StopAndSearch.Requests import FetchPoliceForceList
from StopAndSearch.Form import TwoAreasStopAndSearchArrestResult, AgeRange, Outcome, StopAndSearchByEthnicity, StopAndSearchByGender
from Covid.Form import AreasWithHighestCasesEachDay, PctChangeInDaily, AreasWithHighestCasesEachMonth, CompareTwoRegions
from Covid.PlotFunctions import CheckFormInputs
import unittest

# from StopAndSearch.Requests import FetchStopAndSearchCases
from Index import app

class HelperModules(unittest.TestCase):

    @pytest.mark.asyncio
    # this will start the tkinter window without launching it
    async def _start_app(self):
        self.app.mainloop()

    def setUp(self):
        warnings.filterwarnings("ignore")
        self.app = app()
        self._start_app()

    def tearDown(self):
        self.app.destroy()
    
    ########## this tests verifies if a label from tkinter is returned ##########
    def test_TkLabel(self):
        Label = TkLabel(self.app, "This is a test label", 0, 0).winfo_class()
        self.assertEqual(Label, "Label")
    
    ########## this tests verifies that a Menubutton from tkinter is returned ##########
    def test_TkMenuDropdown(self):
        MenuDropdown = TkMenuDropdown(self.app, 10, ["1", "2"], 0, 0).winfo_class()
        self.assertEqual(MenuDropdown, "Menubutton")
        
    ########## this test checks that a dictionary is returned from the ListOfMonths functions ##########
    def test_ListOfMonths(self):
        Months = ListOfMonths()
        self.assertIsInstance(Months, dict)
        
    ########## this tests if data type is a list ##########
    def test_AllRegions(self):
        RegionList = AllRegions()
        self.assertIsInstance(RegionList, list)
        
class StopAndSearchModule(unittest.TestCase):
    
    async def _start_app(self):
        self.app.mainloop()

    def setUp(self):
        warnings.filterwarnings("ignore")
        self.app = app()
        self._start_app()

    def tearDown(self):
        self.app.destroy()
        
    ########## this tests that the function to fetch police force returns a dictionary
    def testPoliceForceDictionary(self):
        PoliceList = FetchPoliceForceList()
        Type = isinstance(PoliceList, dict)
        self.assertEqual(Type, True)

    # Checks the length of widgets
    def getFormWidgetLength(self, function, expected):
        Form = self.app.winfo_children()[-1]
        function(Form)
        NoOfWidgetsOnForm = len(Form.winfo_children())
        self.assertEqual(NoOfWidgetsOnForm, expected)
        
    # this tests if all widgets; label, Menubutton, button for AreasWithHighestCasesEachDay function renders
    def test_AreasWithHighestCasesEachDay(self): 
        self.getFormWidgetLength(AreasWithHighestCasesEachDay, 7)
        
    # this tests if all widgets; label, Menubutton, button for PctChangeInDaily function renders
    def test_AreasWithHighestCasesEachDay(self): 
        self.getFormWidgetLength(PctChangeInDaily, 15)
        
    # this tests if all widgets; label, Menubutton, button for AreasWithHighestCasesEachMonth function renders
    def test_AreasWithHighestCasesEachMonth(self): 
        self.getFormWidgetLength(AreasWithHighestCasesEachMonth, 5)
        
    # this tests if all widgets; label, Menubutton, button for CompareTwoRegions function renders
    def test_CompareTwoRegions(self): 
        self.getFormWidgetLength(CompareTwoRegions, 17)
        

class CovidModules(unittest.TestCase):

    async def _start_app(self):
        self.app.mainloop()

    def setUp(self):
        warnings.filterwarnings("ignore")
        self.app = app()
        self._start_app()

    def tearDown(self):
        self.app.destroy()
        
    # Checks the length of widgets
    def getFormWidgetLength(self, function, expected):
        Form = self.app.winfo_children()[-1]
        function(Form)
        NoOfWidgetsOnForm = len(Form.winfo_children())
        self.assertEqual(NoOfWidgetsOnForm, expected)
        
    # this tests if all widgets; label, Menubutton, button for TwoAreasStopAndSearchArrestResult function renders
    def test_TwoAreasStopAndSearchArrestResult(self): 
        self.getFormWidgetLength(TwoAreasStopAndSearchArrestResult, 9)
        
    # this tests if all widgets; label, Menubutton, button for AgeRange function renders
    def test_AgeRange(self): 
        self.getFormWidgetLength(AgeRange, 7)
        
    # this tests if all widgets; label, Menubutton, button for Outcome function renders
    def test_Outcome(self): 
        self.getFormWidgetLength(Outcome, 7)
        
    # this tests if all widgets; label, Menubutton, button for StopAndSearchByEthnicity function renders
    def test_StopAndSearchByEthnicity(self): 
        self.getFormWidgetLength(StopAndSearchByEthnicity, 7)
        
    # this tests if all widgets; label, Menubutton, button for TwoAreasStopAndSearchArrestResult function renders
    def test_StopAndSearchByGender(self): 
        self.getFormWidgetLength(StopAndSearchByGender, 7)
        
    # the tests if the CheckFormInputs function returns a dict
    def test_CheckFormInputs(self):
        Date = CheckFormInputs("1", "2", "January", "April", "2020", "2020")
        Type = isinstance(Date, dict)
        self.assertEqual(Type, True)    
        
        Message = "It can only contain start and end date"
        DateLength = len(Date)
        Expected = 2
        
        self.assertEqual(DateLength, Expected, Message)
        

if __name__ == "__main__":
    unittest.main(verbosity=2)