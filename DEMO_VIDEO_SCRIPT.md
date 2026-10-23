# Nora-Ops Demo Video Script (3 Minutes Max)

**Target Duration:** 2 minutes 45 seconds  
**Tone:** Confident, high-tech, crisp, developer-focused.  
**Screen Setup:** 1080p recording, browser showing `http://localhost:5173` with microphone enabled.

---

### Scene 1: The Problem & Pitch (0:00 - 0:35)
* **Visual:** Full-screen view of the Nora-Ops War Room dashboard with active outage banner (`INCIDENT #AZ-8921: PAYMENT-SERVICE CRITICAL`).
* **Voiceover:**
  > "Production outages are high-stakes, noisy, and chaotic. Engineers lose critical minutes digging through dashboards, runbooks, and past incident reports. 
  > This is **Nora-Ops**—an Enterprise SRE Incident Commander built on the Napster Omniagent API for Microsoft Ignite 2026. 
  > Nora connects directly into our live war room via WebRTC with real-time video, persistent cross-session memory, and live Azure diagnostic tooling."

---

### Scene 2: Live Connection & Persona (0:35 - 1:05)
* **Visual:** Camera zooms to the right-hand panel. Nora's avatar initializes with lip sync. Nora greets the war room.
* **Nora (Voice):**
  > "Hello team. I've joined the war room and am monitoring the latency spike on payment-service."
* **Voiceover:**
  > "Notice Nora's real-time lip-synced video presence. Built with Napster's official Web SDK, she provides a calm, authoritative anchor in high-stress situations."

---

### Scene 3: Distinctive API Feature #1 — Persistent Cross-Session Memory (1:05 - 1:40)
* **Visual:** Engineer speaks into microphone: *"Nora, do you recall how we mitigated this exact memory leak in our last incident?"*
* **Nora (Voice & Video):**
  > "Yes. In last week's post-mortem on October 15th, we found that release candidate 2 introduced an unbounded Redis connection pool. The heap memory steadily climbs to 92% before pods OOMKilled, resulting in 504 gateway timeouts."
* **Voiceover:**
  > "That is Napster's persistent memory in action. Without any manual re-prompting, Nora recalls our incident history across separate sessions."

---

### Scene 4: Distinctive API Feature #2 — Function Tools & Runbook Knowledge (1:40 - 2:15)
* **Visual:** Engineer speaks: *"What does our Azure runbook specify as our rollback target?"*
* **Nora (Voice & Video):**
  > "According to our Azure payment-service runbook, the verified stable rollback target is version v2.0.4 on cluster aks-prod-eastus-01."
* **Engineer speaks:** *"Initiate rollback of payment-service to v2.0.4."*
* **Nora (Voice & Video):**
  > "High-stakes production action detected. Are you sure you want to rollback payment-service from v2.1.0 to v2.0.4?"
* **Engineer speaks:** *"Yes, confirm rollback."*
* **Nora (Voice & Video):**
  > "Executing rollback tool now... Deployment reverted to v2.0.4. Four pods are recycling, and Azure Traffic Manager health checks are recovering."
* **Visual:** The live telemetry stream in the terminal logs the tool execution and latency dropping.

---

### Scene 5: Architecture & Closing (2:15 - 2:45)
* **Visual:** Split screen showing the full-stack architecture: Secure backend token server, REST API integration, and WebRTC streaming.
* **Voiceover:**
  > "Under the hood, our backend enforces enterprise security: the Napster API key never touches the client. Nora leverages Napster Omniagent's WebRTC channel, explicit function routing, and azureOpenAI-grounded runbooks.
  > This isn't just another chatbot—it is an autonomous, persistent teammate built for the future of cloud operations. Thank you!"
