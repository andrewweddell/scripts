import os
import time
from datetime import datetime

vault_path = os.path.expanduser("~/Library/Mobile Documents/iCloud~md~obsidian/Documents/Vault")
daily_folder = "Calendar"
template_path = os.path.expanduser("~/Library/Mobile Documents/iCloud~md~obsidian/Documents/Vault/Atlas/Utilities/Templates/Daily template.md")
filename_format = "%d-%b-%Y.md"

work = input("🛠️ What did you work on? ")
issues = input("❗ Any issues? ")
learned = input("📚 What did you learn? ")
time_logged = input("⏱️ Time logged? (e.g. 45min, 1.5h): ")

now = datetime.now()
entry = (
    f"\n### {now.strftime('%H:%M')} Check-in\n\n"
    f"**Work:** {work}  \n"
    f"**Issues:** {issues}  \n"
    f"**Learned:** {learned}  \n"
    f"**Time Logged:** {time_logged}  \n\n---\n"
)

filename = now.strftime(filename_format)
filepath = os.path.join(vault_path, daily_folder, filename)

if not os.path.exists(filepath):
    with open(template_path, 'r') as tpl:
        template_content = tpl.read()
    with open(filepath, 'w') as f:
        f.write(template_content)
    print("🆕 Daily file created from template.")

with open(filepath, 'a') as f:
    f.write(entry)

print(f"\n✅ Check-in saved to:\n{filepath}")
time.sleep(2)
os.system("osascript -e 'tell application \"Terminal\" to close front window' &")
