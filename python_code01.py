import os
import pandas as pd

# Define your folder
json_dir = r"C:\Users\tae7227\jsonfiles"
output_csv = r"C:\Users\tae7227\bitbucket_json_snippets.csv"

data = []

for root, _, files in os.walk(json_dir):
    for file in files:
        if file.endswith(".json"):
            file_path = os.path.join(root, file)
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    data.append({
                        "file_name": file,
                        "content": content.replace('\n', ' ')[:10000]  # Limit content if needed
                    })
            except Exception as e:
                print(f"Error reading {file}: {e}")

# Save to CSV
df = pd.DataFrame(data)
df.to_csv(output_csv, index=False, encoding='utf-8')
print(f"CSV file created at: {output_csv}")
