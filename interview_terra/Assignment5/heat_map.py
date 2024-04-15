# import plotly.express as px
#
# fig = px.imshow([[1, 20, 30],
#                  [20, 1, 60],
#                  [30, 60, 1]])
# fig.show()
#
# import plotly.graph_objects as go
#
# fig = go.Figure(data=go.Heatmap(
#                     z=[[30, 24, 7,26],
#                       [5, 27, 1,21],
#                       [13,0,14,9],
#                        [12,5,2,4],
#                        [0,1,29,0,0],
#                        [15,25,5,15],
#                        [10,3,19]],
#                     text=[['python', 'AI ML stack', 'Django','java'],
#                           ['Spring boost', 'Anugular Js', 'Node js','PHP'],
#                           ['Mongo DB', 'Influx DB', 'MySql/Postgress Sql','Warrior Famework'],
#                           ['Robot Framework','AWS/Cloud','Optical','L2/L3'],
#                           ['QA-CLI Auromation','TMF API','Angular 14','Java Full Stack Developer'],
#                           ['Mean Stack Developer','IOS Developer','Android Developer','Go Developer'],
#                           ['IOT','Dockers','Kubernetes','Jenkins']],
#                     texttemplate="%{text}",
#                     textfont={"size":30}))


import pandas as pd
import plotly.graph_objects as go

df = pd.read_excel(r"C:\Users\PavanB-3247\Downloads\pavan_data.xlsx")



labels = df['Area'].tolist()
values = df['Existing Team Members Proficient with this area'].tolist()



color_mappings = {
    'White': 'rgb(255, 255, 255)',
    'Light Green': 'rgb(173, 255, 47)',
    'One level above light green': 'rgb(0, 255, 0)',
    'Two levels above light green': 'rgb(0, 128, 0)',
    'Two levels below dark green': 'rgb(0, 32, 0)',
    'One level below dark green': 'rgb(0, 100, 0)',
    'Dark Green': 'rgb(0, 64, 0)',

}


colors = df['Average Team Expertise (1-5)'].map(color_mappings)


fig = go.Figure(go.Treemap(
    labels=labels,
    parents=[''] * len(labels),
    values=values,
    texttemplate="%{label}<br>(%{value})",
    textfont={"size": 15},
    textposition="middle center",
    hoverinfo="text",
    marker=dict(
        colors=colors
    )
))

fig.update_layout(margin=dict(t=0, l=0, r=0, b=0))

fig.show()
