import PyInstaller.__main__
import os

# Get the absolute path to the assets directory
assets_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'assets')
icon_path = os.path.join(assets_dir, 'icon.png')

PyInstaller.__main__.run([
    'src/main.py',
    '--name=spotify_control',
    '--onefile',
    '--noconsole',
    f'--add-data={icon_path};assets',
    f'--icon={icon_path}',
    '--clean'
])
