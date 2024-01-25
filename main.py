from module import generate_subtitles
def main():
    # Define the path to your video and the desired output path for the subtitles
    video_path = "testvideo.mp4"
    output_srt_path = "./subtitles.srt"

    # Call the function to generate and save the subtitles
    generate_subtitles(video_path, output_srt_path)

if __name__ == "__main__":
    main()