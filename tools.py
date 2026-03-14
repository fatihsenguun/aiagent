import os
import time
import random
import sqlite3
from instagrapi import Client
from crewai.tools import tool
from dotenv import load_dotenv

load_dotenv()

def smart_delay(min_sec=15, max_sec=45):
    delay = random.uniform(min_sec, max_sec)
    time.sleep(delay)

cl = Client()
SESSION_FILE = "session.json"


def init_db():
    conn = sqlite3.connect('leads_memory.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS visited_leads (
            username TEXT PRIMARY KEY,
            scanned_at DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

def is_lead_new(username):
    conn = sqlite3.connect('leads_memory.db')
    cursor = conn.cursor()
    cursor.execute('SELECT 1 FROM visited_leads WHERE username = ?', (username,))
    result = cursor.fetchone()
    conn.close()
    return result is None

def save_lead(username):
    conn = sqlite3.connect('leads_memory.db')
    cursor = conn.cursor()
    cursor.execute('INSERT OR IGNORE INTO visited_leads (username) VALUES (?)', (username,))
    conn.commit()
    conn.close()

# --- Login Logic ---
def login_instagram():
    if os.path.exists(SESSION_FILE):
        cl.load_settings(SESSION_FILE)
    try:
        cl.login(os.getenv("IG_USERNAME"), os.getenv("IG_PASSWORD"))
        cl.dump_settings(SESSION_FILE)
        print("Instagram Login Successful!")
    except Exception as e:
        print(f"Login Error: {e}")

init_db()
login_instagram()



@tool("search_instagram_niche")
def search_niche(query: str):
    """Modern ev ve doğal yaşam gibi nişlerde hesap araması yapar."""
    print(f"Searching niche: {query}...")
    users = cl.search_users(query, amount=5)
    results = []
    for user in users:
        time.sleep(random.uniform(2, 4))
        info = cl.user_info(user.pk)
        results.append({"username": info.username, "bio": info.biography})
    return str(results)

@tool("search_hashtag_posts")
def search_hashtag(hashtag: str, amount: int = 10): # Added 'amount' with a default
    """
    Search for the most recent posts using a specific hashtag.
    Now accepts an 'amount' parameter for how many posts to scan.
    """
    # Fix 1: Clean the hashtag (Remove # and spaces)
    clean_hashtag = hashtag.strip().replace("#", "")
    
    # Fix 2: Use the amount the agent requested
    print(f"Scoping out fresh leads in #{clean_hashtag} (Requesting {amount} posts)...")
    
    try:
        medias = cl.hashtag_medias_recent(clean_hashtag, amount=amount)
        
        results = []
        for media in medias:
            username = media.user.username
            if is_lead_new(username):
                results.append({
                    "username": username,
                    "caption": media.caption_text,
                    "like_count": media.like_count
                })
                save_lead(username)
                if len(results) >= 5: break # Keep it small for safety
                smart_delay(5, 10)
        return str(results)
    except Exception as e:
        return f"Error: {str(e)}"