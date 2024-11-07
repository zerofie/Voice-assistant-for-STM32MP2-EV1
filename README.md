# Voice-assistant-for-MPU
An application in python to run the built in applications in ST x-linux-ai distribution package and basic commands or existing applications handsfree via voice command.
Audio drivers needed to be enabled for stm32mp2157f board. This application can be build for practially any MPU.
Muiltitreading and subprocesses implemented for running applications parallelly and running same applications multiple times parallelly.
Daemon used to continuously listen , wake-up command and stop listening command implemented.
Till stop command is triggered , continuously input is taken for any commands or their aliases present in the dictionary commands.py
Initially I have used google speech_to_text , the audio is stored in wav files, each string recorded is cross checked and matched with the supported commands, their intent( start or stop ), or their aliases.
Each time a new command is detected a process opens parallelly to the already running applications . Kill command followed by application name kills all the threads with the existing command name.


Here is a comprehensive list of all the dependencies required to run the provided code, including the necessary packages to be installed and the language/plugin support with their installation syntaxes.

Dependencies
Python Packages
sounddevice: For audio recording.
scipy: For handling scientific computations and reading/writing WAV files.
speech_recognition: For recognizing speech input.
pyttsx3: For text-to-speech conversion.
subprocess: For running system commands.
wavio: For reading/writing WAV files.
soundfile: For reading/writing sound files.
rapidfuzz: For fuzzy string matching.
vosk: For offline speech recognition.
pyaudio: For handling audio streams.
threading: For running tasks in parallel.
Additional Tools
Vosk Model: Pre-trained model for Vosk speech recognition.
sudo: For executing system commands with superuser privileges (if needed).
Installation Instructions
Python Packages
You can install all the required Python packages using pip. Here is the collective command to install all the packages:

sh
pip install sounddevice scipy speechrecognition pyttsx3 wavio soundfile rapidfuzz vosk pyaudio
Vosk Model
Download the Vosk model from the official Vosk website or GitHub repository and place it in the specified directory. For example:

sh
wget https://alphacephei.com/vosk/models/vosk-model-small-en-us-0.15.zip
unzip vosk-model-small-en-us-0.15.zip -d /mnt_mmc/vosk_model/
System Dependencies
Ensure that you have the following system dependencies installed:

PortAudio: Required for PyAudio. You can install it using your package manager.

On Ubuntu/Debian:
sh
sudo apt-get install portaudio19-dev
On macOS:
sh
brew install portaudio
sudo: Ensure you have sudo installed and configured if you need to run commands with superuser privileges.

Additional Configuration
Ensure that your Python environment is properly set up and activated.
Ensure that your audio input device (e.g., microphone) is properly configured and accessible.
Example Command to Install All Dependencies
Here is a combined command to install all the necessary dependencies on an Ubuntu/Debian system:

sh
sudo apt-get update

sudo apt-get install -y portaudio19-dev

pip install sounddevice scipy speechrecognition pyttsx3 wavio soundfile rapidfuzz vosk pyaudio

wget https://alphacephei.com/vosk/models/vosk-model-small-en-us-0.15.zip

unzip vosk-model-small-en-us-0.15.zip -d /mnt_mmc/vosk_model/
