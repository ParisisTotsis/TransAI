"""Modelllogik; kein externer Übersetzungsdienst erforderlich."""
from functools import lru_cache

MODELS = {
    "Englisch": "Helsinki-NLP/opus-mt-de-en",
    "Französisch": "Helsinki-NLP/opus-mt-de-fr",
}
MAX_CHARACTERS = 3000


class TranslationInputError(ValueError):
    pass


def validate_input(text: str, target_language: str) -> str:
    if target_language not in MODELS:
        raise TranslationInputError("Nicht unterstützte Zielsprache.")
    if not isinstance(text, str) or not text.strip():
        raise TranslationInputError("Bitte einen deutschen Text eingeben.")
    if len(text) > MAX_CHARACTERS:
        raise TranslationInputError(f"Bitte höchstens {MAX_CHARACTERS} Zeichen eingeben.")
    return text.strip()


@lru_cache(maxsize=2)
def load_model(target_language: str, local_only: bool = False):
    """Lädt ein Modell einmal pro Sprache; erste Verwendung lädt Dateien herunter.

    Im Offline-Modus werden ausschließlich bereits gecachte Dateien geladen.
    """
    if target_language not in MODELS:
        raise TranslationInputError("Nicht unterstützte Zielsprache.")
    from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
    model_id = MODELS[target_language]
    tokenizer = AutoTokenizer.from_pretrained(model_id, local_files_only=local_only)
    model = AutoModelForSeq2SeqLM.from_pretrained(
        model_id, local_files_only=local_only, use_safetensors=False
    )
    model.eval()
    return tokenizer, model


def translate(text: str, target_language: str, local_only: bool = False) -> str:
    source = validate_input(text, target_language)
    tokenizer, model = load_model(target_language, local_only=local_only)
    import torch
    encoded = tokenizer(source, return_tensors="pt", truncation=True, max_length=512)
    with torch.inference_mode():
        result = model.generate(**encoded, max_new_tokens=512, num_beams=4)
    translation = tokenizer.batch_decode(result, skip_special_tokens=True)[0].strip()
    if not translation:
        raise RuntimeError("Das Modell hat keine Übersetzung ausgegeben.")
    return translation
