import pandas as pd
import numpy as np
import justpy as jp
from datetime import datetime

reviews = pd.read_csv('/Users/py10/projects/zarzadzanije-dannymi/lab-5/reviews_courses.csv')

# Preprocessing data for graph
reviews['Timestamp'] = pd.to_datetime(reviews['Timestamp'])
reviews['Day'] = reviews['Timestamp'].dt.date
day_average = reviews.groupby(['Day']).mean(numeric_only=True).reset_index()

def app():
    wp = jp.WebPage()
    # Header section
    jp.Div(text='Course Ratings Analysis', classes='text-4xl m-2 p-2 text-center text-blue-500', a=wp)
    jp.Div(text='This app analyzes course ratings data', classes='text-2xl m-2 p-2 text-center', a=wp)
    jp.Div(text=f'The number of reviews is {len(reviews)}', classes='text-xl m-2 p-2 text-center', a=wp)
    
    # Create a HighCharts chart for average rating by day
    chart_div = jp.Div(classes='m-4 p-4 border rounded shadow', a=wp, style='height: 550px')
    
    # Format data for HighCharts
    chart_data = []
    for index, row in day_average.iterrows():
        # Convert datetime.date to milliseconds timestamp for HighCharts
        timestamp = int(datetime.combine(row['Day'], datetime.min.time()).timestamp() * 1000)
        chart_data.append([timestamp, row['Rating']])
    
    # Configure HighCharts
    chart = jp.HighCharts(a=chart_div, classes='m-2')
    chart.options = {
        'title': {
            'text': 'Average Rating by Day'
        },
        'xAxis': {
            'type': 'datetime',
            'title': {
                'text': 'Date'
            }
        },
        'yAxis': {
            'title': {
                'text': 'Average Rating'
            }
        },
        'series': [{
            'name': 'Average Rating',
            'data': chart_data
        }]
    }
    
    return wp

if __name__ == '__main__':
    jp.justpy(app, port=8001, start_server=True)
    print('Server started on port 8001')
    print('Press Ctrl+C to stop the server')