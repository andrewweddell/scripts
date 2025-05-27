# Obsidian Terminal Check-In Logger

This setup creates a terminal-based journaling/check-in script that prompts you at scheduled times during the day, appends your responses to your daily Obsidian note, and automatically closes the terminal window afterward. It is triggered using macOS's `launchd` system.

---

## Features

- Prompted check-ins in your terminal  
- Appends responses to a Markdown-formatted daily note in Obsidian  
- Auto-creates the daily note from a template if it doesn't exist  
- Runs automatically at scheduled times (e.g., 11:30 AM, 2:00 PM, 4:30 PM)  
- Brings terminal window to the front and closes it automatically after check-in

---

## Setup Steps

### 1. Create Your Check-In Script

Save the `checkin.py` script (provided below) to:

```
~/scripts/checkin.py
```

### 2. Create Your Daily Note Template

Save a Markdown file with your daily note layout, e.g.:

```markdown
# Daily Note - {{date}}

---

### 📝 Notes

---

## Check-Ins
```

Save it to:

```
~/Library/Mobile Documents/iCloud~md~obsidian/Documents/Vault/Atlas/Utilities/Templates/Daily template.md
```

### 3. Create the Launch Agent

Save the `.plist` file (provided below) to:

```
~/Library/LaunchAgents/com.andrew.checkin.plist
```

### 4. Load the Launch Agent

```bash
launchctl unload ~/Library/LaunchAgents/com.andrew.checkin.plist 2>/dev/null
launchctl load ~/Library/LaunchAgents/com.andrew.checkin.plist
```

---

## Testing the Setup

Run this to test:

```bash
launchctl kickstart -k gui/$(id -u)/com.andrew.checkin
```

---

## Troubleshooting

- **Terminal opens but nothing happens**: use `osascript` to run the command inside Terminal.
- **Terminal doesn't close**: make sure the script ends with `exit` or uses `osascript` to close the window.
- **Not running after reboot**: ensure the `.plist` file is in `~/Library/LaunchAgents/` and is loaded.
- **File edited in rich text**: make sure your `.plist` is saved as plain text, not `.rtf`.

---

## Optional Logging

Add this to the end of your Python script to log executions:

```python
with open(os.path.expanduser("~/checkin.log"), 'a') as log:
    log.write(f"Triggered at {now.strftime('%Y-%m-%d %H:%M:%S')}\n")
```

View logs with:

```bash
tail -f ~/checkin.log
```

---

