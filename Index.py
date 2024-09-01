from tkinter import ttk
import tkinter as tk
from Covid.Form import AreasWithHighestCasesEachDay, PctChangeInDaily, AreasWithHighestCasesEachMonth, CompareTwoRegions
from StopAndSearch.Form import TwoAreasStopAndSearchArrestResult, AgeRange, Outcome, StopAndSearchByEthnicity, StopAndSearchByGender

def app():

    root = tk.Tk()
    root.geometry("900x700")
    root.title("C2526502's element 2")

    tabControl = ttk.Notebook(root)
    Covid = tk.Frame(tabControl)
    StopAndSearch = tk.Frame(tabControl)

    tabControl.add(Covid, text="Covid")
    tabControl.add(StopAndSearch, text="Stop and Search")
    tabControl.pack(expand=1, fill="both")
 
    tk.Button(Covid, text="Areas with highest cases on a given day" , command= lambda: AreasWithHighestCasesEachDay(CovidForm)).place(x=170, y=60)
    tk.Button(Covid, text= "%Change in daily cases", command=lambda: PctChangeInDaily(CovidForm)).place(x=450, y=60)
    tk.Button(Covid, text="Areas with high cases on a given month" , command=lambda: AreasWithHighestCasesEachMonth(CovidForm)).place(x=170, y=90)
    # tk.Button(Covid, text="Total number of cases each month" , command=lambda: AreasWithHighestCasesEachMonth(CovidForm)).place(x=170, y=90)
    tk.Button(Covid, text= "Comparison of two areas", command=lambda: CompareTwoRegions(CovidForm)).place(x=450, y=90) 
    
    tk.Button(StopAndSearch, text="Compare two areas stop and search that resulted in arrest" , command=lambda: TwoAreasStopAndSearchArrestResult(StopAndSearchForm)).place(x=20, y=60)
    tk.Button(StopAndSearch, text="Outcome of stop and search",command=lambda: Outcome(StopAndSearchForm)).place(x=420, y=60)
    tk.Button(StopAndSearch, text="Gender" , command=lambda: StopAndSearchByGender(StopAndSearchForm)).place(x=650, y=60)
    tk.Button(StopAndSearch, text="Stop and search result by Age Range that resulted in A no further action disposal" , command=lambda: AgeRange(StopAndSearchForm)).place(x=20, y=95)
    tk.Button(StopAndSearch, text="Stop and search result by Ethnicity" , command=lambda: StopAndSearchByEthnicity(StopAndSearchForm)).place(x=560, y=95)
    
    CovidForm = tk.Frame(Covid, width=700, height=450)
    CovidForm.place(x=100, y=120)

    StopAndSearchForm = tk.Frame(StopAndSearch, width=700, height=500)
    StopAndSearchForm.place(x=100, y=125)
    
    return root

if __name__ == "__main__":
    app().mainloop()