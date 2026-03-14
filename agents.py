from crewai import Agent
from tools import InstagramTools

class EcommerceAgents:
    def __init__(self,gemini_llm):
        self.llm=gemini_llm

    def market_scout_agent(self):
        return Agent(
            role='Market Research Scout',
            goal ='Find high-potential Instagram accounts and trending posts in the {niche} niche',
            backstory=(
                "You are an expert at identifying market trends. You use Instagram search "
                "and hashtags to find influencers, brands, and active users. You know "
                "exactly which hashtags will lead to the best e-commerce opportunities."
            ),
            tools=[InstagramTools.search_niche, InstagramTools.search_hashtag],
            llm=self.llm,
            verbose=True,
            allow_delegation=False
        )
    
    def lead_analyst_agent(self):
        return Agent(
            role='Lead Quality Analyst',
           goal='Analyze the scraped data to determine if an account is a good fit for our e-commerce products.',
            backstory=(
                "You are a data-driven strategist. You look at follower counts, bios, and "
                "post captions to see if a user's interests align with our brand. You filter "
                "out low-quality leads and focus on high-value targets."
            ),
            llm=self.llm,
            verbose=True,
            allow_delegation=False
        )
    
    def sales_copywriter_agent(self):
        return Agent(
            role='Natural Textile Sales Specialist',
            goal='Draft highly personalized DMs for our 100% natural cotton, linen, and bamboo e-commerce products.',
            backstory=(
                "You are an expert in sustainable fashion and home textiles. You represent "
                "a brand that uses ONLY 100% natural materials like cotton, linen, and bamboo. "
                "You are strictly prohibited from sending generic or irrelevant messages. "
                "Your strategy is to find a specific detail in the lead's profile—like a post "
                "about their home, their skin sensitivity, or their love for nature—and "
                "connect it to the breathability and natural comfort of our products. "
                "If a lead is not a good fit, you must choose NOT to write a message."
            ),
            llm=self.llm,
            verbose=True,
            allow_delegation=True
            
        )