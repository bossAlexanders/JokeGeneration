# Joke Generator (Tkinter + Official Joke API)

## Overview
Joke Generator is a simple desktop GUI application built with Python and Tkinter.  
The application fetches random jokes from the public Official Joke API and displays them in a clean, user-friendly interface.  
The project focuses on code quality, error handling, and clear English documentation.

## Features
- Fetches random jokes from an online API
- Displays both the joke setup and punchline
- Simple and intuitive Tkinter-based GUI
- Robust error handling for network and HTTP issues
- Clean, readable, and maintainable code

## API Used
Official Joke API  
Endpoint: https://official-joke-api.appspot.com/random_joke  

Returned fields:
- setup
- punchline

## Application Workflow
1. Launch the application
2. Click the **Get Joke** button
3. The app sends a request to the Joke API
4. The joke setup and punchline are displayed
5. If an error occurs, a clear error message is shown

## Project Structure
joke_generator.py  
README.md  

## Requirements
- Python 3.8+
- requests library

Install dependencies:
pip install requests

tkinter is included with most standard Python installations.

## How to Run
python joke_generator.py

## GUI Components
- Label — displays the joke text (setup and punchline)
- Get Joke Button — fetches and displays a new joke

## Core Functions
get_joke()  
Sends an HTTP request to the Official Joke API, parses the JSON response, displays the joke setup and punchline, and handles HTTP, network, and unexpected errors.

create_gui()  
Creates and configures the main Tkinter window, initializes GUI widgets, and sets layout behavior.

## Code Quality and Style

### PEP8 Compliance
- Consistent indentation (4 spaces)
- Proper spacing around operators and after commas
- Line length optimized (maximum 79 characters)
- Descriptive variable names

### Typing
- Type hints for function parameters and return values
- Uses Dict[str, Any] for API response typing

### Documentation
- All docstrings written in clear English
- Module-level documentation included
- Detailed function descriptions

### Error Handling
- Handles HTTP errors gracefully
- Catches network-related exceptions
- Handles unexpected runtime errors
- Displays user-friendly error messages in the GUI

## Possible Improvements
- Add loading indicator while fetching jokes
- Support joke categories
- Add copy-to-clipboard functionality
- Improve UI styling
- Refactor to a class-based architecture

## License
This project is provided for educational and demonstration purposes.
