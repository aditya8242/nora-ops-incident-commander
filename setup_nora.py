#!/usr/bin/env python3
"""
Automated Setup for Nora - Azure Incident Commander Omniagent
Executes Steps 2, 3, 4, 5, 6, and 7 against the Napster Omniagent API.
"""

import os
import sys
import json
import urllib.request
import urllib.error

# Ensure UTF-8 output
sys.stdout.reconfigure(encoding='utf-8')

API_BASE = "https://companion-api.napster.com"
PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
ENV_FILE = os.path.join(PROJECT_DIR, ".env")

def load_env():
    env_vars = {}
    if os.path.exists(ENV_FILE):
        with open(ENV_FILE, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#") and "=" in line:
                    k, v = line.split("=", 1)
                    env_vars[k.strip()] = v.strip().strip("'\"")
    return env_vars

def save_env_var(key, value):
    env_vars = load_env()
    env_vars[key] = value
    lines = [f"{k}={v}\n" for k, v in env_vars.items()]
    with open(ENV_FILE, "w", encoding="utf-8") as f:
        f.writelines(lines)
    # Also sync local-token-server/.env
    token_env = os.path.join(PROJECT_DIR, "local-token-server", ".env")
    if os.path.exists(os.path.dirname(token_env)):
        with open(token_env, "w", encoding="utf-8") as f:
            f.writelines(lines)
    print(f"  [Config] Saved {key}={value[:12]}... to .env")

def api_request(method, endpoint, data=None, api_key=None):
    url = f"{API_BASE}{endpoint}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
        "Content-Type": "application/json"
    }
    if api_key:
        headers["X-Api-Key"] = api_key

    body = json.dumps(data).encode("utf-8") if data else None
    req = urllib.request.Request(url, data=body, headers=headers, method=method)

    try:
        with urllib.request.urlopen(req) as response:
            res_body = response.read().decode("utf-8")
            return json.loads(res_body) if res_body else {}
    except urllib.error.HTTPError as e:
        err_msg = e.read().decode("utf-8")
        print(f"  [API Error {e.code}] {method} {endpoint}: {err_msg}")
        raise e

