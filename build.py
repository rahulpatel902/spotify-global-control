import PyInstaller.__main__
import os
import sys

def create_executable():
    # Get the absolute path to the assets directory
    base_path = os.path.dirname(os.path.abspath(__file__))
    assets_dir = os.path.join(base_path, 'assets')
    icon_path = os.path.join(assets_dir, 'icon.png')
    
    # Ensure the assets directory exists
    if not os.path.exists(assets_dir):
        print(f"Error: Assets directory not found at {assets_dir}")
        sys.exit(1)
    
    # Ensure the icon file exists
    if not os.path.exists(icon_path):
        print(f"Error: Icon file not found at {icon_path}")
        sys.exit(1)

    # PyInstaller command line arguments
    args = [
        'src/main.py',
        '--name=spotify_control',
        '--onefile',
        '--noconsole',
        '--clean',
        f'--add-data={icon_path};assets',
        f'--icon={icon_path}',
        '--hidden-import=pynput.keyboard._win32',
        '--hidden-import=pynput.mouse._win32',
        '--hidden-import=PIL._tkinter_finder',
        '--hidden-import=pkg_resources.py2_warn',
        '--hidden-import=pkg_resources.markers',
        '--log-level=DEBUG'
    ]

    print("Building executable...")
    print(f"Using icon from: {icon_path}")
    PyInstaller.__main__.run(args)
    print("Build complete! Check the 'dist' directory for spotify_control.exe")

if __name__ == '__main__':
    create_executable()
