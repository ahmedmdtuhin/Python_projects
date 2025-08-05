# Face Recognition Attendance System

**Face Recognition Attendance System** is one of several small Python projects designed to demonstrate practical applications of computer vision. This project uses a webcam to detect and recognize faces in real-time and automatically logs attendance in a `.csv` file.

## 📁 Project Structure

```
faceRecognitionAttendence/
├── .idea/                   # IDE configuration files (optional)
├── faces/                   # Folder containing stored face images of known users
├── 2023-12-05.csv           # Auto-generated attendance CSV file (example)
├── main.py                  # Main script for running the attendance system
```

## 🚀 Features

- Real-time face detection using OpenCV
- Face recognition using a local dataset of known faces
- Automatic attendance logging in a dated CSV file
- Avoids duplicate entries for the same person on the same day

## 🧰 Technologies Used

- Python 3.x
- OpenCV
- face_recognition (Dlib-based library)
- CSV for logging

## 📸 How It Works

1. The webcam captures video in real time.
2. Detected faces are compared with known faces stored in the `faces/` folder.
3. If a match is found, the person's name and timestamp are logged in `YYYY-MM-DD.csv`.
4. Each person is logged only once per day.

## ✅ Prerequisites

Install the required packages:

```bash
pip install opencv-python
pip install face_recognition
```

> ⚠️ Note: You may also need to install `cmake`, `dlib`, and compiler tools depending on your system, especially on Windows.

## 🛠️ How to Use

1. Clone the repository and navigate to the project directory:
   ```bash
   git clone https://github.com/your-username/Python_projects.git
   cd Python_projects/faceRecognitionAttendence
   ```

2. Add clear face images (named after the person) to the `faces/` folder.

3. Run the script:
   ```bash
   python main.py
   ```

4. Attendance will be saved automatically in a CSV file named with the current date.

## 📦 Output Example

```
2023-12-05.csv

Name,Time
John Doe,09:03:45
Jane Smith,09:04:17
```

## 📌 Notes

- Good lighting and front-facing images improve recognition accuracy.
- Face image filenames should match the person’s name (e.g., `JohnDoe.jpg`).
- Designed for simple use cases and educational purposes.

## 📂 About This Repository

This project is part of a collection of small Python projects demonstrating different functionalities such as:
- Weather app
- PDF merger
- Image resizer
- Text-to-speech (RoboSpeaker)

Explore the repository to check out other mini-projects!

## 📄 License

This project is open-source and free to use under the MIT License.
