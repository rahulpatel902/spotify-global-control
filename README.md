# Spotify Global Control

A lightweight system tray application that provides global keyboard shortcuts to control Spotify playback on Windows.

![Spotify Control Icon](assets/icon.png)

## Features 

- Global keyboard shortcuts that work from any application
- Minimalist system tray interface with Spotify-themed icon
- Zero configuration required - works out of the box

### Keyboard Shortcuts 

- `Ctrl + Shift + P`: Play/Pause
- `Ctrl + Shift + Right Arrow`: Next Track
- `Ctrl + Shift + Left Arrow`: Previous Track

### System Tray Menu

Right-click the Spotify icon in your system tray to access:
- Play/Pause
- Next Track
- Previous Track
- Exit

## Installation

### Prerequisites

- Windows OS
- Python 3.8 or higher
- Spotify Desktop App installed

### Quick Install

1. Download the latest release from the [Releases](https://github.com/rahulpatel902/spotify-global-control/releases) page
2. Extract the ZIP file
3. Run `spotify_control.exe`

### Install from Source

1. Clone the repository:
```bash
git clone https://github.com/rahulpatel902/spotify-global-control.git
cd spotify-global-control
```

2. Create a virtual environment (recommended):
```bash
python -m venv .venv
.venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the application:
```bash
python src/main.py
```

## Building from Source

To build the executable yourself:

1. Install pyinstaller:
```bash
pip install pyinstaller
```

2. Build the executable:
```bash
pyinstaller --noconsole --onefile --add-data "assets/icon.png;assets" --icon=assets/icon.png src/main.py --name spotify_control
```

The executable will be created in the `dist` directory.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Icon created using PIL (Python Imaging Library)
- Built with Python's pynput library for global keyboard shortcuts
- Uses pystray for system tray functionality
