import sys
import Tkinter as tk

class Model(object):
  def __init__(self):
    self.money = 0
  def addMoney(self, m):
    self.money += m
  def removeMoney(self, m):
    self.money -= m
  def getMoney(self):
    return self.money

