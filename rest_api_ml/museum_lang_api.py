"""
MuseumLangAPI - API REST per riconoscere la lingua di un testo.

"""

import logging
import pickle
from pathlib import Path

from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field

# ===========================
# Configurazione
# ===========================

# Nome del file del modello salvato
MODEL_PATH = Path("language_detection_pipeline.pkl")

# File di log in cui registrare tutte le richieste
LOG_FILE = "museum_lang_api.log"

# Impostazioni logging: salva data/ora, livello e messaggio
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger("MuseumLangAPI")


# ===========================
# Caricamento del modello
# ===========================

def load_language_model(path: Path):
    """
    Carica il modello di riconoscimento della lingua (.pkl).

    Solleva FileNotFoundError se il file non esiste.
    """
    if not path.exists():
        raise FileNotFoundError(f"File del modello non trovato: {path}")

    try:
        with open(path, "rb") as f:
            model = pickle.load(f)
        logger.info("Modello caricato correttamente.")
        return model

    except Exception as e:
        logger.exception(f"Errore nel caricamento del modello: {e}")
        raise


# Carica il modello all'avvio dell'app
language_model = load_language_model(MODEL_PATH)


# ===========================
# FastAPI
# ===========================

app = FastAPI(
    title="MuseumLangAPI",
    description="API per identificare la lingua di un testo museale.",
    version="1.0.0",
)


# ===========================
# Modelli di input/output
# ===========================

class LanguageRequest(BaseModel):
    """Modello per il JSON di input dell'endpoint."""
    text: str = Field(..., description="Testo da analizzare")


class LanguageResponse(BaseModel):
    """Risposta con lingua identificata e confidenza."""
    language_code: str
    confidence: float


# ===========================
# Logica applicativa
# ===========================

def predict_language(text: str):
    """
    Restituisce (lingua, confidenza) per il testo fornito.

    Solleva ValueError se il testo è vuoto o se la previsione fallisce.
    """
    if not text.strip():
        raise ValueError("Il testo è vuoto.")

    # Previsione della lingua
    try:
        lang = language_model.predict([text])[0]
    except Exception:
        logger.exception("Errore durante la previsione.")
        raise ValueError("Errore nella previsione della lingua.")

    # Confidenza: usiamo predict_proba se disponibile
    try:
        if hasattr(language_model, "predict_proba"):
            proba = language_model.predict_proba([text])[0]
            idx = list(language_model.classes_).index(lang)
            confidence = float(proba[idx])        # Probabilità vera
        else:
            confidence = 1.0                    # Default
    except Exception:
        confidence = 1.0                        # In caso di errore

    return lang, confidence


def log_request(text_preview: str, lang: str | None, conf: float | None, error: str | None):
    """
    Salva nel file di log il risultato della richiesta.

    text_preview: primi 100 caratteri del testo (per privacy)
    lang/conf: risultati (se disponibili)
    error: eventuale messaggio di errore
    """
    if error:
        logger.info(f"Richiesta FALLITA - testo='{text_preview}' - errore={error}")
    else:
        logger.info(f"Richiesta OK - testo='{text_preview}' - lingua={lang} - conf={conf:.4f}")


# ===========================
# Endpoint API
# ===========================

@app.post("/identify-language", response_model=LanguageResponse)
async def identify_language(req: LanguageRequest):
    """
    Identifica la lingua di un testo.

    Input:
        {
            "text": "Questo è un esempio."
        }

    Output:
        {
            "language_code": "IT",
            "confidence": 0.98
        }
    """
    text = req.text
    preview = text[:100].strip()  # Per logging

    try:
        lang, conf = predict_language(text)

    except ValueError as ve:   # Errori gestibili (es. testo vuoto)
        log_request(preview, None, None, str(ve))
        raise HTTPException(status_code=400, detail=str(ve))

    except Exception:          # Errori imprevisti
        log_request(preview, None, None, "Errore interno")
        raise HTTPException(status_code=500, detail="Errore interno del server.")

    # Log e risposta
    log_request(preview, lang, conf, None)
    return LanguageResponse(language_code=lang, confidence=conf)


@app.get("/health")
async def health_check():
    """Ritorna 'ok' se l'API e il modello sono funzionanti."""
    return {"status": "ok" if language_model else "model_not_loaded"}


# ===========================
# Gestione globale degli errori
# ===========================

@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    """Uniforma il formato degli errori REST in output JSON."""
    return JSONResponse(
        status_code=exc.status_code,
        content={"error": exc.detail},
    )
