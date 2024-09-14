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