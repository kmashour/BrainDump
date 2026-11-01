import re
import os

source_file = "inflow/udemy_transcript_802576.txt"
output_dir = "inflow/AZ-104-ScottDuffy"
os.makedirs(output_dir, exist_ok=True)

modules = [
    {
        "id": "01",
        "file": "01_Course_Introduction_Budgeting_and_Tooling.md",
        "title": "Module 01: Course Introduction, Budgeting, and Admin Tooling",
        "start": 1,
        "end": 649,
        "topics": "AZ-104 Certification Guide, Azure Free Account, Cost Budgeting, PowerShell Core, Az Module, Azure CLI"
    },
    {
        "id": "02",
        "file": "02_Administer_Identity_Entra_ID.md",
        "title": "Module 02: Administer Identity (Microsoft Entra ID)",
        "start": 650,
        "end": 3861,
        "topics": "Entra ID (Azure AD), Free vs Premium P1/P2, Custom Domains, Users, Groups, Licenses, Administrative Units, Devices, Bulk Operations, External Users, SSPR"
    },
    {
        "id": "03",
        "file": "03_Administer_Governance_and_Compliance.md",
        "title": "Module 03: Administer Governance and Compliance",
        "start": 3862,
        "end": 5836,
        "topics": "RBAC Built-in and Custom Roles, Scopes, Access Assignments, Storage RBAC, Subscriptions, Management Groups, Cost Management & Advisor, Resource Locks, Azure Policy, Custom Policies, Tags, Resource Move"
    },
    {
        "id": "04",
        "file": "04_Administer_Azure_Storage.md",
        "title": "Module 04: Administer Azure Storage",
        "start": 5837,
        "end": 7611,
        "topics": "Storage Accounts, Redundancy (LRS/ZRS/GRS), Access Tiers, Networking & Firewalls, Data Protection, Encryption, Blobs, Files, Queues, Tables, Access Keys, SAS, Stored Access Policies, Entra ID RBAC, Lifecycle Management, Object Replication, AzCopy, Azure Files & Snapshots"
    },
    {
        "id": "05",
        "file": "05_Administer_Azure_Virtual_Machines_and_VMSS.md",
        "title": "Module 05: Administer Azure Virtual Machines and VMSS",
        "start": 7612,
        "end": 10139,
        "topics": "VM Provisioning, OS & Data Disks, Networking, Resizing, Availability Sets & Zones, Azure Bastion, VMSS Manual & Autoscale, PowerShell VM Creation, Linux VM Web Server Lab"
    },
    {
        "id": "06",
        "file": "06_Administer_Automation_ARM_Templates_and_Bicep.md",
        "title": "Module 06: Automate Resource Deployment with ARM Templates and Bicep",
        "start": 10140,
        "end": 11786,
        "topics": "ARM Templates Syntax, Template Specs, PowerShell Deployment, Custom Script Extensions, Existing VHDs, Azure Bicep Authoring & Deployment in VS Code, ARM Decompilation to Bicep, VM SSE & ADE Encryption"
    },
    {
        "id": "07",
        "file": "07_Administer_PaaS_Compute_App_Services_and_Containers.md",
        "title": "Module 07: Administer PaaS Compute (App Services, Containers & Apps)",
        "start": 11787,
        "end": 13978,
        "topics": "App Service Plans, Web App Creation & Settings, Scaling Up/Out, Deployment Slots, Backups, Custom Domains, TLS/SSL, App Service VNet Integration, ACI Container Instances, Container Groups, Azure Container Apps, ACR, Docker Pull/Push"
    },
    {
        "id": "08",
        "file": "08_Administer_Virtual_Networking_and_InterSite_Connectivity.md",
        "title": "Module 08: Administer Virtual Networking and Intersite Connectivity",
        "start": 13979,
        "end": 15754,
        "topics": "Virtual Networks, Subnets, Public IPs, NICs, RDP Port Management, Global VNet Peering, Virtual Network Gateways, VNet-to-VNet VPN Connections, Azure DNS Public and Private Zones, Custom Domain Mapping"
    },
    {
        "id": "09",
        "file": "09_Administer_Network_Traffic_Security_and_Load_Balancing.md",
        "title": "Module 09: Administer Network Traffic, Security and Load Balancing",
        "start": 15755,
        "end": 17389,
        "topics": "Network Security Groups (NSGs), Effective Rules, Application Security Groups (ASGs), Network Watcher Diagnostics, Azure Standard Load Balancer, Backend Pools, Health Probes, Troubleshooting, Application Gateway v2"
    },
    {
        "id": "10",
        "file": "10_Administer_Monitoring_and_Log_Analytics.md",
        "title": "Module 10: Administer Monitoring and Log Analytics",
        "start": 17390,
        "end": 18183,
        "topics": "Azure Monitor Architecture, Diagnostic Settings, VM Insights, Log Analytics Workspace, Kusto Query Language (KQL) Queries, Metric Alerts, Traffic Management Lab"
    },
    {
        "id": "11",
        "file": "11_Administer_Data_Protection_Backup_and_Recovery.md",
        "title": "Module 11: Administer Data Protection, Backup and Site Recovery",
        "start": 18184,
        "end": 19661,
        "topics": "Azure Backup, Recovery Services Vault, Manual & Scheduled VM Backups, File-Level Recovery, Full VM Restore, On-Premises Backup, Soft Delete, Azure Site Recovery (ASR) Replication & Test Failovers"
    },
    {
        "id": "12",
        "file": "12_AZ104_Last_Minute_Study_Review_and_Exam_Strategies.md",
        "title": "Module 12: AZ-104 Domain Review, Exam Strategies and Certification",
        "start": 19662,
        "end": 24731,
        "topics": "Comprehensive Domain Reviews: Identity, Governance, Storage, Compute, Networking, Monitoring; Certification Renewal, AI-Assisted Study, Practice Questions"
    }
]

