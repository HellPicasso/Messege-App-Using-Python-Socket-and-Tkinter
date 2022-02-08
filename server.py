import socket
from tkinter import *

def send(entry, listBox):
    message = entry.get()
    listBox.insert("end","Server: " + message)
    entry.delete(0, END)
    client.send(bytes(message,"utf-8"))
    # recieve(listBox)

def recieve(listBox):
    clientMessage = client.recv(50)
    listBox.insert("end", "Client: " + clientMessage.decode("utf-8"))

root = Tk()
root.title("Server")

entry = Entry()
entry.pack(side = BOTTOM)

listBox = Listbox(root)
listBox.pack()

button = Button(root, text = "SEND", command = lambda: send(entry, listBox))
button.pack(side = BOTTOM)

rbutton = Button(root, text = "RECIEVE", command = lambda: recieve(listBox))
rbutton.pack(side = BOTTOM)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

hostName = socket.gethostname()
port = 12345  

s.bind((hostName, port))

s.listen(4)
client, address = s.accept()

root.mainloop()