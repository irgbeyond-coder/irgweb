import ollama

def classify_file(filename):
    prompt = f"Classify this filename into one category: 'Work', 'Media', or 'Other'. Return only the category name: {filename}"
    
    response = ollama.chat(model='gemma2:2b', messages=[
        {'role': 'user', 'content': prompt}
    ])
    
    return response['message']['content'].strip()

# Test it out!
test_file = "quarterly_budget_report.mp4"
category = classify_file(test_file)
print(f"File: {test_file} -> Category: {category}")


