from lib.replicate_client import replicate_client

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