from importlib.metadata import entry_points
from setuptools import setup, find_packages
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='sway-input-config',
    version='1.4.3',
    description='input devices configurator for sway',
    license='GPL-3',
    author='Aleksey Samoilov',
    author_email='samoilov.lex@gmail.com',
    url='https://github.com/Sunderland93/sway-input-config',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=find_packages(),
    include_package_data=True,
    package_data={"": ["data/*", "ui/*", "langs/*"]},
    data_files=[
        ('share/applications', ['sway-input-config.desktop']),
        ('share/icons/hicolor/128x128/apps', ['sway-input-config.png']),
        ('share/metainfo', ['io.github.Sunderland93.sway-input-config.metainfo.xml']),
    ],
    install_requires=['PyQt6',
    'i3ipc',
    ],
    entry_points={
        'gui_scripts': [
            'sway-input-config = sway_input_config.main:main'
        ]
    }
)
