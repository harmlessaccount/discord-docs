import uuid
import logging
from curl_cffi import requests
from colorama import Fore, Style, init
import random

init(autoreset=True)

# Logging setup
logging.basicConfig(level=logging.CRITICAL)

class Cookie:
    def __init__(self, dcfduid="", sdcfduid=""):
        self.dcfduid = dcfduid
        self.sdcfduid = sdcfduid

def get_cookie():
    try:
        response = requests.get("https://discord.com", impersonate="chrome")
        response.raise_for_status()
        cookies = response.cookies
        dcfduid = cookies.get("__dcfduid", "")
        sdcfduid = cookies.get("__sdcfduid", "")
        cookie = Cookie(dcfduid, sdcfduid)
        print(Fore.YELLOW + Style.BRIGHT + "[INFO] Cookies obtained successfully!")
        return cookie
    except Exception as e:
        print(Fore.RED + Style.BRIGHT + "[ERROR] Failed to obtain cookies.")
        print(Fore.RED + f"Details: {e}")
        return Cookie()


def generate_session_id():
    try:
        session_id = uuid.uuid4().hex
        print(Fore.GREEN + "[INFO] Session ID generated successfully.")
        return session_id
    except Exception as error:
        print(Fore.RED + Style.BRIGHT + "[ERROR] Failed to generate session ID.")
        print(Fore.RED + f"Details: {error}")
    
    session_id = "10000000100040008000100000000000"
    print(Fore.YELLOW + "[WARN] Using fallback session ID generation.")
    return ''.join(
        hex(int(char, 16) ^ (15 & random.randint(0, 255) >> (int(char) // 4)))[2:]
        if char in '018' else char for char in session_id
    )
def join_guild(invite_code, token):
    url = f"https://discord.com/api/v9/invites/{invite_code}"
    print(Fore.CYAN + f"[INFO] Attempting to join guild with invite code: {invite_code}")
    headers = create_headers(token)
    payload = {"session_id": generate_session_id()}
    
    try:
        # Make the request to join the guild
        response = requests.post(url, headers=headers, impersonate="chrome", json=payload)
        response.raise_for_status()
        if response.status_code == 200:
            print(Fore.GREEN + Style.BRIGHT + "[SUCCESS] Joined the guild successfully!")
        else:
            print(Fore.RED + f"[ERROR] Unexpected status code {response.status_code} while joining the guild.")
    except Exception as e:
        print(Fore.RED + Style.BRIGHT + "[ERROR] Failed to join guild.")
        print(Fore.RED + f"Details: {e}")
def create_headers(token):
    cookie = get_cookie()
    # Not ALL HEADERS are stricly necessary for the request to go through, however, it's better to avoid detections.
    headers = {
        'Host': 'discord.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:132.0) Gecko/20100101 Firefox/132.0',
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate, br, zstd',
        'Content-Type': 'application/json',
        'Authorization': token,
        'X-Context-Properties': 'eyJsb2NhdGlvbiI6IkpvaW4gR3VpbGQiLCJsb2NhdGlvbl9ndWlsZF9pZCI6IjgyOTkyMTg4OTgyODczMjk2OSIsImxvY2F0aW9uX2NoYW5uZWxfaWQiOiI5MDY2NzMyMzUwMjQ4MzA1MjQiLCJsb2NhdGlvbl9jaGFubmVsX3R5cGUiOjV9',
        'X-Super-Properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRmlyZWZveCIsImRldmljZSI6IiIsInN5c3RlbV9sb2NhbGUiOiJlbi1VUyIsImJyb3dzZXJfdXNlcl9hZ2VudCI6Ik1vemlsbGEvNS4wIChXaW5kb3dzIE5UIDEwLjA7IFdpbjY0OyB4NjQ7IHJ2OjEzMi4wKSBHZWNrby8yMDEwMDEwMSBGaXJlZm94LzEzMi4wIiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTMyLjAiLCJvc192ZXJzaW9uIjoiMTAiLCJyZWZlcnJlciI6Imh0dHBzOi8vd3d3Lmdvb2dsZS5jb20vIiwicmVmZXJyaW5nX2RvbWFpbiI6Ind3dy5nb29nbGUuY29tIiwic2VhcmNoX2VuZ2luZSI6Imdvb2dsZSIsInJlZmVycmVyX2N1cnJlbnQiOiIiLCJyZWZlcnJpbmdfZG9tYWluX2N1cnJlbnQiOiIiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfYnVpbGRfbnVtYmVyIjozNDI5NjgsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9',
        'X-Discord-Locale': 'en-US',
        'X-Discord-Timezone': 'Europe/Berlin',
        'X-Debug-Options': 'bugReporterEnabled',
        'Origin': 'https://discord.com/',
        'Referer': 'https://discord.com/',
        'Connection': 'keep-alive',
        'Cookie': f"__dcfduid={cookie.dcfduid}; __sdcfduid={cookie.sdcfduid};"
    }
    print(Fore.GREEN + "[INFO] Headers created successfully.")
    return headers

if __name__ == "__main__":
    token = input(Fore.BLUE + "Enter your Discord account token: ").strip()
    invite_code = input(Fore.BLUE + "Enter the Discord invite code: ").strip()
    join_guild(invite_code, token)