from dotenv import load_dotenv
from agno.agent import Agent
from agno.tools.reasoning import ReasoningTools
from agno.tools.yfinance import YFinanceTools
from agno.models.groq import Groq

load_dotenv()                              # expects GROQ_API_KEY in .env

agent = Agent(
    model=Groq(                            
        id="llama3-70b-8192",
        temperature=0.2,
    ),
    tools=[
        ReasoningTools(add_instructions=True),
        YFinanceTools(
            stock_price=True,
            analyst_recommendations=True,
            company_info=True,
            company_news=True,
        ),
    ],
    instructions=[
        "Use tables to display data",
        "Only output the report, no other text",
    ],
    markdown=True,
)

if __name__ == "__main__":
    agent.print_response(
        message="Write a fundamental & valuation report on APPLE",
        stream=True,                     
        show_full_reasoning=True,
        stream_intermediate_steps=True,
    )