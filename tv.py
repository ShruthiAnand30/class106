import plotly.express as px
import csv

with open("tv.csv") as csvFile:
    df = csv.DictReader(csvFile)
    fig = px.scatter(df, x = "Size of TV", y = "\tAverage time spent watching TV in a week (hours)")
    fig.show()