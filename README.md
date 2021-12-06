# lipstick
Project1: Virtual Makeup Feature 1.

For get an automatic lipstick algorithm , we will need to follow the following sequence of steps those are implemented in [main.py](https://github.com/EdissonM/lipstick/blob/main/main.py):

- Detect the facial landmarks using:
    > shape_predictor_68_face_landmarks.dat.
- Choose the mouth landmarks and obtain that convex polygon for get a mask.

<img src="results/mask.jpg" width="500" height="500" />

- Enhance the mask with blur for soft blending.

<img src="results/mask_gaussian.jpg" width="500" height="500" />

- Isolate mouth and face.

<img src="results/not_mouth.jpg" width="500" height="500" />

<img src="results/mouth.jpg" width="500" height="500" />

- Apply color transformation in HSV space using Huge layer on the mouth image.
<img src="results/mouth_changed.jpg" width="500" height="500" />


- Add mouth and face without mouth, for results.
<img src="results/Lipstick.jpg" width="500" height="500" />
