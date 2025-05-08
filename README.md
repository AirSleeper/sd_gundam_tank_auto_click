# sd_gundam_tank_auto_click
Auto click to make tank in SD gundam G generation. Download the `.exe` under `dist` and run it！

## Description
The Auto Clicker is a Python-based program that automates mouse clicks at specified coordinates. It includes a graphical user interface (GUI) for easy configuration of click positions, delays, and other settings. The program also supports starting and stopping the auto-clicking process via the GUI or keyboard shortcuts.

## Features
- GUI for configuring click positions and delays.
- Buttons to record mouse click positions dynamically.
- Start and stop auto-clicking directly from the GUI.
- Keyboard shortcuts:
  - Press `s` to start auto-clicking.
  - Press `e` to stop auto-clicking.

## Requirements
- Python 3.7 or higher
- Required Python libraries:
  - `pyautogui`
  - `pynput`
  - `tkinter` (comes pre-installed with Python)

## Installation
1. Clone or download the repository to your local machine.
2. Install the required libraries using pip:
   ```bash
   pip install pyautogui pynput
   ```

## Usage
1. Run the program:
   ```bash
   python autoclick.py
   ```
2. The GUI will open by default.
3. Configure the click positions and delays in the GUI.
4. Use the "Start Auto-Clicking" button to begin the process.
5. Use the "Stop Auto-Clicking" button or press `e` to stop the process.

## Converting to an Executable
To convert the program into a standalone `.exe` file:
1. Install PyInstaller:
   ```bash
   pip install pyinstaller
   ```
2. Run the following command in the terminal:
   ```bash
   pyinstaller --onefile --windowed autoclick.py
   ```
3. The executable will be located in the `dist` folder.

## License
This project is licensed under the MIT License.
