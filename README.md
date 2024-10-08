# Hand Gesture Recognition using MediaPipe

Estimate hand pose using MediaPipe (Python version).

This project showcases a sample program that recognizes hand signs and finger gestures through detected key points.

## Contents
- About
- Setup
- Usage
- Gesture Guide

## About

This is a gesture-controlled media player that utilizes hand gesture recognition to execute commands in VLC media player. The goal is to create a touch-free and remote-free interaction method, allowing users to control video playback simply by using their hands.

By leveraging the power of MediaPipe for hand tracking and recognition, this application aims to enhance user experience and increase productivity when interacting with media.

## Setup

To get started, ensure you have VLC media player installed on your computer. Then, follow the steps below:

1. **Install Dependencies**: Use the following command to install the necessary libraries.

    ```bash
    pip install -r install_requires.txt
    ```

2. **Run the Application**: Execute the main program using:

    ```bash
    python HandGestures.py
    ```

## Usage

Once the application is running, follow these steps to control your media:

1. Click the "Browse" button to select an MP4 video file from your computer.
2. The controller will launch, allowing you to use hand gestures to control playback.
3. To exit the application, simply type "Q".

## Gesture Guide

Here’s how to use specific hand gestures to control the media player:

- **Play/Pause**: 
  - **Gesture**: Raise an open palm above your shoulders, with palms facing forward (or close hands).
  - **Description**: This gesture indicates the start of media playback or pauses it.
  
  ![Play Gesture](https://github.com/user-attachments/assets/76354507-6ac4-41c5-97fa-40bf8958a0e1)

---

- **Fast Forward**: 
  - **Gesture**: Touch your index finger and thumb.
  - **Description**: This gesture signals the application to fast forward the video.
  
  ![Fast Forward Gesture](link_to_fast_forward_gesture_image)

---

- **Rewind**: 
  - **Gesture**: Touch your middle finger and thumb.
  - **Description**: This gesture prompts the application to rewind the video.
  
  ![Rewind Gesture](link_to_rewind_gesture_image)

---

- **Increase Volume**: 
  - **Gesture**: Raise one thumb up.
  - **Description**: This gesture increases the media volume.
  
  ![Increase Volume Gesture](link_to_increase_volume_gesture_image)

---

- **Decrease Volume**: 
  - **Gesture**: Lower one thumb down.
  - **Description**: This gesture decreases the media volume.
  
  ![Decrease Volume Gesture](link_to_decrease_volume_gesture_image)

---

## Improvements

Future updates will focus on enhancing the accuracy of gesture recognition, especially at a distance. For optimal performance, ensure that your gestures are framed similarly to the demonstration images.

## Acknowledgments

Special thanks to MediaPipe for providing an excellent hand tracking model and comprehensive documentation, which have been instrumental in developing this project.

