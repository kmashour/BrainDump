import os
import re
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

ref_dir = "Reference Notes"
files = [
    "13-104-01_course_introduction_and_certification.md",
    "13-104-02_administer_identity.md",
    "13-104-03_administer_governance_and_compliance.md",
    "13-104-04_administer_azure_resources.md",
    "13-104-05_administer_virtual_networking.md",
    "13-104-06_administer_intersite_connectivity.md",
    "13-104-07_administer_network_traffic.md",
    "13-104-08_administer_azure_storage.md",
    "13-104-09_administer_azure_virtual_machines.md",
    "13-104-10_administer_paas_compute_options.md",
    "13-104-11_administer_data_protection.md",
    "13-104-12_administer_monitoring.md",
    "13-Index - AZ-104.md"
]

for fname in files:
    fpath = os.path.join(ref_dir, fname)
    if not os.path.exists(fpath):
        print(f"Missing: {fname}")
        continue
    with open(fpath, "r", encoding="utf-8") as f:
        lines = f.readlines()
    headers = [line.strip() for line in lines if line.strip().startswith("## ")]
    print(f"\n[FILE] {fname} ({len(lines)} lines):")
    for h in headers:
        print(f"   {h}")
