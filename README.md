# Cadena LCEL asíncrona

Una pregunta entra como diccionario y sale como texto plano. El flujo es declarativo: `prompt | modelo | parser`. No hay llamada manual al SDK.

## Cadena

`ChatPromptTemplate` tiene rol system y rol human. La variable `{pregunta}` es la misma llave del diccionario que recibe `ainvoke`. `StrOutputParser` deja la respuesta en `str`, no en un `AIMessage`.

## Cómo correrlo

Python 3.12.

```bash
python3.12 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
```

Completá `OPENAI_API_KEY` en `.env`.

```bash
python main.py
```

Imprime una frase. El modelo es `gpt-4o-mini` con `temperature` 0.
