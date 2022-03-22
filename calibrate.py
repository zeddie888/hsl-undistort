"""
Givens:
  Let dimensions of the pattern be n (pts) x m (pts)

Find 3D coordinates for all of chessboard's corners (assume z = 0)
  [
    [0, 0, 0], [0, 1, 0], ... , [0, m-1, 0]
    [1, 0, 0], [1, 1, 0], ... , [1, m-1, 0]
    ...
    [n-1, 0, 0], [n-1, 1, 0], ... , [n-1, m-1, 0]
  ]

Find the pixel coordinates (u, v) for each board corner for each different image
  Use findChessboardCorners(img, patternSize, flags)
    cv.findChessboardCorners(img, (m, n), None)

  Refine corners with cornerSubPix(img, corners, winSize, zeroZone, criteria)
    Assume (-1, -1) for zeroZone

Find camera parameters using calibrateCamera()
  cv.calibrateCamera(objectPoints, imagePoints, imageSize)
  This function returns: retVal, cameraMatrix, distortionCoeffs, rotationVecs, translationVec

Save computed parameters in JSON:
  Distortion coefficients: k1, k2, p1, p2, k3 (k for radial, p for tangential distortion)
  Probably save camera matrix as well

"""

import cv2 as cv
import glob
import numpy as np
import json

TESTING_DIR = "testing/"
WIN_SIZE = (11, 11)
TERM_CRITERIA = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 30, 0.001)

print("Input dimensions of pattern")
n = int(input("Number of rows: "))  # normally use: 6
m = int(input("Number of columns: "))  # normally use: 7

v = input("View corners? (y/n): ")

imgPoints = []
allObjPoints = []

objPoints = np.zeros((n*m, 3), np.float32)
objPoints[:, :2] = np.mgrid[0:m, 0:n].T.reshape(-1, 2)

testImgs = glob.glob(TESTING_DIR + '*.jpg')
imgSize = None

for count, image in enumerate(testImgs):
    img = cv.imread(image)
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    res, corners = cv.findChessboardCorners(gray, (m, n), None)  # no flags
    if res:
        imgSize = gray.shape[::-1]
        allObjPoints.append(objPoints)
        cv.cornerSubPix(gray, corners, WIN_SIZE, (-1, -1),
                        TERM_CRITERIA)  # assume no zero zone
        imgPoints.append(corners)

    if v == 'y':
        cv.drawChessboardCorners(img, (m, n), corners, res)
        cv.imshow(f"Calibration Test Image {count}", img)
        cv.waitKey(0)
        cv.destroyWindow(f"Calibration Test Image {count}")

cv.destroyAllWindows()

allObjPoints = np.array(allObjPoints)

res, cameraMatrix, distortionCoeffs, rotVecs, tVec = cv.calibrateCamera(
    allObjPoints, imgPoints, imgSize, None, None)

print("Distortion Coefficients", distortionCoeffs.flatten())
print("Camera Matrix", cameraMatrix)
# print("Translation Vectors", tVec)  # don't need
# print("Rotation Vectors", rotVecs)  # don't need

res = {
    "distCoeffs": distortionCoeffs.flatten().tolist(),
    "cameraMatrix": cameraMatrix.tolist()
}

with open("calib.json", "w+") as f:
    json.dump(res, f, indent=4)
