import os
import re
import PyPDF2

# -------- CONFIGURATION --------
PDF_FOLDER = "run/cv"  # Folder containing PDFs
OUTPUT_FILE = "extracted_data.txt"  # Change to .rtf if needed

# Regex patterns for name and phone number
# Phone: Matches formats like 1234567890, (123) 456-7890, +8801XXXXXXXXX
PHONE_PATTERN = re.compile(r'(\+?\d[\d\s\-\(\)]{7,}\d)')
# Name: Simplistic pattern assuming "Name: John Doe" or "Full Name: ..."
NAME_PATTERN = re.compile(r'(?:Name|Full Name)\s*[:\-]\s*([A-Za-z\s]+)')

def extract_text_from_pdf(pdf_path):
    """Extracts all text from a PDF file."""
    text = ""
    try:
        with open(pdf_path, "rb") as file:
            reader = PyPDF2.PdfReader(file)
            for page in reader.pages:
                text += page.extract_text() + "\n"
    except Exception as e:
        print(f"Error reading {pdf_path}: {e}")
    return text

def extract_info(text):
    """Extracts name and phone number from text."""
    names = NAME_PATTERN.findall(text)
    phones = PHONE_PATTERN.findall(text)   
    return names, phones

def main():
    results = []
    
    if not os.path.exists(PDF_FOLDER):
        print(f"Folder '{PDF_FOLDER}' not found.")
        return
    
    for filename in os.listdir(PDF_FOLDER):
        if filename.lower().endswith(".pdf"):
            pdf_path = os.path.join(PDF_FOLDER, filename)
            print(f"Processing: {filename}")
            
            text = extract_text_from_pdf(pdf_path)
            names, phones = extract_info(text)
            
            results.append({
                "file": filename,
                "names": names,
                "phones": phones,
                "text": text.strip()
            })
    
    # Save results to file
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        for item in results:
            f.write(f"File: {item['file']}\n")
            f.write(f"Names: {', '.join(item['names']) if item['names'] else 'N/A'}\n")
            f.write(f"Phones: {', '.join(item['phones']) if item['phones'] else 'N/A'}\n")
            f.write("Full Text:\n")
            f.write(item['text'])
            f.write("\n" + "-"*90 + "\n")
    
    print(f"Extraction complete. Data saved to '{OUTPUT_FILE}'.")

if __name__ == "__main__":
    main()
