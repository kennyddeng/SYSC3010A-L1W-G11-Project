# SYSC3010 Computer Systems Development Project  

## IoT Baby Monitor Alert System  
![cover_image drawio](https://user-images.githubusercontent.com/93753142/161402149-f458a4a7-0422-4715-af52-6574e8add1ae.png)

### Group: L1W-G11  
Cristian Figueroa  
Christopher Nguyen  
Kenny Deng  
**TA:** Zein Hajj-Ali  

## Project Summary
Baby Monitors require parents and guardians to actively use their technology and time to monitor their babies. Our group’s goal is to implement a system that passively monitors the baby and notifies parents (through SMS) of alarming events, while also providing 24/7 visual and audio feedback of the baby.  
  
Alarming events can be a change in the room temperature level. The Raspberry Pi SenseHat monitors the ambient room temperature.  If the temperature drops too low or goes too high parents will be notified. Additionally, a sound sensor will monitor the audio levels in the room. If a high noise level is detected (presumably from a baby’s cry) parents will be notified.  
  
High noise level events also trigger a video and audio recording to be taken using the Raspberry Pi Cam and a Microphone. These recordings are uploaded to a database for future viewing. A constant video livestream also monitors the baby.  
  
A web-based GUI is provided to allow parents and guardians to interact with the baby monitor system. Through the GUI, parents can access historical room temperature and sound sensor data to see when events were triggered. Additionally, they can set the minimum and maximum temperature thresholds for which to be notified. Finally, they can view the livestream of the baby and saved recordings.  


## Repo Description
### [audio](audio)
Directory contains the source files needed for recording and uploading audio using the microphone.

### [detect_sound](detect_sound)
Directory contains the source files needed for querying and uploading sound sensor data.

### [flask_app](flask_app)
Directory contains the source files needed to host the flask app on a Pi. The flask app is the source of the front end GUI for the project.

### [Python_Modules](Python_Modules)
Directory contains  the source files for common python classes used in various places.

### [video](video)
Directory contains the source files needed for recording and uploading video using the PiCamera.

### [write](write)
Directory contains the source files needed for querying and uploading temperature data.

## Installation Instructions

## Setup Instructions
