## Real-time head pose estimation project

Head pose implies a person's visual attention and interest. 
It plays an important role in many applications such as, human-machine interaction and driver assistance.

The goal of this project was to determine head pose from 2D landmarks in real time, rather than using 3D landmarks. Traditionally, this involves fitting the 2D points to a 3D face model, a process known as fitting. Instead, I utilized machine learning to eliminate the need for 3D fitting, as well as the camera parameters and projection equations.

The project was built using:
1. Dlib and Mediapipe libraries for detecting 2D face landmarks.2.  Data preprocessing (scaling and cleaning)
3. Fine-tuning machine learning algorithms to predict the three angles (yaw, pitch, and roll) in real time.
 
 

https://user-images.githubusercontent.com/96622170/185152354-c2da7d1a-20d9-4a4a-ad95-b0bbae95d78d.mp4

