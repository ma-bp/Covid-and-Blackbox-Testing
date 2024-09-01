
import tkinter as tk
from Helper.Widgets import TkLabel, TkMenuDropdown
from Helper.DestroyWinfo import DestroyWinfo
from Helper.Regions import AllRegions
from Covid.PlotFunctions import PlotPctChangeInDaily, PlotAreasWithHighestCasesEachMonth, PlotCompareTwoRegions, PlotAreasWithHighestCasesEachDay
from Helper.ListOfMonths import ListOfMonths

Days = list(range(1, 32))
Months = Months = list(ListOfMonths().keys())
Year = [2020]

def AreasWithHighestCasesEachDay(Window): 
    DestroyWinfo(Window)

    TkLabel(Window, "Day", x=270, y=50)
    StartDay = tk.StringVar(Window)
    StartDay.set(Days[0]) 
    TkMenuDropdown(Window, StartDay, Days, x=270, y=70)
    
    TkLabel(Window, "Month Day", x=270, y=120)
    Month = tk.StringVar(Window)
    Month.set(Months[3])
    TkMenuDropdown(Window, Month, Months, x=270, y=140)
    
    TkLabel(Window, "Year", x=270, y=190)
    YearArr = tk.StringVar(Window)
    YearArr.set(Year[0])
    TkMenuDropdown(Window, YearArr, Year, x=270, y=210)
    
    
    Func = lambda: PlotAreasWithHighestCasesEachDay(
        StartDay.get(),
        Month.get(),
        YearArr.get(),
    )
    
    tk.Button(Window, text="View" , command=Func).place(x=270, y=280)
    
def PctChangeInDaily(Window):
    # Clear previous window information before rendering new ones
    DestroyWinfo(Window)
    TkLabel(Window, "Start Day", x=180, y=50)
    StartDay = tk.StringVar(Window)
    StartDay.set(Days[0]) 
    TkMenuDropdown(Window, StartDay, Days, x=180, y=70)
    
    TkLabel(Window, "End Day", x=370, y=50)
    EndDay = tk.StringVar(Window)
    EndDay.set(Days[1])
    TkMenuDropdown(Window, EndDay, Days, x=370, y=70)
    
    TkLabel(Window, "Start Month", x=180, y=120)
    StartMonth = tk.StringVar(Window)
    StartMonth.set(Months[2])
    TkMenuDropdown(Window, StartMonth, Months, x=180, y=140)
    
    TkLabel(Window, "End Month", x=370, y=120)
    EndMonth = tk.StringVar(Window)
    EndMonth.set(Months[3])
    TkMenuDropdown(Window, EndMonth, Months, x=370, y=140)
    
    TkLabel(Window, "Start Year", x=180, y=190)
    StartYear = tk.StringVar(Window)
    StartYear.set(Year[0])
    TkMenuDropdown(Window, StartYear, Year, x=180, y=210)
    
    TkLabel(Window, "End Year", x=370, y=190)
    EndYear = tk.StringVar(Window)
    EndYear.set(Year[0])
    TkMenuDropdown(Window, EndYear, Year, x=370, y=210)
    
    Regions = tk.StringVar(Window)
    Regions.set(AllRegions()[0])
    TkLabel(Window, text="Select region: ", x=270, y=260)
    TkMenuDropdown(Window, Regions, AllRegions(), x=250, y=280)
    
    Func = lambda: PlotPctChangeInDaily(
        StartDay.get(),
        EndDay.get(),
        StartMonth.get(),
        EndMonth.get(),
        StartYear.get(),
        EndYear.get(),
        Regions.get()
    )
    
    tk.Button(Window, text="View" , command=Func).place(x=280, y=340)

def AreasWithHighestCasesEachMonth(Window):
    DestroyWinfo(Window)
        
    TkLabel(Window, "Month", x=270, y=50)
    Month = tk.StringVar(Window)
    Month.set(Months[3])
    TkMenuDropdown(Window, Month, Months, x=270, y=70)
    
    TkLabel(Window, "Year", x=270, y=140)
    YearArr = tk.StringVar(Window)
    YearArr.set(Year[0])
    TkMenuDropdown(Window, YearArr, Year, x=270, y=160)
    
    Func = lambda: PlotAreasWithHighestCasesEachMonth(
        Month.get(),
        YearArr.get(),
    )
    
    tk.Button(Window, text="View" , command=Func).place(x=270, y=230)
    

def CompareTwoRegions(Window):
    DestroyWinfo(Window)
    TkLabel(Window, "Start Day", x=180, y=50)
    StartDay = tk.StringVar(Window)
    StartDay.set(Days[0]) 
    TkMenuDropdown(Window, StartDay, Days, x=180, y=70)
    
    TkLabel(Window, "End Day", x=370, y=50)
    EndDay = tk.StringVar(Window)
    EndDay.set(Days[1])
    TkMenuDropdown(Window, EndDay, Days, x=370, y=70)
    
    TkLabel(Window, "Start Month", x=180, y=120)
    StartMonth = tk.StringVar(Window)
    StartMonth.set(Months[2])
    TkMenuDropdown(Window, StartMonth, Months, x=180, y=140)
    
    TkLabel(Window, "End Month", x=370, y=120)
    EndMonth = tk.StringVar(Window)
    EndMonth.set(Months[3])
    TkMenuDropdown(Window, EndMonth, Months, x=370, y=140)
    
    TkLabel(Window, "Start Year", x=180, y=190)
    StartYear = tk.StringVar(Window)
    StartYear.set(Year[0])
    TkMenuDropdown(Window, StartYear, Year, x=180, y=210)
    
    TkLabel(Window, "End Year", x=370, y=190)
    EndYear = tk.StringVar(Window)
    EndYear.set(Year[0])
    TkMenuDropdown(Window, EndYear, Year, x=370, y=210)
    
    TkLabel(Window, "First Region", x=180, y=260)
    FirstRegion = tk.StringVar(Window)
    FirstRegion.set(AllRegions()[0])
    TkMenuDropdown(Window, FirstRegion, AllRegions(), x=180, y=280)
    
    TkLabel(Window, "Second Region", x=370, y=260)
    SecondRegion = tk.StringVar(Window)
    SecondRegion.set(AllRegions()[1])
    TkMenuDropdown(Window, SecondRegion, AllRegions(), x=370, y=280)
    
    
    Func = lambda: PlotCompareTwoRegions(
        StartDay.get(),
        EndDay.get(),
        StartMonth.get(),
        EndMonth.get(),
        StartYear.get(),
        EndYear.get(),
        FirstRegion.get(),
        SecondRegion.get()
    )
    
    tk.Button(Window, text="View" , command=Func).place(x=290, y=340)