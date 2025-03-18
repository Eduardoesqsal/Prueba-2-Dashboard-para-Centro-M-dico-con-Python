Este código es un ejemplo de cómo construir un dashboard interactivo utilizando Dash, con un conjunto de gráficos y KPIs (indicadores clave de rendimiento) sobre datos médicos. El dashboard incluye varias características como filtros por fechas, especialidad, y médico, visualización de datos a través de gráficos de barras, líneas, y torta, además de permitir cargar un archivo Excel para actualizar los datos mostrados en el dashboard.

Descripción extendida del Dashboard:
Objetivo:
Este dashboard está diseñado para monitorear y analizar la actividad médica dentro de un centro médico, proporcionando una visión clara sobre el número de pacientes atendidos, tiempos de espera, satisfacción de los pacientes, distribución de atenciones por especialidad y la tendencia de atenciones a lo largo del tiempo.

Secciones del Dashboard:
Filtros Interactivos:
Los usuarios pueden seleccionar el rango de fechas, la especialidad médica y el médico para filtrar los datos y ajustar la información que se visualiza en los gráficos y KPIs.

KPIs (Indicadores Clave de Rendimiento):

Total de Pacientes Atendidos: Muestra el número total de pacientes atendidos en el rango de fechas y condiciones seleccionadas.
Tiempo Promedio de Espera: Indica el tiempo promedio de espera para los pacientes en el período filtrado.
Médicos Disponibles: Muestra la cantidad de médicos disponibles para atender en las fechas seleccionadas.
Índice de Satisfacción de Pacientes: Calcula el promedio de satisfacción de los pacientes, basándose en las encuestas o mediciones realizadas.
Gráficos Interactivos:

Gráfico de Barras: Representa las atenciones por especialidad, permitiendo al usuario visualizar qué especialidades tienen más atenciones en el rango de fechas seleccionado.
Gráfico de Torta: Muestra la distribución de pacientes por rango de edad (si los datos están disponibles). Si no existe esta información en el dataset, se muestra un mensaje indicando que no hay datos.
Gráfico de Líneas: Visualiza la tendencia de atenciones a lo largo del tiempo, mostrando el total de atenciones por día, semana o mes según los datos.
Subida de Archivos Excel:
Los usuarios pueden cargar un nuevo archivo Excel para actualizar los datos del dashboard. Esto permite una flexibilidad para que los administradores del centro médico puedan actualizar el sistema con la información más reciente.

Características del Código:
Interactividad: Los elementos como el DatePickerRange (selector de fechas), Dropdowns (selector de especialidad y médico), y Gráficos permiten que el usuario interactúe directamente con los datos, filtrándolos según sus necesidades.
Gráficos con Plotly: Usamos Plotly para los gráficos, lo que permite visualizaciones ricas e interactivas. Los gráficos de barras, torta y líneas permiten representar diversos aspectos de la actividad médica en el centro.
Carga dinámica de datos: Usando Dash Upload y un callback, los usuarios pueden cargar un archivo Excel que reemplaza o actualiza los datos mostrados en el dashboard sin necesidad de reiniciar la aplicación.
Posibles Mejoras:
Validación de datos: Mejorar la validación de datos para garantizar que los archivos Excel cargados sean compatibles con el formato requerido.
Más métricas: Incluir métricas adicionales, como el número de citas programadas, canceladas, o el tiempo promedio de consulta.
Autenticación y autorización: Agregar un sistema de inicio de sesión para diferentes roles (administradores, médicos, personal de soporte) para asegurar que solo los usuarios autorizados puedan acceder a ciertos datos.
Este dashboard es una herramienta potente para el monitoreo y análisis de datos médicos, permitiendo la toma de decisiones informadas basadas en datos actualizados.![Captura de pantalla 2025-03-18 161706](https://github.com/user-attachments/assets/df3656ee-e628-428a-9b38-2b884e6b9da3)
![Captura de pantalla 2025-03-18 135610](https://github.com/user-attachments/assets/586299b3-05a8-42b9-a130-20fd36a012ef)
![Captura de pantalla 2025-03-18 135603](https://github.com/user-attachments/assets/d4ae8864-5787-4dbd-925a-300e9b9417e3)
![Captura de pantalla 2025-03-18 135552](https://github.com/user-attachments/assets/d1403604-ea55-44e9-b6c4-fa8174aee028)
