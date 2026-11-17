"""Streamlit-Oberfläche des TransAI-Demonstrators."""
import streamlit as st
from transai.translator import MODELS, MAX_CHARACTERS, TranslationInputError, translate

st.set_page_config(page_title="TransAI – Übersetzungsdemonstrator", page_icon="🌐")
st.title("TransAI – KI-Sprachübersetzer")
st.caption("Demonstrator für kleine Online-Shops | Deutsch → Englisch / Französisch")
st.info("Nur erfundene oder vollständig anonymisierte Testnachrichten eingeben. Ergebnisse vor Verwendung prüfen.")
language = st.selectbox("Zielsprache", list(MODELS))
source = st.text_area("Deutscher Text", max_chars=MAX_CHARACTERS, height=130,
                      placeholder="Guten Tag, wann wird meine Bestellung geliefert?")
offline = st.checkbox("Nur bereits heruntergeladene Modelle verwenden (offline)", value=False)

if st.button("Übersetzen", type="primary"):
    try:
        with st.spinner("Übersetzung wird erzeugt. Beim ersten Aufruf kann ein Modelldownload nötig sein."):
            result = translate(source, language, local_only=offline)
        st.subheader("Übersetzung")
        st.text_area("Ergebnis", result, height=130)
    except TranslationInputError as error:
        st.warning(str(error))
    except Exception:
        st.error("Übersetzung fehlgeschlagen. Prüfe Internetverbindung, Modellcache und Installation.")
        st.caption("Aus Sicherheitsgründen werden keine internen Fehlerdetails angezeigt.")
st.divider()
st.caption("OPUS-MT-Modelle (Apache-2.0). Keine kostenpflichtige API. Modellqualität ist zu evaluieren.")
