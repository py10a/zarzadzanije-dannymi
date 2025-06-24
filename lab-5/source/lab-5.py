import pandas as pd
import numpy as np
import justpy as jp

reviews = pd.read_csv('/Users/py10/projects/zarzadzanije-dannymi/lab-5/reviews_courses.csv')

def app():
    wp = jp.WebPage()
    jp.Div(text='Hello World', classes='text-4xl m-2 p-2', a=wp)
    jp.Div(text='This is a simple web app using JustPy', classes='text-2xl m-2 p-2', a=wp)
    jp.Div(text=f'The number of reviews is {len(reviews)}', classes='text-xl m-2 p-2', a=wp)
    return wp

if __name__ == '__main__':
    app()
    jp.justpy(app, port=8000, start_server=True)
    print('Server started on port 8000')
    print('Press Ctrl+C to stop the server')