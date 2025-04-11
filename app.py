
import streamlit as st
import plotly.graph_objects as go
import pandas as pd

st.set_page_config(layout="wide", page_title="Streamlit Report App")

st.title("Streamlit Report App")
uploaded_file = st.file_uploader("Carica il file Excel", type=["xlsx"])

if uploaded_file:
    df = pd.read_excel(uploaded_file)
    st.write("Anteprima del file caricato:")
    st.dataframe(df)

    if "Metrica da imbocco [m]" in df.columns and "DESCRIZIONE" in df.columns:
        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=df["Metrica da imbocco [m]"],
            y=[1]*len(df),
            mode='markers',
            marker=dict(color='blue', size=10),
            text=df["DESCRIZIONE"],
            hoverinfo="text"
        ))
        fig.update_layout(height=200, showlegend=False, xaxis_title="Metrica (m)")
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.error("Il file Excel deve contenere le colonne 'Metrica da imbocco [m]' e 'DESCRIZIONE'.")
