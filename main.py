import pandas as pd
import plotly.express as px

df = pd.read.csv("covid_data.csv")
fig = px.scatter(df, x = "date" , y = "cases" , color = "country" , title = "Covid-19 Cases Comparison")
fig.show()