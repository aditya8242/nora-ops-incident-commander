# Nora-Ops: Azure Incident Commander Omniagent
### Napster API Ignite Hackathon 2026 — Official Submission Summary

**Entrant:** Individual Entry  
**Category:** Enterprise AI / Azure Native Integration  
**Channel Architecture:** WebRTC (Real-time Audio & Video Avatar) + Persistent Memory + Function Actions  

---

### 1. What We Built & The Problem It Solves
When mission-critical cloud services suffer an outage, every second in the engineering War Room is dominated by chaos, fragmented metrics, and delayed escalations. Traditional incident response relies on engineers frantically digging through documentation, parsing Grafana dashboards, and context-switching across consoles.

**Nora-Ops** is an Enterprise SRE Incident Commander Omniagent powered by the Napster API. Nora enters the incident War Room as an authoritative, real-time WebRTC video avatar. She continuously diagnoses production health, recalls prior incident post-mortems across sessions, explains root causes via ingested Azure runbooks, and executes safety-gated infrastructure rollbacks through voice commands.

### 2. Who It's For & What They Were Doing Before
Nora is built for Site Reliability Engineers (SREs), DevOps teams, and Cloud Operations leads managing Azure and Kubernetes infrastructure. Before Nora, on-call engineers operated under high cognitive load: manually cross-referencing telemetry alerts with static runbooks, guessing whether a current memory leak resembled an incident from weeks prior, and manually running kubectl/CLI commands with high error risk during high-stress outages.

### 3. Napster API Capabilities Used & Why They Matter
Nora exploits the distinct capabilities of the Napster Omniagent platform that generic LLMs cannot deliver:
- **Persistent Cross-Session Memory**: Nora recognizes historical incident patterns. When a memory leak surfaces in `payment-service`, Nora references the resolution from previous incident post-mortems unprompted.
- **Real-Time WebRTC Video Avatar & Voice**: Lip-synced, photorealistic presence provides a calm, steady commander in high-stress war rooms, reducing alert fatigue.
- **Knowledge Bases & Curated FAQs**: Ingests Azure Kubernetes runbooks and SLA escalation thresholds, grounding technical decisions in authoritative company protocol.
- **Explicit & Implicit Function Tools**: Real-time diagnostic hooks (`check_service_health`, `query_azure_telemetry`, `trigger_service_rollback`, `file_incident_postmortem`).
- **Confirmation Safety Pattern**: High-stakes rollback actions require explicit voice confirmation before mutating production state.

### 4. Key Technical Decisions & Tradeoffs
- **Decoupled Security Gateway**: Server-side token exchange ensures `NAPSTER_API_KEY` never reaches the browser client, issuing ephemeral session tokens.
- **Near-Field Noise Reduction & Turn Detection**: Configured 500ms silence detection and 0.9 threshold in `providerSettings` to enable crisp, natural verbal interruptions during urgent war-room exchanges.
- **Canonical Panel Design**: Integrated the official Napster design system with an Azure Operations dark-mode cockpit.

### 5. What We Would Build Next
With additional time, we will expand Nora across Napster’s VoIP channel (Twilio integration) for automated on-call telephone paging during P0 emergencies, and integrate Edge MCP to allow Nora to visually inspect and manipulate live Azure Portal blades directly within the browser session.
