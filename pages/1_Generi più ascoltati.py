import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

def pagina_generi():
    # Caricamento dati
    df = pd.read_csv("sample_lyrics_and_music_feature.csv")

    # Verifica e conversione della colonna 'year'
    df['year'] = pd.to_numeric(df['year'], errors='coerce')
    df = df.dropna(subset=['year'])
    df['year'] = df['year'].astype(int)

    # Sidebar con immagine
    with st.sidebar:
        st.image("1000173236-Photoroom.png", width=250)

    # CSS personalizzato
    st.markdown("""
    <style>
    .stApp {
        background-color: #F9D3E0;
        padding: 20px;
    }
    h1 {
        color: #D36088 !important;
        font-family: 'Arial Black', Arial, sans-serif;
    }
    .descrizione {
        color: #B266A1 !important;
        font-family: 'Arial', sans-serif;
        font-weight: 600;
        font-size: 18px;
        margin-bottom: 20px;
    }
    div[role="tab"] {
        color: #C45C86 !important;
        font-weight: bold;
        font-size: 18px;
    }
    div.stSelectbox > div > div > div {
        background-color: #E3C4F3 !important;
        border-radius: 8px;
        border: 1px solid #C45C86 !important;
        color: #6A2C91 !important;
        font-weight: 600;
    }
    div[role="listbox"] {
        background-color: #F4A4C0 !important;
        color: #6A2C91 !important;
        font-weight: 600;
    }
    div[role="option"]:hover {
        background-color: #C45C86 !important;
        color: white !important;
    }
    </style>
    """, unsafe_allow_html=True)

    # Titolo e descrizione
    st.markdown("<h1>Generi più ascoltati in base all'anno!</h1>", unsafe_allow_html=True)
    st.markdown(
        "<p class='descrizione'>Ti chiedi come siano cambiati i gusti musicali delle persone nel tempo? "
        "Scegli uno degli anni proposti e potrai analizzare attraverso i nostri grafici la variazione delle preferenze!</p>",
        unsafe_allow_html=True
    )

    # Selezione anno e cutoff
    anni_disponibili = [1970, 1980, 1990, 2000, 2010, 2020]
    choose_year = st.selectbox("Seleziona l'anno", anni_disponibili)
    cutoff = st.slider("Escludi i generi meno frequenti (in %)", 1, 10, 6)

    # Funzione di aggregazione generi
    def prepara_dati(filtro):
        dati_filtrati = df[filtro(df['year'])]
        generi = dati_filtrati['track_genre'].value_counts().reset_index()
        generi.columns = ['track_genre', 'count']
        totale = generi['count'].sum()
        generi['percentage'] = 100 * generi['count'] / totale
        return generi[generi['percentage'] > cutoff]

    # Tabs
    tab1, tab2, tab3 = st.tabs(["Prima dell'anno", "Dopo l'anno", "Confronto"])

    with tab1:
        st.markdown(f"<h3 style='color:#C45C86;'>Generi più ascoltati prima dell'anno {choose_year}</h3>", unsafe_allow_html=True)
        dati_prima = prepara_dati(lambda y: y < choose_year)
        if dati_prima.empty:
            st.write("Nessun dato disponibile. Prova a diminuire il cutoff")
        else:
            fig, ax = plt.subplots(figsize=(8, 8))
            ax.pie(dati_prima['count'], labels=dati_prima['track_genre'], autopct='%1.1f%%', startangle=90)
            ax.axis('equal')
            st.pyplot(fig)

    with tab2:
        st.markdown(f"<h3 style='color:#C45C86;'>Generi più ascoltati dopo l'anno {choose_year}</h3>", unsafe_allow_html=True)
        dati_dopo = prepara_dati(lambda y: y > choose_year)
        if dati_dopo.empty:
            st.write("Nessun dato disponibile. Prova a diminuire il cutoff")
        else:
            fig, ax = plt.subplots(figsize=(8, 8))
            ax.pie(dati_dopo['count'], labels=dati_dopo['track_genre'], autopct='%1.1f%%', startangle=90)
            ax.axis('equal')
            st.pyplot(fig)

    with tab3:
        st.markdown(f"<h3 style='color:#C45C86;'>Confronto generi prima e dopo l'anno {choose_year}</h3>", unsafe_allow_html=True)
        col1, col2 = st.columns(2)

        with col1:
            st.subheader(f"Prima del {choose_year}")
            if dati_prima.empty:
                st.write("Nessun dato. Prova a diminuire il cutoff")
            else:
                for i, row in dati_prima.iterrows():
                    st.write(f"{row['track_genre']}: {row['count']} ascolti")

        with col2:
            st.subheader(f"Dopo il {choose_year}")
            if dati_dopo.empty:
                st.write("Nessun dato. ")
            else:
                for i, row in dati_dopo.iterrows():
                    st.write(f"{row['track_genre']}: {row['count']} ascolti")


pagina_generi()
