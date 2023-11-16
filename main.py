import os
import requests
import io
from io import BytesIO
from pynput import keyboard
from PIL import ImageGrab
from PIL import Image
from pydub import AudioSegment
from pydub.playback import play
from dotenv import load_dotenv
import openai
import base64
# Load environment variables
load_dotenv()

# print(screen)
def capture_screen():
    print("Capturing the screen...")
    screenshot = ImageGrab.grab()
    screenshot.show()  # This line is for demonstration
    gameadvice = generate_game_advice(screenshot)
    perform_tts(gameadvice)

# Function to encode the screenshot to base64
def encode_to_base64(image):
    buffered = BytesIO()
    image.save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue()).decode('utf-8')

# Modified function to generate game advice
def generate_game_advice(screenshot): #def generate_game_advice(screenshot, commentator): to include custom voices/personalities like tyler1, draven, champ selected, joe rogan, etc.
    print("Analyzing the game...")

    # Encode screenshot to base64
    base64_image = encode_to_base64(screenshot)

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {os.environ['OPENAI_API_KEY']}"
    }

    payload = {
        "model": "gpt-4-vision-preview",
        "messages": [
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "What should I do next in this League of Legends game based on the image? Take into account my champ, role, score, the enemy score, and the time remaining in the game. What is the best move in terms of pushing/objectives/macro/winning the game, give me nothing but concise advice as if you are a league of legends pro."
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
        "max_tokens": 300
    }

    response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)
    response_json = response.json()
    advice = response_json.get('choices', [{}])[0].get('message', {}).get('content', 'No advice available.')
    print(advice)
    return advice

# Function to perform Text-to-Speech
def perform_tts(text):
    response = requests.post(
        "https://api.openai.com/v1/audio/speech",
        headers={
            "Authorization": f"Bearer {os.environ['OPENAI_API_KEY']}"
        },
        json={
            "model": "tts-1-1106",
            "input": text,
            "voice": "onyx",
        },
    )

    audio = b""
    for chunk in response.iter_content(chunk_size=1024 * 1024):
        audio += chunk
    # Convert the response content to an audio segment
    audio_stream = io.BytesIO(response.content)
    audio_segment = AudioSegment.from_file(audio_stream, format="mp3")

    # Play the audio segment
    play(audio_segment)

# Function to handle key press
def on_press(key):
    if key == keyboard.KeyCode.from_char('x'):
        capture_screen()

# Listener for key press
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
