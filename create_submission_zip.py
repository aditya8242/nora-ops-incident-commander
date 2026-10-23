import os
import zipfile

project_dir = r"C:\Users\Aditya\.gemini\antigravity\scratch\incident-commander-nora"
desktop_zip = r"C:\Users\Aditya\Desktop\nora-ops-submission.zip"

exclude_dirs = {"node_modules", ".git", "__pycache__"}
exclude_files = {".env", "nora-ops-submission.zip"}

print("Packaging project for submission (excluding secrets & dependencies)...")

with zipfile.ZipFile(desktop_zip, "w", zipfile.ZIP_DEFLATED) as zipf:
    for root, dirs, files in os.walk(project_dir):
        # Filter out directories
        dirs[:] = [d for d in dirs if d not in exclude_dirs]
        for file in files:
            if file in exclude_files:
                continue
            full_path = os.path.join(root, file)
            rel_path = os.path.relpath(full_path, project_dir)
            zipf.write(full_path, arcname=rel_path)
            print(f"  + Added: {rel_path}")

print(f"\n[+] Created submission archive: {desktop_zip}")
