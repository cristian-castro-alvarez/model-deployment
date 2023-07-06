from dash import Dash, html
from dash_bootstrap_components.themes import BOOTSTRAP

from src.components.layout import create_layout


def main() -> None:
    app = Dash(__name__, external_stylesheets=[BOOTSTRAP])
    app.title = "PoF Prediction"
    app.layout = create_layout(app=app)
    app.run(debug=True)


if __name__ == '__main__':
    main()