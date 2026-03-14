import os
from crewai import Agent,Task,Crew,Process
from langchain_google_genai import ChatGoogleGenerativeAI



gemini_llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    verbose=True,
    temperature=0.5,
    google_api_key=os.environ["GOOGLE_API_KEY"]
)

analyst_agent=Agent(
    role='Senior Instagram Profile Analyst',
    goal='Analyze the provided Instagram bio and content to identify the user\'s profession and core interests.',
    backstory='You are an expert in digital marketin and social engineering. You can decode a person\'s lifestyle and needs just by looking at their social media presence.',
    llm=gemini_llm,
    verbose=True,
    allow_delegation=False
)

analysis_task = Task(
    description='Analyze the following Instagram profile: "Coffee lover ☕ | Software Engineer 💻 | Hiking on weekends 🏕️ | Building an AI startup!"',
    expected_output='A concise report including: 1. Profession, 2. Primary Interest, 3. A personalized opening line for a DM.',
    agent=analyst_agent
)

instagram_crew = Crew(
    agents=[analyst_agent],
    tasks=[analysis_task],
    process=Process.sequential,
    verbose=True
)

print("### Starting the AI Agent System ###\n")

result = instagram_crew.kickoff()

print("\n\n########################")
print("## ANALYSIS COMPLETED ##")
print("########################\n")
print(result)