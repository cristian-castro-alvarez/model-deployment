from dash import Dash, html
from dash_bootstrap_components.themes import BOOTSTRAP
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
import numpy as np
from pickle import load

from src.components.layout import create_layout


def main() -> None:
    app = Dash(__name__, external_stylesheets=[BOOTSTRAP])
    app.title = "PoF Prediction"
    app.layout = create_layout(app=app)

    @app.callback(
        [Output('pof', 'children'),
         Output('slope_height', 'value')],
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
    def example_print(n_clicks, slope_height, slope_ira, distance, interface_1_dip, interface_1_dd, interface_1_coh,
                      interface_1_fri, interface_2_dip, interface_2_dd, interface_2_coh, interface_2_fri,
                      rock_density, young_modulus, poisson_ratio, UCS, phreatic_level, GSI, mi):
        if n_clicks:
            if slope_height not in range(60,701):
                slope_height = 60

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
            predictors = np.array([slope_height, interface_1_coh, interface_2_coh, rock_density, young_modulus,
                                   poisson_ratio, UCS, phreatic_level, GSI, mi, slope_ira_cos, slope_ira_sin, int_1_dip_cos,
                                   int_1_dip_sin, int_1_dd_cos, int_1_dd_sin, int_1_fri_cos, int_1_fri_sin, int_2_dip_cos,
                                   int_2_dip_sin, int_2_dd_cos, int_2_dd_sin, int_2_fri_cos, int_2_fri_sin, distance,
                                   ratio])
            # Scale
            return f"{ratio}%", slope_height
        else:
            raise PreventUpdate

    app.run(debug=True)


if __name__ == '__main__':
    main()