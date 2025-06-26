import streamlit as st
import pandas as pd
import numpy as np
import random
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt

df = pd.read_csv("sample_lyrics_and_music_feature.csv")

# Seleziona le colonne rilevanti
features = ['danceability', 'energy', 'loudness', 'speechiness',
            'acousticness', 'instrumentalness', 'valence', 'tempo']

df = df[features + ['tag', 'track_name', 'artists']].dropna()

# Interfaccia
st.title("🎧 Neural Network Genre Classifier")
# Carica dati

st.write("Scegli due generi musicali per addestrare il modello e vedere come classifica le canzoni.")

genres = df['tag'].value_counts().index.tolist()
selected_genres = st.multiselect("Scegli due generi", genres, default=genres[:2])

if len(selected_genres) == 2:
    df_filtered = df[df['tag'].isin(selected_genres)].copy()
    le = LabelEncoder()
    df_filtered['tag_encoded'] = le.fit_transform(df_filtered['tag'])

    X = df_filtered[features].values
    y = df_filtered['tag_encoded'].values
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    X_train_full, X_test_full, _, df_test_full = train_test_split(X, df_filtered, test_size=0.2, random_state=42)

    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    if st.button("🏋️ Addestra il modello"):
        model = keras.Sequential([
            layers.Dense(32, activation='relu', input_shape=(X_train_scaled.shape[1],)),
            layers.Dense(16, activation='relu'),
            layers.Dense(len(le.classes_), activation='softmax')
        ])

        model.compile(optimizer='adam',
                      loss='sparse_categorical_crossentropy',
                      metrics=['accuracy'])

        with st.spinner("Training in corso..."):
            model.fit(X_train_scaled, y_train, epochs=20, batch_size=32, verbose=0)

        st.success("Modello addestrato!")
        st.balloons()

        y_pred = model.predict(X_test_scaled)
        y_pred_labels = np.argmax(y_pred, axis=1)

        cm = confusion_matrix(y_test, y_pred_labels)
        fig, ax = plt.subplots()
        disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=le.classes_)
        disp.plot(ax=ax)
        st.pyplot(fig)

        # st.session_state.model_trained = True
        st.session_state.model = model
        st.session_state.scaler = scaler
        st.session_state.le = le
        st.session_state.X_test_scaled = X_test_scaled
        st.session_state.df_test_full = df_test_full


    if st.button("🔮 Fai una predizione su una canzone casuale"):
        idx = random.randint(0, len(st.session_state.X_test_scaled) - 1)
        sample = st.session_state.X_test_scaled[idx].reshape(1, -1)
        pred = st.session_state.model.predict(sample)
        predicted_label = st.session_state.le.inverse_transform([np.argmax(pred)])
        track_info = st.session_state.df_test_full.iloc[idx]

        st.subheader("🎼 Risultato della predizione")
        st.write(f"🎶 Traccia: {track_info['track_name']}")
        st.write(f"🎤 Artista: {track_info['artists']}")
        st.write(f"✅ Tag vero: {track_info['tag']}")
        st.write(f"🔮 Predizione del modello: {predicted_label[0]}")
else:
    st.warning("Seleziona esattamente due generi.")
