from dash import Dash, html, dcc


def render(app: Dash) -> html.Div:
    return html.Div(
        children=[
            html.Div(
                children=[
                    html.H6('Slope Height (m):', style={'display':'inline-block', 'margin-right': 5}),
                    dcc.Input(id='slope_height',
                              type='number',
                              placeholder='(min, max) = (60, 700)',
                              min=60,
                              max=700,
                              required=True,
                              style={'display': 'inline-block', 'margin-right': 10}),
                    html.H6('Slope IRA (°):', style={'display':'inline-block', 'margin-right': 5}),
                    dcc.Input(id='slope_ira',
                              type='number',
                              placeholder='(min, max) = (37, 89)',
                              min=37,
                              max=89,
                              required=True,
                              style={'display': 'inline-block', 'margin-right': 10}),
                    html.H6('Dip Structure 1 (°):', style={'display': 'inline-block', 'margin-right': 5}),
                    dcc.Input(id='interface_1_dip',
                              type='number',
                              placeholder='(min, max) = (0, 89)',
                              min=0,
                              max=89,
                              required=True,
                              style={'display': 'inline-block', 'margin-right': 10}),
                    html.H6('Dip-Dir Structure 1 (°):', style={'display': 'inline-block', 'margin-right': 5}),
                    dcc.Input(id='interface_1_dd',
                              type='number',
                              placeholder='(min, max) = (0, 89)',
                              min=0,
                              max=89,
                              required=True,
                              style={'display': 'inline-block', 'margin-right': 10})
                ],
                style={'margin-bottom': 10}
            ),
            html.Div(
                children=[
                    html.H6('Cohesion Structure 1 (kPa):', style={'display':'inline-block', 'margin-right': 5}),
                    dcc.Input(id='interface_1_coh',
                              type='number',
                              placeholder='(min, max) = (0, 30)',
                              min=0,
                              max=20,
                              required=True,
                              style={'display': 'inline-block', 'margin-right': 10}),
                    html.H6('Fric. Angle Structure 1 (°):', style={'display': 'inline-block', 'margin-right': 5}),
                    dcc.Input(id='interface_1_fri',
                              type='number',
                              placeholder='(min, max) = (0, 89)',
                              min=0,
                              max=89,
                              required=True,
                              style={'display': 'inline-block', 'margin-right': 10}),
                    html.H6('East Coord. Point Structure 1:', style={'display': 'inline-block', 'margin-right': 5}),
                    dcc.Input(id='interface_1_x',
                              type='number',
                              placeholder='East Coord',
                              required=True,
                              style={'display': 'inline-block', 'margin-right': 10})],
                style={'margin-bottom': 10}),
            html.Div(
                children=[
                    html.H6('North Coord. Point Structure 1:', style={'display': 'inline-block', 'margin-right': 5}),
                    dcc.Input(id='interface_1_y',
                              type='number',
                              placeholder='North Coord',
                              required=True,
                              style={'display': 'inline-block', 'margin-right': 10}),
                    html.H6('Elev. Point Structure 1:',
                            style={'display': 'inline-block', 'margin-right': 5}),
                    dcc.Input(id='interface_1_z',
                              type='number',
                              placeholder='Elev',
                              required=True,
                              style={'display': 'inline-block', 'margin-right': 10}),
                    html.H6('Dip Structure 2 (°):', style={'display': 'inline-block', 'margin-right': 5}),
                    dcc.Input(id='interface_2_dip',
                              type='number',
                              placeholder='(min, max) = (0, 89)',
                              min=0,
                              max=89,
                              required=True,
                              style={'display': 'inline-block', 'margin-right': 10})],
                style={'margin-bottom': 10}),
            html.Div(
                children=[
                    html.H6('Dip-Dir Structure 2 (°):', style={'display': 'inline-block', 'margin-right': 5}),
                    dcc.Input(id='interface_2_dd',
                              type='number',
                              placeholder='(min, max) = (0, 89)',
                              min=0,
                              max=89,
                              required=True,
                              style={'display': 'inline-block', 'margin-right': 10}),
                    html.H6('Cohesion Structure 2 (kPa):', style={'display': 'inline-block', 'margin-right': 5}),
                    dcc.Input(id='interface_2_coh',
                              type='number',
                              placeholder='(min, max) = (0, 30)',
                              min=0,
                              max=20,
                              required=True,
                              style={'display': 'inline-block', 'margin-right': 10}),
                    html.H6('Fric. Angle Structure 2 (°):', style={'display': 'inline-block', 'margin-right': 5}),
                    dcc.Input(id='interface_2_fri',
                              type='number',
                              placeholder='(min, max) = (0, 89)',
                              min=0,
                              max=89,
                              required=True,
                              style={'display': 'inline-block', 'margin-right': 10})],
                style={'margin-bottom': 10}),
            html.Div(
                children=[
                    html.H6('East Coord. Point Structure 2:', style={'display': 'inline-block', 'margin-right': 5}),
                    dcc.Input(id='interface_2_x',
                              type='number',
                              placeholder='East Coord',
                              required=True,
                              style={'display': 'inline-block', 'margin-right': 10}),
                    html.H6('North Coord. Point Structure 2:',
                            style={'display': 'inline-block', 'margin-right': 5}),
                    dcc.Input(id='interface_2_y',
                              type='number',
                              placeholder='North Coord',
                              required=True,
                              style={'display': 'inline-block', 'margin-right': 10}),
                    html.H6('Elev. Point Structure 2:',
                            style={'display': 'inline-block', 'margin-right': 5}),
                    dcc.Input(id='interface_2_z',
                              type='number',
                              placeholder='Elev',
                              required=True,
                              style={'display': 'inline-block', 'margin-right': 10})],
                style={'margin-bottom': 10}),
            html.Div(
                children=[
                    html.H6('Rock Density (kg/m3):', style={'display': 'inline-block', 'margin-right': 5}),
                    dcc.Input(id='rock_density',
                              type='number',
                              required=True,
                              placeholder='Rock Density',
                              style={'display': 'inline-block', 'margin-right': 10}),
                    html.H6('Intact Young Modulus (GPa):', style={'display': 'inline-block', 'margin-right': 5}),
                    dcc.Input(id='young_modulus',
                              type='number',
                              required=True,
                              placeholder='Intact Rock Young Modulus',
                              style={'display': 'inline-block', 'margin-right': 10}),
                    html.H6('Poisson Ratio:', style={'display': 'inline-block', 'margin-right': 5}),
                    dcc.Input(id='poisson_ratio',
                              type='number',
                              required=True,
                              placeholder='Poisson Ratio',
                              style={'display': 'inline-block', 'margin-right': 10}),
                    html.H6('Intact UCS (MPa):', style={'display': 'inline-block', 'margin-right': 5}),
                    dcc.Input(id='UCS',
                              type='number',
                              required=True,
                              placeholder='Intact Rock UCS',
                              style={'display': 'inline-block', 'margin-right': 10})],
                style={'margin-bottom': 10}),
            html.Div(
                children=[
                    html.H6('Phreatic Level (m):', style={'display': 'inline-block', 'margin-right': 5}),
                    dcc.Input(id='phreatic_level',
                              type='number',
                              required=True,
                              placeholder='Meters below surface',
                              style={'display': 'inline-block', 'margin-right': 10}),
                    html.H6('GSI:', style={'display': 'inline-block', 'margin-right': 5}),
                    dcc.Input(id='GSI',
                              type='number',
                              required=True,
                              placeholder='GSI',
                              style={'display': 'inline-block', 'margin-right': 10}),
                    html.H6('mi:', style={'display': 'inline-block', 'margin-right': 5}),
                    dcc.Input(id='mi',
                              type='number',
                              required=True,
                              placeholder='Hoek & Brown mi',
                              style={'display': 'inline-block', 'margin-right': 10})],
                style={'margin-bottom': 30})
        ])