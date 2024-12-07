from pynput.keyboard import Key, Controller
import time

class SpotifyController:
    def __init__(self):
        self.keyboard = Controller()

    def toggle_playback(self):
        self.keyboard.press(Key.media_play_pause)
        time.sleep(0.05)
        self.keyboard.release(Key.media_play_pause)

    def next_track(self):
        self.keyboard.press(Key.media_next)
        time.sleep(0.05)
        self.keyboard.release(Key.media_next)

    def previous_track(self):
        self.keyboard.press(Key.media_previous)
        time.sleep(0.05)
        self.keyboard.release(Key.media_previous)