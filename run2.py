import pdfplumber
import os
import re

# --- CONFIGURATION ---
# Path to your folder containing PDF files
folder_path = r'run/cv' 

# Regex pattern for phone numbers (matches various formats like 123-456-7890, (123) 456-7890, +1...)
phone_pattern = re.compile(r'(\+?\d{1,3}[-.\s]?)?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}')

def extract_pdf_data(folder):
    results = []
    
    # List all files in the directory
    if not os.path.exists(folder):
        print(f"Folder not found: {folder}")
        return

    for filename in os.listdir(folder):
        if filename.endswith('.pdf'):
            file_path = os.path.join(folder, filename)
            print(f"Processing: {filename}...")
            
            file_text = ""
            phone_numbers = []
            
            try:
                # Open the PDF
                with pdfplumber.open(file_path) as pdf:
                    for page in pdf.pages:
                        # Extract text from page
                        text = page.extract_text()
                        if text:
                            file_text += text + "\n"
                            
                            # Search for phone numbers in the text
                            matches = phone_pattern.findall(text)
                            for match in matches:
                                # match is a tuple due to groups, get the first part
                                if isinstance(match, tuple):
                                    phone_numbers.append(match[0])
                                else:
                                    phone_numbers.append(match)
                
                # Remove duplicates from phone numbers
                unique_phones = list(set(phone_numbers))
                
                results.append({
                    "filename": filename,
                    "phone_numbers": unique_phones,
                    "text_preview": file_text[:500] # Storing first 500 chars
                })
                
            except Exception as e:
                print(f"Error reading {filename}: {e}")
                
    return results

# --- EXECUTION ---
if __name__ == "__main__":
    extracted_data = extract_pdf_data(folder_path)
    
    # Display Results
    for data in extracted_data:
        print("\n" + "="*30)
        print(f"File: {data['filename']}")
        print(f"Phone Numbers: {data['phone_numbers']}")
        print(f"Text Preview:\n{data['text_preview']}...")
