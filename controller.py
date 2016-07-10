import sys
import Tkinter as tk
import model
import view

class Controller(object):
  def __init__(self):
    # model must be instantiated before view 'cuz of tk.mainloop()
    self.model = model.Model()
    self.view = view.View(self)
    self.view.notify(0)

  def getMoney(self):
    return self.model.getMoney()

  def addMoney(self):
    self.model.addMoney(10)
    self.view.notify(self.model.getMoney())

  def removeMoney(self):
    self.model.removeMoney(10)
    self.view.notify(self.model.getMoney())

if __name__ == "__main__":
  controller = Controller()
  tk.mainloop()

