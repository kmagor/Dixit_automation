import cv2
import numpy as np
#include features2d.hpp
font = cv2.FONT_HERSHEY_COMPLEX

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    blurred_frame = cv2.GaussianBlur(frame, (5, 5), 0)
    hsv = cv2.cvtColor(blurred_frame, cv2.COLOR_BGR2HSV)

    lower_blue = np.array([89, 60, 0])
    upper_blue = np.array([135, 255, 255])
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Setup SimpleBlobDetector parameters.
    params = cv2.SimpleBlobDetector_Params()

    # Change thresholds
    params.minThreshold = 100
    params.maxThreshold = 200

    # Filter by Area.
    params.filterByArea = True
    params.minArea = 1500

    # Filter by Circularity
    params.filterByCircularity = True
    params.minCircularity = 0.0

    # Filter by Convexity
    params.filterByConvexity = True
    params.minConvexity = 0.85

    # Filter by Inertia
    params.filterByInertia = False
    params.minInertiaRatio = 0.01

    # Create a detector with the parameters
    detector = cv2.SimpleBlobDetector_create(params)

    # Detect blobs.
    keypoints = detector.detect(mask)
    print(len(keypoints))
    # Draw detected blobs as red circles.
    # cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures the size of the circle corresponds to the size of blob
    im_with_keypoints = cv2.drawKeypoints(mask, keypoints, np.array([]), (0, 0, 255),
                                          cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

    # Show keypoints
    cv2.imshow("Keypoints", im_with_keypoints)
    cv2.waitKey(0)

    for contour in contours:
        cv2.drawContours(frame, contour, -1, (0, 255, 0), 3)

    cv2.imshow("Frame", frame)
    cv2.imshow("Mask", mask)
    #cv2.imshow("Keypoints", im_with_keypoints)
    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()


#
#img = cv2.imread("shapes.jpg", cv2.IMREAD_GRAYSCALE)
# _, threshold = cv2.threshold(img, 240, 255, cv2.THRESH_BINARY)
# _, contours, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
#
# for cnt in contours:
#     approx = cv2.approxPolyDP(cnt, 0.01*cv2.arcLength(cnt, True), True)
#     cv2.drawContours(img, [approx], 0, (0), 5)
#     x = approx.ravel()[0]
#     y = approx.ravel()[1]
#     if len(approx) == 3:
#         cv2.putText(img, "Triangle", (x, y), font, 1, (0))
#     elif len(approx) == 4:
#         cv2.putText(img, "Rectangle", (x, y), font, 1, (0))
#     elif len(approx) == 5:
#         cv2.putText(img, "Pentagon", (x, y), font, 1, (0))
#     elif 6 < len(approx) < 15:
#         cv2.putText(img, "Ellipse", (x, y), font, 1, (0))
#     else:
#         cv2.putText(img, "Circle", (x, y), font, 1, (0))
#
#         cv2.imshow("shapes", img)
#         cv2.imshow("Threshold", threshold)
#         cv2.waitKey(0)
#         cv2.destroyAllWindows()