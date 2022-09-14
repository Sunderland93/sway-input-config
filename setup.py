from importlib.metadata import entry_points
from setuptools import setup, find_packages

setup(
    name='sway-input-config',
    version='1.0.0',
    description='input devices configurator for sway',
    license='GPL-3',
    author='Aleksey Samoilov',
    author_email='samoilov.lex@gmail.com',
    url='https://github.com/Sunderland93/sway-input-config',
    packages=find_packages(),
    include_package_data=True,
    package_data={"": ["data/*"]},
    install_requires=[],
    entry_points={
        'gui_scripts': [
            'sway-input-config = sway_input_config.main:main'
        ]
    }
)
