import socket
from tkinter import *

def send(entry, listBox):
    message = entry.get()
    listBox.insert("end", "Client: " + message)
    entry.delete(0, END)
    s.send(bytes(message, "utf-8"))
    recieve(listBox)

def recieve(listBox):
    message = s.recv(50)
    listBox.insert("end", "Server: " + message.decode("utf-8"))

root = Tk()
root.title("Client")

entry = Entry()
entry.pack(side = BOTTOM)

listBox = Listbox(root)
listBox.pack()

button = Button(root, text = "SEND", command = lambda: send(entry, listBox))
button.pack(side = BOTTOM)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

hostName = socket.gethostname()
port = 12345  

s.connect((hostName, port))

root.mainloop()
