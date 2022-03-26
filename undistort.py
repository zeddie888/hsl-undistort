"""
Givens:
  calib.json contains camera matrix K and list of distortion coefficients
  Some arbitrary image

  Formulas:
    Radial distortion:
      x_distorted = x (1+ k1*r^2 + k2*r^4 + k3r^6)
      y_distorted = y (1+ k1*r^2 + k2*r^4 + k3r^6)

    Tangential distortion:
      x_distorted = x + [2p1 * xy + p2(r^2 + 2x^2)]
      y_distorted = y + [p1(r^2 + 2y^2) + 2p2* xy]

Read calib.json to get:
  fx, fy, cx, cy
  k1, k2, p1, p2, k3

TODO

Done!

"""


def undistort(inputCoord, distCoeffs, K, iters=3):
    u, v = inputCoord
    k1, k2, p1, p2, k3 = distCoeffs
    fx = K[0][0]
    fy = K[1][1]
    cx = K[0][2]
    cy = K[1][2]

    x = (u - cx) / fx
    y = (v - cy) / fy
    x0, y0 = x, y
    for _ in range(iters):
        rSq = x*x + y*y  # r^2
        divBy = 1 / (1 + k1*rSq + k2*rSq**2 + k3*rSq**3)
        deltaX = 2*p1*x*y + p2*(rSq+2*x**2)
        deltaY = p1*(rSq + 2*y**2) + 2*p2*x*y
        x = (x0 - deltaX) * divBy
        y = (y0 - deltaY) * divBy

    # now we have (x_ans, y_ans)- the correct coordinates of pixel (u, v)
    x_ans = x * fx + cx
    y_ans = y * fy + cy
    return (x_ans, y_ans)
