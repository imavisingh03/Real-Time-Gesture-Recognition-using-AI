import cv2
import mediapipe as mp
import pyautogui
from math import sqrt

# Initialize MediaPipe hands.
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.8, min_tracking_confidence=0.5)
mp_drawing = mp.solutions.drawing_utils

# Open video capture.
cap = cv2.VideoCapture(0)

# Function to get the coordinates of a landmark.
def get_coords(landmark, frame):
    width = frame.shape[1]
    height = frame.shape[0]
    return int(landmark.x * width), int(landmark.y * height)

# Function to detect volume gestures (thumbs up/down).
def detect_volume_gesture(landmarks, frame):
    thumb_tip = landmarks[mp_hands.HandLandmark.THUMB_TIP]
    middle_finger_pip = landmarks[mp_hands.HandLandmark.MIDDLE_FINGER_PIP]
    wrist = landmarks[mp_hands.HandLandmark.WRIST]

    thumb_tip_coords = get_coords(thumb_tip, frame)
    middle_pip_coords = get_coords(middle_finger_pip, frame)
    wrist_coords = get_coords(wrist, frame)

    if thumb_tip_coords[1] < wrist_coords[1] and thumb_tip_coords[1] < middle_pip_coords[1]:
        return "volume_up"
    elif thumb_tip_coords[1] > wrist_coords[1] and thumb_tip_coords[1] > middle_pip_coords[1]:
        return "volume_down"
    return None

# Function to detect play/pause gestures (open/closed hand).
def detect_play_gesture(landmarks, frame):
    index_finger_tip = landmarks[mp_hands.HandLandmark.INDEX_FINGER_TIP]
    middle_finger_tip = landmarks[mp_hands.HandLandmark.MIDDLE_FINGER_TIP]
    ring_finger_tip = landmarks[mp_hands.HandLandmark.RING_FINGER_TIP]
    pinky_tip = landmarks[mp_hands.HandLandmark.PINKY_TIP]

    index_finger_mcp = landmarks[mp_hands.HandLandmark.INDEX_FINGER_MCP]
    middle_finger_mcp = landmarks[mp_hands.HandLandmark.MIDDLE_FINGER_MCP]
    ring_finger_mcp = landmarks[mp_hands.HandLandmark.RING_FINGER_MCP]
    pinky_mcp = landmarks[mp_hands.HandLandmark.PINKY_MCP]

    # Make two lists one for Tips one for Joints
    finger_Tips = [
        get_coords(index_finger_tip, frame), get_coords(middle_finger_tip, frame), 
        get_coords(ring_finger_tip, frame), get_coords(pinky_tip, frame)]

    finger_mcp_Joints =  [
        get_coords(index_finger_mcp, frame), get_coords(middle_finger_mcp, frame), 
        get_coords(ring_finger_mcp, frame), get_coords(pinky_mcp, frame)]

    open_hand = True
    for fingertips, mcp in zip(finger_Tips, finger_mcp_Joints):
        if fingertips[1] > mcp[1]:
            open_hand = False
    
    if open_hand:
        return "pause_play"
    else:
        return "close_hands"


# Function to detect forward gesture (thumb and index finger distance).
def detect_forward_gesture(landmarks, frame):
    index_finger_tip = landmarks[mp_hands.HandLandmark.INDEX_FINGER_TIP]
    middle_finger_tip = landmarks[mp_hands.HandLandmark.MIDDLE_FINGER_TIP]
    thumb_tip = landmarks[mp_hands.HandLandmark.THUMB_TIP]

    index_tip_coords = get_coords(index_finger_tip, frame)
    middle_tip_coords = get_coords(middle_finger_tip, frame)
    thumb_tip_coords = get_coords(thumb_tip, frame)

    index_x, index_y = int(index_tip_coords[0]), int(index_tip_coords[1])
    thumb_x, thumb_y = int(thumb_tip_coords[0]), int(thumb_tip_coords[1])
    middle_x, middle_y = int(middle_tip_coords[0]), int(middle_tip_coords[1])

    center_x1, center_y1 = (index_x + thumb_x) // 2, (index_y + thumb_y) // 2
    center_x2, center_y2 = (middle_x + thumb_x) // 2, (middle_y + thumb_y) // 2

    cv2.line(frame, (index_x, index_y), (thumb_x, thumb_y), (255, 0, 255), 3)
    cv2.line(frame, (middle_x, middle_y), (thumb_x, thumb_y), (255, 0, 255), 3)

    distance_index_thumb = sqrt((thumb_x - index_x)**2 + (thumb_y - index_y)**2)
    distance_middle_thumb = sqrt((thumb_x - middle_x)**2 + (thumb_y - middle_y)**2)

    cv2.circle(frame, (center_x1, center_y1), 15, (255, 0, 255), -1)
    cv2.circle(frame, (center_x2, center_y2), 15, (255, 0, 255), -1)

    # Adjust the distance threshold as needed for gesture sensitivity
    if distance_index_thumb < 50:
        cv2.circle(frame, (center_x1, center_y1), 15, (0, 255, 0), -1)
        return "forward"
    elif distance_middle_thumb < 50:
        cv2.circle(frame, (center_x2, center_y2), 15, (0, 255, 0), -1)
        return "rewind"

    return None

        

# Main loop for video capture and gesture detection.
last_detected_gesture = None

while True:
    success, frame = cap.read()

    frame = cv2.flip(frame, 1)
    frame = cv2.resize(frame, (0,0), fx=1, fy=1)
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # We have stored information in results
    results = hands.process(frame_rgb)

    # This basically gives you the x,y,z coordinates in form of landmark {x: 0.254973888 y: 0.436065882 z: -0.0972036421}
    # They are in the form of ratios to get the coordinates yoy multiply them with width and height
    # print(results.multi_hand_landmarks)

    current_gesture = None
    # Extract and draw landmarks on the frame
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            landmarks = hand_landmarks.landmark
            
            # Detect gestures
            current_gesture = detect_forward_gesture(landmarks, frame)
            if current_gesture is None:
                current_gesture = detect_volume_gesture(landmarks, frame)
            if current_gesture is None:
                current_gesture = detect_play_gesture(landmarks, frame)

    # Perform action based on detected gesture, only if it has changed
    if current_gesture != last_detected_gesture:
        if current_gesture == "pause_play":
            pyautogui.press('playpause')
            cv2.putText(frame, "Pause/Play", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
        elif current_gesture == "volume_up":
            pyautogui.hotkey('ctrl', 'up')  # Adjust volume up by 5 (using Ctrl+Up)
            cv2.putText(frame, "Volume Up", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
        elif current_gesture == "volume_down":
            pyautogui.hotkey('ctrl', 'down')  # Adjust volume down by 5 (using Ctrl+Down)
            cv2.putText(frame, "Volume Down", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
        elif current_gesture == "forward":
            pyautogui.hotkey('alt', 'right')
            cv2.putText(frame, "Forward 30s", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
        elif current_gesture == "rewind":
            pyautogui.hotkey('alt', 'left')
            cv2.putText(frame, "Rewind 30s", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

        last_detected_gesture = current_gesture

    # Show the frame with annotations
    cv2.imshow('Hand Gestures', frame)

    # Exit condition
    if cv2.waitKey(1) == ord('q'):
        break

# Release the camera and close any open windows
cap.release()
cv2.destroyAllWindows()
