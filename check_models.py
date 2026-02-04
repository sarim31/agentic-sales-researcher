#!/usr/bin/env python3
"""
Quick script to check what Gemini models are available
"""

import os
from dotenv import load_dotenv

load_dotenv()

try:
    from google import genai
    
    client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
    
    print("Available Gemini models:")
    print("=" * 60)
    
    models = client.models.list()
    for model in models:
        if 'generateContent' in model.supported_generation_methods:
            print(f"✓ {model.name}")
    
except Exception as e:
    print(f"Error: {e}")
    print("\nTrying to get model info from API directly...")
    
    import requests
    
    api_key = os.getenv("GEMINI_API_KEY")
    url = f"https://generativelanguage.googleapis.com/v1beta/models?key={api_key}"
    
    response = requests.get(url)
    
    if response.status_code == 200:
        models = response.json().get('models', [])
        print("\nAvailable models that support generateContent:")
        print("=" * 60)
        for model in models:
            if 'generateContent' in model.get('supportedGenerationMethods', []):
                print(f"✓ {model['name']}")
    else:
        print(f"Error: {response.status_code}")
        print(response.text)
