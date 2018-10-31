import json
import requests


def getPassingBy(stop, amount, getHindrance, getColor):
    '''Returns the requested amount of busses that pass at a specific busstop.
    Always starts with current De Lijn Time then always [bus - number - (color)], ends with hindrance if requested.
    stop - int
    amount - int (usually the site limits at 10)
    getHindrance - bool
    getColor - bool
    '''
    
    returnData = []
    
    rawData = requests.get("https://www.delijn.be/rise-api-core/haltes/vertrekken/" + str(stop) + "/" + str(amount))
    data = json.loads(rawData.text)
    
    returnData.append(data["huidigeTijd"])
    for x in range(len(data["lijnen"])):
        returnData.append(data["lijnen"][x]["lijnNummer"])
        returnData.append(data["lijnen"][x]["vertrekTijd"])
        if getColor:
            returnData.append(data["lijnen"][x]["kleurAchterGrond"])

    if getHindrance:
        returnData.append(str(data["storingen"]).strip("['']"))


    return returnData


