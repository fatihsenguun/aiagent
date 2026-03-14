from crewai import Agent
from tools import search_niche, search_hashtag

class EcommerceAgents:
    def __init__(self, llm):
        self.llm = llm

    def market_scout_agent(self):
        return Agent(
            role='Ethical Textile Market Scout',
            goal='Identify high-intent leads who value pure, non-industrial lifestyle aesthetics.',
            backstory=(
                "You are an expert at spotting the 'Natural Living' movement. You use "
                "signals of quality like #slowliving and #organicinteriors to find leads."
            ),

            tools=[search_niche, search_hashtag], 
            llm=self.llm,
            verbose=True
        )
      
    
    def lead_analyst_agent(self):
        return Agent(
            role='Material Integrity Analyst',
            goal='Filter leads to ensure they align with a 100% natural, non-synthetic lifestyle.',
            backstory=(
                "You are a specialist in material ethics. You can distinguish between 'fast-fashion' "
                "enthusiasts and 'natural fiber' connoisseurs. You analyze bios and captions to "
                "find users who mention skin sensitivity, eco-conscious home design, or a "
                "distaste for industrial, synthetic fabrics. You are the gatekeeper: if a lead "
                "prefers cheap, mass-produced industrial textiles, you reject them. We only "
                "want leads who appreciate the 'living' nature of wool, cotton, and linen."
            ),
            llm=self.llm,
            verbose=True,
            allow_delegation=False
        )
    
    def sales_copywriter_agent(self):
        return Agent(
            role='Natural Living Brand Storyteller',
            goal='Draft deeply personal DMs that explain the sensory benefits of natural fibers over industrial ones.',
            backstory=(
                "You represent a high-end boutique that believes industrial materials "
                "have no place in a sanctuary like a bedroom. You speak with the authority "
                "of a founder. When you write, you focus on the 'sensory' experience: the "
                "coolness of linen, the moisture-wicking of bamboo, and the thermal "
                "intelligence of wool. Your DMs must feel like a thoughtful recommendation "
                "from a friend who cares about the lead's sleep health. If you cannot find "
                "a specific 'Natural Hook' in their profile, you remain silent. We value "
                "brand reputation over spamming."
            ),
            llm=self.llm,
            verbose=True,
            allow_delegation=True
        )