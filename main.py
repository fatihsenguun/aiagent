import os
from datetime import datetime
from dotenv import load_dotenv
from crewai import Crew, Process, LLM

from agents import EcommerceAgents
from tasks import EcommerceTasks

load_dotenv()

# 🛠️ THE FIX: Feed CrewAI a dummy key so it stops defaulting to OpenAI
os.environ["OPENAI_API_KEY"] = "NA"
target_keyword = input("Kimi arıyoruz? (Örn: interior designer, boutique hotel): ")

# Setup Local LLM using CrewAI's native LiteLLM wrapper
local_llm = LLM(
    model="ollama/qwen3:8b", # Ensure this tag exactly matches your 'ollama list'
    base_url="http://localhost:11434"
)

agents = EcommerceAgents(local_llm)
tasks = EcommerceTasks()

scout = agents.market_scout_agent()
analyst = agents.lead_analyst_agent()
writer = agents.sales_copywriter_agent()

# Step 2: Get Hashtag from User
target_hashtag = input("Enter the hashtag you want to scout (without the #): ")

task1 = tasks.research_niche_task(scout, target_keyword)
task2 = tasks.analyze_leads_task(analyst)
task3 = tasks.write_dm_task(writer)

ecommerce_crew = Crew(
    agents=[scout, analyst, writer],
    tasks=[task1, task2, task3],
    process=Process.sequential,
    cache=False,
    verbose=True
)

print(f"### Starting E-commerce Agent for: #{target_hashtag} ###")
result = ecommerce_crew.kickoff()

# Step 6 & 11: Build your CRM Database
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
filename = f"crm_leads_{timestamp}.txt"

with open(filename, "w", encoding="utf-8") as file:
    file.write("########################\n")
    file.write("## FINAL SALES REPORT ##\n")
    file.write("########################\n\n")
    file.write(str(result))

print(f"\n✅ Run complete! Results saved to local CRM database: {filename}")