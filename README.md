# Twitter Likes Exporter

Automatically sync and export Twitter/X likes using GitHub Actions.

## Setup

### 1. Get Your Twitter Cookies

1. Open browser and log in to x.com
2. Open DevTools (F12) → Application → Cookies → https://x.com
3. Copy these values:
   - `auth_token`
   - `ct0`
4. Get your User ID from: https://x.com/settings/your_account

### 2. Add GitHub Secrets

Go to Settings → Secrets and variables → Actions → New repository secret:

| Secret Name | Value |
|-------------|-------|
| `X_AUTH_TOKEN` | Your auth_token from cookies |
| `X_CT0` | Your ct0 from cookies |
| `X_USER_ID` | Your Twitter user ID |

### 3. Run

The workflow runs automatically every 6 hours.

Or trigger manually:
- Go to Actions → Sync Twitter Likes → Run workflow
- Optional: Select "Full sync" to reset and fetch all likes

### 4. Results

Export files in `exports/` branch:
- `likes.json` - Full JSON export
- `likes_links.txt` - Plain text list of tweet URLs

## Notes

- Twitter cookies expire periodically. Update secrets when sync fails.
- Rate limits may apply. Large like counts take longer.
