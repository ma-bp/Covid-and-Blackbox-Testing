from tkinter import messagebox
import pandas as pd
from StopAndSearch.Requests import FetchStopAndSearchCases
from Helper.ListOfMonths import ListOfMonths
import numpy as np
from MatplotlibCharts import LollipopChart, BarChart, ScatteredPlot, PieChart, GroupBarChart
 

def FetchRequestAndValidate(month, year, selected_police_force):
    date = year + "-" + ListOfMonths()[month]
    # This list contains two items, the data and the length
    result = FetchStopAndSearchCases(selected_police_force, date)[1]
    if result == []:
        return messagebox.showinfo("showinfo", "No data for this selected month")
    else: 
        return result


def PlotTwoAreasStopAndSearchArrestResult(Month, Year, FirstPoliceForceSelected, SecondPoliceForceSelected):
    if FirstPoliceForceSelected == SecondPoliceForceSelected:
        return messagebox.showinfo("showinfo", "You cannot compare same police force result")
    # Fetch result for the two different police force
    DfFirst = pd.DataFrame.from_dict(FetchRequestAndValidate(Month, Year, FirstPoliceForceSelected))
    FirstResult = DfFirst.groupby(["age_range"], as_index=False)[["involved_person"]].count()
    
    DfSecond = pd.DataFrame.from_dict(FetchRequestAndValidate(Month, Year, SecondPoliceForceSelected))
    SecondResult = DfSecond.groupby(["age_range"], as_index=False)[["involved_person"]].count()
    # Include the result of the second into the first
    FirstResult["involved_person_for_second_region"] = SecondResult["involved_person"]
    # Replace all missing values with zero
    FirstResult.replace([np.inf, -np.inf], np.nan, inplace=True)
    FirstResult.fillna(0, inplace=True)
    Title = "Comparison between \nfor " + FirstPoliceForceSelected + " and " + SecondPoliceForceSelected + " in " + Month + ", " + Year
    
    GroupBarChart(Title, FirstResult, "age_range", "Cases", [FirstPoliceForceSelected, SecondPoliceForceSelected])
    
def PlotAgeRangeResult(Month, Year, SelectedPoliceForce):
    Df = pd.DataFrame.from_dict(FetchRequestAndValidate(Month, Year, SelectedPoliceForce))
    Df = Df.loc[Df['outcome'] == "A no further action disposal"]
    Df = Df.reset_index()
    Result = Df.groupby(["age_range"], as_index=False)[["involved_person"]].count()
    Title = "Stop and search cases by age range \n for " + SelectedPoliceForce + " in " + Month + ", " + Year
    if len(Result["involved_person"]) == 4:
        Colors = np.array(["#94D2BD","gold", "#FFB703", "#E6CCB2"])
    elif len(Result["involved_person"]) == 5:
        Colors = np.array(["#94D2BD","gold", "#FFB703", "#E6CCB2", "#9B2226"])
    
def PlotResultOutcome(Month, Year, SelectedPoliceForce):
    Df = pd.DataFrame.from_dict(FetchRequestAndValidate(Month, Year, SelectedPoliceForce))
    Result = Df.groupby(['outcome'], as_index=False).count()
    print(Result)
    Title = "Outcome of Stop and Search Cases by " + SelectedPoliceForce + " in " + Month + ", " + Year
    
    BarChart(Title, Result, Result["involved_person"], Result["outcome"] )
    
def PlotStopAndSearchByGender(Month, Year, SelectedPoliceForce):
    Df = pd.DataFrame.from_dict(FetchRequestAndValidate(Month, Year, SelectedPoliceForce))
    Result = Df.groupby(['gender'], as_index=False).count()
    # Result = Result.reset_index()
    Title = "Stop and search cases by gender \n for " + SelectedPoliceForce + " in " + Month + ", " + Year
    MaxValue=Result.max()
    # Gets the max value in the data
    Max = MaxValue['involved_person'] 
    
    LollipopChart(Result.index, Result["involved_person"], Result["gender"], Max, Title=Title, Data=Result)
    
def PlotSStopAndSearchByEthnicity(Month, Year, SelectedPoliceForce):
    Df = pd.DataFrame.from_dict(FetchRequestAndValidate(Month, Year, SelectedPoliceForce))
    Result = Df.groupby(["officer_defined_ethnicity"], as_index=False)[["involved_person"]].count()
    Title = "Stop and Search Cases Breakdown by Ethnicity \nfor " + SelectedPoliceForce + " in " + Month + ", " + Year

    PieChart(Title, Result["involved_person"], Result["officer_defined_ethnicity"])