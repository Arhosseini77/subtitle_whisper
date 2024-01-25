import os
import torch
import whisper

# Function to format the model output to subtitles
def format_subtitles(model_output):
    formatted_output = ""
    for segment in model_output['segments']:
        start_time = segment['start']
        end_time = segment['end']
        text = segment['text'].strip()
        formatted_output += f"{start_time} --> {end_time}\n{text}\n\n"
    return formatted_output.strip()

def generate_subtitles(video_path, output_srt_path):
    # Load the Whisper model
    model_name = "large-v3"
    model = whisper.load_model(model_name, download_root="models")

    # Transcribe the video
    res = model.transcribe(video_path, language='fa')

    # Get formatted subtitles
    formatted_subtitle = format_subtitles(res)

    # Create directory if it doesn't exist
    os.makedirs(os.path.dirname(output_srt_path), exist_ok=True)

    # Save the formatted subtitles to a .srt file
    with open(output_srt_path, 'w', encoding='utf-8-sig') as file:
        file.write(formatted_subtitle)
    print(f"Subtitles have been saved to {output_srt_path}")
