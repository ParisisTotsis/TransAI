"""Modellunabhängige Unit-Tests und ein Test mit simulierten Modellkomponenten."""
import pytest
from transai import translator


def test_blank_text_rejected():
    with pytest.raises(translator.TranslationInputError):
        translator.validate_input("  ", "Englisch")


def test_unsupported_language_rejected():
    with pytest.raises(translator.TranslationInputError):
        translator.validate_input("Hallo", "Spanisch")


def test_max_length_rejected():
    with pytest.raises(translator.TranslationInputError):
        translator.validate_input("a" * 3001, "Englisch")


def test_valid_text_trimmed():
    assert translator.validate_input(" Hallo ", "Französisch") == "Hallo"


def test_configured_models():
    assert translator.MODELS["Englisch"].endswith("de-en")
    assert translator.MODELS["Französisch"].endswith("de-fr")


def test_translation_with_mocked_model(monkeypatch):
    import sys
    from types import SimpleNamespace

    class FakeContext:
        def __enter__(self): return self
        def __exit__(self, *args): return False
    class FakeTokenizer:
        def __call__(self, source, **kwargs):
            assert source == "Guten Tag"
            return {"input_ids": [1, 2]}
        def batch_decode(self, tokens, skip_special_tokens):
            return ["Good day"]
    class FakeModel:
        def generate(self, **kwargs): return [[1, 2, 3]]
    monkeypatch.setattr(translator, "load_model", lambda *args, **kwargs: (FakeTokenizer(), FakeModel()))
    monkeypatch.setitem(sys.modules, "torch", SimpleNamespace(inference_mode=lambda: FakeContext()))
    assert translator.translate("Guten Tag", "Englisch") == "Good day"
