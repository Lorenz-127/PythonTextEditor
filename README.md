# Python Text Editor

A feature-rich text editor built with Python and Tkinter, inspired by Notepad++.

## Features

- [ ] Basic text editing capabilities
- [ ] File operations (New, Open, Save, Save As)
- [ ] Edit functions (Cut, Copy, Paste, Undo, Redo, Select All, Clear)
- [ ] Text formatting (Bold, Italics)
- [ ] Color customization (Text color, Background color)
- [ ] Night mode
- [ ] Print functionality
- [ ] Toolbar for quick access to common functions

## Planned Enhancements

- [ ] Cross-platform printing support
- [ ] Find and replace functionality
- [ ] Syntax highlighting for various programming languages
- [ ] Line numbering
- [ ] Multiple document interface (tabbed editing)

## Menu Options

- **File**: New, Open, Save, Save As, Print File, Exit
- **Edit**: Cut, Copy, Paste, Undo, Redo, Select All, Clear
- **Colors**: Change color of selected text, all text, or background
- **Options**: Toggle Night Mode on/off

## Toolbar

The toolbar provides quick access to:
- Bold
- Italics
- Undo
- Redo
- Text Color

## Keyboard Shortcuts

- Cut: Ctrl+X
- Copy: Ctrl+C
- Paste: Ctrl+V
- Select All: Ctrl+A
- Undo: Ctrl+Z
- Redo: Ctrl+Y

## Notes

- The print functionality is currently set up for Windows systems.
- The icon path is set to 'c:/gui/codemy.ico'. You may need to adjust this path or provide your own icon.

## Requirements

- Python 3.x
- Tkinter (usually comes pre-installed with Python)
- win32print and win32api (for Windows printing functionality)

## Installation

1. Ensure you have Python 3.x installed on your system.
2. Install required libraries:
   ```
   pip install pywin32
   ```
3. Clone this repository or download the source code.

## Usage

Run the script using Python:

```
python text_edit.py

This project serves as both a practical tool for everyday use and a learning experience in Python GUI development and text processing.