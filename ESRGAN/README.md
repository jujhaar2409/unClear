# ESRGAN

This directory contains the jupyter notebooks that I have used to implement ESRGAN. The model uses a relativistic discriminator, an RRDB based generator and also incorporates perceptual loss. The main ideas have been taken from [this paper on ESRGAN](https://arxiv.org/abs/1809.00219).

## Basic Functioning

The way this works is like a typical GAN with some modifications(mentioned in the paper linked above). The working of a GAN is quite simple, the generator produces an output, the discriminator then tries to determine if the output is a realistic high resolution image and then based on the output of the discriminator, the generator values are tuned.

The perceptual loss and VGG loss are 2 major additions to the basic model of SRGAN. They make the images look more realistic. This is because these losses corelate more strongly to human image perception itself rather than a standard loss function like mean squared loss.

Another addition is the use of RRDBs which are not used in SRGAN.

## Results

Some of the results, which can also be found in the notebooks are given below.

In each of the below images, the image on the left is the input to the generator, the image in the center is the target output/ground truth and the image on the right is the image produced by the ESRGAN model.

### From the first notebook

![](./imgs/imgs1/img1.png)
![](./imgs/imgs1/img2.png)
![](./imgs/imgs1/img3.png)
![](./imgs/imgs1/img4.png)
![](./imgs/imgs1/img5.png)

### From the second notebook

![](./imgs/imgs2/img1.png)
![](./imgs/imgs2/img2.png)
![](./imgs/imgs2/img3.png)
![](./imgs/imgs2/img4.png)
![](./imgs/imgs2/img5.png)
![](./imgs/imgs2/img6.png)
![](./imgs/imgs2/img7.png)
![](./imgs/imgs2/img8.png)
![](./imgs/imgs2/img9.png)

### From the third notebook

![](./imgs/imgs3/img1.png)
![](./imgs/imgs3/img2.png)
![](./imgs/imgs3/img3.png)
![](./imgs/imgs3/img4.png)
![](./imgs/imgs3/img5.png)
