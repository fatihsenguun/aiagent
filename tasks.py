from crewai import Task

class EcommerceTasks:
    def research_niche_task(self, agent, niche):
        return Task(
            description=(
                f"Identify 10 high-potential leads in the {niche} category. "
                "Focus on these high-intent hashtags: #linenbedding, #woolblanket, #slowlivinghome, #organicinteriors. "
                "Look for people showing off their bedroom setups or discussing 'sleep hygiene'. "
                "Crucially: If you see someone complaining about synthetic sheets or skin irritation, prioritize them."
            ),
            expected_output="A list of 10 usernames with a summary of their lifestyle values and current home aesthetic.",
            agent=agent
        )

    def analyze_leads_task(self, agent):
        return Task(
            description=(
                "Filter the leads. Discard anyone who promotes fast-fashion or mass-produced industrial items. "
                "We are looking for 'Pure Fiber' enthusiasts. Identify a 'Natural Hook' for each: "
                "e.g., Did they post about organic food? (Hook: clean materials for sleep). "
                "Did they post a cold-weather photo? (Hook: the thermal intelligence of our wool sets)."
            ),
            expected_output="A prioritized list of the top 5 leads, categorized by their preferred material (Cotton, Linen, or Wool).",
            agent=agent
        )

    def write_dm_task(self, agent):
        return Task(
            description=(
                "Draft a DM that sounds like a boutique founder sharing a secret. "
                "The message must focus on the sensory experience: \n"
                "1. Mention the lead's specific interest (the Hook).\n"
                "2. Briefly explain how our 100% natural fibers (No Industrial Synthetics) improve sleep health.\n"
                "3. Use words like 'breathable', 'artisanal', and 'moisture-wicking'.\n"
                "4. End with a low-pressure invitation to chat about natural textiles.\n"
                "IF NO RELEVANT HOOK IS FOUND, DO NOT DRAFT A MESSAGE."
            ),
            expected_output="A list of sophisticated, high-end DMs personalized for our natural textile collection.",
            agent=agent
        )