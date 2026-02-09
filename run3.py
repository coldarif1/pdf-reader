import os
import re
from pypdf import PdfReader

def extract_info_from_pdfs(folder_path):
    # Regex for phone numbers (matches formats like 123-456-7890 or (123) 456-7890)
    phone_pattern = r'\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}'
    
    # Simple regex for names (look for capitalized words, often needs manual refinement)
    name_pattern = r'\b[A-Z][a-z]+(?:\s[A-Z][a-z]+)+\b'

    results = []

    # Loop through files in folder
    for filename in os.listdir(folder_path):
        if filename.endswith('.pdf'):
            file_path = os.path.join(folder_path, filename)
            try:
                reader = PdfReader(file_path)
                full_text = ""
                
                # Extract text page by page
                for page in reader.pages:
                    text = page.extract_text()
                    if text:
                        full_text += text + "\n"

                # Find matches using regex
                phones = list(set(re.findall(phone_pattern, full_text)))
                names = list(set(re.findall(name_pattern, full_text)))

                results.append({
                    "filename": filename,
                    "names": names,
                    "phones": phones,
                    "text_preview": full_text[:700]  # First 700 characters
                })
            except Exception as e:
                print(f"Error reading {filename}: {e}")

    return results

# Usage
folder = "run/cv"
data = extract_info_from_pdfs(folder)

for item in data:
    print(f"File: {item['filename']}")
    print(f"Names Found: {item['names']}")
    print(f"Phones Found: {item['phones']}")
    print("-" * 100)
