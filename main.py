import asyncio
import os
from dotenv import load_dotenv
from openai import AsyncOpenAI
from agents import Agent, OpenAIChatCompletionsModel, Runner, set_tracing_disabled

load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")

client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

set_tracing_disabled(True)

async def detect_topic(prompt: str) -> str:
    response = await client.chat.completions.create(
        model="gemini-2.0-flash",
        messages=[
            {"role": "system", "content": "You are a topic classifier. You only respond with one word or phrase that defines the topic of the user prompt."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content.strip()

async def generate_haiku(prompt: str, topic: str) -> str:
    agent = Agent(
        name="EduHaiku",
        instructions=f"You are a poetic teacher. Based on the topic '{topic}', respond in a haiku format to the following question.",
        model=OpenAIChatCompletionsModel(
            model="gemini-2.0-flash",
            openai_client=client
        )
    )
    result = await Runner.run(agent, prompt)
    return result.final_output

async def main():
    user_input = input("Ask your educational question: ")
    topic = await detect_topic(user_input)
    print(f"\n📚 Detected Topic: {topic}\n")
    haiku = await generate_haiku(user_input, topic)
    print("🎓 Haiku Response:\n")
    print(haiku)

if __name__ == "__main__":
    asyncio.run(main())
