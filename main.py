import tkinter as tk
import requests
def get_joke():
    try:
        reponse=requests.get("https://official-joke-api.appspot.com/random_joke")
        if reponse.status_code == 200:
            joke_data = reponse.json()
            setup = joke_data.get('setup', 'error setup')
            punchline = joke_data.get('punchline', 'error punchline')
            joke_label.config(text=f'{setup}\n{punchline}', fg = 'black')
        else:
             joke_label.config(text=f'ошибка {reponse.status_code}', fg='red')
    except Exception as e:
        joke_label.config(text=f'ошибка {e}', fg='red')
    
    
root = tk.Tk()
# root.geometry('400x300')
root.title("Генератор шуток")
joke_label = tk.Label(root, text="нажми ради шутки",
                      wraplength=400,
                      font=('Arial', 12)
)
get_joke_button = tk.Button(root, text="Получить шутку", command=get_joke, font=("Arial", 12))
joke_label.grid(row=0, column=0,padx=12, pady=10)
get_joke_button.grid(row=1, column=0, padx=10, pady=10)
root.mainloop()