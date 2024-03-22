import tkinter as tk
from tkinter import messagebox
import base64

list = []

app = tk.Tk()
app.title("formelctables form reader")
app.geometry("400x300")


def grabandstrip():
    points = 0
    filename = file_entry.get()
    with open(filename, 'r') as file:
        lines = file.readlines()

    # Create variables to store each line
    line1 = lines[0].strip()  # Assuming line numbering starts from 1
    line2 = lines[1].strip()
    line3 = lines[2].strip()
    line4 = lines[3].strip()
    line5 = lines[4].strip()
    line6 = lines[5].strip()

    q1 = base64.b64decode(line1).decode('utf-8')
    a1 = base64.b64decode(line2).decode('utf-8')
    q2 = base64.b64decode(line3).decode('utf-8')
    a2 = base64.b64decode(line4).decode('utf-8')
    q3 = base64.b64decode(line5).decode('utf-8')
    a3 = base64.b64decode(line6).decode('utf-8')

    app.title("new")

    
    submit_button.pack_forget()


    q1_label = tk.Label(app, text=f'{q1}', bg='white')
    q1_label.grid(row=0, column=0, padx=10, pady=5, sticky=tk.E)
    q1_entry = tk.Entry(app, width=30)
    q1_entry.grid(row=0, column=1, padx=20, pady=5)


    q2_label = tk.Label(app, text=f'{q2}', bg='white')
    q2_label.grid(row=1, column=0, padx=10, pady=5, sticky=tk.E)
    q2_entry = tk.Entry(app, width=30)
    q2_entry.grid(row=1, column=1, padx=20, pady=5)

    q3_label = tk.Label(app, text=f'{q3}', bg='white')
    q3_label.grid(row=2, column=0, padx=10, pady=5, sticky=tk.E)
    q3_entry = tk.Entry(app, width=30)
    q3_entry.grid(row=2, column=1, padx=20, pady=5)

    q11 = q1_entry.get()
    q22 = q2_entry.get()
    q33 = q3_entry.get()

    
    newpoints = str(points)

    def submit():
        nonlocal points
        q11 = q1_entry.get()
        q22 = q2_entry.get()
        q33 = q3_entry.get()

        if q11 == a1:
            points += 1
        if q22 == a2:
            points += 1
        if q33 == a3:
            points += 1
    
        newpoints = str(points)
        messagebox.showinfo(f'{newpoints} points')
    
    sub_button = tk.Button(app, text=f"submit awnserd",width=15,height=2 ,command=submit)
    sub_button.grid(row=3, columnspan=2, pady=10)



file_label = tk.Label(app, text="file", bg='white')
file_label.grid(row=0, column=0, padx=10, pady=5, sticky=tk.E)
file_entry = tk.Entry(app, width=30)
file_entry.grid(row=0, column=1, padx=20, pady=5)


submit_button = tk.Button(app, text=f"play form:",width=15,height=2 ,command=grabandstrip)
submit_button.grid(row=1, columnspan=2, pady=10)


app.mainloop()
