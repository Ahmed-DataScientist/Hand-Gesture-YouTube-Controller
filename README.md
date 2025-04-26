Hand Gesture YouTube Controller 🎥🖐️
This project allows users to control YouTube videos using hand gestures detected via a webcam.
It uses OpenCV, Mediapipe, and PyAutoGUI to recognize the number of fingers raised and trigger different YouTube actions like Play, Pause, Volume Up, Volume Down, and Next Video — without touching the keyboard or mouse!

✨ Features:
Detect hand gestures using live webcam feed.

Control YouTube with the following gestures:

1 Finger ➔ Play Video

2 Fingers ➔ Pause Video

3 Fingers ➔ Volume Up

4 Fingers ➔ Volume Down

5 Fingers ➔ Next Video

Real-time feedback of detected gesture and action displayed on screen.

Simple and lightweight — works even on low-end systems.

🛠️ Built With:
Python 3

OpenCV (for image processing)

Mediapipe (for hand landmark detection)

PyAutoGUI (for keyboard control)

🚀 How to Run:
Clone the repository.

Install the required libraries:

bash
Copy
Edit
pip install opencv-python mediapipe pyautogui
Run the program:

bash
Copy
Edit
python main.py
Make sure YouTube tab is open and in focus while using the gestures
