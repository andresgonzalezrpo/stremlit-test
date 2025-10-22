import streamlit as st
import pandas as pd
import io
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(layout="centered", 
                   page_title="Mi Primera App con Streamlit", page_icon=":smiley:")
t1, t2 = st.columns([0.3, 0.7])
with t1:
    st.image("https://streamlit.io/images/brand/streamlit-mark-color.png", width=100)

with t2:
    st.title("Mi Primera App con Streamlit")
    st.markdown("**¡Bienvenido a mi primera aplicación web usan**")

steps = st.tabs(["Introducción", "Datos", "Visualización"])
df = pd.read_csv('Analisis_Innovador/Mision 2/penguins.csv')
print(df.info())


with steps[0]:
    st.header("Introducción")
    st.write("Esta es una aplicación web sencilla creada con Streamlit.")
    st.write("Aquí puedes explorar datos y visualizaciones de manera interactiva.")
    # Mostrar información del DataFrame
    st.subheader("Información del Dataset de Pingüinos")
    
    # Capturar df.info() y mostrarlo
   
    buffer = io.StringIO()
    df.info(buf=buffer)
    s = buffer.getvalue()
    st.text(s)
    st.dataframe(df)
    st.write(df.describe())

with steps[1]:
    st.header("Datos")
    st.write("Aquí puedes ver los datos cargados:")
    st.dataframe(df)
    species = st.selectbox("Selecciona una especie de pingüino:", df["species"].unique())
    x = st.selectbox("Selecciona la variable para el eje X:", df.columns[2:])
    y = st.selectbox("Selecciona la variable para el eje Y:", df.columns[2:])
    fig, ax = plt.subplots()
    ax = sns.scatterplot(x=df[x], y=df[y], data=df)
    plt.xlabel(x)
    plt.ylabel(y)
    st.pyplot(fig)


    


import sklearn 
import joblib
rfc = joblib.load('random_forest_penguin.pickle')
unique_penguin_mapping = joblib.load('output_penguin.pickle')
with steps[2]:
    # Para ver si carga el modelo
    st.write(rfc)
    st.write(unique_penguin_mapping)
        # Opciones para el ususario
    island = st.selectbox('Isla', options=['Biscoe', 'Dream', 'Torgerson'])
    sex = st.selectbox('Sex', options=['Female', 'Male'])
    bill_length = st.number_input('Bill Length (mm)', min_value=0)
    bill_depth = st.number_input('Bill Depth (mm)', min_value=0)
    flipper_length = st.number_input('Flipper Length (mm)', min_value=0)
    body_mass = st.number_input('Body Mass (g)', min_value=0)
    st.write('Los datos ingresados son {}'.format([island, sex, bill_length, 
                                                  bill_depth, flipper_length, body_mass]))
        # Codificación para las islas
    island_biscoe, island_dream, island_torgerson = 0, 0, 0
    if island == 'Biscoe':
        island_biscoe = 1
    elif island == 'Dream':
        island_dream = 1
    elif island == 'Torgerson':
        island_torgerson = 1

    sex_female, sex_male = 0, 0
    if sex == 'Female':
        sex_female = 1
    elif sex == 'Male':
        sex_male = 1
        
        # Modelo ML
    new_prediction = rfc.predict([[bill_length, bill_depth, flipper_length, body_mass, 
                                       island_biscoe,island_dream, island_torgerson,
                                         sex_female,sex_male]])
    prediction_species = unique_penguin_mapping[new_prediction][0]
    st.write('La especie del pingüino es {}'.format(prediction_species))  

st.write("¡Hola, Streamlit!")



