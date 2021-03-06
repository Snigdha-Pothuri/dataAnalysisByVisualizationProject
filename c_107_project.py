import pandas as pd
import csv
import plotly.graph_objects as go 
import plotly.express as px
df=pd.read_csv("project_data.csv")
print(df.groupby(["student_id", "level"], as_index=False)["attempt"].mean())
figure=px.scatter(mean,x="student_id",y="level",size="attempt", color="attempt",title="Student levels and marks on pixel math app")
figure.show()