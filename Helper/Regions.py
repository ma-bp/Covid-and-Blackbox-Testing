import pandas as pd
from Store import Cache

Df = pd.read_csv('Csv/specimenDate_ageDemographic-unstacked.csv', low_memory=False)

def AllRegions():
    TargetKey = "AllRegions"
    
    if TargetKey in Cache:
        return Cache[TargetKey]
    else:
        AllRegions = Df.areaName.unique().tolist()
        Cache[TargetKey] = AllRegions
        return AllRegions