import requests
import json

# Define the API endpoint URL
url = "http://localhost:11434/api/generate"

# Prepare the request data
data = {
    "model": "llama3",
    "prompt": "Objasni sta je teorija grupa u apstraktnoj algebri."
}

# Send the POST request using requests library
response = requests.post(url, json=data)

# Print the raw response content for debugging
print(f"Response content: {response.content}")

# Check for successful response
if response.status_code == 200:
    try:
        # Split the response content by newlines to get individual JSON objects
        response_content = response.content.decode('utf-8')
        json_objects = response_content.strip().split('\n')

        # Initialize a variable to collect the full response
        full_response = ""

        # Parse each JSON object and concatenate the 'response' fields
        for obj in json_objects:
            response_data = json.loads(obj)
            full_response += response_data.get("response", "")

        # Print the full concatenated response
        print(f"Llama3 Response: {full_response}")
    except json.JSONDecodeError as e:
        print(f"JSON decode error: {e}")
else:
    print(f"Error: API request failed with status code {response.status_code}")
