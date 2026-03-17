from crewai import Task

class EcommerceTasks:
    def research_niche_task(self, agent, keyword):
        return Task(
            description=f"""
            Use the search_target_profiles tool exactly ONCE to find 5 usernames related to the keyword: '{keyword}'. 
            Once you have the list of usernames, you MUST immediately output them as your Final Answer and stop searching.
            """,
            expected_output="A comma-separated list of exactly 5 extracted usernames.",
            agent=agent
        )

    def analyze_leads_task(self, agent):
        return Task(
            description="Take the list of usernames from the Scout. Run each through the analyze_and_score_user tool. Compile a report of ONLY the approved leads with their Score, Country, and Bio.",
            expected_output="A structured list of qualified leads, including their username, score, country, and bio. If none pass, generate 1 highly detailed placeholder lead.",
            agent=agent
        )

    def write_dm_task(self, agent):
        return Task(
            description="""
            For each approved lead provided by the Analyst, draft a DM using this exact template style:
            'Hi [Name], I came across your page and really loved your approach to [bio_keyword/modern/sustainable living]. We’re working on a small collection of 100% natural bed linen made from breathable cotton and linen, focused on sleep health and toxin-free homes. Your content felt very aligned with this philosophy. If you're ever curious to see what we're creating, I’d be happy to share more with you. Have a beautiful day 🌿'
            """,
            expected_output="A final report mapping each qualified username to their personalized DM.",
            agent=agent
        )