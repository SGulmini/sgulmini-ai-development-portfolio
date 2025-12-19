# README.md

# Modello di identificazione della lingua per testi museali

Questo progetto sviluppa un **modello di Machine Learning** per l’identificazione automatica della lingua di testi descrittivi museali.

Il modello è addestrato su descrizioni in **italiano, inglese e tedesco** e utilizza tecniche di **Natural Language Processing (NLP)** basate su n-grammi di caratteri.

## Obiettivo

Realizzare un sistema in grado di:
- riconoscere automaticamente la lingua di un testo
- supportare applicazioni multilingua in ambito museale
- ridurre il lavoro manuale di classificazione linguistica

## Tecnologie utilizzate

- Python
- Pandas
- NLTK
- Scikit-learn
- TF-IDF (character n-grams)
- Multinomial Naive Bayes
- Random Forest
- Joblib

## Dataset

Il dataset è composto da **294 descrizioni museali**, ciascuna associata a un codice lingua (`it`, `en`, `de`).

I dati vengono caricati direttamente da un file CSV pubblico su GitHub.

## Preprocessing

Le operazioni principali includono:
- conversione in minuscolo
- rimozione di simboli e caratteri non alfabetici
- normalizzazione degli spazi

Viene creata una colonna di testo pulito utilizzata per l’addestramento.

## Addestramento del modello

- Rappresentazione testuale tramite **TF-IDF su n-grammi di caratteri (1–3)**
- Suddivisione train/test (80% / 20%) con stratificazione
- Modello principale: **Multinomial Naive Bayes**
- Modello alternativo di confronto: **Random Forest**

## Valutazione

Il modello raggiunge:
- **accuratezza del 100%** sul set di test
- classificazione perfetta per tutte le lingue presenti

La performance è confermata anche dalla matrice di confusione.

## Salvataggio e riutilizzo

Vengono salvati su file:
- il modello addestrato
- il vettorizzatore TF-IDF

Questi artefatti possono essere riutilizzati direttamente in applicazioni future o integrati in una API REST.

## Conclusioni

Il progetto dimostra che un approccio basato su n-grammi di caratteri è efficace per il riconoscimento della lingua in testi museali.

Il modello è facilmente estendibile a nuove lingue o a dataset più ampi.

## Autore

SGulmini  
AI Development Portfolio
