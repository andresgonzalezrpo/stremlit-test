# 🐧 Penguin Species Classifier

Una aplicación web interactiva construida con Streamlit que predice la especie de pingüinos basándose en características físicas usando Machine Learning.

## 🚀 Demo en Vivo
[Ver la aplicación en Streamlit Cloud](https://tu-app.streamlit.app)

## 📊 Características
- **Exploración de Datos**: Visualiza las características de diferentes especies de pingüinos
- **Predicción Interactiva**: Ingresa las medidas de un pingüino y obtén la predicción de su especie
- **Modelo de Machine Learning**: Utiliza RandomForest con 98.5% de precisión
- **Visualizaciones**: Gráficos interactivos con Plotly y Seaborn

## 🛠️ Tecnologías Utilizadas
- **Streamlit**: Framework para la aplicación web
- **Scikit-learn**: Modelo de Machine Learning
- **Pandas & NumPy**: Manipulación de datos
- **Plotly & Seaborn**: Visualizaciones interactivas
- **Joblib**: Serialización del modelo

## 📋 Dataset
Utiliza el famoso dataset de Palmer Penguins que incluye medidas de:
- Longitud y grosor del pico
- Longitud de las aletas
- Masa corporal
- Isla de origen
- Sexo

## 🎯 Especies Predichas
- **Adelie**: Pingüinos Adelie
- **Chinstrap**: Pingüinos Barbijo
- **Gentoo**: Pingüinos Gentoo

## 🏃‍♂️ Ejecución Local
```bash
pip install -r requirements.txt
streamlit run app.py
```

## 📁 Estructura del Proyecto
```
streamlit-app/
├── app.py                           # Aplicación principal Streamlit
├── requirements.txt                 # Dependencias
├── penguins.csv                     # Dataset
├── random_forest_penguin.pickle     # Modelo entrenado
└── output_penguin.pickle           # Codificación de variables
```

Desarrollado con ❤️ usando Streamlit y Scikit-learn