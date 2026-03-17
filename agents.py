from crewai import Agent
# BURAYI GÜNCELLEDİK: Eski search_hashtag yerine yeni search_target_profiles geldi
from tools import search_target_profiles, analyze_and_score_user

class EcommerceAgents:
    def __init__(self, llm):
        self.llm = llm

    def market_scout_agent(self):
        return Agent(
            role='Instagram Profile Scout',
            goal='Scrape 5 potential usernames targeting specific professions or keywords.',
            backstory="You are a targeted data scraper. Your job is to find high-quality usernames using the profile search tool.",
            tools=[search_target_profiles], # ARAÇ BURADA DA GÜNCELLENDİ
            llm=self.llm,
            allow_delegation=False,
            verbose=True
        )
    
    def lead_analyst_agent(self):
        return Agent(
            role='Lead Scoring Analyst',
            goal='Analyze extracted usernames, apply scoring logic, and filter out unqualified leads.',
            backstory="You are a strict QA analyst. You use the analyze_and_score_user tool on the usernames provided by the Scout. You only pass leads with a score of 1 or higher to the copywriter.",
            tools=[analyze_and_score_user],
            llm=self.llm,
            allow_delegation=False,
            verbose=True
        )
    
    def sales_copywriter_agent(self):
        return Agent(
            role='Boutique DM Specialist',
            goal='Draft hyper-personalized, non-salesy DMs based on the approved leads.',
            backstory="You are a lifestyle brand founder. You never sound like a marketer. You write soft, elegant DMs focused on sleep health, natural fibers, and shared philosophies. You always use variables like {username} and {bio_keyword}.",
            llm=self.llm,
            allow_delegation=False,
            verbose=True
        )