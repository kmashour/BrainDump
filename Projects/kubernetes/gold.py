#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import os
import json
import subprocess

# Import database records
try:
    from study_data import STUDY_QUESTIONS
    from scenarios_data import SCENARIOS
except ImportError:
    print("Error: Missing database files (study_data.py or scenarios_data.py) in the current directory.")
    sys.exit(1)

# ANSI Colors
BLUE = "\033[94m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
CYAN = "\033[96m"
BOLD = "\033[1m"
RESET = "\033[0m"

PROGRESS_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), ".progress-adv.json")
# Reference to config in peer directory
KIND_CONFIG = "/home/karim/Desktop/BrainDump/Projects/CKA/kubernetes-Gold/kind-3node-config.yaml"

def load_progress():
    if os.path.exists(PROGRESS_FILE):
        try:
            with open(PROGRESS_FILE, 'r') as f:
                return json.load(f)
        except Exception:
            return {}
    return {}

def save_progress(progress):
    try:
        with open(PROGRESS_FILE, 'w') as f:
            json.dump(progress, f)
    except Exception as e:
        print(f"Error saving progress: {e}")

def run_cmd(cmd, check=False):
    res = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if check and res.returncode != 0:
        raise Exception(res.stderr)
    return res

def check_cluster_active():
    context_res = run_cmd("kubectl config current-context")
    if "kind-cka-gold" not in context_res.stdout:
        return False
    node_res = run_cmd("kubectl get nodes")
    return node_res.returncode == 0

def init_cluster():
    print(f"\n{BOLD}{CYAN}=== Initializing 3-Node Advanced Cluster ==={RESET}")
    print("Checking if cka-gold cluster already exists...")
    clusters = run_cmd("kind get clusters").stdout
    if "cka-gold" in clusters:
        print(f"{YELLOW}Deleting existing 'cka-gold' cluster...{RESET}")
        run_cmd("kind delete cluster --name cka-gold")
    
    print(f"Creating KinD cluster using {KIND_CONFIG}...")
    create_res = run_cmd(f"kind create cluster --config={KIND_CONFIG}")
    if create_res.returncode != 0:
        print(f"{RED}Failed to create KinD cluster:{RESET}\n{create_res.stderr}")
        return False
    
    print(f"{GREEN}Cluster created successfully! Setting context...{RESET}")
    run_cmd("kubectl config use-context kind-cka-gold")
    
    print("Waiting for cluster nodes to settle...")
    run_cmd("kubectl wait --for=condition=Ready nodes --all --timeout=60s")
    
    print(f"{BOLD}{GREEN}Advanced cluster is active!{RESET}\n")
    return True

def reset_cluster():
    if not check_cluster_active():
        print(f"{RED}Cluster 'cka-gold' is inactive.{RESET}")
        return
    print(f"\n{BOLD}{YELLOW}=== Sweeping Advanced Configurations ==={RESET}")
    
    # Delete webhooks
    print("Cleaning webhook configurations...")
    run_cmd("kubectl delete validatingwebhookconfiguration validate-webhook --ignore-not-found=true")
    run_cmd("kubectl delete mutatingwebhookconfiguration mutate-webhook --ignore-not-found=true")
    
    # Delete CRDs
    print("Cleaning CRDs...")
    run_cmd("kubectl delete crd crontabs.stable.example.com --ignore-not-found=true")
    
    # Delete Gateway API
    print("Cleaning Gateway API...")
    run_cmd("kubectl delete httproute app-route --ignore-not-found=true")
    run_cmd("kubectl delete gateway test-gateway --ignore-not-found=true")
    
    # Delete RuntimeClasses & priority
    print("Cleaning custom Node/Priority configurations...")
    run_cmd("kubectl delete runtimeclass gvisor --ignore-not-found=true")
    run_cmd("kubectl delete priorityclass high-priority --ignore-not-found=true")
    
    # Delete APIService
    run_cmd("kubectl delete apiservice v1beta1.custom.metrics.k8s.io --ignore-not-found=true")
    
    # Clean namespaces (except system)
    ns_res = run_cmd("kubectl get ns -o jsonpath='{.items[*].metadata.name}'").stdout.split()
    for ns in ns_res:
        if ns not in ["default", "kube-system", "kube-public", "kube-node-lease"]:
            run_cmd(f"kubectl delete namespace {ns} --timeout=15s --ignore-not-found=true")
            
    # Clean default resources
    resources = ["deployments", "pods", "services", "ingress", "daemonsets", "statefulsets", "replicasets", "jobs", "cronjobs", "configmaps", "secrets", "pv", "pvc", "netpol", "lease"]
    for r in resources:
        run_cmd(f"kubectl delete {r} --all -n default --timeout=10s --ignore-not-found=true")
        
    print(f"{GREEN}Advanced cluster reset completed.{RESET}")

