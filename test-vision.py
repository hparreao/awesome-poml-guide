#!/usr/bin/env python3

"""
Script to test GPT Vision API with POML image analysis example
This script reads the image-analysis.poml file and sends it to OpenAI's GPT Vision API
"""

import os
import base64
import json
import requests
import xml.etree.ElementTree as ET
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configuration
API_KEY = os.getenv('OPENAI_API_KEY')
MODEL = 'gpt-4-vision-preview'
MAX_TOKENS = 300

# Check if API key is provided
if not API_KEY:
    print('Error: OPENAI_API_KEY environment variable is not set.')
    print('Please set your OpenAI API key in the .env file or as an environment variable.')
    exit(1)

def image_to_base64(image_path):
    """
    Convert image to base64
    :param image_path: Path to the image file
    :return: Base64 encoded image
    """
    try:
        with open(image_path, 'rb') as image_file:
            return base64.b64encode(image_file.read()).decode('utf-8')
    except Exception as e:
        print(f'Error reading image file: {str(e)}')
        exit(1)

def parse_poml_file(poml_path):
    """
    Parse POML file to extract image information
    :param poml_path: Path to the POML file
    :return: Image information dictionary
    """
    try:
        with open(poml_path, 'r') as file:
            content = file.read()
            
        # Simple parsing to extract img tag attributes
        # In a real implementation, you might want to use an XML parser
        import re
        
        img_src_match = re.search(r'<img\s+[^>]*src=["\']([^"\']+)["\'][^>]*\/?>', content, re.IGNORECASE)
        alt_match = re.search(r'<img\s+[^>]*alt=["\']([^"\']+)["\'][^>]*\/?>', content, re.IGNORECASE)
        processing_match = re.search(r'<img\s+[^>]*processing=["\']([^"\']+)["\'][^>]*\/?>', content, re.IGNORECASE)
        focus_areas_match = re.search(r'<img\s+[^>]*focus_areas=["\']([^"\']+)["\'][^>]*\/?>', content, re.IGNORECASE)
        
        if not img_src_match:
            raise Exception('No image source found in POML file')
            
        return {
            'src': img_src_match.group(1),
            'alt': alt_match.group(1) if alt_match else '',
            'processing': processing_match.group(1) if processing_match else '',
            'focusAreas': focus_areas_match.group(1) if focus_areas_match else ''
        }
    except Exception as e:
        print(f'Error parsing POML file: {str(e)}')
        exit(1)

def create_prompt(poml_data):
    """
    Create prompt for GPT Vision API
    :param poml_data: POML data extracted from file
    :return: Formatted prompt
    """
    return f"""You are a technical image analysis expert with expertise in system architecture.
    
Analyze the provided image and describe the architectural components in detail, including:
1. Architectural style
2. Materials used
3. Identifiable functional elements

Additional context:
- Image description: {poml_data['alt']}
- Processing type: {poml_data['processing']}
- Focus areas: {poml_data['focusAreas']}"""

def call_gpt_vision_api(prompt, base64_image):
    """
    Send request to OpenAI GPT Vision API
    :param prompt: Text prompt
    :param base64_image: Base64 encoded image
    :return: API response
    """
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    }

    payload = {
        "model": MODEL,
        "messages": [
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": prompt
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/png;base64,{base64_image}"
                        }
                    }
                ]
            }
        ],
        "max_tokens": MAX_TOKENS
    }

    try:
        response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)
        return response.json()
    except Exception as e:
        print(f'API request failed: {str(e)}')
        exit(1)

def main():
    """
    Main function
    """
    print('Testing GPT Vision API with POML image analysis example...\\n')
    
    # Parse the POML file
    poml_path = os.path.join(os.path.dirname(__file__), 'examples', 'image-analysis.poml')
    print(f'Parsing POML file: {poml_path}')
    poml_data = parse_poml_file(poml_path)
    print(f"Found image reference: {poml_data['src']}\\n")
    
    # Resolve the image path
    image_path = os.path.join(os.path.dirname(__file__), poml_data['src'])
    print(f'Loading image: {image_path}')
    
    # Convert image to base64
    base64_image = image_to_base64(image_path)
    print('Image loaded and converted to base64\\n')
    
    # Create prompt
    prompt = create_prompt(poml_data)
    print('Generated prompt for GPT Vision API:\\n')
    print(prompt)
    print('\\n' + '='*80 + '\\n')
    
    # Call GPT Vision API
    print('Sending request to GPT Vision API...')
    response = call_gpt_vision_api(prompt, base64_image)
    
    # Process and display response
    if 'choices' in response and len(response['choices']) > 0:
        print('GPT Vision API Response:\\n')
        print(response['choices'][0]['message']['content'])
    else:
        print('Unexpected API response format:')
        print(json.dumps(response, indent=2))
    
    if 'usage' in response:
        print('\\n' + '='*80 + '\\n')
        print('Token usage:')
        print(f"- Prompt tokens: {response['usage']['prompt_tokens']}")
        print(f"- Completion tokens: {response['usage']['completion_tokens']}")
        print(f"- Total tokens: {response['usage']['total_tokens']}")

if __name__ == '__main__':
    main()