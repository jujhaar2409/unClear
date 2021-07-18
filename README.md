# (un)clear

This project is based on Single Image Super-resolution using Machine Learning. The technique we used to finally implement this is called ESRGAN. More can be learned about this from [this paper](https://arxiv.org/abs/1809.00219).

The initial phases of the project involved getting to know many of the tools that we finally required to complete the implementation. To get familiar with these we also did many mini-projects associated with certain topics. The code for the mini-projects is in the assignments directory. The Project itself started in the first week of April.

## Outline

1. OpenCV basics
2. Assignments 1, 2 and 3 to do with OpenCV
3. Google ML course
4. Tensorflow course on Udemy
5. Implementing a digit recognizer model using a Convolutional Neural Network 
6. Learning about RESNETS
7. Learning about GAN and CGAN
8. Implementing CGAN sketch colorizer model
9. Reading papers and articles related to ESRGAN
10. Final Implementation of ESRGAN model

## Topics in Detail

### OpenCV Basics

We learnt a lot about opencv and how to use it in our project in this stage of SoC. Rotating, cropping, blurring, and many more operations were learnt. We also had to use opencv to create a sketch image of ourselves from a live video feed as our assignment.

### Learning the Basics of Maching Learning

In this phase we mainly learnt about the theoretical aspects of machine learning through the google ML course. It helped build a strong foundation for building and training models.

### Maching Learning with Tensorflow

This phase was mostly hands on. We had multiple coding assignments in this phase through the way of the Tensorflow course on Udemy that we followed. This taught us to apply the previously learned theory in a practical setup. We built a digit recognizer using CNNs in this section. The code can be found in [this file](./assignments/MNIST_num_recog.ipynb)

### Learning about different architectures of ML models

We learnt about different types of ML models like RESNETs, GAN, CGAN and then implemented our learning in a project which was the anime sketch colorizer. This project involves the use of a CGAN to generate colored images from pencil sketches. The code for this is [here](./assignments/sketch_colorizer.ipynb)

### ESRGAN

ESRGAN, which is short for Enhanced Super-Resolution Generative Adversarial Network, was the final goal of our SoC. We had to read papers and articles about this topic and finally create our own implementation. A detailed account of the implementation is given in the README.md in the final directory. The code also resides there.
