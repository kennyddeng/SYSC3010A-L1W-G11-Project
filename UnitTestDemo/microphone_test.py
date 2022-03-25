from pathlib import Path
import pyaudio
import wave
import pyrebase
import unittest

class TestMicrophone(unittest.TestCase):
    def test_hardware(self): # save file locally
        form_1 = pyaudio.paInt16 # 16-bit resolution
        chans = 1 # 1 channel
        samp_rate = 44100 # 44.1kHz sampling rate
        chunk = 4096 # 2^12 samples for buffer
        record_secs = 5 # seconds to record
        dev_index = 1 # device index found by p.get_device_info_by_index(ii)
        wav_output_filename = str(Path().resolve().parent) + '/recordings/test0.wav'  # record and save to filename

        audio = pyaudio.PyAudio() # create pyaudio instantiation
        fileExists = False # boolean if saved audio file exists

        # create pyaudio stream
        stream = audio.open(format = form_1,rate = samp_rate,channels = chans, \
                            input_device_index = dev_index,input = True, \
                            frames_per_buffer=chunk)
        print("started recording")
        frames = []

        # loop through stream and append audio chunks to frame array
        for ii in range(0,int((samp_rate/chunk)*record_secs)):
            data = stream.read(chunk)
            frames.append(data)

        print("finished recording")

        # stop the stream, close it, and terminate the pyaudio instantiation
        stream.stop_stream()
        stream.close()
        audio.terminate()

        # save the audio frames as .wav file
        wavefile = wave.open(wav_output_filename,'wb')
        wavefile.setnchannels(chans)
        wavefile.setsampwidth(audio.get_sample_size(form_1))
        wavefile.setframerate(samp_rate)
        wavefile.writeframes(b''.join(frames))
        wavefile.close()
        
        if Path(wav_output_filename).is_file():
            # file exists
            exists = True
        
        self.assertEqual(True, exists)
        
    def test_send_to_firebase(self): # send file to firebase storage
        # Firebase Config
        api_key = "AIzaSyBWMHPeUjEqT_P6g_jrxlKC431pr2xkTaU"
        project_id = "sysc3010-project"
        database_url = "https://sysc3010-project-default-rtdb.firebaseio.com/"

        config = {
        "apiKey": api_key,
        "authDomain": "{}.firebaseapp.com".format(project_id),
        "databaseURL": database_url,
        "storageBucket": "{}.appspot.com".format(project_id)
        }

        # Firebase Storage Setup
        firebase = pyrebase.initialize_app(config)
        sr = firebase.storage()

        name = str(Path().resolve().parent) + "/recordings/test0.wav"
        sr.child("recordings").child("audio").child("test0.wav").put(name)
        print(name, "sent to Firebase Storage")
        
        dbEntryURL = sr.child("recordings").child("audio").child("test0.wav").get_url(None)
        audFilePathURL = "https://firebasestorage.googleapis.com/v0/b/sysc3010-project.appspot.com/o/recordings%2Faudio%2Ftest0.wav?alt=media"
        #print(storage.child().get_url(None))
        #print(dbEntryURL)
        self.assertEqual(dbEntryURL, audFilePathURL)          

if __name__ == "__main__":
    unittest.main()