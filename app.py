import dash
from dash import dcc, html, Input, Output, State
from dash.exceptions import PreventUpdate
import pandas as pd
import plotly.express as px
import dash_bootstrap_components as dbc
from datetime import datetime
import io
import base64

# Crear la app Dash
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Cargar los datos (archivo Excel de ejemplo)
df = pd.read_excel('datos_medicos.xlsx')

# Layout de la app
app.layout = html.Div([  
    # Título del Dashboard
    dbc.Row([  
        dbc.Col(html.H1("Dashboard del Centro Médico", className="text-center"), width=12),
    ], className="mb-4"),

    # Filtros interactivos: Fecha, Especialidad, Médico
    dbc.Row([  
        dbc.Col([dcc.DatePickerRange(
                    id='date-picker-range',
                    start_date=df['Fecha'].min().strftime('%Y-%m-%d'),
                    end_date=df['Fecha'].max().strftime('%Y-%m-%d'),
                    display_format='YYYY-MM-DD'
                )], width=12, md=4, lg=3),
        
        dbc.Col([dcc.Dropdown(
                    id='specialty-dropdown',
                    options=[{'label': specialty, 'value': specialty} for specialty in df['Especialidad'].unique()],
                    value=df['Especialidad'].unique()[0]
                )], width=12, md=4, lg=3),
        
        dbc.Col([dcc.Dropdown(
                    id='doctor-dropdown',
                    options=[{'label': doctor, 'value': doctor} for doctor in df['Medico'].unique()],
                    value=df['Medico'].unique()[0]
                )], width=12, md=4, lg=3),
    ], className="mb-4"),

    # KPI: Indicadores
    dbc.Row([  
        dbc.Col(
            dbc.Card(
                dbc.CardBody([ 
                    html.H4("Total de Pacientes Atendidos", className="card-title", style={"color": "#007bff"}),
                    html.P(id='patient-count', className="card-text", style={"color": "#007bff"}),
                ]), style={"margin-top": "20px"},
            ), width=12, sm=6, md=4, lg=3
        ),
        dbc.Col(
            dbc.Card(
                dbc.CardBody([ 
                    html.H4("Tiempo Promedio de Espera", className="card-title", style={"color": "#007bff"}),
                    html.P(id='average-wait-time', className="card-text", style={"color": "#007bff"}),
                ]), style={"margin-top": "20px"},
            ), width=12, sm=6, md=4, lg=3
        ),
        dbc.Col(
            dbc.Card(
                dbc.CardBody([ 
                    html.H4("Médicos Disponibles", className="card-title", style={"color": "#007bff"}),
                    html.P(id='doctor-count', className="card-text", style={"color": "#007bff"}),
                ]), style={"margin-top": "20px"},
            ), width=12, sm=6, md=4, lg=3
        ),
        dbc.Col(
            dbc.Card(
                dbc.CardBody([ 
                    html.H4("Índice de Satisfacción de Pacientes", className="card-title", style={"color": "#007bff"}),
                    html.P(id='satisfaction-index', className="card-text", style={"color": "#007bff"}),
                ]), style={"margin-top": "20px"},
            ), width=12, sm=6, md=4, lg=3
        ),
    ], className="mb-4"),

    # Gráficos: Barras, Torta, Líneas
    dbc.Row([  
        dbc.Col([dcc.Graph(id='bar-chart')], width=12, sm=12, md=6, lg=6),
        dbc.Col([dcc.Graph(id='age-distribution-chart')], width=12, sm=12, md=6, lg=6),
    ], className="mb-4"),

    # Tendencia de atenciones
    dbc.Row([  
        dbc.Col([dcc.Graph(id='line-chart')], width=12),
    ], className="mb-4"),

    # Cargar Excel
    dbc.Row([  
        dbc.Col([dcc.Upload(
            id='upload-data',
            children=html.Button('Subir Excel'),
            multiple=False
        )], width=12, sm=12, md=6, lg=4),
    ], className="mb-4"),

    # Mostrar el nombre del archivo cargado
    html.Div(id='output-data-upload', className="text-center mt-4")
])

# Callbacks para actualizar los gráficos y KPIs
@app.callback(
    [Output('patient-count', 'children'), 
     Output('doctor-count', 'children'),
     Output('average-wait-time', 'children'),
     Output('satisfaction-index', 'children'),
     Output('bar-chart', 'figure'), 
     Output('age-distribution-chart', 'figure'), 
     Output('line-chart', 'figure')],
    [Input('date-picker-range', 'start_date'),
     Input('date-picker-range', 'end_date'),
     Input('specialty-dropdown', 'value'),
     Input('doctor-dropdown', 'value')]
)
def update_dashboard(start_date, end_date, specialty, doctor):
    # Filtrar los datos según los parámetros
    filtered_df = df[(df['Fecha'] >= start_date) & (df['Fecha'] <= end_date)]
    filtered_df = filtered_df[filtered_df['Especialidad'] == specialty]
    filtered_df = filtered_df[filtered_df['Medico'] == doctor]

    # KPIs
    total_patients = len(filtered_df)
    avg_wait_time = filtered_df['Tiempo_espera'].mean()
    total_doctors = len(filtered_df['Medico'].unique())
    satisfaction_index = filtered_df['Satisfaccion'].mean()

    # Gráfico de barras: Pacientes atendidos por especialidad
    bar_chart = px.bar(filtered_df, x='Especialidad', y='Atenciones', title="Pacientes Atendidos por Especialidad")

    # Verificar si existe la columna Rango_edad
    if 'Rango_edad' in filtered_df.columns:
        # Gráfico de torta: Distribución de pacientes por rango de edad
        age_distribution_chart = px.pie(filtered_df, names='Rango_edad', title="Distribución de Pacientes por Rango de Edad")
    else:
        # Si no existe la columna, mostrar un mensaje en lugar de un gráfico
        age_distribution_chart = {
            "data": [],
            "layout": {"title": "Distribución de Pacientes por Rango de Edad", "annotations": [{"text": "No hay datos de rango de edad", "x": 0.5, "y": 0.5, "showarrow": False, "font": {"size": 20, "color": "red"}}]}
        }

    # Gráfico de líneas: Tendencia de atenciones
    line_chart = px.line(filtered_df.groupby(['Fecha'])['Atenciones'].sum().reset_index(), 
                         x='Fecha', y='Atenciones', title="Tendencia de Atenciones en los Últimos 6 Meses")

    return (f"{total_patients} pacientes atendidos", 
            f"{total_doctors} médicos disponibles", 
            f"{avg_wait_time:.2f} minutos de espera promedio", 
            f"{satisfaction_index:.2f} de satisfacción promedio", 
            bar_chart, age_distribution_chart, line_chart)

# Función para cargar el archivo Excel
@app.callback(
    Output('output-data-upload', 'children'),
    Input('upload-data', 'contents'),
    State('upload-data', 'filename'),
    prevent_initial_call=True
)
def update_output(contents, filename):
    if contents is None:
        raise PreventUpdate

    # Procesar el archivo y actualizar el DataFrame
    content_type, content_string = contents.split(',')
    decoded = base64.b64decode(content_string)
    new_df = pd.read_excel(io.BytesIO(decoded))

    # Actualizar el DataFrame global
    global df
    df = new_df

    return f'Archivo cargado: {filename}'

# Ejecutar la app
if __name__ == '__main__':
    app.run(debug=True)
