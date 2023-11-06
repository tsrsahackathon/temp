**Inscribd**

This repository contains the code for a project that uses a Raspberry Pi and a microphone to record speech and transcribe it into text with punctuation. The project was created by the team inscribd

**Requirements**

To run this project, you will need:

- A Raspberry Pi 4 or 5 with Raspbian OS/ NodeMCU
- A USB microphone connected to the Raspberry Pi
- Python 3.7 or higher
- The following Python packages installed:
  - sounddevice
  - transformers
  - numpy
  - scipy
  - requests
- The Google Speech-to-Text API key

**Installation**

To install the required packages, you can use the following command:

pip3 install -r requirements.txt

You will also need to download the pre-trained transformer model for punctuation prediction. You can use the following command:

wget https://huggingface.co/roberta-large/resolve/main/pytorch\_model.bin

You will also need to set up the Google Speech-to-Text API key as an environment variable. You can follow the instructions [here](https://cloud.google.com/speech-to-text/docs/transcribe-streaming-audio) to get the API key and [here](https://support.google.com/websearch/answer/6030020?hl=en&co=GENIE.Platform%3DDesktop) to set it as an environment variable.

**Usage**

To run the project, you can use the following command:

python3 Main.py

This will start the recording and transcription process. You can speak into the microphone and see the transcribed text on the terminal. The text will also be saved in a file called PUNC\_transcript.txt.

To stop the recording and transcription, you can press the button on the raspberry pi.

**How it works**

The project uses the following steps to transcribe speech into text with punctuation:

- Record the audio from the microphone using the sounddevice package.
- Split the audio into chunks of 3 seconds using the scipy package.
- Send the audio chunks to the Google Speech-to-Text API using the requests package.
- Get the output text from the API without punctuation.
- Tokenize the text using the transformers package.
- Feed the tokens into a pre-trained transformer model for punctuation prediction using the transformers package.
- Get the output tokens with punctuation.
- Convert the tokens back into text using the transformers package.
- Print and save the text with punctuation.

**Database:**

A MongoDB database stores transcriptions, quizzes, summaries, and keywords as Json.

**Tech stack of the frontend repository**

The frontend uses a streamlitApp as a website. The json files are processed locally to display (interactable quiz).