def setup_scenario(scenario_id):
    if not check_cluster_active():
        print(f"{RED}Error: Cluster 'cka-gold' is inactive. Initialize it to context first.{RESET}")
        return False
    
    sc = next((s for s in SCENARIOS if s["id"] == scenario_id), None)
    if not sc:
        print(f"{RED}Scenario {scenario_id} not found.{RESET}")
        return False
    
    print(f"\n{YELLOW}Injecting configuration for {BOLD}{sc['title']}{RESET}...")
    if "cleanup" in sc and sc["cleanup"]:
        run_cmd(sc["cleanup"])
        
    res = run_cmd(sc["setup"])
    if res.returncode == 0:
        print(f"{GREEN}Advanced scenario injected!{RESET}")
        return True
    else:
        print(f"{RED}Setup failed:{RESET}\n{res.stderr}")
        return False

def check_scenario(scenario_id):
    if not check_cluster_active():
        print(f"{RED}Error: Cluster 'cka-gold' is inactive.{RESET}")
        return False
        
    sc = next((s for s in SCENARIOS if s["id"] == scenario_id), None)
    if not sc:
        print(f"{RED}Scenario {scenario_id} not found.{RESET}")
        return False
        
    print(f"\n{YELLOW}Checking solution for {BOLD}{sc['title']}{RESET}...")
    res = run_cmd(sc["check"])
    if res.returncode == 0:
        print(f"{BOLD}{GREEN}★ PASS: Scenario resolved correctly.{RESET}")
        return True
    else:
        print(f"{BOLD}{RED}❌ FAIL: Challenge not fully solved yet.{RESET}")
        return False

def get_stats(progress):
    completed_study = sum(1 for q in STUDY_QUESTIONS if progress.get(q["id"]))
    completed_env = sum(1 for s in SCENARIOS if progress.get(s["id"]))
    total_q = len(STUDY_QUESTIONS) + len(SCENARIOS)
    total_completed = completed_study + completed_env
    percent = (total_completed / total_q) * 100 if total_q > 0 else 0
    return completed_study, completed_env, total_completed, total_q, percent

def print_header(cluster_active, progress):
    os.system('clear' if os.name == 'posix' else 'cls')
    c_status = f"{GREEN}ACTIVE{RESET}" if cluster_active else f"{RED}INACTIVE/MISSING{RESET}"
    comp_s, comp_e, comp_tot, tot, pct = get_stats(progress)
    
    print("=" * 60)
    print(f"🚀 {BOLD}ADVANCED KUBERNETES PLAYBOOK: INTERACTIVE DECK{RESET} 🚀")
    print("=" * 60)
    print(f"Cluster Context: {BOLD}kind-cka-gold{RESET} | Status: {c_status}")
    print(f"Overall Progress: {BOLD}{comp_tot}/{tot} Solved ({pct:.1f}%){RESET}")
    print(f"  └─ Study Q&A: {comp_s}/{len(STUDY_QUESTIONS)} | Environment Scenarios: {comp_e}/{len(SCENARIOS)}")
    print("=" * 60)

def main_menu():
    progress = load_progress()
    while True:
        cluster_active = check_cluster_active()
        print_header(cluster_active, progress)
        
        domains = [
            "Advanced API & Extensions / Webhooks",
            "CKS Security & Container Isolation",
            "Advanced Services & Routing (Gateway API)",
            "Advanced Workloads & Scheduling",
            "Advanced Cluster Administration"
        ]
        
        print("Select Advanced Topic to practice:")
        for idx, d in enumerate(domains, 1):
            print(f" {idx}. {d}")
        print("-" * 60)
        print(" 6. Initialize / Create shared cka-gold Cluster")
        print(" 7. Re-verify Cluster Connection")
        print(" 8. Reset Cluster (Wipe advanced resources)")
        print(" 9. Exit")
        print("=" * 60)
        
        choice = input(f"{BOLD}Enter choice [1-9]: {RESET}").strip()
        if choice in [str(i) for i in range(1, 6)]:
            domain_idx = int(choice) - 1
            domain_menu(domains[domain_idx], progress)
        elif choice == "6":
            init_cluster()
            input("\nPress Enter to return to main menu...")
        elif choice == "7":
            print("\nRe-verifying cluster context...")
            if check_cluster_active():
                print(f"{GREEN}Cluster is active!{RESET}")
            else:
                print(f"{RED}Cluster is offline.{RESET}")
            input("\nPress Enter to return...")
        elif choice == "8":
            reset_cluster()
            input("\nPress Enter to return...")
        elif choice == "9":
            print("\nExiting advanced suite. Good luck!")
            sys.exit(0)

