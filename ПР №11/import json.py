import requests
import json
def F():
    S = name.get()
    response = requests.get('https://api.github.com/users/NixOS')

    f = json.loads(response.text)

    y = dict.fromkeys(['company'], f['company'])
    y2 = dict.fromkeys(['created_at'], f['created_at'])
    y3 = dict.fromkeys(['email'], f['email'])
    y4 = dict.fromkeys(['id'], f['id'])
    y5 = dict.fromkeys(['name'], f['name'])
    y6 = dict.fromkeys(['url'], f['url'])
    j = (y,y2,y3,y4,y5,y6)
    if S == 'NixOS':
        with open('C:\\Users\user\\Desktop\\vivod.json', 'w') as file:
            json.dump(j,file)      
    else:
        print('Нету')
import tkinter as tk
window = tk.Tk()
window.geometry('600x500')
window.title("interface") 
name = tk.Entry(window)
name.grid(padx=250, pady=50)
btn = tk.Button(window, text="      Нажми :)      ", command=F)
btn.grid(padx=250, pady=50)
window.mainloop()
F()
