# Hand Gesture Recognition using MediaPipe

Estimate hand pose using MediaPipe (Python version).

This project showcases a sample program that recognizes hand signs and finger gestures through detected key points.

❗️ This is the English-translated version of the original repo. All content is translated to English, including comments and notebooks. ❗️

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
    $ pip install -r dependencies.txt
    ```

2. **Run the Application**: Execute the main program using:

    ```bash
    python main.py
    ```

## Usage

Once the application is running, follow these steps to control your media:

1. Click the "Browse" button to select an MP4 video file from your computer.
2. The controller will launch, allowing you to use hand gestures to control playback.
3. To exit the application, simply type "Q".

## Gesture Guide

Here’s how to use specific hand gestures to control the media player:

- **Play**: 
  - **Gesture**: Raise an open palm above your shoulders, with palms facing forward.
  - **Description**: This gesture indicates the start of media playback.
  
  ![Play Gesture](link_to_play_gesture_image)

---

- **Pause**: 
  - **Gesture**: Touch the index finger and thumb together to form a circle.
  - **Description**: This gesture pauses the currently playing media.
  
  ![Pause Gesture](link_to_pause_gesture_image)

---

- **Fast Forward**: 
  - **Gesture**: Use your middle finger and thumb to form a 'thumbs up' gesture.
  - **Description**: This gesture signals the application to fast forward the video.
  
  ![Fast Forward Gesture](link_to_fast_forward_gesture_image)

---

- **Rewind**: 
  - **Gesture**: Use a 'thumbs down' gesture.
  - **Description**: This gesture prompts the application to rewind the video.
  
  ![Rewind Gesture](link_to_rewind_gesture_image)

---

- **Increase Volume**: 
  - **Gesture**: Raise both thumbs up.
  - **Description**: This gesture increases the media volume.
  
  ![Increase Volume Gesture](link_to_increase_volume_gesture_image)

---

- **Decrease Volume**: 
  - **Gesture**: Lower both thumbs down.
  - **Description**: This gesture decreases the media volume.
  
  ![Decrease Volume Gesture](link_to_decrease_volume_gesture_image)

---

## Improvements

Future updates will focus on enhancing the accuracy of gesture recognition, especially at a distance. For optimal performance, ensure that your gestures are framed similarly to the demonstration images.

## Acknowledgments

Special thanks to MediaPipe for providing an excellent hand tracking model and comprehensive documentation, which have been instrumental in developing this project.

