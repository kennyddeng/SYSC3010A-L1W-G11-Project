import os
import time
import pyaudio
import wave
from pathlib import Path


def record():
    form_1 = pyaudio.paInt16  # 16-bit resolution
    chans = 1  # 1 channel audio
    samp_rate = 44100  # 44.1kHz sampling rate
    chunk = 4096  # 2^12 samples for buffer
    record_secs = 11  # seconds to record
    # 1 second is "wasted", video/audio will only render 10 seconds
    # ex. if you want a 10 second rendered audio/video clip,
    # you will need to record for 10+1 seconds (11 seconds)
    dev_index = 1  # device index found by p.get_device_info_by_index(ii)
    wav_output_filename = str(Path().resolve().parent) + '/SYSC3010A-L1W-G11-Project/recordings/audio.wav'  # record and save to filename

    # remove existing audio file if exists
    if os.path.exists(wav_output_filename):
        os.remove(wav_output_filename)

    audio = pyaudio.PyAudio()  # create pyaudio instantiation

    # create pyaudio stream
    stream = audio.open(format=form_1, rate=samp_rate,
                        channels=chans, input_device_index=dev_index,
                        input=True, frames_per_buffer=chunk)
    print("started audio recording")
    frames = []
    # loop through stream and append audio chunks to frame array
    for ii in range(0, int((samp_rate/chunk)*record_secs)):
        data = stream.read(chunk)
        frames.append(data)

    print("finished audio recording")

    # stop the stream, close it, and terminate the pyaudio instantiation
    stream.stop_stream()
    stream.close()
    audio.terminate()

    # save the audio frames as .wav file
    wavefile = wave.open(wav_output_filename, "wb")
    wavefile.setnchannels(chans)
    wavefile.setsampwidth(audio.get_sample_size(form_1))
    wavefile.setframerate(samp_rate)
    wavefile.writeframes(b''.join(frames))
    wavefile.close()

    # add 5 second delay for reliability when
    # saving file (ensure file is saved before file is used)
    time.sleep(5)
