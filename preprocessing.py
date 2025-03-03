import librosa
import soundfile as sf
import os

# Load the audio file
input_file = "long_audio.wav"  # Change to your actual file
audio, sr = librosa.load(input_file, sr=None)  # Keep original sampling rate

# Define parameters
segment_duration = 1  # Each segment should be 1 second
samples_per_segment = sr * segment_duration  # Samples in 1 second
num_segments = 1500  # Total number of 1-sec segments

# Output directory
output_dir = "audio_segments"
os.makedirs(output_dir, exist_ok=True)

# Split and save segments
for i in range(num_segments):
    start_sample = i * samples_per_segment
    end_sample = start_sample + samples_per_segment

    # Ensure we don't exceed audio length
    if end_sample > len(audio):
        break  # Stop if we reach the end of the audio

    segment = audio[start_sample:end_sample]
    
    # Save as a new WAV file
    output_file = os.path.join(output_dir, f"segment_{i+1}.wav")
    sf.write(output_file, segment, sr)

    print(f"Saved: {output_file}")

print("Audio splitting completed!")
