from crewai import Task

class EcommerceTasks:
    def research_niche_task(self,agent,niche):
        return Task(
            description=(
                f"Identify 5 potential leads in the {niche} niche using Instagram. "
                "Use the hashtag search tool to find recent posts. Look for people "
                "interested in home decor, sustainable living, or natural lifestyle. "
                "Collect their usernames, bios, and recent post captions."
            ),
            expected_output=(
                "A detailed list of 5 Instagram accounts including their username, "
                "biography, and a summary of their recent post content."
            ),
            agent=agent
        )
    
    def analyze_leads_task(self, agent):
        return Task(
            description=(
                "Review the list of leads found by the scout. Filter for users who "
                "show a preference for quality, nature, or sustainability. Look for "
                "keywords like 'organic', 'natural', 'homestyle', or 'eco-friendly'. "
                "Determine the 'hook' for each person (e.g., they just moved house, "
                "they love bamboo, etc.)."
            ),
            expected_output=(
                "A refined list of high-quality leads with a specific 'hook' or "
                "reason why our natural cotton/linen products would appeal to them."
            ),
            agent=agent

            
        )
    def write_dm_task(self, agent):
        return Task(
            description=(
                "Draft a personalized Instagram DM for the top leads. "
                "The message must: \n"
                "1. Reference a specific detail from their profile (the hook).\n"
                "2. Mention our 100% natural cotton, linen, or bamboo products.\n"
                "3. Focus on the benefits: breathability, comfort, and natural luxury.\n"
                "4. Be conversational and non-spammy. \n"
                "IF A LEAD IS NOT RELEVANT, DO NOT WRITE A MESSAGE FOR THEM."
            ),
            expected_output=(
                "A set of personalized DMs ready to be sent, each tailored to the "
                "specific user and our natural product line."
            ),
            agent=agent
        )