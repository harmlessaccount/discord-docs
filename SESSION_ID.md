# Information about Session IDs

This is a document about Session IDs on Discord. Reversing JS is necessary to know how they are generated. Work in progress.

### Session ID

- **Format**: Usually a 32-character hexadecimal string, e.g., `"a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6"`.

### `getSessionId()` Function

- **Usage**: Retrieves the current session ID.
- **Used**: Used to validate join requests and probably other requests.
- **Example Usage**: `body: { session_id: getSessionId() }`.

### JavaScript Files that contain references to the function (obfuscated, minified and unreadable)

1. **`web.f7758e8677fcf200f813.js`**
   - Likely contains the `getSessionId` function.
   - Search this file for `getSessionId()` definition.

2. **`sentry.5575a25b27781c170673.js`**
   - Calls session ID.

3. **`ff9a1ab7e45ba219c075.js`**
   - Calls session ID.

4. **`1113b7c20e8fe37006b0.js`**
   - Calls session ID.

5. **`57e7663fa57cb00398c3.js`**
   - Calls session ID.

6. **`1ceee1234b86c54b526b.js`**
   - Calls session ID.

Request example:

POST - https://discord.com/api/v9/invites/{invite_code}

Response - 

```{
    "type": 0,
    "code": "XXXXX",
    "inviter": {
        "id": "XXXXXXXXXXXX",
        "username": "username",
        "avatar": "avatar_hash",
        "discriminator": "0",
        "public_flags": 0,
        "flags": 0,
        "banner": null,
        "accent_color": null,
        "global_name": "GlobalName",
        "avatar_decoration_data": null,
        "banner_color": null,
        "clan": null
    },
    "expires_at": "YYYY-MM-DDTHH:MM:SS+00:00",
    "flags": 2,
    "guild": {
        "id": "XXXXXXXXXXXX",
        "name": "Guild Name",
        "splash": "splash_hash",
        "banner": "banner_hash",
        "description": null,
        "icon": "icon_hash",
        "features": [
            "FEATURE_1",
            "FEATURE_2",
            "FEATURE_3",
            "FEATURE_4",
            "FEATURE_5",
            "FEATURE_6",
            "FEATURE_7",
            "FEATURE_8",
            "FEATURE_9",
            "FEATURE_10",
            "FEATURE_11",
            "FEATURE_12",
            "FEATURE_13"
        ],
        "verification_level": 3,
        "vanity_url_code": "vanityurl",
        "nsfw_level": 0,
        "nsfw": false,
        "premium_subscription_count": 0
    },
    "guild_id": "XXXXXXXXXXXX",
    "channel": {
        "id": "XXXXXXXXXXXX",
        "type": 0,
        "name": "channel_name"
    },
    "new_member": true
}
```
