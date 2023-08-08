from dash import Dash, html

from src.components import input_variables


def create_layout(app: Dash) -> html.Div:
    return html.Div(
        className='app-div',
        children=[
            html.H1(children="Prediction of Probability of Instalibity",
                    style={'textAlign': 'center',
                           'color': 'black',
                           'font-weight': 'bold'}),
            html.H3(children="Slope with Two Geological Structures",
                    style={'textAlign': 'center',
                           'color': 'black',
                           'font-weight': 'bold'}),
            html.Div(children=[
                html.H6(children="by:", style={'display':'inline-block', 'margin-right': 5}),
                html.A('Cristian Castro Álvarez', href='https://www.linkedin.com/in/cristiancastroa/',
                       style={'display':'inline-block', 'margin-right': 5}),
                html.H6(children="(Geomechanics Engineer at", style={'display':'inline-block', 'margin-right': 5}),
                html.A('Itasca Chile SpA', href='https://www.itasca.cl/', style={'display':'inline-block'}),
                html.H6(children=")", style={'display':'inline-block'})]),
            html.Img(src='assets/images/Pic.png',
                     style={'height':'40%', 'width':'40%', 'margin': '20px'}),
            html.Div(children=[
                html.H6(children="Please fill each box with the required parameter and then press 'Calculate PoI'",
                        style={'marginTop': 25})]),
            html.Div(children=[
                html.H6(children="Each variable has a given [min_value, max_value] range.",
                        style={'marginBottom': 50})]),
            html.Div(className='inputs',
                     children=[
                         input_variables.render(app=app)
                     ]),
            html.H2(children="Probability of Instability is:"),
            html.H2(id='pof', children='%'),
            html.H6(children="This model was trained to recognize the following failure mechanisms:",
                    style={'marginBottom': 20, 'marginTop': 50}),
            html.Img(src='assets/images/model_mechanisms.png',
                    style={'height': '40%', 'width': '65%', 'margin': '10px'}),
            html.H5(children="DISCLAIMER", style={'color': 'red', 'marginTop': 30}),
            html.H6(children="This is a Surrogate Model trained on top of numerical modeling results using deep "
                                   "learning techniques. This model does not replace the decision of a competent "
                                   "rock mechanics engineer.", style={'marginBottom': 20, 'marginTop': 20})
        ],
        style={'textAlign': 'center'}
    )