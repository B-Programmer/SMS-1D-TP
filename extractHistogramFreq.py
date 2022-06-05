# Define a function to extract the frequency of occurrence of each unique Histogram Value in the value List
def extractHistogramFreq(valueList, uniqHistList):
    uniqueHistoFreqList = []
    for i in uniqHistList:
        uniqueHistoFreqList.append(valueList.count(i))
    return uniqueHistoFreqList