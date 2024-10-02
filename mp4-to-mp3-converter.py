import os
from moviepy.editor import VideoFileClip

def convert_mp4_to_mp3(input_file, output_file):
    try:
        # Load the video file
        video = VideoFileClip(input_file)
        
        # Extract the audio
        audio = video.audio
        
        # Write the audio to an MP3 file
        audio.write_audiofile(output_file)
        
        # Close the video file
        video.close()
        
        return True
    except Exception as e:
        print(f"Conversion failed: {str(e)}")
        return False

def main():
    print("MP4 to MP3 Converter")
    
    while True:
        # Get input file path
        input_file = input("Enter the path to the MP4 file (or 'q' to quit): ")
        
        if input_file.lower() == 'q':
            break
        
        # Check if the file exists and has a valid format
        if not os.path.exists(input_file) or not input_file.lower().endswith('.mp4'):
            print("Invalid format or file does not exist.")
            continue
        
        # Generate output file path
        output_file = os.path.splitext(input_file)[0] + '.mp3'
        
        print("Converting video to audio...")
        
        # Perform the conversion
        if convert_mp4_to_mp3(input_file, output_file):
            print(f"Conversion successful. MP3 file saved as: {output_file}")
        else:
            print("Conversion failed.")

if __name__ == "__main__":
    main()
