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
The following instructions detail how to configure the hardware needed for this project. The following figure depicts the deployment diagram that is followed in this project.

![Babymon drawio (2)](https://user-images.githubusercontent.com/93753142/161405517-7803758d-29e9-411f-b2dc-5b877db42501.png)


### SenseHat Installation
Raspberry Pi 1 is connected to the SenseHat. To install the SenseHat perform the following:  
1. Turn off and disconnect the Raspberry Pi from the power supply.
2. Align the SenseHat with the GPIO pins on the Raspberry Pi, push down until the SenseHat rests firmly on top of the Pi. *Insert image?*

### Camera, Microphone, and Sound Sensor Installation

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

### Raspberry Pi 1

### Raspberry Pi 2

### Raspberry Pi 3
Raspberry Pi 3 is responsible for hosting the Flask server that serves as the Front End GUI for this project. To set up the flask server, perform the following:  
1. On Raspberry Pi 3, create a new directory to clone this repo.
2. Open the termincal, navigate to the new directory and clone the repo using the command: git clone https://github.com/kennyddeng/SYSC3010A-L1W-G11-Project.git
3. Navigate to the flask_app directory in the newly cloned repo
4. Edit [firebase.py](flask_app/firebase.py) and write the api_key, project_id, and database_url, for the Firebase database.
5. Open [requirements.txt](flask_app/requirements.txt), and install any missing python packages that are listed in the file.
6. Open the terminal, navigate to the flask_app directory, and start the flask app using the command: source start_flask.sh
