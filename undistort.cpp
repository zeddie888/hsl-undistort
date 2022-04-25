/*

if (true)
{
  const Camera *cam = input.InputCamera();
  Stars *undistortedStars = new Stars();

  for (long unsigned i = 0; i < inputStars->size(); i++)
  {
    Star currStar = inputStars->at(i);

    float u = currStar.position.x;
    float v = currStar.position.y;

    float x = (u - cam->XCenter()) / cam->FocalLengthX();
    float y = (v - cam->YCenter()) / cam->FocalLengthY();

    float x0 = x;
    float y0 = y;

    for (int j = 0; j < cam->ITERS(); j++)
    {
      float rSq = x * x + y * y;
      float divBy = 1 + cam->K1() * rSq + cam->K2() * pow(rSq, 2) + cam->K3() * pow(rSq, 3);
      float deltaX = 2 * cam->P1() * x * y + cam->P2() * (rSq + 2 * pow(x, 2));
      float deltaY = cam->P1() * (rSq + 2 * pow(y, 2)) + 2 * cam->P2() * x * y;

      x = (x0 - deltaX) / divBy;
      y = (y0 - deltaY) / divBy;
    }
    float xAns = x * cam->FocalLengthX() + cam->XCenter();
    float yAns = y * cam->FocalLengthY() + cam->YCenter();

    Star undistortedStar(xAns, yAns, currStar.radiusX, currStar.radiusY, currStar.magnitude);
    undistortedStars->push_back(undistortedStar);
  }

  // Printing star coordinates for test
  result.stars = std::unique_ptr<Stars>(undistortedStars);
  std::cerr << "inputStars before: "
            << "\n";
  for (long unsigned i = 0; i < inputStars->size(); i++)
  {
    std::cerr << "\t"
              << "(" << inputStars->at(i).position.x << ", " << inputStars->at(i).position.y << ")"
              << ", \n";
  }

  inputStars = undistortedStars;
  std::cout << "\n\ninputStars after: "
            << "\n";
  for (long unsigned i = 0; i < inputStars->size(); i++)
  {
    std::cerr << "\t"
              << "(" << inputStars->at(i).position.x << ", " << inputStars->at(i).position.y << ")"
              << ", \n";
  }
}

*/