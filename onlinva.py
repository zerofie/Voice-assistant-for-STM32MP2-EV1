import sounddevice as sd
from scipy.io.wavfile import write
import speech_recognition as sr
import pyttsx3
import subprocess
import wavio
import soundfile as sf
from commands import commands
import os
import threading
import time
from rapidfuzz import fuzz

recognizer = sr.Recognizer()
running_threads = {}
wake_word = "hello mp2"
stop_listening_command = "stop listening"
listening = False

def SpeakText(command):
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()

def check_supported_sample_rates():
    """Prints the supported sample rates for the default audio device."""
    default_device = sd.query_devices(kind='input')  # Query default input device
    if default_device:
        supported_rates = default_device['default_samplerate']
        print("Supported sample rates:", supported_rates)
    else:
        print("No default audio input device found.")

def detect_command(user_input):
    words = user_input.lower().split()
    print(f"{time.ctime()}: Words: {words}")
    if "reboot" in words or "restart" in words:
        print(f"{time.ctime()}: Reboot command detected. Rebooting system...")
        subprocess.run(["sudo", "reboot"], check=False)
        return None, None
    for command_file, details in commands.items():
        if any(word in details["aliases"] or word == details["command"] for word in words):
            for word in words:
                
                if word in details["intents"]:
                    intent = details["intents"][word]
                    full_command_details = details["full_commands"][intent]
                    final_command = full_command_details["command"]
                    action = full_command_details["action"]
                    return final_command, action
    return None, None

def stop_action(command_name, action):
    print(f"{time.ctime()}: Stopping all instances of {command_name}")
    if command_name in running_threads:
        for process in running_threads[command_name]:
            process.terminate()
            process.wait()  # Wait for the process to terminate
        del running_threads[command_name]
        print(f"{time.ctime()}: Stopped all instances of {command_name}")
    else:
        print(f"{time.ctime()}: No running instances of {command_name} found, attempting to force kill")
        if command_name in ["pose", "estimation"]:
            #subprocess.run(["pkill -f", action])
            os.system("pkill -f stai_mpu_pose_estimation.py")
        else:
            subprocess.run(["killall", action])

def execute_action(action, command_name):
    def run_command():
        process = subprocess.Popen(action, shell=True)
        if command_name not in running_threads:
            running_threads[command_name] = []
        running_threads[command_name].append(process)
        print(f"{time.ctime()}: Started {command_name} with PID {process.pid}")
        process.wait()  # Wait for the process to complete
        running_threads[command_name].remove(process)
        if not running_threads[command_name]:
            del running_threads[command_name]
        print(f"{time.ctime()}: Completed {command_name}")

    thread = threading.Thread(target=run_command)
    thread.start()

def listen_for_commands():
    global listening
    print(f"{time.ctime()}: Listening for commands...")
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        while listening:
            print(f"{time.ctime()}: Waiting for next command...")
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
            try:
                start_time = time.time()
                text = recognizer.recognize_google(audio).lower()
                end_time = time.time()
                print(f"{time.ctime()}: Recognized command: {text} (processing time: {end_time - start_time:.2f} seconds)")
                if stop_listening_command in text:
                    print(f"{time.ctime()}: Stop listening command detected. Exiting command loop.")
                    listening = False
                    break
                final_command, action = detect_command(text)
                if final_command and action:
                    print(f"{time.ctime()}: Final command: {final_command}")
                    print(f"{time.ctime()}: Executing action: {action}")
                    if "kill" in final_command:
                        stop_action(final_command.split()[1], action)
                    else:
                        execute_action(action, final_command)
                else:
                    print(f"{time.ctime()}: Command not recognized")
            except sr.UnknownValueError:
                print(f"{time.ctime()}: Could not understand audio")
            except sr.RequestError as e:
                print(f"{time.ctime()}: Could not request results; {e}")
            except Exception as e:
                print(f"{time.ctime()}: An error occurred: {e}")

def listen_for_wake_word():
    global listening
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        while True:
            print(f"{time.ctime()}: Listening for wake word...")
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
            try:
                start_time = time.time()
                text = recognizer.recognize_google(audio).lower()
                end_time = time.time()
                print(f"{time.ctime()}: Recognized text: {text} (processing time: {end_time - start_time:.2f} seconds)")
                similarity = fuzz.ratio(wake_word, text)
                print(f"{time.ctime()}: Similarity with wake word: {similarity}")
                if similarity > 80:  # Adjust this threshold as needed
                    print(f"{time.ctime()}: Wake word detected!")
                    listening = True
                    listen_for_commands()
            except sr.UnknownValueError:
                print(f"{time.ctime()}: Could not understand audio")
            except sr.RequestError as e:
                print(f"{time.ctime()}: Could not request results; {e}")
            except Exception as e:
                print(f"{time.ctime()}: An error occurred: {e}")

def main():
    check_supported_sample_rates()
    wake_word_thread = threading.Thread(target=listen_for_wake_word)
    wake_word_thread.daemon = True
    wake_word_thread.start()
    wake_word_thread.join()

if __name__ == "__main__":
    main()
