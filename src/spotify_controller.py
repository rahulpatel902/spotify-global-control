from pynput.keyboard import Key, Controller
import time
import logging
from typing import Callable
import win32gui
import win32process
import psutil

class SpotifyController:
    def __init__(self):
        self.keyboard = Controller()
        self.setup_logging()
        self._last_action_time = 0
        self.min_action_interval = 0.1  # Minimum time between actions in seconds

    def setup_logging(self):
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s'
        )
        self.logger = logging.getLogger('SpotifyController')

    def _rate_limit(func: Callable) -> Callable:
        """Decorator to prevent rapid-fire key presses"""
        def wrapper(self, *args, **kwargs):
            current_time = time.time()
            if current_time - self._last_action_time < self.min_action_interval:
                return
            self._last_action_time = current_time
            return func(self, *args, **kwargs)
        return wrapper

    def is_spotify_running(self) -> bool:
        """Check if Spotify is running"""
        return "Spotify.exe" in (p.name() for p in psutil.process_iter(['name']))

    def is_spotify_active(self) -> bool:
        """Check if Spotify window is currently focused"""
        try:
            active_window = win32gui.GetForegroundWindow()
            _, pid = win32process.GetWindowThreadProcessId(active_window)
            process = psutil.Process(pid)
            return process.name() == "Spotify.exe"
        except Exception:
            return False

    @_rate_limit
    def toggle_playback(self):
        """Toggle play/pause"""
        try:
            if not self.is_spotify_running():
                self.logger.warning("Spotify is not running")
                return
            self.keyboard.press(Key.media_play_pause)
            time.sleep(0.05)
            self.keyboard.release(Key.media_play_pause)
            self.logger.info("Toggled playback")
        except Exception as e:
            self.logger.error(f"Error toggling playback: {e}")

    @_rate_limit
    def next_track(self):
        """Play next track"""
        try:
            if not self.is_spotify_running():
                self.logger.warning("Spotify is not running")
                return
            self.keyboard.press(Key.media_next)
            time.sleep(0.05)
            self.keyboard.release(Key.media_next)
            self.logger.info("Skipped to next track")
        except Exception as e:
            self.logger.error(f"Error skipping track: {e}")

    @_rate_limit
    def previous_track(self):
        """Play previous track"""
        try:
            if not self.is_spotify_running():
                self.logger.warning("Spotify is not running")
                return
            self.keyboard.press(Key.media_previous)
            time.sleep(0.05)
            self.keyboard.release(Key.media_previous)
            self.logger.info("Returned to previous track")
        except Exception as e:
            self.logger.error(f"Error returning to previous track: {e}")

    @_rate_limit
    def volume_up(self):
        """Increase volume"""
        try:
            if not self.is_spotify_running():
                self.logger.warning("Spotify is not running")
                return
            with self.keyboard.pressed(Key.ctrl):
                self.keyboard.press(Key.up)
                time.sleep(0.05)
                self.keyboard.release(Key.up)
            self.logger.info("Increased volume")
        except Exception as e:
            self.logger.error(f"Error increasing volume: {e}")

    @_rate_limit
    def volume_down(self):
        """Decrease volume"""
        try:
            if not self.is_spotify_running():
                self.logger.warning("Spotify is not running")
                return
            with self.keyboard.pressed(Key.ctrl):
                self.keyboard.press(Key.down)
                time.sleep(0.05)
                self.keyboard.release(Key.down)
            self.logger.info("Decreased volume")
        except Exception as e:
            self.logger.error(f"Error decreasing volume: {e}")