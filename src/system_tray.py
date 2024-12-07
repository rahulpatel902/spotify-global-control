import pystray
from PIL import Image
import os
import sys
import webbrowser
import logging

def get_resource_path(relative_path):
    """Get the absolute path to a resource, works for dev and for PyInstaller"""
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    
    return os.path.join(base_path, relative_path)

class SystemTray:
    def __init__(self, app_controller):
        self.app_controller = app_controller
        self.icon = None
        self.setup_logging()
        self.setup_icon()

    def setup_logging(self):
        self.logger = logging.getLogger('SystemTray')

    def setup_icon(self):
        try:
            icon_path = get_resource_path('assets/icon.png')
            image = Image.open(icon_path)
            
            self.icon = pystray.Icon(
                "spotify_control",
                image,
                "Spotify Global Control\nRight-click for menu",
                menu=self.create_menu()
            )
        except Exception as e:
            self.logger.error(f"Error setting up system tray icon: {e}")
            self.logger.error(f"Attempted icon path: {icon_path}")
            sys.exit(1)

    def create_menu(self):
        """Create the system tray menu items"""
        return pystray.Menu(
            pystray.MenuItem(
                "Playback Controls",
                pystray.Menu(
                    pystray.MenuItem(
                        "Play/Pause",
                        lambda: self.app_controller.spotify.toggle_playback(),
                        default=True
                    ),
                    pystray.MenuItem(
                        "Next Track",
                        lambda: self.app_controller.spotify.next_track()
                    ),
                    pystray.MenuItem(
                        "Previous Track",
                        lambda: self.app_controller.spotify.previous_track()
                    )
                )
            ),
            pystray.MenuItem(
                "Keyboard Shortcuts",
                pystray.Menu(
                    pystray.MenuItem("Play/Pause (Ctrl+Alt+Shift+P)", lambda: None, enabled=False),
                    pystray.MenuItem("Next Track (Ctrl+Alt+Shift+Right)", lambda: None, enabled=False),
                    pystray.MenuItem("Previous Track (Ctrl+Alt+Shift+Left)", lambda: None, enabled=False)
                )
            ),
            pystray.Menu.SEPARATOR,
            pystray.MenuItem(
                "About",
                lambda: webbrowser.open('https://github.com/YOUR_USERNAME/spotify-global-control')
            ),
            pystray.MenuItem(
                "Exit",
                self.stop
            )
        )

    def run(self):
        if self.icon:
            self.icon.run()

    def stop(self, icon=None, item=None):
        if self.icon:
            self.icon.stop()

    def cleanup(self):
        self.stop()