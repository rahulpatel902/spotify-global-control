# Spotify Global Control

A lightweight desktop application that provides global keyboard shortcuts and system tray controls for Spotify playback.

## Features

- Global keyboard shortcuts for Spotify control
- System tray icon with playback controls
- Minimal resource usage
- Automatic Spotify process detection
- Comprehensive error handling and logging

## Keyboard Shortcuts

| Action | Shortcut |
|--------|----------|
| Play/Pause | Ctrl + Alt + Shift + P |
| Next Track | Ctrl + Alt + Shift + Right |
| Previous Track | Ctrl + Alt + Shift + Left |

## System Requirements

- Windows OS
- Spotify Desktop App
- Python 3.12 or higher

## Installation

1. Download the latest release from the releases page
2. Extract the zip file
3. Run the executable

Or install from source:

```bash
git clone https://github.com/yourusername/spotify-global-control
cd spotify-global-control
pip install -r requirements.txt
python src/main.py
```

## Dependencies

- pynput
- pystray
- Pillow
- pywin32
- psutil

## Building from Source

To build the executable:

```bash
python build.py
```

The executable will be created in the `dist` directory.

## Usage

1. Run the application
2. A Spotify icon will appear in your system tray
3. Use the keyboard shortcuts or right-click the tray icon for controls
4. The application will automatically detect when Spotify is running

## Contributing

Feel free to open issues or submit pull requests for any improvements.

## License

MIT License - see LICENSE file for details

## Version History

See [CHANGELOG.md](CHANGELOG.md) for version history and latest changes.
