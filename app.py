
import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.set_page_config(layout="wide", page_title="Streamlit Report App")

st.title("📊 Streamlit Report App")

uploaded_file = st.file_uploader("Carica il file Excel", type=["xlsx"])

if uploaded_file:
    df = pd.read_excel(uploaded_file)
    st.dataframe(df)

    if "imbocco" in df.columns and "descrizione" in df.columns:
        fig = go.Figure()
        for i, row in df.iterrows():
            fig.add_trace(go.Scatter(
                x=[row["imbocco"]], y=[0],
                mode='markers',
                marker=dict(size=10, color='blue'),
                text=row["descrizione"],
                name=row["descrizione"]
            ))
        fig.update_layout(title="Visualizzazione metrica (0-3000m)",
                          xaxis=dict(range=[0, 3000], title="Metri da imbocco"),
                          yaxis=dict(visible=False))
        st.plotly_chart(fig, use_container_width=True)

    if st.button("Salva dati aggiornati"):
        df.to_excel("dati_aggiornati.xlsx", index=False)
        st.success("Dati salvati in 'dati_aggiornati.xlsx'")
