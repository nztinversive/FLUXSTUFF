# Flux with Replicate Documentation

Use this guide to setup generating images with Flux and Replicate.

Write the complete code for every step. Do not get lazy. Write everything that is needed.

Your goal is to completely finish the feature.

# Flux with Replicate Documentation

Use this guide to set up generating images with Flux and Replicate.

## Helpful Links

- [Replicate](https://replicate.com)
- [Flux Schnell](https://replicate.com/black-forest-labs/flux-schnell?input=python)

## Required Environment Variables

Make sure the following environment variable is set:
```bash
export REPLICATE_API_TOKEN=
Install Replicate

Install the Replicate package:


pip install replicate


1. Create a Replicate Client
Create a file named replicate_client.py in your project’s library folder (/lib):

# Create the Replicate client
import os
import replicate


replicate_client = replicate.Client(api_token=os.getenv("REPLICATE_API_TOKEN"))


#2. Create a Server Action
Create a new file named replicate_actions.py in the actions directory (/actions):


from replicate_client import replicate_client

async def generate_flux_image(prompt: str):
    input_params = {
        "prompt": prompt,
        "num_outputs": 1,
        "aspect_ratio": "1:1",
        "output_format": "webp",
        "output_quality": 80,
    }

    output = replicate_client.run(
        "black-forest-labs/flux-schnell", input=input_params
    )
    
    return output


#3. Run the Action
To use the generate_flux_image function, import and call it in your code like this:


import asyncio
from actions.replicate_actions import generate_flux_image

# Example usage
async def main():
    prompt = "A futuristic cityscape"
    output = await generate_flux_image(prompt)
    print(output)

asyncio.run(main())
