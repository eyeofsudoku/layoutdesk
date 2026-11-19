# Layout Desk

layoutdesk.bearblog.dev: the work journal of DTP Services Berlin, published to Bear Blog through the Bear API.

- `posts/`: one Markdown file per article, with a short header (title, slug, date, tags, meta_description).
  The `date` can be in the past; Bear shows the post under that date.
- `blog.json`: blog title, home page text and navigation.
- `publish.py`: sends posts and settings to Bear. Edited files update the existing post.
- `posts/published.json`: written by the workflow; links each slug to its Bear post. Don't edit by hand.

Every push that changes a post or `blog.json` publishes automatically.
Settings: repo secret `BEAR_API_KEY` (the key of the layoutdesk blog).

House rules for articles: real jobs only, never a client name or anything that identifies one,
first person "I" (never "we"), UK English, no em dashes, one or two links to dtp-services.de
plus one useful outside resource (never a competitor), written and checked with the no-ai-tells rules.
