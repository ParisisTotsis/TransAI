# Wissenschaftlich begründete Komponentenwahl – Arbeitsstand

| Kriterium | OPUS-MT | NLLB-200-distilled-600M | Argos Translate |
|---|---|---|---|
| Kosten der Modellsoftware | kostenlos | kostenlos | kostenlos |
| Lizenz | Apache 2.0 (de-en, de-fr) | CC BY-NC 4.0 (nicht für kommerziellen Einsatz freigegeben) | Python-Software MIT/CC0; Sprachpakete gesondert prüfen |
| Nutzung im KMU-Kontext | grundsätzlich geeignete Lizenz, Pflichten prüfen | Lizenznachteil für den vorgesehenen KMU-Einsatz | abhängig von konkreten Sprachpaketen |
| Lokal | ja | ja | ja |
| Integrationsaufwand (Hypothese) | gering/mittel | höher | gering/mittel |
| Übersetzungsqualität | noch nicht gemessen | noch nicht gemessen | noch nicht gemessen |

**Vorläufige Auswahl:** OPUS-MT passt besser zu zwei festen Sprachen und zum kostenlosen lokalen Demonstrator. Das ist eine *Anforderungsauswahl*, kein empirischer Qualitätsvergleich. Kommerzielle Nutzung bleibt von allen weiteren vertraglichen und rechtlichen Pflichten abhängig.

## Literatur und technische Quellen (APA-7-orientiert, zu prüfen)

- Papineni, K., Roukos, S., Ward, T., & Zhu, W.-J. (2002). BLEU: A method for automatic evaluation of machine translation. *Proceedings of the 40th Annual Meeting of the Association for Computational Linguistics*, 311–318. https://doi.org/10.3115/1073083.1073135
- Helsinki-NLP. (o. D.). *opus-mt-de-en* [Modellkarte]. Hugging Face. https://huggingface.co/Helsinki-NLP/opus-mt-de-en
- Helsinki-NLP. (o. D.). *opus-mt-de-fr* [Modellkarte]. Hugging Face. https://huggingface.co/Helsinki-NLP/opus-mt-de-fr
- Meta AI. (o. D.). *nllb-200-distilled-600M* [Modellkarte]. Hugging Face. https://huggingface.co/facebook/nllb-200-distilled-600M
- Argos Open Technologies. (o. D.). *Argos Translate* [Quellcode]. GitHub. https://github.com/argosopentech/argos-translate
- Hugging Face. (o. D.). *Transformers migration guide for version 5*. GitHub. https://github.com/huggingface/transformers/blob/main/MIGRATION_GUIDE_V5.md

Weitere peer-reviewte Literatur mit DOI wird vor der finalen Einreichung ergänzt. Alle Quellen sind auf Eignung und Bibliografiedetails zu kontrollieren.
- Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A. N., Kaiser, Ł., & Polosukhin, I. (2017). Attention is all you need. *Advances in Neural Information Processing Systems, 30*, 5998–6008. https://proceedings.neurips.cc/paper/2017
