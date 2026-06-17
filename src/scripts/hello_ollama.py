import ollama
import sys

print("--- Connecting to InnerReality AI Assistant ---")

try:
    # We use stream=True so we don't have to wait for the whole thing
    stream = ollama.chat(
        model='gemma2:2b',
        messages=[{'role': 'user', 'content': 'Say hello and tell me one fun fact about Python!'}],
        stream=True,
    )

    print("AI Response: ", end="", flush=True)
    
    for chunk in stream:
        # Print each piece of text as it arrives
        content = chunk['message']['content']
        print(content, end="", flush=True)

    print("\n--- End of Transmission ---")

except Exception as e:
    print(f"\nOops! Something went wrong: {e}")