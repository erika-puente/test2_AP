import requests
import time
import json

# Define your tasks
prompts = {
    "qa_en": "What are the causes of climate change?",
    "qa_es": "¿Cuáles son las causas del cambio climático?",
    "qa_fr": "Quelles sont les causes du changement climatique?",

    "translation_en_to_es": "Translate this to Spanish: 'The cat is on the roof.'",
    "translation_fr_to_en": "Translate this to English: 'Il pleut des cordes.'",

    "idiom_es": "What does the Spanish expression 'estar en las nubes' mean?",
    "idiom_fr": "What does the French phrase 'avoir le cafard' mean?"
}

# Define the models to compare
models = ["tinyllama", "mistral", "llama2"]

# Set up result storage
results = {}

# Base URL for Ollama API
base_url = "http://127.0.0.1:11434/api/generate"

# Loop through each model and prompt
for model in models:
    results[model] = {}

    for task, prompt in prompts.items():
        start_time = time.time()

        response = requests.post(base_url, json={
            "model": model,
            "prompt": prompt,
            "stream": False
        })

        elapsed = time.time() - start_time
        output = response.json()["response"] if response.status_code == 200 else "Error"

        results[model][task] = {
            "prompt": prompt,
            "output": output,
            "time_seconds": round(elapsed, 2)
        }


# Save results to JSON
with open("ollama_model_comparison.json", "w") as f:
    json.dump(results, f, indent=2)

print("✅ All results saved to ollama_model_comparison.json")
