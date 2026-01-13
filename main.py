import tkinter as tk
import requests
from typing import Dict, Any


def get_joke() -> None:
    """
    Fetches a random joke from the joke API and displays it.
    
    Retrieves a joke from the official-joke-api and updates the label
    with the setup and punchline. Handles errors appropriately.
    """
    try:
        response = requests.get("https://official-joke-api.appspot.com/random_joke")
        
        if response.status_code == 200:
            joke_data: Dict[str, Any] = response.json()
            setup = joke_data.get('setup', 'Error: Missing setup')
            punchline = joke_data.get('punchline', 'Error: Missing punchline')
            joke_label.config(text=f'{setup}\n\n{punchline}', fg='black')
        else:
            joke_label.config(text=f'Error: {response.status_code}', fg='red')
    
    except requests.exceptions.RequestException as e:
        joke_label.config(text=f'Network error: {e}', fg='red')
    except Exception as e:
        joke_label.config(text=f'Unexpected error: {e}', fg='red')


def create_gui() -> None:
    """
    Creates and configures the main GUI window for the joke generator.
    
    Sets up the window, label, and button for displaying jokes.
    """
    global root, joke_label
    
    root = tk.Tk()
    root.title("Joke Generator")
    root.resizable(False, False)
    
    # Joke display label
    joke_label = tk.Label(
        root, 
        text="Click for a joke!",
        wraplength=400,
        font=('Arial', 12),
        justify='center',
        height=6,
        width=40
    )
    
    # Button to fetch new joke
    get_joke_button = tk.Button(
        root, 
        text="Get Joke", 
        command=get_joke, 
        font=("Arial", 12),
        bg='#4CAF50',
        fg='white',
        padx=20,
        pady=10
    )
    
    # Layout using grid
    joke_label.grid(row=0, column=0, padx=20, pady=20, sticky='nsew')
    get_joke_button.grid(row=1, column=0, padx=20, pady=(0, 20))
    
    # Configure grid weights
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)


if __name__ == "__main__":
    """
    Joke Generator Application
    
    A simple desktop app that fetches and displays random jokes from an API.
    Features a clean interface with error handling for network issues.
    """
    create_gui()
    root.mainloop()
