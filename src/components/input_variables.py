from dash import Dash, html, dcc


def render(app: Dash) -> html.Div:
    return html.Div(
        children=[
            html.Div(
                children=[
                    html.H6('Slope Height (m) [60, 700]:', style={'display':'inline-block', 'margin-right': 5}),
                    dcc.Input(id='slope_height',
                              type='number',
                              placeholder='(min, max) = (60, 700)',
                              min=60,
                              max=700,
                              value=100,
                              required=True,
                              debounce=True,
                              style={'display': 'inline-block', 'margin-right': 10, 'width':'5%'}),
                    html.H6('Slope IRA (°) [37°, 89°]:', style={'display':'inline-block', 'margin-right': 5}),
                    dcc.Input(id='slope_ira',
                              type='number',
                              placeholder='(min, max) = (37, 89)',
                              min=37,
                              max=89,
                              value=38,
                              required=True,
                              debounce=True,
                              style={'display': 'inline-block', 'margin-right': 10, 'width':'5%'}),
                    html.H6('Dist. Between Mapping Points (m):', style={'display': 'inline-block', 'margin-right': 5}),
                    dcc.Input(id='distance',
                              type='number',
                              placeholder='Euclidean Distance',
                              min=1,
                              max=1000,
                              value=50,
                              required=True,
                              debounce=True,
                              style={'display': 'inline-block', 'margin-right': 10, 'width': '5%'})
                ],
                style={'margin-bottom': 10}
            ),
            html.Div(
                children=[
                    html.H6('Dip Structure 1 (°) [0°, 89°]:', style={'display': 'inline-block', 'margin-right': 5}),
                    dcc.Input(id='interface_1_dip',
                              type='number',
                              placeholder='(min, max) = (0, 89)',
                              min=0,
                              max=89,
                              value=37,
                              required=True,
                              debounce=True,
                              style={'display': 'inline-block', 'margin-right': 10, 'width': '5%'}),
                    html.H6('Dip-Dir Structure 1 (°) [300°, 100°]:', style={'display': 'inline-block', 'margin-right': 5}),
                    dcc.Input(id='interface_1_dd',
                              type='number',
                              placeholder='(min, max) = (300°, 100°)',
                              min=0,
                              max=359,
                              value=60,
                              required=True,
                              debounce=True,
                              style={'display': 'inline-block', 'margin-right': 10, 'width': '5%'}),
                    html.H6('Cohesion Structure 1 (kPa) [0, 60]:', style={'display':'inline-block', 'margin-right': 5}),
                    dcc.Input(id='interface_1_coh',
                              type='number',
                              placeholder='(min, max) = (0, 60)',
                              min=0,
                              max=60,
                              value=10,
                              required=True,
                              debounce=True,
                              style={'display': 'inline-block', 'margin-right': 10, 'width':'5%'}),
                    html.H6('Fric. Angle Structure 1 (°) [0°, 45°]:', style={'display': 'inline-block', 'margin-right': 5}),
                    dcc.Input(id='interface_1_fri',
                              type='number',
                              placeholder='(min, max) = (0°, 45°)',
                              min=0,
                              max=45,
                              value=38,
                              required=True,
                              debounce=True,
                              style={'display': 'inline-block', 'margin-right': 10, 'width':'5%'})],
                style={'margin-bottom': 10}),
            html.Div(
                children=[
                    html.H6('Dip Structure 2 (°) [0°, 89°]:', style={'display': 'inline-block', 'margin-right': 5}),
                    dcc.Input(id='interface_2_dip',
                              type='number',
                              placeholder='(min, max) = (0°, 89°)',
                              min=0,
                              max=89,
                              value=38,
                              required=True,
                              debounce=True,
                              style={'display': 'inline-block', 'margin-right': 10, 'width': '5%'}),
                    html.H6('Dip-Dir Structure 2 (°) [40°, 230°]:', style={'display': 'inline-block', 'margin-right': 5}),
                    dcc.Input(id='interface_2_dd',
                              type='number',
                              placeholder='(min, max) = (40°, 230°)',
                              min=0,
                              max=359,
                              value=135,
                              required=True,
                              debounce=True,
                              style={'display': 'inline-block', 'margin-right': 10, 'width':'5%'}),
                    html.H6('Cohesion Structure 2 (kPa) [0, 60]:', style={'display': 'inline-block', 'margin-right': 5}),
                    dcc.Input(id='interface_2_coh',
                              type='number',
                              placeholder='(min, max) = (0, 60)',
                              min=0,
                              max=60,
                              value=10,
                              required=True,
                              debounce=True,
                              style={'display': 'inline-block', 'margin-right': 10, 'width':'5%'}),
                    html.H6('Fric. Angle Structure 2 (°) [0°, 45°]:', style={'display': 'inline-block', 'margin-right': 5}),
                    dcc.Input(id='interface_2_fri',
                              type='number',
                              placeholder='(min, max) = (0, 45°)',
                              min=0,
                              max=45,
                              value=38,
                              required=True,
                              debounce=True,
                              style={'display': 'inline-block', 'margin-right': 10, 'width':'5%'})],
                style={'margin-bottom': 10}),
            html.Div(
                children=[
                    html.H6('Rock Density (kg/m3) [2000, 3900]:', style={'display': 'inline-block', 'margin-right': 5}),
                    dcc.Input(id='rock_density',
                              type='number',
                              required=True,
                              placeholder='(min, max) = (2000, 3900)',
                              min=2000,
                              max=3900,
                              value=2700,
                              debounce=True,
                              style={'display': 'inline-block', 'margin-right': 10, 'width':'5%'}),
                    html.H6('Intact Young Modulus (GPa) [20, 100]:', style={'display': 'inline-block', 'margin-right': 5}),
                    dcc.Input(id='young_modulus',
                              type='number',
                              required=True,
                              placeholder='(min, max) = (20, 100)',
                              min=20,
                              max=100,
                              value=40,
                              debounce=True,
                              style={'display': 'inline-block', 'margin-right': 10, 'width':'5%'}),
                    html.H6('Poisson Ratio [0.18, 0.40]:', style={'display': 'inline-block', 'margin-right': 5}),
                    dcc.Input(id='poisson_ratio',
                              type='number',
                              required=True,
                              placeholder='(min, max) = (0.18, 0.40)',
                              min=0.18,
                              max=0.4,
                              value=0.25,
                              debounce=True,
                              style={'display': 'inline-block', 'margin-right': 10, 'width':'5%'}),
                    html.H6('Intact UCS (MPa) [30, 225]:', style={'display': 'inline-block', 'margin-right': 5}),
                    dcc.Input(id='UCS',
                              type='number',
                              required=True,
                              placeholder='(min, max) = (30, 220)',
                              min=30,
                              max=227,
                              value=70,
                              debounce=True,
                              style={'display': 'inline-block', 'margin-right': 10, 'width':'5%'})],
                style={'margin-bottom': 10}),
            html.Div(
                children=[
                    html.H6('Phreatic Level (m) [20, 70]:', style={'display': 'inline-block', 'margin-right': 5}),
                    dcc.Input(id='phreatic_level',
                              type='number',
                              required=True,
                              min=20,
                              max=70,
                              value=50,
                              placeholder='Meters below surface',
                              debounce=True,
                              style={'display': 'inline-block', 'margin-right': 10, 'width':'5%'}),
                    html.H6('GSI [35, 90]:', style={'display': 'inline-block', 'margin-right': 5}),
                    dcc.Input(id='GSI',
                              type='number',
                              required=True,
                              placeholder='(min, max) = (35, 90))',
                              min=35,
                              max=90,
                              value=60,
                              debounce=True,
                              style={'display': 'inline-block', 'margin-right': 10, 'width':'5%'}),
                    html.H6('Hoek & Brown mi [2, 35]:', style={'display': 'inline-block', 'margin-right': 5}),
                    dcc.Input(id='mi',
                              type='number',
                              required=True,
                              placeholder='(min, max) = (2, 35)',
                              min=2,
                              max=35,
                              value=15,
                              debounce=True,
                              style={'display': 'inline-block', 'margin-right': 10, 'width':'5%'})],
                style={'margin-bottom': 10}),
            html.Div(children=[
                html.Button(id='calculate-button',
                            children='Calculate PoF',
                            n_clicks=0,
                            style={'margin': '30px'})
            ])
        ])