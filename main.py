import asyncio
import os

from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

load_dotenv()

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "Respondé en español, en una frase clara."),
        ("human", "{pregunta}"),
    ]
)

model = ChatOpenAI(model="gpt-4o-mini", temperature=0)
chain = prompt | model | StrOutputParser()


async def main() -> None:
    if not os.getenv("OPENAI_API_KEY", "").strip():
        raise RuntimeError("Falta OPENAI_API_KEY. Copiá .env.example a .env y completalo.")
    respuesta = await chain.ainvoke({"pregunta": "¿Qué es LCEL en una frase?"})
    print(respuesta)


if __name__ == "__main__":
    asyncio.run(main())
