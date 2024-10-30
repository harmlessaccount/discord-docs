# List of Discord Endpoints That Do Not Trigger CAPTCHA

This is a list of Discord endpoints that do not trigger CAPTCHA for user accounts. Discord is constantly updating its spam prevention methods, so this list may not always be accurate. We will try to update it as frequently as possible.

# Endpoints

### 1. Get user's information

- **Endpoint**: `GET /users/@me`
- **Description**: Retrieves the user object of the current user.

**Request example**:
```http
GET https://discord.com/api/v10/users/@me
Authorization: TOKEN
```
**Response example**:
```json
{
    "id": "1234",
    "username": "harmlessaccount",
    "avatar": null,
    "discriminator": "0",
    "public_flags": 0,
    "flags": 0,
    "banner": null,
    "accent_color": null,
    "global_name": "Harmless",
    "avatar_decoration_data": null,
    "banner_color": null,
    "clan": null,
    "mfa_enabled": false,
    "locale": "en-US",
    "premium_type": 0,
    "email": "harm@less.net",
    "verified": true,
    "phone": null,
    "nsfw_allowed": true,
    "linked_users": [],
    "bio": "",
    "authenticator_types": []
}
```
### 2. Get user's guilds

- **Endpoint**: `GET /users/@me/guilds`
- **Description**: Retrieves a list of guilds the current user is a member of.

**Request example**:
```http
GET https://discord.com/api/v10/users/@me/guilds
Authorization: TOKEN
```
**Response example**:
```json
{
    "id": "000000000000000001",
    "name": "Server A",
    "icon": "icon_hash_placeholder_1",
    "banner": "banner_hash_placeholder_1",
    "owner": false,
    "permissions": "2221838205716481",
    "features": [
        "ANIMATED_ICON",
        "NEW_THREAD_PERMISSIONS",
        "ENABLED_DISCOVERABLE_BEFORE",
        "GUILD_ONBOARDING",
        "ROLE_ICONS",
        "ANIMATED_BANNER",
        "MEMBER_VERIFICATION_GATE_ENABLED",
        "GUILD_ONBOARDING_HAS_PROMPTS",
        "CHANNEL_ICON_EMOJIS_GENERATED",
        "VANITY_URL",
        "GUILD_ONBOARDING_EVER_ENABLED",
        "AUTO_MODERATION",
        "PRIVATE_THREADS",
        "NEWS",
        "SEVEN_DAY_THREAD_ARCHIVE",
        "MEMBER_PROFILES",
        "COMMUNITY",
        "THREADS_ENABLED",
        "INVITE_SPLASH",
        "SOUNDBOARD",
        "BANNER",
        "PREVIEW_ENABLED",
        "GUILD_SERVER_GUIDE",
        "THREE_DAY_THREAD_ARCHIVE"
    ]
}

```

### **(GET)** /soundboard-default-sounds
> Returns a JSON array with a sound object for each default sound.  

> **Example Response**
> ```
> [
>     {
>         "name": "quack",
>         "sound_id": "1",
>         "volume": 1,
>         "emoji_id": null,
>         "emoji_name": "🦆",
>         "override_path": "default_quack.mp3",
>         "user_id": "643945264868098049"
>     },
>     ...
> ]
> ```

### **(POST)** /channels/{channel.id}/voice-channel-effects
> Plays the sound given in JSON body in the given channel; returns nothing.  

> **JSON Params**
> | FIELD | TYPE | DESCRIPTION |
> | ----- | ---- | ----------- |
> | sound_id | string | The sound's ID |
> | emoji_id | string | The emoji's ID |
> | emoji_name | string | The utf-8 version of the emoji or name of the custom emoji, example: 👻 |
> | override_path | string | Read below for further information about this |
> | source_guild_id | string | The guild id the sound is from |

> We're unsure what the `override_path` is but from speculations it seems that it is the name of the sound file discord hosts. We've found that you only need to input this when playing a default sound.

### **(POST)** /guilds/{guild.id}/soundboard-sounds
> Uploads a custom sound to the given guild.  

> **JSON Params**
> | FIELD | TYPE | DESCRIPTION |
> | ----- | ---- | ----------- |
> | name | string | The name for the sound |
> | emoji_id | string | The emoji's ID |
> | volume | int | The volume level of the sound, max is 1 |
> | sound | base64 data uri | Read below for further information about this |

> To upload the sound through the API you need to encode your audio in Data URI base64.

### **(DELETE)** /guilds/{guild.id}/soundboard-sounds/{sound.id}
> Delete the given sound from the given guild.  
