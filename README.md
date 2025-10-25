# airDraw
Here’s a comprehensive README for your hand-tracking drawing project using OpenCV and MediaPipe. I formatted it so anyone can understand and run your code:

⸻

Hand Tracking Drawing Application

A real-time virtual paint application using OpenCV and MediaPipe, which allows you to draw on the screen using hand gestures. Users can select colors, draw, and erase using only their hands in front of a webcam.

⸻

Features
	•	Hand Tracking: Detects hand landmarks using MediaPipe.
	•	Drawing Mode: Draw on the canvas using the index finger.
	•	Selection Mode: Switch colors or tools by raising index and middle fingers.
	•	Eraser Mode: Erase drawings using a specific gesture.
	•	Dynamic Header: Shows selected color/tool images.
	•	FPS Display: Shows real-time FPS for performance monitoring.

⸻

Screenshots

(Add your screenshots here showing the canvas, header, and hand gestures in action)

⸻

Requirements
	•	Python 3.7+
	•	OpenCV (cv2)
	•	MediaPipe (mediapipe)
	•	NumPy (numpy)

⸻

Installation
	1.	Clone the repository:
  git clone https://github.com/yourusername/hand-drawing-app.git
  cd hand-drawing-app
  2.	Install dependencies:
  pip install opencv-python mediapipe numpy
  	3.	Prepare header images:

	•	Place your toolbar images (e.g., colors, eraser) in a folder named img in the project root.
	•	Make sure the images are wide enough to fit the top header bar.

⸻

Usage
	1.	Run the main drawing script:
  python main.py

  	2.	Controls:

	•	Selection Mode: Raise index and middle fingers to select a color/tool.
	•	Drawing Mode: Raise only the index finger to draw on the canvas.
	•	Eraser: Select the eraser icon to erase drawings.

⸻

Code Overview
	•	handTrackingModule.py – Contains the HandDetector class using MediaPipe for hand detection and landmark tracking.
	•	main.py – The main application script, includes:
	•	Webcam capture
	•	Hand gesture detection
	•	Drawing on a canvas
	•	Tool selection and color switching
Color Codes Used

OpenCV uses BGR format for colors:
Color          BGR Value
Red            (0, 0, 255)
Blue           (255, 0, 0)
Yellow         (0, 255, 255)
Green          (0, 128, 0)
Eraser         (0, 0, 0)

Notes
	•	Ensure your webcam resolution matches the canvas size (default: 1280x720).
	•	The application assumes right-hand usage for thumb detection.
	•	Header images must match the width ranges set in the code for correct selection.

⸻

Troubleshooting
	•	Hand not detected: Ensure good lighting and a clear background.
	•	Drawing not smooth: Increase FPS or reduce brushThickness.
	•	Incorrect color selection: Verify BGR values and header image order.

⸻

License

This project is open-source and free to use.

⸻

I can also rewrite your code structure so it’s modular, with a proper main.py and handTrackingModule.py, making it easier for others to run.
