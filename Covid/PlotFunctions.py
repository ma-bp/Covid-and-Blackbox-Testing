import pandas as pd
import numpy as np
from tkinter import messagebox
from MatplotlibCharts import Lollipop, TreeMap, DonutChart, AreaChart
import datetime as dt
from Helper.ListOfMonths import ListOfMonths
from Helper.Regions import AllRegions

DataFrame = pd.read_csv('Csv/specimenDate_ageDemographic-unstacked.csv', low_memory=False)

# To select the columns we need
DataFrame = DataFrame[["areaType", "areaCode", "areaName", "date", "newCasesBySpecimenDate-0_59", "newCasesBySpecimenDate-60+"]]

# Get the total cases for each day
DataFrame["newCasesBySpecimenDate-Total"] = (DataFrame["newCasesBySpecimenDate-0_59"] + DataFrame["newCasesBySpecimenDate-60+"])

# Replace all missing values with zero
DataFrame.replace([np.inf, -np.inf], np.nan, inplace=True)
DataFrame.fillna(0, inplace=True)

# Convert date column to datetime object
DataFrame["date"] = pd.to_datetime(DataFrame["date"])

# Percent change in infection rate daily
DataFrame["%changeInfectionRate-Total"] = (DataFrame.groupby("areaName")["newCasesBySpecimenDate-Total"].pct_change() * 100)
DataFrame["%changeInfectionRate-0_59"] = (DataFrame.groupby("areaName")["newCasesBySpecimenDate-0_59"].pct_change() * 100)
DataFrame["%changeInfectionRate-60+"] = (DataFrame.groupby("areaName")["newCasesBySpecimenDate-60+"].pct_change() * 100)

def CheckFormInputs( StartDay, EndDay, StartMonth, EndMonth, StartYear, EndYear ):
    
    try:
        StartDate = dt.datetime( day=int(StartDay),month=int(ListOfMonths()[StartMonth]),year=int(StartYear) )
        EndDate = dt.datetime( day=int(EndDay), month=int(ListOfMonths()[EndMonth]), year=int(EndYear) )  
    except:
        messagebox.showinfo("showinfo", "Looks like you have selected an invalid date, try again")
    
    if StartDate > EndDate:
       return messagebox.showinfo("showinfo", "Oops, Look what you have entered, start date cannot be greater than end date!")
    else:
        return { "StartDate": StartDate, "EndDate" : EndDate }
  

def PlotAreasWithHighestCasesEachDay(StartDay, Month, Year):
    Date = CheckFormInputs(StartDay, EndDay="1", StartMonth=Month, StartYear=Year, EndMonth="December", EndYear="2020")
        
    if type(Date) is dict: 
        StartDate = Date["StartDate"]
        Df = DataFrame.loc[((DataFrame["date"] == StartDate))]
        if(len(Df) <= 0):
            return messagebox.showinfo("showinfo", "No data available for this day")
        
        Df = Df.loc[(Df["areaName"] != "United Kingdom") & (Df["areaName"] != "England")].sort_values(["newCasesBySpecimenDate-Total"],ascending=False)
        Df = Df[["areaName","newCasesBySpecimenDate-Total"]][:10]
        
        
        Title =  "Areas with highest cases for " + StartDay + "/" + Month + "/" + Year 
        colors = np.array(["green","#94D2BD","gold","cyan","blue", "#E9EDC9", "#264653", "#FFB703", "#E6CCB2", "#9B2226"])
        explode = (0.05, 0.05, 0.05, 0.08, 0.05, 0.1, 0.05, 0.05, 0.07, 0.05)
        DonutChart(Title, Df["newCasesBySpecimenDate-Total"], Df["areaName"], colors, explode)
    
