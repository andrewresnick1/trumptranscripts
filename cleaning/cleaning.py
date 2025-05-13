import os

# STEP 1: Load transcript
with open("cleaning/dirty_text/dirty_hannity_jan22_2025.txt", "r", encoding="utf-8") as f:
    raw_transcript = f.read()

# STEP 2: Clean and parse
lines = raw_transcript.splitlines()
cleaned = []
current_speaker = None

for line in lines:
    line = line.strip()

    # Skip meta lines
    if not line or line.startswith('Note') or line.startswith('['):
        continue

    # Set speaker if line has their name
    elif line.startswith('Sean Hannity') or line.startswith('Donald Trump'):
        current_speaker = 'Sean Hannity' if 'Sean Hannity' in line else 'Donald Trump'

    # If we have a speaker and it's not noise, add the line
    elif current_speaker and not line.startswith('No StressLens') and not line.startswith('No Signal'):
        cleaned.append(f"{current_speaker}: {line}")

# STEP 3: Save cleaned transcript
folder_path = "cleaned_text"
filename = "cleaned_Trump_Hannity_Interview1.txt"
os.makedirs(folder_path, exist_ok=True)

output_path = os.path.join(folder_path, filename)
with open(output_path, "w", encoding="utf-8") as f:
    f.write("\n".join(cleaned))

print(f"✅ Cleaned transcript saved to: {output_path}")
