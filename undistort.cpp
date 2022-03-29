/*

if(isUndistortEnabled){
  const Camera* cam = input.InputCamera();
  Stars* undistortedStars = new Stars();

  for(int i = 0; i < inputStars->size(); i++){
    Star currStar = inputStars->at(i);

    float u = currStar.position.x;
    float v = currStar.position.y;

    float x = (u - cam->XCenter()) / cam->FocalLengthX();
    float y = (v - cam->YCenter()) / cam->FocalLengthY();

    float x0 = x;
    float y0 = y;

    for(int j = 0; j < iters; j++){
      float rSq = x*x + y*y;
      float divBy = 1 + cam->K1()*rSq + cam->K2()*pow(rSq, 2) + cam->K3()*pow(rSq, 3);
      float deltaX = 2*cam->P1()*x*y + cam->P2()*(rSq + 2*pow(x,2));
      float deltaY = cam->P1() * (rSq + 2*pow(y, 2)) + 2*cam->P2()*x*y;

      x = (x0 - deltaX) / divBy;
      y = (y0 - deltaY) / divBy;
    }
    float xAns = x * cam->FocalLengthX() + cam->XCenter();
    float yAns = y * cam->FocalLengthY() + cam->YCenter();


  }

}

Changes to Camera.hpp:

float FocalLengthX() const { return fx; };
float FocalLengthY() const { return fy; };

float XCenter() const { return cx; };
float YCenter() const { return cy; };

float K1() const {return k1; };
float K2() const {return k2; };
float P1() const {return p1; };
float P2() const {return p2; };
float K3() const {return k3; };


QUESTIONS:
1. How should calib.py give values to Camera.hpp?
2. How do you actually save the new undistorted coordinates?












*/