import cv2
import librosa

# Load video file
cap = cv2.VideoCapture('video.mp4')

# Load audio file
y, sr = librosa.load('audio.wav')

# Define output paths for audio and video files
audio_path = 'audio.wav'
video_path = 'frames/'

# Initialize frame counter
frame_num = 0

# Loop over frames in video
while cap.isOpened():
    # Read frame from video
    ret, frame = cap.read()

    if ret:
        # Save frame to output folder
        cv2.imwrite(video_path + 'frame_' + str(frame_num) + '.jpg', frame)

        # Increment frame counter
        frame_num += 1
    else:
        break

# Release video capture object
cap.release()

# Save audio to output folder
librosa.output.write_wav(audio_path, y, sr)
