import pandas as pd
import plotly.express as px
import streamlit as st 

car_data = pd.read_csv('vehicles_us.csv') # leer los datos
car_data ['price_k'] = car_data['price'] / 1000 # Crear una nueva columna de precios en miles
st.header('Análisis Exploratorio de Datos de Vehículos')
st.write('Este es un análisis exploratorio de los datos de vehículos en Estados Unidos.')   
st.sidebar.header('Filtros de Datos') #Crea una barra lateral para los filtros


#Haremos una casilla de verificacion para elegir histograma o grafico de dispersión
show_scatter = st.sidebar.checkbox('Mostrar Gráfico de Dispersión de Precios vs. Año') #Crea una casilla de verificacion para mostrar el grafico de dispersión
if show_scatter: #Si la casilla de verificacion esta marcada, se mostrara el grafico de dispersión
    fig = px.scatter(car_data, x='model_year', y='price_k', title='Gráfico de Dispersión: Precio vs Año',labels={'price_k': 'Precio (en miles de $)', 'model_year': 'Año del Modelo'})
    st.plotly_chart(fig) #Muestra el grafico de dispersión en la aplicacion de streamlit    

show_odometer_scatter = st.sidebar.checkbox('Mostrar Gráfico de Dispersión de Precios vs. Odómetro') #Crea una casilla de verificacion para mostrar el grafico de dispersión
if show_odometer_scatter: #Si la casilla de verificacion esta marcada, se mostrara el grafico de dispersión
    fig = px.scatter(car_data, x='odometer', y='price_k', title='Gráfico de Dispersión: Precio vs Odómetro', labels={'price_k': 'Precio (en miles de $)', 'odometer': 'Kilometraje'})
    st.plotly_chart(fig) #Muestra el grafico de dispersión en la aplicacion de streamlit

show_histogram = st.sidebar.checkbox('Mostrar Histograma de Precios') #Crea una casilla de verificacion para mostrar el histograma
if show_histogram: #Si la casilla de verificacion esta marcada, se mostrara
    fig = px.histogram(car_data, x='price_k', nbins=50, title='Histograma de Precios de Vehículos', labels={'price_k': 'Precio (en miles de $)'})
    st.plotly_chart(fig) #Muestra el histograma en la aplicacion de streamlit

#Creamos un boton para representar un grafico de barras de los 10 modelos mas caros
if st.sidebar.button('Mostrar Gráfico de Barras de los 10 Modelos Más Caros'):
    avg_price_by_model = car_data.groupby('model')['price_k'].mean().reset_index()  # Agrupa por modelo y calcula el precio promedio
    top_10_expensive = avg_price_by_model.nlargest(10, 'price_k')  # Obtiene los 10 modelos más caros
    fig = px.bar(top_10_expensive, x='model', y='price_k', title='Top 10 Modelos Más Caros', labels={'price_k': 'Precio (en miles de $)', 'model': 'Modelo'})
    st.plotly_chart(fig)  # Muestra el gráfico de barras en la aplicación de Streamlit

#Creamos un boton para representar un grafico de barras de los 10 modelos mas baratos
if st.sidebar.button('Mostrar Gráfico de Barras de los 10 Modelos Más Economicos'):
    avg_price_by_model = car_data.groupby('model')['price_k'].mean().reset_index()  # Agrupa por modelo y calcula el precio promedio
    top_10_cheapest = avg_price_by_model.nsmallest(10, 'price_k')  # Obtiene los 10 modelos más baratos
    fig = px.bar(top_10_cheapest, x='model', y='price_k', title='Top 10 Modelos Más Económicos', labels={'price_k': 'Precio (en miles de $)', 'model': 'Modelo'})
    st.plotly_chart(fig)  # Muestra el gráfico de barras en la aplicación de Streamlit  


