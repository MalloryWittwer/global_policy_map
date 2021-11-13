import plotly.express as px

def serve_figure(dataframe):

    color_map = {
        'Unassigned': 'rgb(240,240,240)',
        'In Progress': 'rgb(255,150,80)',
        'Finished': 'rgb(80,255,160)',
    }

    globe_fig = px.choropleth(dataframe, 
        locationmode = 'country names',
        locations = dataframe['Country'],
        color="Status",
        color_discrete_map=color_map,
        hover_name="Country",
        hover_data={
            "Country": False,
            "Assigned to": True,
            "Status": False,
        },
    )

    globe_fig.update_layout(
        margin={"r":0,"t":0,"l":0,"b":0},
        geo=dict(
            showframe=True,
            projection_type='equirectangular',
        ),
    )

    return globe_fig
