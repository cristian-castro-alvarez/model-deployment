from pathlib import Path
from pickle import load

import numpy as np
import tensorflow as tf
from dash import Dash, no_update
from dash.dependencies import Input, Output, State
from dash_bootstrap_components.themes import BOOTSTRAP

from src.components.layout import create_layout

app_description = """Surrogate Model for Prediction of Probability of Failure in Open Pits with Two Geological Structures.
by: Cristian Castro Álvarez (Geomechanics Engineer at Itasca Chile SpA)"""
app_title = "PoF Prediction"
app_image = "https://i.ibb.co/pL26M96/Captura.jpg"
metas = [
    {"name": "viewport", "content": "width=device-width, initial-scale=1"},
    {"property": "twitter:card", "content": "summary_large_image"},
    {"property": "twitter:url", "content": "https://pof-prediction.onrender.com/"},
    {"property": "twitter:title", "content": app_title},
    {"property": "twitter:description", "content": app_description},
    {"property": "twitter:image", "content": app_image},
    {"property": "og:title", "content": app_title},
    {"property": "og:type", "content": "website"},
    {"property": "og:description", "content": app_description},
    {"property": "og:image", "content": app_image},
]

app = Dash(__name__,
           external_stylesheets=[BOOTSTRAP],
           meta_tags=metas)
server = app.server
app.title = app_title
app.layout = create_layout(app=app)


