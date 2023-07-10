from pathlib import Path
from pickle import load

import numpy as np
from dash import Dash
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
from dash_bootstrap_components.themes import BOOTSTRAP
from tensorflow.keras.models import load_model

from src.components.layout import create_layout

model_dir = Path.cwd() / 'src' / 'assets' / 'model' / 'binary_model.h5'
model = load_model(model_dir)

scaler_dir = Path.cwd() / 'src' / 'assets' / 'scaler' / 'scaler.pkl'
scaler = load(open(scaler_dir, 'rb'))

slope_ira_cos = np.cos(np.radians(38))
slope_ira_sin = np.sin(np.radians(38))
int_1_dip_cos = np.cos(np.radians(37))
int_1_dip_sin = np.sin(np.radians(37))
int_1_dd_cos = np.cos(np.radians(60))
int_1_dd_sin = np.sin(np.radians(60))
int_1_fri_cos = np.cos(np.radians(38))
int_1_fri_sin = np.sin(np.radians(38))
int_2_dip_cos = np.cos(np.radians(38))
int_2_dip_sin = np.sin(np.radians(38))
int_2_dd_cos = np.cos(np.radians(135))
int_2_dd_sin = np.sin(np.radians(135))
int_2_fri_cos = np.cos(np.radians(38))
int_2_fri_sin = np.sin(np.radians(38))
ratio = 50 / 100

# Order Variables
predictors = np.array([[100, 1000 * 10, 1000 * 10, 2700,
                       1_000_000_000 * 40, 0.25, 1_000_000 * 70, -70, 60, 15,
                       slope_ira_cos, slope_ira_sin, int_1_dip_cos, int_1_dip_sin, int_1_dd_cos,
                       int_1_dd_sin, int_1_fri_cos, int_1_fri_sin, int_2_dip_cos, int_2_dip_sin,
                       int_2_dd_cos, int_2_dd_sin, int_2_fri_cos, int_2_fri_sin, 50, ratio]])
# Scale
scaled_predictors = scaler.transform(predictors.reshape(-1,1))
probi = model.predict(scaled_predictors)

print('test')