import csv
import numpy as np

def getDataSource(data_path):
    tvSize = []
    timeSpent = []

    with open(data_path) as csvFile:
        csvReader = csv.DictReader(csvFile)
        for row in csvReader:
            tvSize.append(float(row["Size of TV"]))
            timeSpent.append(float(row["\tAverage time spent watching TV in a week (hours)"]))
    return {"x" :tvSize , "y" :timeSpent}

def findCorrelation(dataSource):
    corr = np.corrcoef(dataSource["x"], dataSource["y"])
    print("Correlation = ", corr[0,1])

def main():
    data_path = "tv.csv"
    dataSource = getDataSource(data_path)
    findCorrelation(dataSource)

main()