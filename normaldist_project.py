# import csv
# import plotly.figure_factory as ff
# import pandas as pd

# df = pd.read_csv("https://raw.githubusercontent.com/whitehatjr/bell-curve--normal-distribution/master/data.csv")
# fig = ff.create_distplot([df["Avg Rating"].tolist()], ["rating"])

# fig.show()

import csv
import plotly.figure_factory as ff

import pandas as pd
df = pd.read_csv("https://raw.githubusercontent.com/whitehatjr/finding-correlation/master/Student%20Marks%20vs%20Days%20Present.csv")
fig = ff.create_distplot([df["Marks In Percentage"].tolist()], ["marks percent"], show_hist=False)

fig.show()