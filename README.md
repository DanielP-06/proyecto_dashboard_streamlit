El enlace para visualizar el proyecto en render es el siguiente:
https://proyecto-sprint7-voph.onrender.com

# Análisis Interactivo de Precios de Vehículos en EE. UU.

Este proyecto presenta una aplicación web interactiva desarrollada con Streamlit y Plotly para realizar un análisis exploratorio de datos sobre los precios de vehículos en Estados Unidos. La herramienta permite a los usuarios visualizar y comprender mejor los factores que influyen en el precio de los vehículos, como el año del modelo y el kilometraje. 

## El problema:
Los precios de vehículos usados varían mucho según año, kilometraje, modelo y otras características. Para vendedores y analistas es crítico identificar tendencias, modelos con mayor/menor valor y cómo el kilometraje impacta el precio para optimizar fijación de precio, inventario y decisiones comerciales.

## Datos
Datos

Archivo principal: vehicles_us.csv (incluye registros de vehículos usados).

Columnas relevantes (típicas): price, year, odometer (kilometraje), make, model, condition, state, transmission, listing_date.

Limpieza aplicada: manejo de nulos, filtro de outliers en price y odometer, normalización de nombres de modelo/marca y conversión de fechas.


## Características

*   **Visualización de Gráficos Interactivos:**
    *   Gráfico de dispersión de precios vs. año del modelo.
    *   Gráfico de dispersión de precios vs. kilometraje (odómetro).
    *   Histograma de la distribución de precios de los vehículos.
*   **Análisis de Modelos:**
    *   Identificación y visualización de los 10 modelos de vehículos más caros.
    *   Identificación y visualización de los 10 modelos de vehículos más económicos.
*   **Filtros de Datos:** Barra lateral para seleccionar y visualizar los diferentes gráficos.

## Resultados KPIs
Precio medio y mediana por año de modelo (permite ver la depreciación típica).
Relación precio vs. kilometraje (scatter interactivo + tendencia): permite estimar elasticidad por kilometraje.
Top 10 modelos más caros / más económicos (por precio medio).
Distribución de precios (percentiles: 10/25/50/75/90) para valorar rango de mercado.
Número de registros analizados y porcentaje filtrado tras limpieza (calidad de datos).
Score de modelo sencillo (R² o MAE) si se ejecuta la parte de modelado, para medir cuán explicable es el precio con las features disponibles.

Estos KPIs se muestran en dashboards y se actualizan con los filtros que aplique el usuario.

## Utilidad y Potencial para los Negocios

Esta aplicación tiene un gran potencial para diversos actores en la industria automotriz y el mercado de vehículos usados:

*   **Concesionarios de Automóviles:** Permite comprender las tendencias de precios, identificar modelos de alta y baja demanda, y optimizar las estrategias de fijación de precios.
*   **Analistas de Mercado:** Facilita la exploración rápida de los datos para identificar patrones, correlaciones y oportunidades de mercado.
*   **Compradores y Vendedores:** Ayuda a tomar decisiones informadas sobre la compra o venta de vehículos, al proporcionar información sobre precios y factores influyentes.
*   **Instituciones Financieras:** Puede ser utilizada para evaluar el valor de los vehículos en préstamos o seguros.

## Herramientas Utilizadas

*   **Python:** Lenguaje de programación principal.
*   **Pandas:** Para la manipulación y análisis de datos.
*   **Plotly Express:** Para la creación de visualizaciones de datos interactivas y atractivas.
*   **Streamlit:** Para el desarrollo rápido de la aplicación web interactiva.
*   **Render:** Plataforma utilizada para desplegar y alojar la aplicación web.

## Cómo Ejecutar Localmente

1.  Clona este repositorio.
2.  Instala las dependencias: `pandas, plotly, streamlit`
3.  Ejecuta la aplicación: `streamlit run tu_script.py`.
4.  O para visualizar el resultado directo dar click al link al inicio del documento
5.  Los datos utilizados en este proyecto provienen del archivo `vehicles_us.csv`.

## Autor

Daniel Pineda