with open(source_file, "r", encoding="utf-8", errors="ignore") as f:
    all_lines = f.readlines()

def clean_transcript_lines(lines_slice):
    cleaned = []
    prev_blank = False
    for line in lines_slice:
        stripped = line.strip()
        # skip standalone subtitle index numbers (e.g. 1, 2, 105)
        if re.match(r"^\d+$", stripped):
            continue
        # handle section headers
        if stripped.startswith("=== ") and stripped.endswith(" ==="):
            sec_name = stripped.strip("= ")
            cleaned.append(f"\n## 🏛️ Section: {sec_name}\n")
            prev_blank = False
            continue
        # handle lesson headers
        if stripped.startswith("--- ") and stripped.endswith(" ---"):
            les_name = stripped.strip("- ")
            cleaned.append(f"\n### 📺 Lesson: {les_name}\n")
            prev_blank = False
            continue
        if stripped == "":
            if not prev_blank:
                cleaned.append("")
                prev_blank = True
        else:
            cleaned.append(line.rstrip())
            prev_blank = False
    return "\n".join(cleaned)

for mod in modules:
    mod_lines = all_lines[mod["start"]-1 : mod["end"]]
    cleaned_body = clean_transcript_lines(mod_lines)
    
    frontmatter = f"""---
obsidianUIMode: preview
class: inflow-note
tier: inflow
domains:
  - azure
  - az-104
course: "AZ-104: Microsoft Azure Administrator"
instructor: "Scott Duffy"
module_id: "{mod['id']}"
title: "{mod['title']}"
source: "Udemy - AZ-104 Microsoft Azure Administrator (Scott Duffy)"
tags:
  - azure/az-104
  - status/raw
---

# {mod['title']}

**Instructor:** Scott Duffy  
**Course:** AZ-104 Microsoft Azure Administrator  
**Key Topics:** {mod['topics']}  
**Line Range:** Lines {mod['start']} – {mod['end']} of master transcript  

---

## 📋 Module Overview & Cleaned Transcripts

{cleaned_body}
"""
    dest_path = os.path.join(output_dir, mod["file"])
    with open(dest_path, "w", encoding="utf-8") as out:
        out.write(frontmatter)
    print(f"Generated: {dest_path} ({len(mod_lines)} raw lines)")

print("\nSuccessfully split all 12 modules into inflow/AZ-104-ScottDuffy/!")
