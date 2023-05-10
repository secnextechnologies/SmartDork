import requests
import json

def search_dorkgpt(query):
    url = f"https://api.dorkgpt.com/dork/?query={query}"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        
        # Convert JSON to text
        result_text = json.dumps(data, indent=4)
        
        # Print the output
        print(result_text)
        
    except requests.exceptions.RequestException as err:
        print(f"An error occurred: {err}")

# Get user input
user_query = input("Enter your search query: ")

# Perform the search
search_dorkgpt(user_query)
