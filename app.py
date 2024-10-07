import streamlit as st

st.title("Mi primera aplicación")
st.sidebar.title("parámetros")
st.sidebar.image("imagen.png")

modulo=st.sidebar.selectbox("seleccione un módulo",["modulo1","modulo2","modulo3"])

ge=st.number_input("Ingrese un valor de gravedad específica",min_value=0.1,max_value=1.0,value=0.8)

api=(141.5/ge)-131.5
st.write("El grado API es: ",round(api,2))
