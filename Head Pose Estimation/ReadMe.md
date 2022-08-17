## Real-time head pose estimation project

Head pose implies a person's visual attention and interest. 
It plays an important role in many applications such as, human-machine interaction and driver assistance.

This project is to get the head pose from '2D' landmarks not 3D landmarks in real time.
To do this with the classical way they have to fit the 2d points with a 3d face model which is considered as a fitting technique. 
But in our case, it is not a deterministic solution and has its problems. Here comes the ML to replace the 3d fitting assumption, 
the camera parameters and the projection equations.

We used the following to build our project :
 1- dlib and mediapipe libraries for detecting the 2D face landmarks.
 2- Different machine learning algorithms to predict 3 angles(yaw-pitch-roll) in real time.
 
 

https://user-images.githubusercontent.com/96622170/185152354-c2da7d1a-20d9-4a4a-ad95-b0bbae95d78d.mp4

