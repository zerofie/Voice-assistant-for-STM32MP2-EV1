# Voice-assistant-for-STM32MP2-EV1
An application in python to run the built in applications in ST x-linux-ai distribution package and basic commands or existing applications handsfree via voice command.
Audio drivers needed to be enabled for stm32mp2157f board. This application can be build for practially any MPU.
Muiltitreading and subprocesses implemented for running applications parallelly and running same applications multiple times parallelly.
Daemon used to continuously listen , wake-up command and stop listening command implemented.
Till stop command is triggered , continuously input is taken for any commands or their aliases present in the dictionary commands.py
Initially I have used google speech_to_text , the audio is stored in wav files, each string recorded is cross checked and matched with the supported commands, their intent( start or stop ), or their aliases.
Each time a new command is detected a process opens parallelly to the already running applications . Kill command followed by application name kills all the threads with the existing command name.


