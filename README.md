# Flux Image Generator App

Flux Image Generator is a web application that allows users to generate images based on text prompts using AI. It features a sleek, responsive design with dark mode support and a history of generated images.

![Flux Image Generator](pandastuff.png)

## Features

- Generate images from text prompts using AI
- Download generated images in PNG format
- Dark mode toggle for comfortable viewing
- Responsive design for mobile and desktop
- History of generated images with quick-access functionality
- Animated background for enhanced visual appeal

## Technologies Used

- HTML5 & CSS3 for structure and styling
- JavaScript for client-side interactions
- Python with FastAPI for the backend server
- Replicate API for AI-powered image generation

## Setup and Installation

1. Clone the repository:
   ```
   git clone https://github.com/nztinversive/Flux-Simple-App.git
   cd Flux-Simple-App
   ```

2. Install the required Python packages:
   ```
   pip install -r requirements.txt
   ```

3. Set up your environment variables:
   Create a `.env` file in the root directory and add your Replicate API token:
   ```
   REPLICATE_API_TOKEN=your_api_token_here
   ```

4. Run the FastAPI server:
   ```
   uvicorn server:app --reload
   ```

5. Open `index.html` in your web browser or set up a local server to serve the file.

## Usage

1. Enter a descriptive text prompt in the input field.
2. Click the "Generate Image" button or press Enter.
3. Wait for the AI to generate the image based on your prompt.
4. Once generated, you can download the image or create a new one.
5. View your generation history in the "Generated Images" section below.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the [MIT License](LICENSE).

## Acknowledgements

- [Replicate](https://replicate.com/) for providing the AI image generation API
- [FastAPI](https://fastapi.tiangolo.com/) for the efficient Python web framework
