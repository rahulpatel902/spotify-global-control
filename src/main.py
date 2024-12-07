from pynput import keyboard
from spotify_controller import SpotifyController
from system_tray import SystemTray

class ShortcutController:
    def __init__(self):
        self.spotify = SpotifyController()
        self.system_tray = SystemTray(self)
        self.keyboard_listener = None
        self.setup_keyboard_listener()

    def setup_keyboard_listener(self):
        try:
            self.keyboard_listener = keyboard.GlobalHotKeys({
                '<ctrl>+<shift>+p': self.spotify.toggle_playback,
                '<ctrl>+<shift>+<right>': self.spotify.next_track,
                '<ctrl>+<shift>+<left>': self.spotify.previous_track
            })
            self.keyboard_listener.start()
        except Exception as e:
            print(f"Error setting up keyboard listener: {e}")

    def cleanup(self):
        if self.keyboard_listener:
            self.keyboard_listener.stop()
        self.system_tray.cleanup()

def main():
    try:
        app = ShortcutController()
        app.system_tray.run()
    except Exception as e:
        print(f"Error starting application: {e}")
    finally:
        if 'app' in locals():
            app.cleanup()

if __name__ == "__main__":
    main()