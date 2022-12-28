################################
#pip install requests
#pip install tkinter
#https://realpython.com/python-gui-tkinter/
################################

import requests
import tkinter as tk

# Vytvoření dialogového okna
root = tk.Tk()
root.title("Zobrazení průběhu reindexace")

# Přihlášení pomocí basic auth
auth = requests.auth.HTTPBasicAuth('jmeno', 'heslo')

url = "https://moje.adresa.nodu"

# Odeslání POST požadavku
response = requests.post('https://myurl.com/rest/api/2/reindex', auth=auth, data={'type': 'FOREGROUND'})


# Získání taskId ze získaného JSONu
taskId = response.json()['taskId']

# Odeslání GET požadavku pro získání informací o průběhu
response = requests.get(f'https://myurl.com/rest/api/2/reindex/progress?taskId={taskId}', auth=auth)

# Získání informací o průběhu a success ze získaného JSONu
currentProgress = response.json()['currentProgress']
success = response.json()['success']

# Vytvoření labelů pro zobrazení informací
label1 = tk.Label(root, text=f"Průběh: {currentProgress}%")
label2 = tk.Label(root, text=f"Úspěch: {success}")

# Zobrazení labelů
label1.pack()
label2.pack()

# Spuštění dialogového okna
root.mainloop()
