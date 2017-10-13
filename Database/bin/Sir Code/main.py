from tkinter import ttk
import tkinter as tk
import sys

from prisoner import Prisoner
from prisonerRepository import PrisonerRepository

class MainForm:
    
  def main(self):
    root = tk.Tk()
    root.title("XSCAPE PRISON MANAGER")

    # initialise a dictionary for indexing values in the listbox
    # TODO: surely there is a better way to deal with this!
    self.prisonerDictionary = {}

    # create a notebook object
    nb = ttk.Notebook(root)

    # ADD FIRST PAGE
    page1 = ttk.Frame(nb)
    
    # add a list box
    self.listbox = tk.Listbox(page1)
    self.listbox.pack(fill=tk.BOTH, expand=1)
    
    # add a button to delete items
    self.btnDelete = ttk.Button(page1, text="RELEASE!", command = self.delete)
    self.btnDelete.pack()
    
    # ADD SECOND PAGE
    page2 = ttk.Frame(nb)

    # prompt
    self.heading = ttk.Label(page2, text="PRISONER REGISTRATION:")

    # title
    self.lblTitle = ttk.Label(page2, text="Title:")
    self.entTitle = ttk.Entry(page2)

    # first name
    self.lblFirst = ttk.Label(page2, text="First name:")
    self.entFirst = ttk.Entry(page2)

    # middle name
    self.lblMiddle = ttk.Label(page2, text="Middle name:")
    self.entMiddle = ttk.Entry(page2)

    # last name
    self.lblLast = ttk.Label(page2, text="Last name:")
    self.entLast = ttk.Entry(page2)

    # sentence type
    self.lblSentence = ttk.Label(page2, text="Sentence Type (MIN/MAX):")
    self.entSentence = ttk.Entry(page2)

    # submit button
    self.btnAdd = ttk.Button(page2, text="IMPRISON!", command = self.add)
        
    # LAYOUT SECOND PAGE
    # NOTE: using grid layout here
    self.heading.grid(row=1, column=1)

    self.lblTitle.grid(column=1, row=2)
    self.entTitle.grid(column=2, row=2)
    
    self.lblFirst.grid(column=1, row=3)
    self.entFirst.grid(column=2, row=3)

    self.lblMiddle.grid(column=1, row=4)
    self.entMiddle.grid(column=2, row=4)

    self.lblLast.grid(column=1, row=5)
    self.entLast.grid(column=2, row=5)

    self.lblSentence.grid(column=1, row=6)
    self.entSentence.grid(column=2, row=6)

    self.btnAdd.grid(column=2, row=7)

    # ADD PAGES TO NOTEBOOK
    nb.add(page1, text='INMATE LIST')
    nb.add(page2, text='NEW PRISONER')

    # LAYOUT THE NOTEBOOK
    nb.pack(expand=1, fill="both")

    # size the window
    root.geometry("300x300")

    # read the list
    self.list()
    
    root.mainloop()

  def list(self):
        
    # remove all items from the listbox
    self.listbox.delete(0, tk.END)

    # read all items from the repository
    repo = PrisonerRepository("./_db/prisoner.db")
    prisoners = repo.readall()
    
    # add items to the listbox
    # and to the dictionary
    # NOTE: need to add the prisoner objects to the dictionary here
    # as otherwise we cannot delete them from the repository (how would we know the ID)
    # This is why the id is included in the display string (to make it unique)
    self.prisonerDictionary.clear()
    
    for p in prisoners:
      self.listbox.insert(tk.END, p)
      self.prisonerDictionary[str(p)] = p
    
  def add(self):
    # create a prisoner object
    # TODO: add validation
    p = Prisoner()
    p.title = self.entTitle.get()
    p.firstname = self.entFirst.get()
    p.middlename = self.entMiddle.get()
    p.lastname = self.entLast.get()
    p.sentenceType = self.entSentence.get()

    # send to prison!
    repo = PrisonerRepository("./_db/prisoner.db")
    p = repo.create(p)

    # reload list from db
    self.list()

  def delete(self):

    # get current selection
    selection = self.listbox.curselection()

    # do we have a selected item
    if selection:
      # get the selected item sting value
      selectedString = self.listbox.get(tk.ACTIVE)

      # get the prisoner object from the dictionary
      p = self.prisonerDictionary[selectedString]
            
      # release the prisoner!
      repo = PrisonerRepository("./_db/prisoner.db")
      passengers = repo.delete(p.id)

      # reload list from db
      self.list()
  
if __name__ == "__main__":
    form = MainForm()
    form.main()
