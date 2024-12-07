from pynput import keyboard
from spotify_controller import SpotifyController
from system_tray import SystemTray
import psutil
import subprocess
import time
import threading
import os
import winreg as reg
import sys

class ShortcutController:
    def __init__(self):
        # First check if Spotify is running
        if not self.is_spotify_running():
            print("Spotify is not running. Exiting...")
            sys.exit(0)
            
        self.spotify = SpotifyController()
        self.system_tray = SystemTray(self)
        self.keyboard_listener = None
        self.exe_process = None
        self.running = True
        self.setup_keyboard_listener()
        self.setup_autostart()
        self.start_spotify_monitor()

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

    def setup_autostart(self):
        try:
            key = reg.OpenKey(reg.HKEY_CURRENT_USER, "Software\\Microsoft\\Windows\\CurrentVersion\\Run", 0, reg.KEY_ALL_ACCESS)
            reg.SetValueEx(key, "SpotifyGlobalControl", 0, reg.REG_SZ, sys.executable)
            reg.CloseKey(key)
        except Exception as e:
            print(f"Error setting up autostart: {e}")

    def is_spotify_running(self):
        try:
            for proc in psutil.process_iter(['name']):
                if proc.info['name'] == "Spotify.exe":
                    try:
                        # Check if process is responding
                        proc.status()
                        return True
                    except psutil.NoSuchProcess:
                        continue
        except:
            pass
        return False

    def terminate_exe(self):
        try:
            if self.exe_process:
                self.exe_process.terminate()
                time.sleep(1)
                if self.exe_process.poll() is None:
                    self.exe_process.kill()
                self.exe_process = None
        except Exception as e:
            print(f"Error terminating exe: {e}")

    def start_spotify_monitor(self):
        def monitor():
            exe_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "spotify-global-control.exe")
            last_state = True  # Since we checked at startup
            
            while self.running:
                try:
                    current_state = self.is_spotify_running()
                    if current_state and not last_state:
                        # Spotify just started
                        try:
                            self.exe_process = subprocess.Popen([exe_path])
                            print("Started exe process")
                        except Exception as e:
                            print(f"Error starting exe: {e}")
                    elif not current_state and last_state:
                        # Spotify just closed
                        self.terminate_exe()
                        print("Terminated exe process")
                        # Exit the application when Spotify closes
                        self.cleanup()
                        os._exit(0)
                    
                    last_state = current_state
                    time.sleep(2)
                except Exception as e:
                    print(f"Error in monitor loop: {e}")
                    time.sleep(2)

        monitor_thread = threading.Thread(target=monitor, daemon=True)
        monitor_thread.start()

    def cleanup(self):
        print("Cleaning up...")
        self.running = False
        if self.keyboard_listener:
            self.keyboard_listener.stop()
        self.terminate_exe()
        if self.system_tray and self.system_tray.icon:
            self.system_tray.icon.stop()
        print("Cleanup complete")

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