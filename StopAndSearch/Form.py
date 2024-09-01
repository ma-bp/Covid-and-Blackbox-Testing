import tkinter as tk
from Helper.Widgets import TkLabel, TkMenuDropdown
from StopAndSearch.Requests import FetchPoliceForceList
from StopAndSearch.PlotFunctions import PlotTwoAreasStopAndSearchArrestResult, PlotAgeRangeResult, PlotResultOutcome, PlotStopAndSearchByGender, PlotSStopAndSearchByEthnicity
from Helper.DestroyWinfo import DestroyWinfo
from datetime import date
from Helper.ListOfMonths import ListOfMonths

# PoliceForceList
# FetchStopAndSearchCases
CurrentYear = date.today().year
Months = list(ListOfMonths().keys())
Year = [int(CurrentYear), int(CurrentYear) + 1, int(CurrentYear) + 2]

def TwoAreasStopAndSearchArrestResult(Window):
    DestroyWinfo(Window)
    
    TkLabel(Window, "Month", x=240, y=70)
    MonthList = tk.StringVar(Window)
    MonthList.set(Months[0]) 
    TkMenuDropdown(Window, MonthList, Months, x=240, y=95)

    TkLabel(Window, "Year", x=240, y=135)
    YearList = tk.StringVar(Window)
    YearList.set(Year[0])
    TkMenuDropdown(Window, YearList, Year, x=240, y=160)
    
    FirstPoliceForce = list(FetchPoliceForceList().keys())
    TkLabel(Window, "First Police Force", x=240, y=200)
    FirstPoliceForceList = tk.StringVar(Window)
    FirstPoliceForceList.set(FirstPoliceForce[0])
    TkMenuDropdown(Window, FirstPoliceForceList, FirstPoliceForce, x=240, y=225)
    
    SecondPoliceForce = list(FetchPoliceForceList().keys())
    TkLabel(Window, "Second Police Force", x=240, y=265)
    SecondPoliceForceList = tk.StringVar(Window)
    SecondPoliceForceList.set(SecondPoliceForce[1])
    TkMenuDropdown(Window, SecondPoliceForceList, SecondPoliceForce, x=240, y=290)
    
    Func = lambda: PlotTwoAreasStopAndSearchArrestResult(
        MonthList.get(),
        YearList.get(),
        FirstPoliceForceList.get(),
        SecondPoliceForceList.get()
    )
    
    tk.Button(Window, text="View" , command=Func).place(x=240, y=350)
    
def AgeRange(Window):
    DestroyWinfo(Window)
    
    TkLabel(Window, "Month", x=240, y=70)
    MonthList = tk.StringVar(Window)
    MonthList.set(Months[0]) 
    TkMenuDropdown(Window, MonthList, Months, x=240, y=95)
    
    TkLabel(Window, "Year", x=240, y=145)
    YearList = tk.StringVar(Window)
    YearList.set(Year[0])
    TkMenuDropdown(Window, YearList, Year, x=240, y=170)
    
    PoliceForce = list(FetchPoliceForceList().keys())
    TkLabel(Window, "Police Force", x=240, y=225)
    PoliceForceList = tk.StringVar(Window)
    PoliceForceList.set(PoliceForce[0])
    TkMenuDropdown(Window, PoliceForceList, PoliceForce, x=240, y=250)
    
    Func = lambda: PlotAgeRangeResult(
        MonthList.get(),
        YearList.get(),
        PoliceForceList.get(),
    )
    
    tk.Button(Window, text="View" , command=Func).place(x=240, y=320)
    
def Outcome(Window):
    DestroyWinfo(Window)
    
    TkLabel(Window, "Month", x=240, y=70)
    MonthList = tk.StringVar(Window)
    MonthList.set(Months[0]) 
    TkMenuDropdown(Window, MonthList, Months, x=240, y=95)

    TkLabel(Window, "Year", x=240, y=145)
    YearList = tk.StringVar(Window)
    YearList.set(Year[0])
    TkMenuDropdown(Window, YearList, Year, x=240, y=170)
    
    PoliceForce = list(FetchPoliceForceList().keys())
    TkLabel(Window, "Police Force", x=240, y=225)
    PoliceForceList = tk.StringVar(Window)
    PoliceForceList.set(PoliceForce[0])
    TkMenuDropdown(Window, PoliceForceList, PoliceForce, x=240, y=250)
    
    Func = lambda: PlotResultOutcome(
        MonthList.get(),
        YearList.get(),
        PoliceForceList.get(),
    )
    
    tk.Button(Window, text="Outcome" , command=Func).place(x=240, y=320)
    
def StopAndSearchByGender(Window):
    DestroyWinfo(Window)
    
    TkLabel(Window, "Month", x=240, y=70)
    MonthList = tk.StringVar(Window)
    MonthList.set(Months[0]) 
    TkMenuDropdown(Window, MonthList, Months, x=240, y=95)

    TkLabel(Window, "Year", x=240, y=145)
    YearList = tk.StringVar(Window)
    YearList.set(Year[0])
    TkMenuDropdown(Window, YearList, Year, x=240, y=170)
    
    PoliceForce = list(FetchPoliceForceList().keys())
    TkLabel(Window, "Police Force", x=240, y=225)
    PoliceForceList = tk.StringVar(Window)
    PoliceForceList.set(PoliceForce[0])
    TkMenuDropdown(Window, PoliceForceList, PoliceForce, x=240, y=250)
    
    Func = lambda: PlotStopAndSearchByGender(
        MonthList.get(),
        YearList.get(),
        PoliceForceList.get(),
    )
    
    tk.Button(Window, text="View Result" , command=Func).place(x=240, y=320)
    
def StopAndSearchByEthnicity(Window):
    DestroyWinfo(Window)
    
    TkLabel(Window, "Month", x=240, y=70)
    MonthList = tk.StringVar(Window)
    MonthList.set(Months[0]) 
    TkMenuDropdown(Window, MonthList, Months, x=240, y=95)

    TkLabel(Window, "Year", x=240, y=145)
    YearList = tk.StringVar(Window)
    YearList.set(Year[0])
    TkMenuDropdown(Window, YearList, Year, x=240, y=170)
    
    PoliceForce = list(FetchPoliceForceList().keys())
    TkLabel(Window, "Police Force", x=240, y=225)
    PoliceForceList = tk.StringVar(Window)
    PoliceForceList.set(PoliceForce[0])
    TkMenuDropdown(Window, PoliceForceList, PoliceForce, x=240, y=250)
    
    Func = lambda: PlotSStopAndSearchByEthnicity(
        MonthList.get(),
        YearList.get(),
        PoliceForceList.get(),
    )
    
    tk.Button(Window, text="View" , command=Func).place(x=240, y=320)