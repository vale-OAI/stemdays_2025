import streamlit as st

def pagina_generi():
    with st.sidebar:
        st.image("1000173236.png", width=250)

st.markdown("""
   <style>
   /* Sfondo pagina */
   .stApp {
       background-color: #F9D3E0;
       padding: 20px;
   }
   </style>
   """, unsafe_allow_html=True)

if __name__=='__main__':
    pagina_generi()


# Titolo
st.title("Ranking canzoni popolari 🎵")
st.markdown(
    """ 
    Viene presentata una **tabella** che elenca le **12 canzoni** più **popolari** su Spotify **dal 1973 al 2022 📋**.
    """
)


import streamlit as st
import pandas as pd

# Carica il file CSV dal progetto
df = pd.read_csv("popularity_lyrics.csv")

# Mostra la tabella
st.dataframe(df)

st.link_button("▶️ Ascolta la playlist", "https://open.spotify.com/playlist/5UZJX9dUE6bOjM2DT55N6W?si=-R20ZXyrQPG0HNH4mfPIxQ&pi=yIFvw6dNQp2_L")


import pandas as pd
import matplotlib.pyplot as plt


# Carica il file CSV che contiene i dati
df = pd.read_csv('sample_lyrics_and_music_feature.csv')

#Grafico 1 Istogramma della popolarità
plt.hist(df['popularity'],color='mediumvioletred', bins=14)
#plt.title('Grafico della colonna popolarità')
plt.ylabel('Indice')
plt.xlabel('popularity')
plt.show()

#Grafico 2 Andamento della popolarità negli anni
df_sorted=df.sort_values(by=['year'])
print('dati ordinati')
print(df_sorted[['year']].head(10))
y_values = df_sorted['popularity'].sort_values().reset_index(drop=True)
plt.plot(y_values)
step = 1000
positions = range(0, len(y_values), step)

# Etichette corrispondenti agli anni
labels = df_sorted['year'].iloc[positions].astype(str)

plt.xticks(positions, labels, rotation=45)  # ruota le etichette per leggibilità
plt.xlabel('Year')
plt.ylabel('Popularity')
#plt.title('Popularity over years')
plt.tight_layout()
plt.show()






import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

# Titolo dell'app
st.title("Analisi dei dati di popolarità musicale")

# Caricamento del file CSV
df = pd.read_csv('sample_lyrics_and_music_feature.csv')

# --- Grafico 1: Istogramma della popolarità ---
st.subheader("Distribuzione della Popolarità")

fig1, ax1 = plt.subplots()
ax1.hist(df['popularity'], color='mediumvioletred', bins=14)
ax1.set_xlabel('Popularity')
ax1.set_ylabel('Frequenza')
# ax1.set_title('Distribuzione della Popolarità')

st.pyplot(fig1)

# --- Grafico 2: Andamento della popolarità negli anni ---
st.subheader("Andamento della Popolarità negli Anni")

df_sorted = df.sort_values(by=['year'])
y_values = df_sorted['popularity'].sort_values().reset_index(drop=True)
step = 1000
positions = range(0, len(y_values), step)
labels = df_sorted['year'].iloc[positions].astype(str)

fig2, ax2 = plt.subplots()
ax2.plot(y_values)
ax2.set_xticks(positions)
ax2.set_xticklabels(labels, rotation=45)
ax2.set_xlabel('Year')
ax2.set_ylabel('Popularity')
# ax2.set_title('Popularity Over the Years')
fig2.tight_layout()

st.pyplot(fig2)
