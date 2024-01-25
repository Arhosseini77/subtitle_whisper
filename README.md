# Video Subtitle Generator

This project utilizes the Whisper model for automatic speech recognition to generate subtitles for video files. It consists of two main Python scripts: `module.py` and `main.py`.

## Overview

### module.py
`module.py` contains two primary functions:

- `format_subtitles(model_output)`: Takes the transcription result from the Whisper model and formats it into the SRT subtitle format.
- `generate_subtitles(video_path, output_srt_path)`: Takes the path to a video file and the desired output path for the SRT file, transcribes the video using the Whisper model, formats the transcription, and saves it to the specified path.

### main.py
`main.py` is the entry point of the application. It calls the `generate_subtitles` function from `module.py` with the specified video file path and output path for the subtitles.

## System Requirements

- Python 3.10
- torch 2.1.0 + cu121
- Whisper (can be installed directly from GitHub)

## Quick Start

1. **Install Whisper**  
   Whisper needs to be installed before running the application. You can install it using the following command:

   ```bash
   pip install git+https://github.com/openai/whisper.git
   ```

2. **Running the Application**  
   Navigate to the project directory in your terminal and run:

   ```bash
   python main.py
   ```

   Ensure you have updated the `main.py` with the correct paths to your video file and the desired output path for the subtitles.

## Notes

- The script `main.py` is configured to run with the paths specified within the script. Modify the paths according to your local setup.
- The transcription is currently set to the 'fa' (Farsi) language. If you want to transcribe in a different language, modify the `language` parameter in the `generate_subtitles` function call inside `module.py`.
- Ensure that the output file path specified in `main.py` has a `.srt` extension as the script generates subtitles in SRT format.

---
