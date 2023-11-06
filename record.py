import pyaudio
import wave
import RPi.GPIO as GPIO # import GPIO library to use gpio pins

form_1 = pyaudio.paInt16 # 16-bit resolution
chans = 1 #1 channel
samp_rate = 16000# 16kHz sampling rate
chunk = 4096 # 2^12 samples for buffer
dev_index = 2 # device index found by p.get_device_info_by_index(ii)
wav_output_filename = 'test1.wav' # name of .wav file

audio = pyaudio.PyAudio() # create pyaudio instantiation

# create pyaudio stream
stream = audio.open(format = form_1,rate = samp_rate,channels = chans, \
                    input_device_index = dev_index,input = True, \
                    frames_per_buffer=chunk)

# set up gpio pin 17 as input with pull-down resistor
GPIO.setmode(GPIO.BCM) # use BCM numbering scheme
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # set pin 17 as input with pull-down

print("press the button to start recording")
frames = []

# loop until the button is pressed twice
while True:
    # wait for the button to be pressed
    GPIO.wait_for_edge(17, GPIO.RISING)
    print("recording")
    # record audio until the button is pressed again
    while not GPIO.input(17):
        data = stream.read(chunk)
        frames.append(data)
    print("finished recording")
    # break the loop if the button is pressed twice
    if len(frames) > 0:
        break

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
