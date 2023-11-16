# MultiModal AI Video Game Coach

## Description
This project was originally intended to create an AI-powered coach for League of Legends (LoL) players. By integrating OpenAI's GPT-4 model with in-game screenshots(or continous video  thanks to 128k context, see [future enhancements](Future_Enhancements), the tool provides real-time strategic advice to players. The current version allows players to press a hotkey during the game, which captures a screenshot and sends it to GPT-4 for professional esports analysis. The AI then returns actionable advice, which is read aloud using a Text-to-Speech (TTS) model.

## How It Works
1. **In-Game Screenshot**: During the game, the player presses a designated hotkey (e.g., 'X') to capture a screenshot of the current game state.
2. **AI Analysis**: The screenshot is sent to GPT-4, which analyzes various elements like KDA (Kills/Deaths/Assists), map positioning, minion status, game time, etc.
3. **Strategic Advice**: GPT-4 generates advice based on the current game situation.
4. **Text-to-Speech Output**: This advice is then converted to speech using a TTS model and played back to the player.

## Installation

```bash
# Clone the repository
git clone [URL]

# Install dependencies
pip install -r requirements.txt
```
## Usage
Run the script before starting a League of Legends match.  
```
python main.py
```
During the game, press 'X' to activate the AI coach.  
Listen to the AI-generated advice.  

## Current Features
Screenshot capture on hotkey press.  
Integration with GPT-4V for image analysis.  
Generation of high quality advice based on visual game data.  
TTS output of AI-generated advice.  

## Future Enhancements
this project is not to be taken seriously, and does not endorse cheating.
**Continuous Video Analysis**: Implement [real-time video processing](https://cookbook.openai.com/examples/gpt_with_vision_for_video_understanding) to provide ongoing advice without the need for screenshot capture.   
**Voice Cloning Based on Selected Champion**: Integrate ElevenLabs or tortoise-tts for voice cloning to match the in-game champion. Could add celebrities like tyler1, joe rogan, idk.
**Interactive Voice Commands**: Allow players to ask specific questions using WhisperV3 STT for more personalized advice.   
**Personalization & Data Visualization for Improvement**: Implement user profiles for better personalized advice based on player history and preferences, and the ability to automatically create excel sheets, graphs, charts, based on player improvement and ability to further prompt gpt for analysis on that data for specific improvement points to hone players skill.   

## Contributions
We welcome contributions and ideas to enhance this tool. Please feel free to fork the repository, make changes, and submit pull requests. You can also open issues for bugs or feature suggestions.
