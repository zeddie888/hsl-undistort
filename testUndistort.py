"""
Testing script for undistort.py

Performs undistortion on chosen distorted image, then displays resulting image

Note:
    Resulting image contains flaws, likely due to rounding of corrected pixel coordinates,
    otherwise cannot index image matrix with non-integers

"""


import cv2 as cv
import json
import undistort

ITERS = 3

with open("calib.json") as f:
    data = json.load(f)

fname = input("Name of image to undistort: ")

# Read an image
img = cv.imread(f"sourceImages/{fname}")

n = img.shape[0]
m = img.shape[1]

res = img.copy()

for i in range(n):
    for j in range(m):
        # pixel = img[i, j]
        # (xd, yd) = (j, i): (xd, yd) are COORDINATES on Cartesian plane*
        u, v = j, i
        x_ans, y_ans = undistort.undistort(
            (u, v), data["distCoeffs"], data["cameraMatrix"], ITERS)

        # TESTING: x and y are floats, so we have to turn them into ints in order to index the image array
        # NOTE: due to this rounding, the undistorted image is slightly messed up- this shouldn't be a problem in reality
        x_ans = int(x_ans)
        y_ans = int(y_ans)

        if 0 <= x_ans < m and 0 <= y_ans < n:
            res[y_ans][x_ans] = img[i][j]

cv.imshow("New image", res)
cv.waitKey(0)
cv.destroyAllWindows()
