import pystray
from PIL import Image
import os

class SystemTray:
    def __init__(self, controller):
        self.controller = controller
        self.icon = None
        self.setup_icon()

    def setup_icon(self):
        # Get the path to the icon file
        icon_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'assets', 'icon.png')
        
        # Load the icon
        image = Image.open(icon_path)
        
        # Create the system tray icon
        self.icon = pystray.Icon(
            "Spotify Control",
            image,
            menu=pystray.Menu(
                pystray.MenuItem("Play/Pause", self.controller.spotify.toggle_playback),
                pystray.MenuItem("Next Track", self.controller.spotify.next_track),
                pystray.MenuItem("Previous Track", self.controller.spotify.previous_track),
                pystray.Menu.SEPARATOR,
                pystray.MenuItem("Exit", self.stop_application)
            )
        )

    def run(self):
        self.icon.run()

    def stop_application(self):
        self.cleanup()

    def cleanup(self):
        if self.icon:
            self.icon.stop()