
import streamlit as st

# CSS per cambiare lo sfondo della pagina
page_bg_css = """
<style>
    /* Sfondo della pagina principale */
    [data-testid="stAppViewContainer"] {
        background-color: #F9D3E0;
    }
</style>
"""

st.markdown(page_bg_css, unsafe_allow_html=True)


# Mostra un'immagine locale
st.image("copertina webby1.png", use_container_width=True)




from PIL import Image  # se vuoi lavorare con immagini locali


unsafe_allow_html=True
# Titolo della pagina

import streamlit as st

# Caricamento font e stile personalizzato
st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@300&display=swap" rel="stylesheet">

<style>
.best-light-title {
    font-family: 'Playfair Display', serif;
    font-weight: 300;
    font-size: 90px;
    color: #C45C86;
    margin-top: 30px;
    margin-bottom: 20px;
}
</style>

<div class="best-light-title">chi siamo?</div>
""", unsafe_allow_html=True)

import streamlit as st
from PIL import Image

# Carica le immagini
img1 = Image.open("IMG_4787.jpeg")
img2 = Image.open("IMG_4792.jpeg")

# Crea due colonne
col1, col2 = st.columns(2)

# immagine nella prima colonna
with col1:
    st.image("IMG_4787.jpeg")

# immagine nella seconda colonna
with col2:
    st.image("IMG_4792.jpeg")

# Impostazioni pagina
st.set_page_config(page_title="SteamDays - Home", layout="wide")

# HTML + CSS con Google Fonts
html_code = """
<!-- Font Questrial & sostituto di Best Light (Playfair Display) -->
<link href="https://fonts.googleapis.com/css2?family=Questrial&family=Playfair+Display:wght@300&display=swap" rel="stylesheet">

<style>
.title {
    font-family: 'Playfair Display', serif;
    font-size: 90px;
    color: #C45C86;
    margin-top: 40px;
    margin-bottom: 20px;
}

.text {
    font-family: 'Questrial', sans-serif;
    font-size: 30px;
    color: #B75C81;
    line-height: 1.6;
    margin-bottom: 40px;
}
</style>

<div class="title">Progetto Spotify con dashboard e grafici</div>

<div class="text">
Noi siamo il gruppo Webby e oggi siamo qui per presentarvi il nostro progetto che unisce musica, dati e tecnologia. <br>
Siamo un gruppo di studenti appassionati di informatica, design e... ovviamente, musica!<br>
In particolare, ci siamo concentrati su Spotify, una delle piattaforme di streaming più popolari al mondo, per analizzare i dati legati alle canzoni e agli artisti.
</div>

<div class="title">Cos’è il progetto SteamDays</div>

<div class="text">
Il nostro progetto si chiama SteamDays. L’idea è nata dalla voglia di unire due mondi: il mondo dei dati e quello della musica. <br>
SteamDays si basa sull’analisi di dati reali presi da Spotify: abbiamo raccolto informazioni come il numero di ascolti, la durata delle canzoni, il genere musicale e molto altro. <br>
Tutto questo per cercare di rispondere a domande interessanti, come: Quali sono gli artisti più ascoltati? Quali generi vanno di più? Le canzoni più popolari sono anche le più lunghe?
</div>

<div class="title">Cos’è Webby?</div>

<div class="text">
Come dicevamo prima, il nostro gruppo si chiama Webby perché stiamo realizzando un sito web interattivo dove presentiamo i risultati delle nostre analisi. <br>
Webby è un po’ il cuore del nostro lavoro: oltre a scrivere codice per analizzare i dati, abbiamo anche curato la parte grafica del sito, per rendere tutto più comprensibile e accattivante. <br>
Il sito è pensato per essere semplice da usare, anche per chi non ha competenze tecniche. Basta navigare tra le pagine per esplorare grafici, statistiche e curiosità sul mondo della musica.
</div>

<div class="title">Cos’è la Dashboard</div>

<div class="text">
Una delle parti più importanti del nostro progetto è la Dashboard. <br>
Si tratta di una sezione del sito dove abbiamo inserito grafici interattivi e visualizzazioni di dati. <br>
Per esempio, potete vedere un grafico a barre con gli artisti più ascoltati nel 2024, oppure una mappa che mostra in quali Paesi certi generi musicali sono più popolari. <br>
La Dashboard ci permette di vedere i dati, non solo leggerli. Così anche chi non è esperto di numeri può capire subito quali sono le tendenze. <br>
Abbiamo usato strumenti come Python per rendere tutto interattivo.
</div>

<div class="title">END</div>

<div class="text">
In conclusione, con SteamDays abbiamo voluto dimostrare che la musica non è solo arte, ma anche dati e tendenze. <br>
Grazie a Webby, chiunque può esplorare questi dati in modo semplice e intuitivo. <br>
Speriamo che il nostro lavoro vi ispiri a guardare il mondo della musica con occhi nuovi, più analitici ma sempre con passione! <br>
Grazie per l’attenzione!
</div>
"""
# Visualizza il contenuto
st.markdown(html_code, unsafe_allow_html=True)
with st.sidebar:
   st.image("1000173236-Photoroom.png", width=250)

