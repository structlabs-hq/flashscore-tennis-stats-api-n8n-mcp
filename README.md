# Flashscore Tennis Stats API — n8n Workflow & MCP Server

Tennis results API for AI agents and automation. Pull match scores, per-set games, durations, winners and the full match statistics table from Flashscore's public tennis feed, with day-window, tour, status and tournament filters.

- **Apify Actor:** [Flashscore Tennis Stats API](https://apify.com/structlabs/flashscore-tennis-stats-api)
- **MCP server:** `https://mcp.apify.com/?actors=structlabs/flashscore-tennis-stats-api`
- **n8n workflow:** [`n8n/flashscore-tennis-stats-api-workflow.json`](n8n/flashscore-tennis-stats-api-workflow.json)
- **Category:** Sports match data
- **Pricing (Gold):** $2.04 per 1,000 matches + $0.05 per 1,000 starts. [Full pricing](https://apify.com/structlabs/flashscore-tennis-stats-api)

## What it returns

One row per match with `match_id`, URL, start time, status, tour, tournament, surface, match type, players, sets won, per-set games and durations, winner, result type, total duration, odds flag and the full `stats` object for the match and each set.

## Quick start with n8n

1. Download [`n8n/flashscore-tennis-stats-api-workflow.json`](n8n/flashscore-tennis-stats-api-workflow.json).
2. In n8n: **Workflows → Import from File**.
3. Add `APIFY_TOKEN` to the n8n environment (Settings → Environment Variables).
4. Open the workflow, set the day/tour/status filters, and run once.
5. The HTTP Request node calls `run-sync-get-dataset-items` and returns the match rows directly.

## Quick start with Python

```bash
export APIFY_TOKEN=<your-token>
python examples/quickstart.py
```

## Quick start with Node.js

```bash
export APIFY_TOKEN=<your-token>
node examples/quickstart.mjs
```

## Input

```json
{
  "dayOffsets": ["0"],
  "tours": ["atp", "wta"],
  "matchStatuses": ["finished"],
  "maxItems": 10
}
```

`dayOffsets` accepts `-7` to `+2`; `0` is today. `tours` accepts `atp`, `wta`, `itf`, `challenger`; an empty array means all tours. `matchStatuses` accepts `finished`, `live`, `scheduled` or `all`. `tournaments` is a case-insensitive partial match on the tournament name.

## Sample output

Three real sanitized rows from a succeeded cloud run are in [`examples/sample_output.json`](examples/sample_output.json). One finished row:

```json
{
  "match_id": "ED4yCVJO",
  "match_url": "https://www.flashscore.com/match/ED4yCVJO/",
  "start_time_utc": "2026-11-22T20:45:00+00:00",
  "status": "finished",
  "tour": "wta",
  "tournament_name": "WTA - SINGLES: Billie Jean King Cup - World Group (World) - Relegation - Play Offs",
  "tournament_url": "https://www.flashscore.com/tennis/wta-singles/billie-jean-king-cup-world-group/",
  "surface": null,
  "match_type": "singles",
  "round": null,
  "note": null,
  "home_player": {
    "name": "Krueger A.",
    "player_id": "jP0X7eBG",
    "slug": "krueger-ashlyn",
    "nationality": "USA",
    "ranking": 200,
    "photo_url": "https://static.flashscore.com/res/image/data/tQDMPh8k-f7v3Inzp.png"
  },
  "away_player": {
    "name": "Nagy A.",
    "player_id": "Oxau6ZuT",
    "slug": "nagy-adrienn",
    "nationality": "Hungary",
    "ranking": 91,
    "photo_url": "https://static.flashscore.com/res/image/data/hn6j94Qq-zyqr0PYl.png"
  },
  "sets_won_home": 2,
  "sets_won_away": 0,
  "sets": [
    {"set": 1, "home_games": 6, "away_games": 2, "duration": "0:30", "winner": "home"},
    {"set": 2, "home_games": 6, "away_games": 1, "duration": "0:29", "winner": "home"}
  ],
  "winner": "home",
  "result_type": "normal",
  "total_duration": "0:59",
  "has_odds": false,
  "stats": {
    "match": {
      "service": {
        "aces": {"home": "7", "away": "3", "home_num": 7, "away_num": 3},
        "double_faults": {"home": "0", "away": "7", "home_num": 0, "away_num": 7}
      },
      "return": {
        "break_points_converted": {"home": "5/9", "away": "1/4", "home_num": 5, "away_num": 1}
      }
    },
    "sets": [
      {"set": 1, "service": {"aces": {"home": "3", "away": "3", "home_num": 3, "away_num": 3}}}
    ]
  },
  "scraped_at": "2026-11-23T10:57:31.957276+00:00"
}
```

Scheduled matches are valid rows too: `sets` is empty and `stats` is `null`. Player names are public sports data; no contact details are collected.

## Use cases

- Daily tennis results and set-score feed for a dashboard.
- Match-stat comparisons for betting research or content.
- Tournament or tour monitoring across ATP, WTA, ITF and Challenger.
- Feed finished matches into Sheets, Airtable, Postgres or an LLM agent.

## MCP configuration

Copy [`mcp/mcp_config.json`](mcp/mcp_config.json) into your MCP client (Claude Desktop, Cursor, Windsurf):

```json
{
  "mcpServers": {
    "apify-flashscore-tennis-stats-api": {
      "url": "https://mcp.apify.com/?actors=structlabs/flashscore-tennis-stats-api"
    }
  }
}
```

## Feed token note

The public feed uses the client header `x-fsign: SW9D1eZo`. It is not a user login or API key. If Flashscore rotates it, re-extract the current value from the public site and update the Actor.

## Links

- Apify Store: https://apify.com/structlabs/flashscore-tennis-stats-api
- n8n: https://n8n.io
- MCP: https://modelcontextprotocol.io

## License

MIT
