import os
from dotenv import load_dotenv
from crewai import Crew, Process
from langchain_ollama import ChatOllama

from agents import EcommerceAgents
from tasks import EcommerceTasks
from crewai import LLM

load_dotenv()

local_llm = LLM(
    model="ollama/qwen3:8b",
    base_url="http://localhost:11434"
)

agents = EcommerceAgents(local_llm)
tasks = EcommerceTasks()

scout = agents.market_scout_agent()
analyst = agents.lead_analyst_agent()
writer = agents.sales_copywriter_agent()

my_niche = "modern home, sustainable living and luxury bed linen"

task1 = tasks.research_niche_task(scout, my_niche)
task2 = tasks.analyze_leads_task(analyst)
task3 = tasks.write_dm_task(writer)

ecommerce_crew = Crew(
    agents=[scout, analyst, writer],
    tasks=[task1, task2, task3],
    process=Process.sequential, # Tasks happen one after another
    verbose=True
)

print(f"### Starting E-commerce Agent for: {my_niche} ###")
result = ecommerce_crew.kickoff()

print("\n\n########################")
print("## FINAL SALES REPORT ##")
print("########################\n")
print(result)