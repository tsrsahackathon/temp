import pyaudio
import wave
import RPi.GPIO as GPIO

form_1 = pyaudio.paInt16  # 16-bit resolution
chans = 1  # 1 channel
samp_rate = 16000  # 44.1kHz sampling rate
chunk = 4096  # 2^12 samples for buffer
dev_index = 2  # device index found by p.get_device_info_by_index(ii)
wav_output_filename = 'test1.wav'  # name of .wav file

audio = pyaudio.PyAudio()

# create pyaudio stream
stream = audio.open(format=form_1, rate=samp_rate, channels=chans,
                    input_device_index=dev_index, input=True,
                    frames_per_buffer=chunk)

GPIO.setmode(GPIO.BOARD)
GPIO.setup(3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

print("Waiting for button press...")

while GPIO.input(3) == GPIO.LOW:
    pass
while GPIO.input(3) == GPIO.HIGH:
    pass

print("Button pressed, recording...")

frames = []

while GPIO.input(3) == GPIO.LOW:
    data = stream.read(chunk)
    frames.append(data)

print("Button released, stopped recording.")
print("Finished recording.")

# Stop the stream, close it, and terminate the pyaudio instantiation
stream.stop_stream()
stream.close()
audio.terminate()

# Save the audio frames as a .wav file
wavefile = wave.open(wav_output_filename, 'wb')
wavefile.setnchannels(chans)
wavefile.setsampwidth(audio.get_sample_size(form_1))
wavefile.setframerate(samp_rate)
wavefile.writeframes(b''.join(frames))
wavefile.close()
