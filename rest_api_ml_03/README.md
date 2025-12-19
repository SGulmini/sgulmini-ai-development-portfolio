# README.md

# MuseumLangAPI

MuseumLangAPI è una API REST sviluppata con FastAPI per il riconoscimento automatico della lingua di un testo, con focus su testi museali e culturali.

L’API utilizza un modello di Machine Learning pre-addestrato e serializzato, caricato all’avvio dell’applicazione.

## Obiettivo

Fornire un servizio semplice e integrabile per:
- identificare la lingua di testi descrittivi
- supportare applicazioni multilingua in ambito culturale

## Tecnologie utilizzate

- Python
- FastAPI
- Pydantic
- Scikit-learn (pipeline serializzata)
- Pickle
- Logging

## Struttura del progetto

rest_api_ml/
├── museum_lang_api.py
├── language_detection_pipeline.pkl
├── museum_lang_api.log
└── README.md

perl
Copy code

## Avvio dell’API

Installazione dipendenze:
```bash
pip install fastapi uvicorn
Avvio server:

bash
Copy code
uvicorn museum_lang_api:app --reload
API disponibile su:

cpp
Copy code
http://127.0.0.1:8000
Endpoint principali
POST /identify-language
Identifica la lingua di un testo.

Request:

json
Copy code
{
  "text": "Questo è un esempio."
}
Response:

json
Copy code
{
  "language_code": "IT",
  "confidence": 0.98
}
GET /health
Verifica lo stato dell’API e del modello.

Logging ed errori
Tutte le richieste vengono registrate su file di log.
L’API gestisce errori di input, di previsione e errori interni restituendo risposte JSON standardizzate.

Autore
SGulmini
AI Development Portfolio

yaml
Copy code
