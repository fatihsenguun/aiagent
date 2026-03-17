import os, time, random
from instagrapi import Client
from crewai.tools import tool
from dotenv import load_dotenv

load_dotenv()
cl = Client()
SESSION_FILE = "session.json"

def smart_delay(min_s=15, max_s=35):
    delay = random.uniform(min_s, max_s)
    print(f"--- 😴 Stealth Delay: {round(delay)}s ---")
    time.sleep(delay)

def login_instagram():
    if os.path.exists(SESSION_FILE):
        cl.load_settings(SESSION_FILE)
    try:
        cl.login(os.getenv("IG_USERNAME"), os.getenv("IG_PASSWORD"))
        cl.dump_settings(SESSION_FILE)
        print("🚀 Instagram Login Successful!")
    except Exception as e:
        print(f"❌ Login Error: {e}")

login_instagram()

@tool("search_target_profiles")
def search_target_profiles(keyword: str, amount: int = 5):
    """
    Searches directly for Instagram users by keyword (e.g., 'interior designer', 'boutique hotel').
    Returns a list of targeted usernames.
    """
    print(f"--- 🎯 Searching Profiles for: '{keyword}' ---")
    
    try:
        # hashtag aramak yerine doğrudan kullanıcı arıyoruz
        users = cl.search_users(keyword) 
        results = []
        
        for user in users[:amount]:
            smart_delay(5, 10)
            results.append(user.username)
            
        return str(list(set(results))) 
    except Exception as e:
        return f"Error: {e}. Use placeholders: ['london_interiors', 'boutique_stays']"

@tool("analyze_and_score_user")
def analyze_and_score_user(username: str):
    """Pulls user bio, filters them based on criteria, guesses country, and scores them."""
    print(f"--- 👤 Analyzing: {username} ---")
    smart_delay(6, 15)
    
    try:
        user_info = cl.user_info_by_username(username)
        bio = user_info.biography.lower()
        followers = user_info.follower_count
        
        # Step 4: Reject filters
        reject_words = ["crypto", "trading", "marketing agency"]
        if any(word in bio for word in reject_words):
            return f"{username} rejected (Contains banned keywords)."
            
        # Step 4: Follower limits
        if not (2000 <= followers <= 50000):
            return f"{username} rejected (Followers: {followers} out of range)."

        # Step 5: Country Detection
        country = "Unknown"
        country_hints = {"nyc": "USA", "la": "USA", "🇺🇸": "USA", "london": "UK", "🇬🇧": "UK", "berlin": "Germany", "🇩🇪": "Germany"}
        for hint, c in country_hints.items():
            if hint in bio:
                country = c
                break

        # Step 9: Lead Scoring
        score = 0
        score_map = {"interior designer": 3, "sustainable living": 3, "modern home": 2, "slow living": 2, "wellness": 1}
        for keyword, pts in score_map.items():
            if keyword in bio:
                score += pts

        return {
            "username": username,
            "followers": followers,
            "bio": user_info.biography,
            "country": country,
            "score": score,
            "status": "Approved" if score > 0 else "Low Score"
        }
    except Exception as e:
        return f"Could not retrieve details for {username}."