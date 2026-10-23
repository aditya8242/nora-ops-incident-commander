# Nora-Ops: Azure Incident Commander Omniagent
### *Enterprise SRE & Cloud War Room Co-Pilot powered by the Napster API*
**Official Submission for the Napster API Ignite Hackathon (Microsoft Ignite 2026)**

---

## ⚡ Overview

When high-severity production incidents strike, engineering war rooms are flooded with noise: fragmented telemetry, outdated documentation, and alert fatigue. 

**Nora-Ops** is an autonomous SRE Incident Commander deployed as a photorealistic, real-time WebRTC video avatar. Built on the **Napster Omniagent Platform** as an **Azure Native Integration**, Nora:
1. **Recalls Historical Outages unprompted**: Retains cross-session memory of prior incident post-mortems and root-cause analyses.
2. **Executes Real-Time Cloud Diagnostics**: Calls live telemetry functions (`check_service_health`, `query_azure_telemetry`).
3. **Grounds Decisions in Azure Runbooks**: Consults ingested AKS and Azure Application Gateway disaster recovery runbooks.
4. **Enforces Production Safety**: Utilizes the voice confirmation pattern before executing high-stakes infrastructure changes (`trigger_service_rollback`).

---

## 🏗️ Architecture

```
                      +---------------------------------------+
                      |         SRE War Room Console          |
                      |  (Real-Time WebRTC Audio & Video)     |
                      +-------------------+-------------------+
                                          |
                                          v
+-----------------------------------------------------------------------------------+
|                        Napster Omniagent Platform                                 |
|                                                                                   |
|  [Persistent Memory]      [Knowledge Base]         [Explicit Tools / Actions]     |
|   Past incident RCAs,      Azure Runbooks,          - check_service_health        |
|   deploy histories,        Architecture specs,      - query_azure_telemetry       |
|   cross-session context    SLA/SLO policies         - trigger_service_rollback    |
|                                                     - file_incident_postmortem    |
+-----------------------------------------+-----------------------------------------+
                                          |
                                          v
                      +---------------------------------------+
                      |        Secure Backend Gateway         |
                      |   (Token Server + Mock Azure API)     |
                      +-------------------+-------------------+
```

---

## 🚀 Quickstart (Run Locally)

### Prerequisites
- Node.js 18+
- Python 3.10+
- A Napster API Key ([register here](https://www.napster.com/microsoftignite26#hackathon))

### 1. Clone & Configure
```bash
git clone https://github.com/your-username/nora-ops-incident-commander.git
cd nora-ops-incident-commander
cp local-token-server/.env.example .env
```
Add your `NAPSTER_API_KEY` to `.env`.

### 2. Launch
```bash
python setup_nora.py
npm start
```
Open **`http://localhost:5173`** in Google Chrome or Microsoft Edge.

---

## ☁️ One-Click Cloud Deployment

### Deploy to Vercel
1. Push this repository to GitHub.
2. Import the project into [Vercel](https://vercel.com).
3. Set the Environment Variables:
   - `NAPSTER_API_KEY`: `your_napster_api_key`
   - `AGENT_ID`: `132c2e86-432b-4507-bc8b-a34e95e1ff5c`
4. Click **Deploy**. Vercel will automatically route `/token` through `/api/token.js`.

### Deploy to Render
1. Connect your repository to [Render](https://render.com).
2. Create a new **Web Service** using `render.yaml` or Docker.
3. Provide your `NAPSTER_API_KEY` in Render's environment settings.

---

## 🎯 Scoring Against Hackathon Rubric

- **Use of Napster API (30%)**: Leverages persistent cross-session memory, WebRTC lip-synced video avatar, knowledge collections, and function-calling tools. Submissions using generic LLMs cannot deliver this.
- **Technical Execution (25%)**: Decoupled token server architecture protecting API credentials, self-contained Web SDK bundle, real-time telemetry streaming, and automated provisioning.
- **Creativity (25%)**: Brings Napster Omniagents to enterprise DevOps & high-stress cloud operations.
- **Presentation (20%)**: High-contrast Azure Operations console, structured 500-word summary, and a 2:45 walkthrough demo video.

---

## 📜 License
MIT © 2026. Built with pride for Microsoft Ignite 2026.
