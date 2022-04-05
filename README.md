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
The following is a breakdown of the repository structure that details where the source files for each software application are located.

### [Python_Modules](Python_Modules)
Directory contains  the source files for common python classes used in various places.

### [audio](audio)
Directory contains the source files needed for recording and uploading audio using the microphone.

### [detect_sound](detect_sound)
Directory contains the source files needed for querying and uploading sound sensor data.

### [flask_app](flask_app)
Directory contains the source files needed to host the flask app on a Pi. The flask app is the source of the front end GUI for the project.

### [video](video)
Directory contains the source files needed for recording and uploading video using the PiCamera.

### [write](write)
Directory contains the source files needed for querying and uploading temperature data.

## Installation Instructions
The following instructions detail how to configure the hardware needed for this project. The following figure depicts the deployment diagram that is followed in this project.

![Babymon drawio (2)](https://user-images.githubusercontent.com/93753142/161405517-7803758d-29e9-411f-b2dc-5b877db42501.png)


### SenseHat Installation
Raspberry Pi 1 is connected to the SenseHat. To install the SenseHat perform the following:  
1. Turn off and disconnect the Raspberry Pi from the power supply.
2. Align the SenseHat with the GPIO pins on the Raspberry Pi, push down until the SenseHat rests firmly on top of the Pi. *Insert image?*

### PiCamera Installation
Raspberry Pi 2 is connected to the PiCamera. To install the PiCamera perform the following:
1. Turn off and disconnect the Raspberry Pi from the power supply.
2. Open Raspberry Pi CSI port clasp. Align the PiCamera module with the CSI port on the Raspberry Pi, push down until the PiCamera module is fully seated in the CSI port. Close Raspberry Pi CSI port clasp. *Insert image?*

### USB Microphone Installation
Raspberry Pi 2 is connected to the USB Microphone. To install the USB Microphone perform the following:
1. Turn off and disconnect the Raspberry Pi from the power supply.
2. Plug USB Microphone into any available USB port on the Raspberry Pi. Rotate 180 degrees if USB Microphone does not insert. Try 3x as you were right the first attempt. *Insert image?*

### Sound Sensor Installation
Raspberry Pi 2 is connected to the Sound Sensor. To install the Sound Sensor perform the following:
1. Turn off and disconnect the Raspberry Pi from the power supply.
2. Plug Male end of Male-Female Jumper Wires to Sound Sensor Pinout. 1x for OUT/D.OUT, 1x for 5V, 1x for GND. Refer to Figure 1 for pin labels. NOTE: In Figure 1, OUT/A.OUT is not required (it is an additional microphone feature built into this make and model sound sensor, for this tutorial it is not required to be used).
3. Plug Female end of Male-Female Jumper Wires to Raspberry Pi 4 Header Pins. Refer to Figure 1 for pin labels. Plug OUT/D.OUT wire into GPIO2 (PIN 3), Plug 5V into 5V (PIN 4), Plug GND into GROUND (PIN 6). NOTE: For more advanced users, you may be able to use different GPIO pins other then the ones listed in this tutorial. Please refer to Further Relevant Readings: Raspberry Pi GPIO Pins for reference.

## Setup Instructions
The following instructions detail how to configure software infrastructure needed for this project. Refer to the deployment diagram above for the software deployment.

### Firebase Database and Storage
The Firebase database is used to store sensor data, temperature thresholds, as well as video and audio recordings. To set up the Firebase database perform the following:  
1. Navigate to https://console.firebase.google.com/ and sign in with a google account
2. Select add project
3. Enter information, disable analytics and select create project
4. Once project is created, navigate to Realtime Database on the left sidebar
5. Select start in test mode and enable.
6. Perform steps 5-6 for Storage
7. Navigate to Authentication on the left sidebar
8. At the top, select Sign-in method and then select Anonymous
9. Navigate to the settings icon next to Project Overview on the left sidebar and select project settings, take note of the Project ID and Web API Key
10. Finally navigate to the Realtime Database again and take note of Database URL which can be copied.

### Twilio SMS Service
Twilio SMS service allows for sending SMS messages through Python. Twilio provides a phone number as well as a Python API that can be used to send SMS messages. To set up Twilio perform the following:  
1. Navigate to https://www.twilio.com/ and sign up for a free trial
2. Go through the Twilio tutorial to get a phone number
3. Once the phone number has been created, take note of the Phone Number, Account SID, and Auth Token in the main console.
4. Navigate to Develop on the left sidebar, select Phone Numbers > Manage > Verified Caller ID's and add phone numbers which will receive the SMS messages.

### Clone Repository
1. Create a new directory to clone this repo.
2. Open the terminal, navigate to the new directory and clone the repo using the command: git clone https://github.com/kennyddeng/SYSC3010A-L1W-G11-Project.git

### Configure Firebase Database Configuration
1. Edit [firebase.py](Python_Modules/firebase.py) and write the api_key, project_id, and database_url, for the Firebase database.

## Raspberry Pi/Device Setup
### Raspberry Pi 1

### Raspberry Pi 2
Raspberry Pi 2 is responsible for hosting the Video Livestream and monitoring/detecting ambient sound levels. When the ambient sound level reaches over a certain threshold, a video/audio file will be captured and uploaded to Firebase Storage for viewing on a Flask Server.
1. To host the Video Livestream, navigate to [livestream.py](livestream.py) in the root directory and run the script.
2. To constantly poll the ambient environment and detect high sound levels (and also record video/audio when this event occurs), navigate to [device2_monitor.py](device2_monitor.py) in the root directory and run the script.

### Raspberry Pi 3
Raspberry Pi 3 is responsible for hosting the Flask server that serves as the Front End GUI for this project. To set up the flask server, perform the following:
1. Navigate to the flask_app directory in the cloned repo
2. Edit [firebase.py](flask_app/firebase.py) and write the api_key, project_id, and database_url, for the Firebase database.
3. Open [requirements.txt](flask_app/requirements.txt), and install any missing python packages that are listed in the file.
4. Open the terminal, navigate to the flask_app directory, and start the flask app using the command: source start_flask.sh
