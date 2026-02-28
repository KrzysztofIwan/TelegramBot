# Zadanie 1 - Tworzenie chatbota

Treść zadania: 
```bash
https://github.com/mkrzywda/WSEI_NLP/blob/main/Lab01.md
```

## Wymagania wstępne
* Python 3.8+
* Biblioteki z pliku `requirements.txt`

## Uruchomienie projektu

Zaleca się korzystanie ze środowiska wirtualnego (**venv**), aby uniknąć konfliktów zależności.
Przed uruchomieniem należy dodać folder wraz z plikiem w lokalizacji:
```
/data/setup_api.json
```

Następnie należy w pliku 'setup_api.json' wstawić swój token który został zwrócony przez FatherBot-a, poniżej zamieszczam treść pliku

```xml
{
    "token" : "TWÓJ TOKEN BOTA"
}
```

**1. Konfiguracja środowiska (Windows):**
```bash
python -m venv venv
pip install -r requirements.txt
```
**2. Uruchomienie projetku:**
```bash
streamlit run main.py
```

