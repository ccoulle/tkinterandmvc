#!/usr/bin/python

import os, sys
import Tkinter as tk

TITLE = "Learning Tkinter: Label"
GEOMETRY = '640x480+10+10'
ANIMALS = ['cat', 'dog', 'horse', 'mule', 'rabbit']

class Labels(object):
  def __init__(self):
    self.root = tk.Tk()
    self.root.geometry(GEOMETRY)
    self.root.title(TITLE)
    self.root.bind('<Escape>', (lambda event: self.quit())) 
    self.textFont = ('symbol', 14, 'bold')
    self.labelFont = ('symbol', 18, 'bold')
    self.init()
    self.root.mainloop()

  def printSelection(self, event):
    #index = event.widget.curselection()
    #item = event.widget.get(index)
    index = self.box.curselection()
    item = self.box.get(index)
    print "You selected:", item

  def init(self):
    frame = tk.Frame(self.root)
    frame.pack(side=tk.TOP)

    label = tk.Label(frame, text = "Hello World")
    label.config(bg='black', fg='yellow')
    label.config(font=self.labelFont, height=3, width=20)
    label.pack(side=tk.LEFT)
    button = tk.Button(frame, text="Quit", command=self.quit)
    button.config(height=3, width=20, font=self.labelFont, bg='yellow')
    button.pack(side=tk.RIGHT)
    self.box = tk.Listbox(self.root, width=40, height=60)
    self.box.config(font=self.textFont)
    self.box.pack(side=tk.BOTTOM)
    self.box.bind('<Double-1>', self.printSelection)
    for x in range(1, 5):
      self.box.insert(tk.END, str(x)+'. '+ANIMALS[x]) 

  def quit(self):
    sys.exit()


if __name__ == '__main__':
  template = Labels()
