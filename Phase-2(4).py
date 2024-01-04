import pyaudio
import wave
import tkinter as tk
from tkinter import messagebox

class AudioRecorder:
    def __init__(self, root):
        self.root = root
        self.root.title("Voice Recorder")

        self.audio = pyaudio.PyAudio()
        self.is_recording = False

        self.record_button = tk.Button(self.root, text="Record", command=self.toggle_recording)
        self.record_button.pack(pady=20)

    def toggle_recording(self):
        if not self.is_recording:
            self.start_recording()
            self.record_button.config(text="Stop")
        else:
            self.stop_recording()
            self.record_button.config(text="Record")

    def start_recording(self):
        self.is_recording = True
        self.stream = self.audio.open(format=pyaudio.paInt16,
                                channels=1,
                                rate=44100,
                                frames_per_buffer=1024,
                                input=True)
        self.frames = []

    def stop_recording(self):
        self.is_recording = False
        self.stream.stop_stream()
        self.stream.close()
        self.audio.terminate()
        self.save_recording()

    def save_recording(self):
        try:
            wf = wave.open("output.wav", "wb")
            wf.setnchannels(1)
            wf.setsampwidth(self.audio.get_sample_size(pyaudio.paInt16))
            wf.setframerate(44100)
            wf.writeframes(b''.join(self.frames))
            wf.close()
            messagebox.showinfo("Recording Saved", "Recording saved as 'output.wav'")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

    def callback(self, in_data, frame_count, time_info, status):
        self.frames.append(in_data)
        return in_data, pyaudio.paContinue

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = AudioRecorder(root)
    app.run()
