# SMART_SPECS
This project is an aid to the blind. Till date there has been not much technological advancement in the way the blind navigate. So I have tried using deep learning particularly CNN so that they can get some external help to navigate through the streets.
<br>
<br>
![SMART_SPECTACLES](https://user-images.githubusercontent.com/54498757/229739684-8a0fe594-a0ec-4613-9fe0-cb4e54fc7175.png)


# The Approach 
## Collecting Training Data
This is an implementation of CNN's, and we all know that they require a large amount of training data. So the first obstruction in my way was to get access to correclty labeled dataset of images. So I went around places and recorded a lot of videos(of all types of roads and offroads).Then wrote a basic python script to  save images from the video(1 image out of every 5 frames, because the consecutive frame are almost identical). Collection of almost 10000 such images almost 3300 for each class(i.e. left right and center) has been used.This is present in repo.

## Training the Model
A collection of CNN architectures has been made to train the model. Then I evaluated the performance of all the models and chose the one with the best accuracy. I got a training accuracy of about ~97%.I got roughly same accuracy for all the trained model but I realized that the model in which implemented regularization performed better on this particular test set.
  
## Interfacing with the Arduino
The next problem was how can I tell the blind people in which direction to move .
So I connected my python program to an Arduino. I connected the servo motors to arduino and fixed the servo motors to the sides of an spectacle.  Using Serial communication I can tell the arduino which servo motor to move which would then press to one side of the blind person's head and would indicate him in which direction to move.Intial attempts also included giving voice commands for more complex instructions,but decided not to as it will bring added inability to user.

# Detection of stop signs. ##
This is done using opencv. I load in a pretrained stop sign haar cascade and then identify the location of the stop sign so that the device can steer the blind person.

# Face Detection
This is achieved using Dlibs face detector.(trying to implement face recognition)

## Requirements
0. Python 3.x
1. Tensorflow
2. Keras
3. OpenCV 3.4(for loading,resizing images)
4. h5py(for saving trained model)
5. pyttsx3
6. A good CPU (preferably with a GPU).

## Installing the requirements
1. Start your terminal of cmd depending on your os.
  2. If you have a NVidia GPU then make sure you have the prerequisites for Tensorflow GPU installation (Refer to official site). Then use this commmand

    pip install -r requirements_gpu.txt

  3. In case you do not have a GPU then use this command

    pip install -r requirements_cpu.txt

## Train your own classifier
To train your own classifier you need to gather data for all three type(.i.e images from left side of road, right side, and center region of the road) and then run model_trainer.py(you need to change the directories of images in model_trainer.py first).I used around 10000 images.
It took me about 30 minutes to train each network.<br>