def PlotPctChangeInDaily(StartDay, EndDay, StartMonth, EndMonth, StartYear, EndYear, Region):
    Date = CheckFormInputs(StartDay, EndDay, StartMonth, EndMonth, StartYear, EndYear)
    
    if Region not in AllRegions():
        return messagebox.showinfo("showinfo", "Invalid region selected.")
        
    if type(Date) is dict: 
        StartDate = Date["StartDate"]
        EndDate = Date["EndDate"]
        Df = DataFrame.loc[((DataFrame["areaName"] == Region) & (DataFrame["date"] >= StartDate) & (DataFrame["date"] <= EndDate))]
        
        if(len(Df) <= 0):
            return messagebox.showinfo("showinfo", "No data available for this range")
        
        Title =  "Daily and %Change in cases for " + Region + " from " + StartDay + "/" +  StartMonth + "/" + StartYear + " to " + EndDay + "/" + EndMonth + "/" + EndYear
        AreaChart(Title, "%Change in Total Daily Cases", "%Change of Daily Case By Age Group", Df, "date", "%changeInfectionRate-Total", "Total Daily Cases", "%changeInfectionRate-0_59", "%changeInfectionRate-60+", "Cases", Legends=["Age Group 0-59", "Age Group 60+"])
    
    
def PlotAreasWithHighestCasesEachMonth( Month, Year):
    
    Title =  "Total Cases by age group for the month of " + Month + " " + Year
    
    if len(ListOfMonths()[Month]) == 1:
        MonthValue = "0" + ListOfMonths()[Month]
    else:
        MonthValue = ListOfMonths()[Month]
    DataFrame['month'] = pd.to_datetime(DataFrame['date']).dt.to_period('M')
    Df = DataFrame.loc[(DataFrame['month'] == Year + "-" + MonthValue)]
    Df = Df.groupby(["areaName"], as_index=False)[["newCasesBySpecimenDate-0_59", "newCasesBySpecimenDate-60+", "newCasesBySpecimenDate-Total"]].sum()
    Df = Df.loc[(Df["areaName"] != "United Kingdom") & (Df["areaName"] != "England")].sort_values(["newCasesBySpecimenDate-Total"],ascending=False)
    Df = Df[["areaName","newCasesBySpecimenDate-Total"]][:10]
    Labels = Df.apply(lambda x: str(x[0]) + "\n (" + str(x[1]) + ")", axis=1)
    TreeMap(Title, Df["newCasesBySpecimenDate-Total"], Labels )
    
def PlotCompareTwoRegions(StartDay, EndDay, StartMonth, EndMonth, StartYear, EndYear, RegionOne, RegionTwo):
    Date = CheckFormInputs(StartDay, EndDay, StartMonth, EndMonth, StartYear, EndYear)
    if RegionOne == RegionTwo:
        return messagebox.showinfo("showinfo", "You cannot compare same region")
    
    if type(Date) is dict: 
        StartDate = Date["StartDate"]
        EndDate = Date["EndDate"]
        
        Title =  "Total Cases between " + RegionOne + " and " + RegionTwo + " from\n" +" 01/" + StartMonth + "/2020" + " to " + " 31/" + EndMonth + "/" + "2020"
        Df = DataFrame.loc[
            (
                (DataFrame["date"] >= StartDate)
                & (DataFrame["date"] <= EndDate)
            )
        ]
        Df = Df.groupby(["areaName"], as_index=False)[["newCasesBySpecimenDate-0_59", "newCasesBySpecimenDate-60+", "newCasesBySpecimenDate-60+"]].sum()
        Df = Df.loc[(Df['areaName'] == RegionOne) | (Df['areaName'] == RegionTwo)].sort_values(["newCasesBySpecimenDate-0_59", "newCasesBySpecimenDate-60+"],ascending=False)
        Df = Df.reset_index()
        FirstRegion = [Df['newCasesBySpecimenDate-0_59'][0], Df['newCasesBySpecimenDate-60+'][0], Df['newCasesBySpecimenDate-Total'][0]]
        SecondRegion = [Df['newCasesBySpecimenDate-0_59'][1], Df['newCasesBySpecimenDate-60+'][1], Df['newCasesBySpecimenDate-Total'][1]]
        AgeRange = ["0-59", "60+", "Total"]
        
        if(len(Df) <= 0):
            return messagebox.showinfo("showinfo", "No data available for this day")
        
        if len(Df) > 1:
                Lollipop( Title,  FirstRegion,  SecondRegion,  RegionOne,  RegionTwo,  "Number of Cases",  "Age Range",  AgeRange)
