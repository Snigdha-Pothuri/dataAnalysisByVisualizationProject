import pandas as pd
import csv
import plotly.graph_objects as go 
import plotly.express as px
df=pd.read_csv("project_data.csv")
print(df.groupby("level")["attempt"].mean())
figure=px.scatter(df,x="level",y="attempt",title="Student levels and marks on pixel math app")
figure.show()