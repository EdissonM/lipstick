# lipstick
Project1: Virtual Makeup Feature 1.

![result](results/Lipstick.jpg)
For get an automatic lipstick algorithm , we will need to follow the following sequence of steps:
- Detect the facial landmarks using:
    > shape_predictor_68_face_landmarks.dat.
- Choose the mouth landmarks and obtain that convex polygon for get a mask.
![mask](results/mask.jpg)
- Enhance the mask with blur for soft blending.
![blur](results/mask_gaussian.jpg)
- Isolate mouth and face.
![face without mouth](results/not_mouth.jpg)

![mouth](results/mouth.jpg)
- Apply color transformation in HSV space using Huge layer on the mouth image.
![mouth_changed](results/mouth_changed.jpg)

- Add mouth and face without mouth, for results.
![result](results/Lipstick.jpg)