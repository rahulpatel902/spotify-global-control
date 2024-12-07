from pynput import keyboard
from spotify_controller import SpotifyController
from system_tray import SystemTray
import logging
import sys
import os

class ShortcutController:
    def __init__(self):
        self.setup_logging()
        self.spotify = SpotifyController()
        self.system_tray = SystemTray(self)
        self.keyboard_listener = None
        self.setup_keyboard_listener()

    def setup_logging(self):
        # Create logs directory if it doesn't exist
        log_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'logs')
        os.makedirs(log_dir, exist_ok=True)
        
        # Set up logging to file and console
        log_file = os.path.join(log_dir, 'spotify_control.log')
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler(log_file),
                logging.StreamHandler(sys.stdout)
            ]
        )
        self.logger = logging.getLogger('ShortcutController')

    def setup_keyboard_listener(self):
        try:
            self.keyboard_listener = keyboard.GlobalHotKeys({
                '<ctrl>+<alt>+<shift>+p': self.spotify.toggle_playback,
                '<ctrl>+<alt>+<shift>+<right>': self.spotify.next_track,
                '<ctrl>+<alt>+<shift>+<left>': self.spotify.previous_track
            })
            self.keyboard_listener.start()
            self.logger.info("Keyboard shortcuts initialized successfully")
        except Exception as e:
            self.logger.error(f"Error setting up keyboard listener: {e}")
            sys.exit(1)

    def cleanup(self):
        try:
            if self.keyboard_listener:
                self.keyboard_listener.stop()
            self.system_tray.cleanup()
            self.logger.info("Application cleanup completed")
        except Exception as e:
            self.logger.error(f"Error during cleanup: {e}")

def main():
    try:
        app = ShortcutController()
        app.logger.info("Starting Spotify Global Control")
        app.system_tray.run()
    except Exception as e:
        logging.error(f"Error starting application: {e}")
        sys.exit(1)
    finally:
        if 'app' in locals():
            app.cleanup()

if __name__ == "__main__":
    main()