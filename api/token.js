export default async function handler(req, res) {
  res.setHeader('Access-Control-Allow-Credentials', true);
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'GET,OPTIONS,POST');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type, X-Api-Key');

  if (req.method === 'OPTIONS') {
    res.status(200).end();
    return;
  }

  const NAPSTER_API_KEY = process.env.NAPSTER_API_KEY;
  const AGENT_ID = process.env.AGENT_ID || '132c2e86-432b-4507-bc8b-a34e95e1ff5c';

  if (!NAPSTER_API_KEY) {
    res.status(500).json({ error: 'Missing NAPSTER_API_KEY in Vercel environment variables.' });
    return;
  }

  try {
    const response = await fetch(`https://companion-api.napster.com/public/agents/${AGENT_ID}/connections`, {
      method: 'POST',
      headers: {
        'X-Api-Key': NAPSTER_API_KEY,
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0'
      },
      body: JSON.stringify({ channelType: 'webrtc' })
    });

    if (!response.ok) {
      const errText = await response.text();
      res.status(response.status).json({ error: errText });
      return;
    }

    const data = await response.json();
    res.status(200).json(data);
  } catch (err) {
    res.status(500).json({ error: String(err.message || err) });
  }
}