def main():
    print("================================================================")
    print("   Nora-Ops: Napster Omniagent Automated Provisioning Script    ")
    print("================================================================")

    env = load_env()
    api_key = env.get("NAPSTER_API_KEY")

    if not api_key:
        print("\n[!] NAPSTER_API_KEY is not set in .env.")
        print(f"    Please double-click Edit-Napster-Key.bat on your Desktop or open:")
        print(f"    {ENV_FILE}")
        print("    Paste your key after NAPSTER_API_KEY= and run this script again.\n")
        sys.exit(1)

    print("\n[Step 2] Verifying API Key authentication...")
    try:
        stock = api_request("GET", "/public/companions/napster-stock?pageSize=1", api_key=api_key)
        print("  [+] API Key verified successfully! (HTTP 200 OK)")
    except Exception as e:
        print(f"  [-] Failed to authenticate with Napster API. Please check your key.")
        sys.exit(1)

    # Step 3: Choose or Create Persona
    print("\n[Step 3] Configuring Persona (Nora - SRE Incident Commander)...")
    companion_id = env.get("COMPANION_ID")
    if not companion_id:
        # Check existing custom companions
        try:
            comps = api_request("GET", "/public/companions", api_key=api_key)
            existing = [c for c in (comps if isinstance(comps, list) else comps.get("items", [])) if c.get("firstName") == "Nora"]
            if existing:
                companion_id = existing[0]["id"]
                print(f"  [+] Found existing Nora companion: {companion_id}")
            else:
                # Create custom Nora companion
                payload = {
                    "firstName": "Nora",
                    "lastName": "Vance",
                    "description": "A calm, senior Site Reliability Engineer and Azure Incident Commander. Patient, sharp, and highly technical. Helps engineers troubleshoot production outages, references past incident post-mortems from memory, diagnoses telemetry metrics, and executes rollbacks.",
                    "gender": "female"
                }
                res = api_request("POST", "/public/companions", data=payload, api_key=api_key)
                companion_id = res.get("id")
                print(f"  [+] Created custom Nora companion: {companion_id}")
        except Exception as e:
            # Fallback to first stock companion
            stock_items = stock if isinstance(stock, list) else stock.get("items", [])
            companion_id = stock_items[0]["id"] if stock_items else "comp_stock_default"
            print(f"  [*] Using stock companion as fallback: {companion_id}")

        save_env_var("COMPANION_ID", companion_id)
    else:
        print(f"  [+] Using existing companion ID: {companion_id}")

    # Step 5: Create Explicit & Implicit SRE Tools
    print("\n[Step 5] Defining SRE Diagnostics Tools...")
    function_ids = []

    tools_to_create = [
        {
            "name": "check_service_health",
            "description": "Inspect live pod health, heap memory usage, and Redis connection pool status for an Azure microservice.",
            "parameters": {
                "type": "object",
                "properties": {
                    "service": {"type": "string", "description": "The service name, e.g. payment-service"}
                },
                "required": ["service"]
            },
            "prompt": "When to use: When the user asks to check service health, pod heap usage, or why payment-service is degraded. When NOT to use: For general questions. Use the preamble pattern: say 'Checking the Azure telemetry and pod health now' before calling.",
            "flow": "implicit"
        },
        {
            "name": "trigger_service_rollback",
            "description": "Revert an AKS deployment to a prior stable version tag.",
            "parameters": {
                "type": "object",
                "properties": {
                    "service": {"type": "string", "description": "Service to rollback, e.g. payment-service"},
                    "targetVersion": {"type": "string", "description": "Target version tag, e.g. v2.0.4"}
                },
                "required": ["service", "targetVersion"]
            },
            "prompt": "When to use: When the user instructs to roll back a service deployment. Confirmation pattern: You MUST explicitly ask the user for confirmation ('Are you sure you want to rollback payment-service to v2.0.4?') and wait for their confirmation before calling.",
            "flow": "implicit"
        }
    ]

    for tool in tools_to_create:
        try:
            tool_payload = {
                "data": {
                    "name": tool["name"],
                    "description": tool["description"],
                    "parameters": tool["parameters"]
                },
                "flow": tool["flow"],
                "prompt": tool["prompt"]
            }
            fn_res = api_request("POST", "/public/functions", data=tool_payload, api_key=api_key)
            fn_id = fn_res.get("id")
            if fn_id:
                function_ids.append(fn_id)
                print(f"  [+] Created tool '{tool['name']}': {fn_id}")
        except Exception as e:
            print(f"  [*] Tool '{tool['name']}' setup note: {e}")

    # Step 6: Create FAQs & Knowledge Base
    print("\n[Step 6] Configuring SRE Runbook Knowledge...")
    faq_collection_id = None
    try:
        faq_payload = {
            "name": "Azure Payment-Service Runbook FAQs",
            "faqs": [
                {
                    "question": "What is the stable rollback target for payment-service?",
                    "answer": "The stable rollback target for payment-service is release v2.0.4, running on AKS cluster aks-prod-eastus-01."
                },
                {
                    "question": "What causes the p99 latency spike and 504 errors in payment-service?",
                    "answer": "The latency spike is caused by an unbounded Redis connection pool and memory leak introduced in v2.1.0-rc2, causing pod heap exhaustion and pod restarts."
                },
                {
                    "question": "What is the SLA threshold for payment-service?",
                    "answer": "The SLO is 99.95% availability with p99 latency strictly under 250ms and HTTP error rate below 0.05%."
                }
            ]
        }
        faq_res = api_request("POST", "/public/faqs", data=faq_payload, api_key=api_key)
        faq_collection_id = faq_res.get("id")
        print(f"  [+] Created FAQ collection: {faq_collection_id}")
    except Exception as e:
        print(f"  [*] FAQ setup note: {e}")

    # Step 4: Assemble the Omniagent
    print("\n[Step 4] Assembling the Omniagent (Nora)...")
    agent_id = env.get("AGENT_ID")
    if not agent_id:
        agent_payload = {
            "companionId": companion_id,
            "name": "Nora - Azure Incident Commander",
            "voiceId": "alloy",
            "language": "en",
            "providerSettings": {
                "temperature": 0.7,
                "turnDetection": {
                    "threshold": 0.9,
                    "prefix_padding_ms": 400,
                    "silence_duration_ms": 500
                },
                "noiseReduction": {
                    "type": "nearField"
                }
            }
        }
        if function_ids:
            agent_payload["functions"] = function_ids
        if faq_collection_id:
            agent_payload["faqCollections"] = [faq_collection_id]

        try:
            agent_res = api_request("POST", "/public/agents", data=agent_payload, api_key=api_key)
            agent_id = agent_res.get("id")
            print(f"  [+] Successfully assembled Omniagent: {agent_id}")
            save_env_var("AGENT_ID", agent_id)
        except Exception as e:
            print(f"  [-] Failed to create agent: {e}")
            sys.exit(1)
    else:
        print(f"  [+] Using existing AGENT_ID: {agent_id}")

    # Step 7: WebRTC Channel Configuration
    print("\n[Step 7] Activating WebRTC channel for Agent...")
    try:
        channel_payload = {}
        api_request("PUT", f"/public/agents/{agent_id}/channels/webrtc", data=channel_payload, api_key=api_key)
        print("  [+] WebRTC channel verified and active!")
    except Exception as e:
        print(f"  [*] WebRTC channel note: {e}")

    print("\n================================================================")
    print("   Provisioning Complete! Ready to launch War Room Console.    ")
    print("================================================================")
    print("Run: npm start (or node local-token-server/token-server.js)")
    print("Then open: http://localhost:5173 in Google Chrome or Microsoft Edge")
    print("================================================================")

if __name__ == "__main__":
    main()
