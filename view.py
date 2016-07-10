import sys
import Tkinter as tk
import controller

class NotAController(object):
  def getMoney(self): print "Get money"
  def addMoney(self): print "Adding money"

class View(object):
  def __init__(self, controller):
    self.controller = controller
    root = tk.Tk()
    root.title('MVC')
    self.moneyVar = tk.IntVar()
    button = tk.Button(root, text="Add Money", width=20) 
    button.configure(command=self.controller.addMoney)
    button.pack(side=tk.TOP)
    button = tk.Button(root, text="Remove Money", width=20) 
    button.configure(command=self.controller.removeMoney)
    button.pack(side=tk.TOP)
    button = tk.Button(root, text="Quit", width=10) 
    button.configure(command=sys.exit)
    button.pack(side=tk.TOP)

    view = tk.Toplevel()
    label = tk.Label(view, text="Money Available").pack(side=tk.LEFT)
    self.entry = tk.Entry(view, textvariable=self.moneyVar)
    self.entry.pack(side=tk.LEFT)
    self.moneyVar.set(self.controller.getMoney)

  def notify(self, m):
    self.moneyVar.set(m)

if __name__ == "__main__":
  view = View(NotAController())
