import cv2
import numpy as np

cap = cv2.VideoCapture(0)


transformation_state = {'S': False, 'T': False, 'L': False}

while True:
   
    ret, frame = cap.read()
    key = cv2.waitKey(10) & 0xFF
    if key == ord('q'):
        break
    elif key == ord('S'):
         transformation_state['S'] = not transformation_state['S']
    elif key == ord('T'):
        transformation_state['T'] = not transformation_state['T']
    elif key == ord('L'):
       transformation_state['L'] = not transformation_state['L']

    
    if transformation_state['S']:
        frame = cv2.resize(frame, None, fx=4, fy=4, interpolation=cv2.INTER_LINEAR)
    if transformation_state['T']:
        M = np.float32([[1, 0, -100], [0, 1, 65]])
        frame = cv2.warpAffine(frame, M, (frame.shape[1], frame.shape[0]))
    if transformation_state['L']:
        frame = cv2.flip(frame, 1)

    
    cv2.imshow('Video Feed', frame)


cap.release()
cv2.destroyAllWindows()