def domain_menu(domain_name, progress):
    while True:
        cluster_active = check_cluster_active()
        print_header(cluster_active, progress)
        print(f"{BOLD}{CYAN}Domain: {domain_name}{RESET}")
        print("-" * 60)
        
        # Match questions by domain
        domain_study = [q for q in STUDY_QUESTIONS if q["domain"] == domain_name]
        domain_env = [s for s in SCENARIOS if s["domain"] == domain_name]
        
        combined_list = []
        for q in domain_study:
            combined_list.append({"item": q, "type": "study"})
        for s in domain_env:
            combined_list.append({"item": s, "type": "env"})
            
        for idx, entry in enumerate(combined_list, 1):
            item = entry["item"]
            status = f"{GREEN}[✓]{RESET}" if progress.get(item["id"]) else "[ ]"
            type_lbl = f"{BLUE}(Study){RESET}" if entry["type"] == "study" else f"{YELLOW}(Scenario){RESET}"
            print(f" {idx:2d}. {status} {item['id']} - {item['title'] if 'title' in item else item['question'][:50]+'...'} {type_lbl}")
            
        print("-" * 60)
        print(" B. Back to Main Menu")
        print("=" * 60)
        
        choice = input(f"{BOLD}Select a question [1-{len(combined_list)}] or 'B' to go back: {RESET}").strip().lower()
        if choice == "b":
            break
        try:
            val = int(choice)
            if 1 <= val <= len(combined_list):
                view_item(combined_list[val-1], progress)
        except ValueError:
            pass

def view_item(entry, progress):
    item = entry["item"]
    is_study = (entry["type"] == "study")
    
    while True:
        cluster_active = check_cluster_active()
        print_header(cluster_active, progress)
        type_lbl = f"{BLUE}STUDY QUESTION{RESET}" if is_study else f"{YELLOW}ENVIRONMENT CHALLENGE{RESET}"
        
        print(f"{BOLD}ID:{RESET} {item['id']} | {BOLD}Type:{RESET} {type_lbl}")
        print(f"{BOLD}Domain:{RESET} {item['domain']}")
        print(f"{BOLD}Title/Question:{RESET}")
        if is_study:
            print(f"  {item['question']}")
        else:
            print(f"  {item['title']}")
            print(f"\n{BOLD}Problem Description:{RESET}\n  {item['problem']}")
            
        print("-" * 60)
        
        status_str = f"{GREEN}SOLVED (✓){RESET}" if progress.get(item["id"]) else f"{RED}UNSOLVED{RESET}"
        print(f"Current Status: {status_str}")
        print("-" * 60)
        
        if is_study:
            print(" 1. Show Answer / Solution")
            print(" 2. Toggle Solved/Completed Status")
            print(" B. Back to List")
            print("=" * 60)
            choice = input(f"{BOLD}Select Option: {RESET}").strip().lower()
            if choice == "b":
                break
            elif choice == "1":
                print(f"\n{BOLD}{GREEN}=== Standard Answer ==={RESET}")
                print(item["answer"])
                print("=" * 60)
                input("\nPress Enter to continue...")
            elif choice == "2":
                curr = progress.get(item["id"], False)
                progress[item["id"]] = not curr
                save_progress(progress)
        else:
            print(" 1. Setup Scenario (Inject issues into cluster)")
            print(" 2. Run Solution Check (Auto Validation)")
            print(" 3. Clean up / Reset Scenario State")
            print(" 4. Show Hint")
            print(" 5. Show Step-by-Step Solution Guide")
            print(" 6. Toggle Solved/Completed Status")
            print(" B. Back to List")
            print("=" * 60)
            choice = input(f"{BOLD}Select Option: {RESET}").strip().lower()
            if choice == "b":
                break
            elif choice == "1":
                setup_scenario(item["id"])
                input("\nPress Enter to continue...")
            elif choice == "2":
                passed = check_scenario(item["id"])
                if passed:
                    progress[item["id"]] = True
                    save_progress(progress)
                input("\nPress Enter to continue...")
            elif choice == "3":
                print("\nCleaning up scenario environment...")
                run_cmd(item["cleanup"])
                print(f"{GREEN}Environment reset command executed.{RESET}")
                input("\nPress Enter to continue...")
            elif choice == "4":
                print(f"\n{BOLD}{CYAN}=== HINT ==={RESET}")
                print(item["hint"])
                print("=" * 60)
                input("\nPress Enter to continue...")
            elif choice == "5":
                print(f"\n{BOLD}{GREEN}=== STEP-BY-STEP SOLUTION ==={RESET}")
                print(item["solution"])
                print("=" * 60)
                input("\nPress Enter to continue...")
            elif choice == "6":
                curr = progress.get(item["id"], False)
                progress[item["id"]] = not curr
                save_progress(progress)

if __name__ == "__main__":
    try:
        main_menu()
    except KeyboardInterrupt:
        print("\nExiting. Good luck studying!")
        sys.exit(0)