@app.callback(
    [Output('pof', 'children'),
     Output('slope_height', 'value'),
     Output('slope_ira', 'value'),
     Output('interface_1_dip', 'value'),
     Output('interface_1_dd', 'value'),
     Output('interface_1_coh', 'value'),
     Output('interface_1_fri', 'value'),
     Output('interface_2_dip', 'value'),
     Output('interface_2_dd', 'value'),
     Output('interface_2_coh', 'value'),
     Output('interface_2_fri', 'value'),
     Output('rock_density', 'value'),
     Output('young_modulus', 'value'),
     Output('poisson_ratio', 'value'),
     Output('UCS', 'value'),
     Output('phreatic_level', 'value'),
     Output('GSI', 'value'),
     Output('mi', 'value')],
    [Input('calculate-button', 'n_clicks')],
    [
        State('slope_height', 'value'),
        State('slope_ira', 'value'),
        State('distance', 'value'),
        State('interface_1_dip', 'value'),
        State('interface_1_dd', 'value'),
        State('interface_1_coh', 'value'),
        State('interface_1_fri', 'value'),
        State('interface_2_dip', 'value'),
        State('interface_2_dd', 'value'),
        State('interface_2_coh', 'value'),
        State('interface_2_fri', 'value'),
        State('rock_density', 'value'),
        State('young_modulus', 'value'),
        State('poisson_ratio', 'value'),
        State('UCS', 'value'),
        State('phreatic_level', 'value'),
        State('GSI', 'value'),
        State('mi', 'value')
    ]
)
def get_probability(n_clicks, slope_height, slope_ira, distance, interface_1_dip, interface_1_dd, interface_1_coh,
                    interface_1_fri, interface_2_dip, interface_2_dd, interface_2_coh, interface_2_fri,
                    rock_density, young_modulus, poisson_ratio, UCS, phreatic_level, GSI, mi):
    if n_clicks:
        model = tf.keras.models.load_model('binary_model.h5')
        scaler = load(open('scaler.pkl', 'rb'))

        if slope_height is None:
            slope_height = 60
        if slope_ira is None:
            slope_ira = 37
        if interface_1_dip is None:
            interface_1_dip = 0
        if interface_1_dd is None:
            interface_1_dd = 0
        if interface_1_coh is None:
            interface_1_coh = 60
        if interface_1_fri is None:
            interface_1_fri = 45
        if interface_2_dip is None:
            interface_2_dip = 0
        if interface_2_dd is None:
            interface_2_dd = 0
        if interface_2_coh is None:
            interface_2_coh = 60
        if interface_2_fri is None:
            interface_2_fri = 45
        if rock_density is None:
            rock_density = 2700
        if young_modulus is None:
            young_modulus = 40
        if poisson_ratio is None:
            poisson_ratio = 0.25
        if UCS is None:
            UCS = 70
        if phreatic_level is None:
            phreatic_level = 50
        if GSI is None:
            GSI = 50
        if mi is None:
            mi = 15

        # Check ranges
        if not 60 <= slope_height <= 700 or slope_height == None:
            slope_height = 60
        if not 37 <= slope_ira <= 89:
            slope_ira = 37
        if not 0 <= interface_1_dip <= 89:
            interface_1_dip = 0
        if not 300 <= interface_1_dd%360 <= 360:
            if not 0 <= interface_1_dd%360 <= 100:
                interface_1_dd = 0
        if not 0 <= interface_1_coh <= 60:
            interface_1_coh = 60
        if not 0 <= interface_1_fri <= 45:
            interface_1_fri = 45
        if not 0 <= interface_2_dip <= 89:
            interface_2_dip = 0
        if not 0 <= interface_2_dd%360 <= 230:
            interface_2_dd = 40
        if not 0 <= interface_2_coh <= 60:
            interface_2_coh = 60
        if not 0 <= interface_2_fri <= 45:
            interface_2_fri = 45
        if not 2000 <= rock_density <= 3900:
            rock_density = 2700
        if not 20 <= young_modulus <= 100:
            young_modulus = 40
        if not 0.18 <= poisson_ratio <= 0.40:
            poisson_ratio = 0.25
        if not 30 <= UCS <= 225:
            UCS = 70
        if not 20 <= phreatic_level <= 70:
            phreatic_level = 50
        if not 35 <= GSI <= 90:
            GSI = 50
        if not 2 <= mi <= 35:
            mi = 15

        # New Predictors
        slope_ira_cos = np.cos(np.radians(slope_ira))
        slope_ira_sin = np.sin(np.radians(slope_ira))
        int_1_dip_cos = np.cos(np.radians(interface_1_dip))
        int_1_dip_sin = np.sin(np.radians(interface_1_dip))
        int_1_dd_cos = np.cos(np.radians(interface_1_dd))
        int_1_dd_sin = np.sin(np.radians(interface_1_dd))
        int_1_fri_cos = np.cos(np.radians(interface_1_fri))
        int_1_fri_sin = np.sin(np.radians(interface_1_fri))
        int_2_dip_cos = np.cos(np.radians(interface_2_dip))
        int_2_dip_sin = np.sin(np.radians(interface_2_dip))
        int_2_dd_cos = np.cos(np.radians(interface_2_dd))
        int_2_dd_sin = np.sin(np.radians(interface_2_dd))
        int_2_fri_cos = np.cos(np.radians(interface_2_fri))
        int_2_fri_sin = np.sin(np.radians(interface_2_fri))
        ratio = distance/slope_height

        # Order Variables
        predictors = np.array([[slope_height, 1000*interface_1_coh, 1000*interface_2_coh, rock_density,
                               1_000_000_000*young_modulus, poisson_ratio, 1_000_000*UCS, -phreatic_level, GSI, mi,
                               slope_ira_cos, slope_ira_sin, int_1_dip_cos, int_1_dip_sin, int_1_dd_cos,
                               int_1_dd_sin, int_1_fri_cos, int_1_fri_sin, int_2_dip_cos, int_2_dip_sin,
                               int_2_dd_cos, int_2_dd_sin, int_2_fri_cos, int_2_fri_sin, distance, ratio]])
        # Scale
        scaled_predictors = scaler.transform(predictors)
        probi = model.predict(scaled_predictors)[0][0]*100

        return f"{round(probi,1)}%", slope_height, slope_ira, interface_1_dip, interface_1_dd, interface_1_coh, \
            interface_1_fri, interface_2_dip, interface_2_dd, interface_2_coh, interface_2_fri, rock_density, \
            young_modulus, poisson_ratio, UCS, phreatic_level, GSI, mi
    else:
        return no_update, no_update, no_update, no_update, no_update, no_update, no_update, no_update, no_update, \
            no_update, no_update, no_update, no_update, no_update, no_update, no_update, no_update, no_update


if __name__ == "__main__":
    app.run_server(debug=True)