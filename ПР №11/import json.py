import json
import tkinter as tk
def F():
    S = name.get()
    f= """
    {
    'company': None
    'created_at': '2010-11-18T20:33:18Z'
    'email': None
    'id': 487568
    'name': 'Nix/Nixpkgs/NixOS'
    'url': 'https://api.github.com/users/NixOS'
    }"""

    if S == 'NixOS':
        with open('C:\\Users\\user\\Desktop\\vivod.json', 'w') as file:
            json.dump(f,file)      
    else:
        print('Нету')

window = tk.Tk()
window.geometry('600x500')
window.title("interface") 
name = tk.Entry(window)
name.grid(padx=160, pady=20)
btn = tk.Button(window, text="      Нажми :)      ", command=F)
btn.grid(padx=120, pady=20)
window.mainloop()
F()