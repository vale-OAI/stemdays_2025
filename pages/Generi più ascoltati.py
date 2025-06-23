import streamlit as st

def pagina_generi():
    # Sidebar con immagine (senza sfondo)
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
    div.stSelectbox > div > div > div > div {
        color: #6A2C91 !important;
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

    anni_disponibili = [1980, 1990, 2000, 2010, 2020]
    anno_scelto = st.selectbox("Seleziona l'anno", anni_disponibili)

    tab1, tab2, tab3 = st.tabs(["Prima dell'anno", "Dopo l'anno", "Confronto"])

    # Dati vuoti (da popolare in futuro)
    dati_prima = {}
    dati_dopo = {}

    def somma_generi(dati, filtro):
        generi_aggregati = {}
        for anno, generi in dati.items():
            if filtro(anno):
                for g, val in generi.items():
                    generi_aggregati[g] = generi_aggregati.get(g, 0) + val
        return generi_aggregati

    with tab1:
        st.markdown(f"<h3 style='color:#C45C86;'>Generi più ascoltati prima dell'anno {anno_scelto}</h3>", unsafe_allow_html=True)
        generi = somma_generi(dati_prima, lambda anno: anno < anno_scelto)
        if not generi:
            st.write("Nessun dato disponibile.")
        else:
            for genere, val in generi.items():
                st.write(f"{genere}: {val} ascolti")

    with tab2:
        st.markdown(f"<h3 style='color:#C45C86;'>Generi più ascoltati dopo l'anno {anno_scelto}</h3>", unsafe_allow_html=True)
        generi = somma_generi(dati_dopo, lambda anno: anno > anno_scelto)
        if not generi:
            st.write("Nessun dato disponibile.")
        else:
            for genere, val in generi.items():
                st.write(f"{genere}: {val} ascolti")

    with tab3:
        st.markdown(f"<h3 style='color:#C45C86;'>Confronto generi prima e dopo l'anno {anno_scelto}</h3>", unsafe_allow_html=True)
        generi_prima = somma_generi(dati_prima, lambda anno: anno < anno_scelto)
        generi_dopo = somma_generi(dati_dopo, lambda anno: anno > anno_scelto)

        col1, col2 = st.columns(2)

        with col1:
            st.subheader(f"Prima dell'anno {anno_scelto}")
            if not generi_prima:
                st.write("Nessun dato disponibile.")
            else:
                for genere, val in generi_prima.items():
                    st.write(f"{genere}: {val} ascolti")

        with col2:
            st.subheader(f"Dopo l'anno {anno_scelto}")
            if not generi_dopo:
                st.write("Nessun dato disponibile.")
            else:
                for genere, val in generi_dopo.items():
                    st.write(f"{genere}: {val} ascolti")

if __name__ == "__main__":
    pagina_generi()



import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


# Titolo dell'app
st.title("Analisi dei Generi Musicali 🎶")
st.markdown("Grafico a torta dei generi musicali per canzoni rilasciate prima o dopo un anno selezionato.")


# Caricamento del file CSV locale
df = pd.read_csv("sample_lyrics_and_music_feature.csv")


# Mostra anteprima dei dati
st.subheader("Anteprima del Dataset")
st.dataframe(df.head(7))


# Parametri selezionabili
st.subheader("Parametri")


choose_year = st.slider("Seleziona l'anno di riferimento", min_value=int(df['year'].min()), max_value=int(df['year'].max()), value=1980)
filter_option = st.radio("Filtra i dati:", ("Prima dell'anno", "Dopo l'anno"))


# Selezione dei dati
if filter_option == "Prima dell'anno":
   df_grafico = df[df['year'] < choose_year]
else:
   df_grafico = df[df['year'] >= choose_year]


# Calcolo dei generi
genre_counts = df_grafico['track_genre'].value_counts().reset_index()
genre_counts.columns = ['track_genre', 'count']
total = genre_counts['count'].sum()
genre_counts['percentage'] = 100 * genre_counts['count'] / total


# Cutoff per includere solo i generi principali
cutoff = st.slider("Escludi i generi meno frequenti (in %)", 1, 20, 6)
filtered_genres = genre_counts[genre_counts['percentage'] > cutoff]


# Grafico a torta
st.subheader("Grafico a torta dei generi musicali")


fig, ax = plt.subplots(figsize=(8, 8))
ax.pie(filtered_genres['count'], labels=filtered_genres['track_genre'], autopct='%1.1f%%', startangle=90)
ax.axis('equal')
st.pyplot(fig)


# Tabella con i dati filtrati
st.subheader("Tabella dei Generi Selezionati")
st.dataframe(filtered_genres)






import os
st.write("Current working directory:", os.getcwd())
