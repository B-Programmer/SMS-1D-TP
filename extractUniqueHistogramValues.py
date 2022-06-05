# Define a function to extract the unique Histogram Value
def extractUniqueHistogramValues(valueList, histLength):
    uniqueHistoValueList = []
    for i in range(0, 2 ** histLength):
        if (i in valueList):
            uniqueHistoValueList.append(i)
    return uniqueHistoValueList