import tkinter as tk
import base64

list = []

app = tk.Tk()
app.title("formelctables")
app.geometry("400x300")

def submit():
    q1 = q1_entry.get()
    a1 = a1_entry.get()
    q2 = q2_entry.get()
    a2 = a2_entry.get()
    q3 = q3_entry.get()
    a3 = a3_entry.get()
  
    q1b64 = base64.b64encode(q1.encode('utf-8')).decode('utf-8')
    a1b64 = base64.b64encode(a1.encode('utf-8')).decode('utf-8')
    q2b64 = base64.b64encode(q2.encode('utf-8')).decode('utf-8')
    a2b64 = base64.b64encode(a2.encode('utf-8')).decode('utf-8')
    q3b64 = base64.b64encode(q3.encode('utf-8')).decode('utf-8')
    a3b64 = base64.b64encode(a3.encode('utf-8')).decode('utf-8')

    with open('blank.txt', 'w') as f:
        f.write(f'{q1b64}\n')
        f.write(f'{a1b64}\n')
        f.write(f'{q2b64}\n')
        f.write(f'{a2b64}\n')
        f.write(f'{q3b64}\n')
        f.write(f'{a3b64}\n')

q1_label = tk.Label(app, text="Question 1", bg='white')
q1_label.grid(row=0, column=0, padx=10, pady=5, sticky=tk.E)
q1_entry = tk.Entry(app, width=30)
q1_entry.grid(row=0, column=1, padx=20, pady=5)

a1_label = tk.Label(app, text="Answer 1", bg='white')
a1_label.grid(row=1, column=0, padx=10, pady=5, sticky=tk.E)
a1_entry = tk.Entry(app, width=30)
a1_entry.grid(row=1, column=1, padx=20, pady=5)

q2_label = tk.Label(app, text="Question 2", bg='white')
q2_label.grid(row=2, column=0, padx=10, pady=5, sticky=tk.E)
q2_entry = tk.Entry(app, width=30)
q2_entry.grid(row=2, column=1, padx=20, pady=5)

a2_label = tk.Label(app, text="Answer 2", bg='white')
a2_label.grid(row=3, column=0, padx=10, pady=5, sticky=tk.E)
a2_entry = tk.Entry(app, width=30)
a2_entry.grid(row=3, column=1, padx=20, pady=5)

q3_label = tk.Label(app, text="Question 3", bg='white')
q3_label.grid(row=4, column=0, padx=10, pady=5, sticky=tk.E)
q3_entry = tk.Entry(app, width=30)
q3_entry.grid(row=4, column=1, padx=20, pady=5)

a3_label = tk.Label(app, text="Answer 3", bg='white')
a3_label.grid(row=5, column=0, padx=10, pady=5, sticky=tk.E)
a3_entry = tk.Entry(app, width=30)
a3_entry.grid(row=5, column=1, padx=20, pady=5)

key_label = tk.Label(app, text="key?", bg='white')
key_label.grid(row=6, column=0, padx=10, pady=5, sticky=tk.E)
key_entry = tk.Entry(app, width=30)
key_entry.grid(row=6, column=1, padx=20, pady=5)

submit_button = tk.Button(app, text="Submit", width=10, height=2, command=submit)
submit_button.grid(row=7, column=1, columnspan=2, pady=15)

submit_button = tk.Button(app, text="aden oztas 2024.", width=10, height=2,)
submit_button.grid(row=8, column=1, columnspan=2, pady=15)



app.mainloop()
