from Store import Cache
import requests

def FetchPoliceForceList():
    DictKey = "PoliceForce"

    # we check the cache to see if the data is available else fetch it
    if DictKey in Cache:
        return Cache[DictKey]
    else:
        Response = requests.get("https://data.police.uk/api/forces")
        if Response.status_code == 200:
            data = Response.json()
            PoliceForce = {item["name"] : item["id"] for item in data}
            Cache[DictKey] = PoliceForce
        else:
            PoliceForce = {}
        return PoliceForce
    
def FetchStopAndSearchCases(SelectedPoliceForce, Date):
    PoliceForceCache = FetchPoliceForceList()
    # we need to cache request of stop and search cases by Date
    DictKey = SelectedPoliceForce + "-" + Date
    if DictKey in Cache:
        return Cache[DictKey]
    else:
        response = requests.get(
            "https://data.police.uk/api/stops-force?force="
            + PoliceForceCache[SelectedPoliceForce]
            + "&date="
            + Date
        )
        if response.status_code == 200:
            Data = response.json()
            Cache[DictKey] = [len(Data), Data]
            return len(Data), Data
        else:
            return []