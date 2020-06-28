import numpy as np
import cv2 as cv

def main():
    cap = cv.VideoCapture(0)
    width = int(cap.get(3))
    height = int(cap.get(4))
    print(width, height)

    while cap.isOpened():
        rect, frame = cap.read()
        
        cv.imshow("Coolest man in the world", frame)
        edges = cv.Canny(frame, 50, 100)
        cv.imshow("edges", edges)
        # 640, 480, 1
        colored_edges = np.zeros((height, width, 3)) # 640, 480, 3
        # (0, 0, 0)
        # # frame[xx][yy]
        for xx in range(height):
            for yy in range(width):
                if (edges[xx][yy] == 0):
                    colored_edges[xx][yy][0] = 0
                    colored_edges[xx][yy][1] = 0
                    colored_edges[xx][yy][2] = 0
                else:
                    colored_edges[xx][yy][0] = frame[xx][yy][0]
                    colored_edges[xx][yy][1] = frame[xx][yy][1]
                    colored_edges[xx][yy][2] = frame[xx][yy][2]
        print(colored_edges)
        cv.imshow("Colored", colored_edges)
        key = cv.waitKey(5) & 0xFF 
        exitKeys = [ord('q'), ord('e'), ord('Q'), ord('E'), 27]
        if key in exitKeys:
            cap.release() # Close the window

if __name__ == "__main__":
    main()



#Mission: Read Numpy Doc.
# Numpy can do 21 and 22 automatically. 
# Single Function that will receive 2 arrays in a condition.
# Array1, Array2, Array1 = 5. Everytime finds array5 in array1, copy volume of array two, otherwise copy the volume of array one. 
# If not met: copy 1. if met: copy 2  ==> into 3. 
#Optimizes the line 20 to 29. 
