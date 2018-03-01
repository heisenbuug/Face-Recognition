# Face-Recognition

This project is made to recognise front-view face, eyes and smile. 

### Introduction

Image recognition, in the context of machine vision, is the ability of software to identify objects, places, people, writing and actions in images. Computers can use machine vision technologies in combination with a camera and artificial intelligence software to achieve image recognition.
Image recognition has very wide range of applications, some examples are: 
* Powering self-driving cars
* Boosting augmented reality applications and gaming
* Teaching machines to see
* Image Classification for Websites with Large Visual Databases
* Image Search

### Technologies Used

I made this project on Ubuntu 16.04 LTS
* Python
* Anaconda
* Spyder 3.1.4
* OpenCV
* XML

### Voila-Jones Algorithm

P. Viola, M. J. Jones, “Robust Real-Time Face
Detection”, International Journal of Computer Vision
57(2), 137–154, 2004

Check Source Folder for the original paper 

###### Three main steps in appling this algorithm are:
* Haar like features
* Integral Image
* Adaptive Bosting

###### Haar like features
Haar-like features are digital image features used in object recognition. They owe their name to their intuitive similarity with Haar wavelets and were used in the first real-time face detector. Here I have used rectangular features.

###### Integral Image
The integral image at location x , y contains the sum of the pixels above and to the left of x , y. The integral image allows integrals for the Haar extractors to be calculated by adding only four numbers.

###### AdaBoost
The training process uses AdaBoost to select a subset of features and construct the classifier. A large set of images, with size corresponding to the size of the detection window, is prepared. This set must contain positive examples for the desired filter (e.g. only front view of faces), and negative examples (nonfaces). Each image has index l, l = 1…L. For each image, a corresponding value yl, is established. yl=1 for faces and yl=0 for nonfaces.
