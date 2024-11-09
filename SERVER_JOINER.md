# Discord Guild Joiner

This will teach you how to use `curl_cffi`, a really great library for impersonating TLS fingerprints. It is the most up-to-date library for botting purposes currently.

## What is needed

You'll need a **great** Discord token that doesn't get CAPTCHA on join. If your main account can join a server using the script, but a new account cannot, it indicates that the new account's token is **bad**.

## How does joining works

When you join a server, your browser sends a request to this endpoint: `https://discord.com/api/v9/invites/dropshipping`.

This request includes a payload with your Session ID. For more details on how Session IDs are generated, refer to [this document](https://github.com/harmlessaccount/discord-docs/blob/main/SESSION_ID.md).

However, Discord doesn't only check the Session ID. It also verifies the following:

1. **TLS Fingerprints**: Discord checks your TLS fingerprints to ensure your connection is "human".
2. **Cookies**: Discord checks two specific cookies:
   - `__dcfduid`: This is a user identifier cookie.
   - `__sdcfduid`: This is a session cookie, used to track or manage your session on Discord.

The `curl_cffi` library already takes care of handling TLS fingerprints for us, but you'll need to make sure these cookies are set correctly to join a server successfully.

There is more cookies, but Discord doesn't check on them when joining servers.

## How to generate those cookies

Whenever you access any website, the back-end will generate cookies for you, and send you those cookies in the response, for example:

```py
from curl_cffi import requests
def get_cookie():
    response = requests.get("https://discord.com", impersonate="chrome")
    response.raise_for_status()
    cookies = response.cookies
    print(cookies)

get_cookie()
```

The output should be something like this, but different for each session:

```js
<Cookies[<Cookie __dcfduid=1234567890abcdef1234567890abcdef for discord.com />, <Cookie __sdcfduid=abcdef1234567890abcdef12345678901234567890abcdef for discord.com />, <Cookie __cfruid=abcdef1234567890abcdef1234567890abcdef for .discord.com />, <Cookie _cfuvid=abcdefg12345hijklmnop67890qrstuvwxz-123456789012-0.0.1.1-604800000 for .discord.com />]>
```

# Automation Script

Now that we know how it all works, let's begin coding our program.

```python
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
        response = requests.post(url, headers=headers, impersonate="chrome", json=payload)
        response.raise_for_status()
        if response.status_code == 200:
            print(Fore.GREEN + Style.BRIGHT + "[SUCCESS] Joined the guild successfully!")
        else:
            print(Fore.RED + f"[ERROR] Unexpected status code {response.status_code} while joining the guild.")
    except Exception as e:
        print(Fore.RED + Style.BRIGHT + "[ERROR] Failed to join guild.")
        print(Fore.RED + f"Error message: {e}")

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
        'X-Context-Properties': 'eyJsb2NhdGlvbiI6IkpvaW4gR3VpbGQiLCJsb2NhdGlvbl9ndWlsZF9pZCI6Ijk5OTk5OTk5OTk5OTk5OTk5OSIsImxvY2F0aW9uX2NoYW5uZWxfaWQiOiI5OTk5OTk5OTk5OTk5OTk5OTkiLCJsb2NhdGlvbl9jaGFubmVsX3R5cGUiOjV9',
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
```


### Ok, let's try to understand the code, bit by bit: 
- `uuid`: This is used to generate unique identifiers (in our case, session IDs).
- `curl_cffi.requests`: Our HTTP client. It supports TLS impersonation, making it perfect for our use case.
- We go to https://discord.com/ to get our cookies, which will be later used to validate requests on join.
- We then generate our Session ID with `generate_session_id`. We'll use the value the function returns on the payload.
- Since we now have everything required to make the request, we proceed whilst using the newest Chrome TLS fingerprints.
- The headers are necessary to avoid detection, but they're not all stricly required. Headers such as `X-Super-Properties` and `X-Context-Properties` are nothing more than base64 encoded payloads. That means we can generate those headers if needed. Thankfully, we do not need to generate them in our program.

### If the program worked, you should see something like this: 
```js
Enter your Discord account token: harmlessaccount
Enter the Discord invite code: discord
[INFO] Attempting to join guild with invite code: discord
[INFO] Cookies obtained successfully!
[INFO] Headers created successfully.
[INFO] Session ID generated successfully.
[SUCCESS] Joined the guild successfully!
```
