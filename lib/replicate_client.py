import os
import replicate

replicate_api_token = os.getenv("REPLICATE_API_TOKEN")
print(f"Replicate API Token: {replicate_api_token}")  # Add this line for debugging

if not replicate_api_token:
    raise ValueError("REPLICATE_API_TOKEN environment variable is not set")

replicate_client = replicate.Client(api_token=replicate_api_token)