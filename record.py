import pyaudio
import wave
import RPi.GPIO as GPIO

form_1 = pyaudio.paInt16  # 16-bit resolution
chans = 1  # 1 channel
samp_rate = 16000  # 44.1kHz sampling rate
chunk = 4096  # 2^12 samples for buffer
dev_index = 2  # device index found by p.get_device_info_by_index(ii)
wav_output_filename = 'test1.wav'  # name of .wav file

audio = pyaudio.PyAudio()  # create pyaudio instantiation

# create pyaudio stream
stream = audio.open(format=form_1, rate=samp_rate, channels=chans,
                    input_device_index=dev_index, input=True,
                    frames_per_buffer=chunk)

button_pin = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

print("Press the button to start recording...")

# Wait for the button press to start recording
while GPIO.input(button_pin) == GPIO.HIGH:
    pass

print("Recording...")

frames = []

recording = True

# Record until the button is pressed again
while recording:
    data = stream.read(chunk)
    frames.append(data)
    if GPIO.input(button_pin) == GPIO.LOW:
        recording = False

print("Finished recording")

# stop the stream, close it, and terminate the pyaudio instantiation
stream.stop_stream()
stream.close()
audio.terminate()

# save the audio frames as .wav file
wavefile = wave.open(wav_output_filename, 'wb')
wavefile.setnchannels(chans)
wavefile.setsampwidth(audio.get_sample_size(form_1))
wavefile.setframerate(samp_rate)
wavefile.writeframes(b''.join(frames))
wavefile.close()

GPIO.cleanup()
