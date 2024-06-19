import threading
import numpy as np
import sounddevice as sd


def generate_audio():
    t = np.linspace(0, duration, int(duration * sample_rate), endpoint=False)
    data = 0.5 * np.sin(2 * np.pi * frequency * t)
    return data


def play_audio():
    print("playing audio...")
    sd.play(audio_data, sample_rate)
    sd.wait()


def schedule_task():
    play_audio()
    timer = threading.Timer(580, schedule_task)
    timer.start()


duration = 3.0
sample_rate = 44100
frequency = 19000
audio_data = generate_audio()

schedule_task()
