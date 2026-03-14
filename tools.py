import os
import time
import random
from instagrapi import Client
from crewai.tools import tool
from dotenv import load_dotenv

load_dotenv()

# We initialize the client ONCE at the top level to prevent repeated logins
cl = Client()
SESSION_FILE = "session.json"

def login_instagram():
    """Helper function to handle login once."""
    username = os.getenv("IG_USERNAME")
    password = os.getenv("IG_PASSWORD")

    if os.path.exists(SESSION_FILE):
        print(f"Loading session for {username}...")
        cl.load_settings(SESSION_FILE)
    
    try:
        cl.login(username, password)
        cl.dump_settings(SESSION_FILE)
        print("Instagram Login successful!")
    except Exception as e:
        print(f"Login failed: {e}")

# Run login once when the module is imported
login_instagram()

class InstagramTools:
    @tool("search_instagram_niche")
    def search_niche(query: str):
        """
        Search for Instagram accounts in a specific niche (e.g., 'home decor').
        Returns a list of usernames and their bios.
        """
        print(f"Searching for niche: {query}...")
        users = cl.search_users(query, amount=5) 
        
        results = []
        for user in users:
            # We add a small delay to be safe
            time.sleep(random.uniform(1, 2))
            info = cl.user_info(user.pk)
            results.append({
                "username": info.username,
                "bio": info.biography,
                "followers": info.follower_count
            })
        return str(results)

    @tool("search_hashtag_posts")
    def search_hashtag(hashtag: str):
        """
        Search for the most recent posts using a specific hashtag.
        Returns usernames and captions of people posting in that niche.
        """
        print(f"Scoping out the #{hashtag} scene...")
        medias = cl.hashtag_medias_recent(hashtag, amount=5)
        
        results = []
        for media in medias:
            results.append({
                "username": media.user.username,
                "caption": media.caption_text,
                "like_count": media.like_count
            })
            time.sleep(random.uniform(1, 3))
            
        return str(results)