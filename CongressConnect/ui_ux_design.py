```python
from tkinter import Tk, Label, Button, Entry, IntVar, END, W, E

class CongressConnectUI:
    def __init__(self, master):
        self.master = master
        master.title("CongressConnect")

        self.login_label = Label(master, text="Login")
        self.login_label.grid(row=0, column=0, sticky=W)

        self.login_entry = Entry(master)
        self.login_entry.grid(row=0, column=1, sticky=W)

        self.login_button = Button(master, text="Login", command=self.login_user)
        self.login_button.grid(row=0, column=2, sticky=W)

        self.legislation_label = Label(master, text="Legislation")
        self.legislation_label.grid(row=1, column=0, sticky=W)

        self.legislation_button = Button(master, text="Update", command=self.update_legislation)
        self.legislation_button.grid(row=1, column=2, sticky=W)

        self.constituent_label = Label(master, text="Constituent")
        self.constituent_label.grid(row=2, column=0, sticky=W)

        self.constituent_button = Button(master, text="Update", command=self.update_constituent)
        self.constituent_button.grid(row=2, column=2, sticky=W)

        self.campaign_label = Label(master, text="Campaign")
        self.campaign_label.grid(row=3, column=0, sticky=W)

        self.campaign_button = Button(master, text="Update", command=self.update_campaign)
        self.campaign_button.grid(row=3, column=2, sticky=W)

        self.event_label = Label(master, text="Event")
        self.event_label.grid(row=4, column=0, sticky=W)

        self.event_button = Button(master, text="Update", command=self.update_event)
        self.event_button.grid(row=4, column=2, sticky=W)

    def login_user(self):
        # Placeholder for login function
        pass

    def update_legislation(self):
        # Placeholder for update legislation function
        pass

    def update_constituent(self):
        # Placeholder for update constituent function
        pass

    def update_campaign(self):
        # Placeholder for update campaign function
        pass

    def update_event(self):
        # Placeholder for update event function
        pass

root = Tk()
my_gui = CongressConnectUI(root)
root.mainloop()
```