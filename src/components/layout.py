from dash import Dash, html

from src.components import input_variables


def create_layout(app: Dash) -> html.Div:
    return html.Div(
        className='app-div',
        children=[
            html.H1(children="Prediction of Probability of Failure",
                    style={'textAlign': 'center',
                           'color': 'black',
                           'font-weight': 'bold'}),
            html.H3(children="Open Pit Slope with Two Geological Structures",
                    style={'textAlign': 'center',
                           'color': 'black',
                           'font-weight': 'bold'}),
            html.Div(children=[
                html.H6(children="by:", style={'display':'inline-block', 'margin-right': 5}),
                html.A('Cristian Castro Álvarez', href='https://github.com/cristian-castro-alvarez', style={'display':'inline-block', 'margin-right': 5}),
                html.H6(children="(Geomechanics Engineer at", style={'display':'inline-block', 'margin-right': 5}),
                html.A('Itasca Chile SpA', href='https://www.itasca.cl/', style={'display':'inline-block'}),
                html.H6(children=")", style={'display':'inline-block'})]),
            html.Img(src='assets/images/Pic.png',
                     style={'height':'40%', 'width':'40%', 'margin': '20px'}),
            html.Div(className='inputs',
                     children=[
                         input_variables.render(app=app)
                     ]),
            html.H2(children="Probability of Failure is: %")
        ],
        style={'textAlign': 'center'}
    )