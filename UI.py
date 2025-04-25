from tkinter.filedialog import dialogstates

import customtkinter

import dataProcess
from dataBase import Database
from dataProcess import DataProcessor


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.db = Database("127.0.0.1", "root", "admin", "band_stuff")
        self.db.connect()
        self.title("Band Application")
        self.geometry("1280x720")
        self.grid_columnconfigure((0, 5), weight=1)


        self.textbox = customtkinter.CTkTextbox(master=self, width=400, corner_radius=0)

        self.button_add_band = customtkinter.CTkButton(self, text="Add new Band", command=self.add_new_band, width=120,
                                              height=120)
        self.button_print_bands = customtkinter.CTkButton(self, text="Print Bands", command=self.print_bands, width=120,
                                              height=120)
        self.button_add_gig = customtkinter.CTkButton(self, text="Add gig", command=self.add_new_band, width=120,
                                              height=120)
        self.button_add_stage = customtkinter.CTkButton(self, text="Add stage", command=self.add_new_stage, width=120,
                                              height=120)
        self.button_add_schedule = customtkinter.CTkButton(self, text="Add schedule", command=self.add_new_schedule, width=120,
                                              height=120)
        self.button_add_expenses = customtkinter.CTkButton(self, text="Add Expenses", command=self.add_new_expenses, width=120,
                                              height=120)


        self.button_add_band.grid(row=0, column=0, padx=20, pady=20, sticky="ew")
        self.button_print_bands.grid(row=1, column=0, padx=20, pady=20, sticky="ew")
        self.button_add_gig.grid(row=2, column=0, padx=20, pady=20, sticky="ew")
        self.button_add_stage.grid(row=2, column=0, padx=20, pady=20, sticky="ew")
        self.button_add_schedule.grid(row=3, column=0, padx=20, pady=20, sticky="ew")
        self.button_add_expenses.grid(row=4, column=0, padx=20, pady=20, sticky="ew")
        self.textbox.grid(row=2, column=3, sticky="nsew")

    def add_new_expenses(self):
        rent = self._setRentOfVenue()
        travel = self._setTravelExpense()
        equipment = self._setEquipmentExpense()
        other = self._setOtherExpense()
        data_processor = DataProcessor(self.db, self.textbox)
        data_processor.insert_new_expense(rent, travel, equipment, other)

    def add_new_schedule(self):
        soundcheck = self._setSoundcheck()
        openDoor = self._setOpenDoor()
        showTime = self._setShowtime()
        endTime = self._setEnd()
        data_processor = DataProcessor(self.db, self.textbox)
        data_processor.insert_new_schedule(soundcheck, openDoor, showTime, endTime)

    def _setSoundcheck(self):
        dialog = customtkinter.CTkInputDialog(text="Soundcheck (hh:mm:ss) )", title="Soundcheck")
        text = dialog.get_input()
        self.textbox.insert("0.0", f"Soundcheck is: {text}\n ")  # insert at line 0 character 0
        return text

    def _setOpenDoor(self):
        dialog = customtkinter.CTkInputDialog(text="Open doors (hh:mm:ss) )", title="Open doors")
        text = dialog.get_input()
        self.textbox.insert("0.0", f"Doors open: {text}\n ")  # insert at line 0 character 0
        return text

    def add_new_stage(self):
        stageName = self._setStageName()
        address = self._setAddress()
        capacity = self._setCapacity()
        contact = self._setContact()
        data_processor = DataProcessor(self.db, self.textbox)
        data_processor.insert_new_stage(stageName, address, capacity, contact)

    def _setStageName(self):
        dialog = customtkinter.CTkInputDialog(text="Stages name: )", title="Stages name")
        text = dialog.get_input()
        self.textbox.insert("0.0", f"Stages name is: {text}\n ")  # insert at line 0 character 0
        return text

    def _setAddress(self):
        dialog = customtkinter.CTkInputDialog(text="Address of stage: ", title="Address of stage")
        text = dialog.get_input()
        self.textbox.insert("0.0", f"Address of the stage is: {text}\n ")  # insert at line 0 character 0
        return text

    def _setCapacity(self):
        dialog = customtkinter.CTkInputDialog(text="Venue capacity: )", title="Venue capacity")
        text = dialog.get_input()
        self.textbox.insert("0.0", f"Venue capacity: {text}\n ")  # insert at line 0 character 0
        return text

    def _setContact(self):
        dialog = customtkinter.CTkInputDialog(text="Venue Contact: )", title="Venue Contact")
        text = dialog.get_input()
        self.textbox.insert("0.0", f"Venue Contact: {text}\n ")  # insert at line 0 character 0
        return text

    def add_new_gig(self):
        date = self._setDate()
        showTime = self._setShowtime()
        endtime = self._setEnd()
        description = self._setDescription()
        data_processor = DataProcessor(self.db, self.textbox)
        data_processor.insert_new_gig(date, showTime, endtime, description)

    def _setDate(self):
        dialog = customtkinter.CTkInputDialog(text="Date (YYYY-MM-DD)", title="Date")
        text = dialog.get_input()
        self.textbox.insert("0.0", f"New date is: {text}\n ")  # insert at line 0 character 0
        return text

    def _setShowtime(self):
        dialog = customtkinter.CTkInputDialog(text="Show Time (hh:mm:ss)", title="Show Time")
        text = dialog.get_input()
        self.textbox.insert("0.0", f"Showtime is: {text}\n ")  # insert at line 0 character 0
        return text

    def _setEnd(self):
        dialog = customtkinter.CTkInputDialog(text="End time (hh:mm:ss)", title="End Time")
        text = dialog.get_input()
        self.textbox.insert("0.0", f"Show ends: {text}\n ")  # insert at line 0 character 0
        return text

    def _setDescription(self):
        dialog = customtkinter.CTkInputDialog(text="Describe gig", title="Describe gig")
        text = dialog.get_input()
        self.textbox.insert("0.0", f"Gig went like this: {text}\n ")  # insert at line 0 character 0
        return text

    def add_new_band(self):
        name = self._setName()
        genre = self._setGenre()
        jasenet = self._setJasenet()
        manager = self._setManagerinYhteystiedot()
        data_processor = DataProcessor(self.db, self.textbox)
        data_processor.insert_new_band(name, genre, jasenet, manager)

    def _setName(self):
        dialog = customtkinter.CTkInputDialog(text="Bands name", title="Bands name")
        text = dialog.get_input()
        self.textbox.insert("0.0", f"Bands name is: {text}\n ")  # insert at line 0 character 0
        return text

    def _setGenre(self):
        dialog = customtkinter.CTkInputDialog(text="Genre:", title="Genre")
        text = dialog.get_input()
        self.textbox.insert("0.0", f"Bands genre is: {text} \n")
        return text

    def _setJasenet(self):
        dialog = customtkinter.CTkInputDialog(text="Jasenten LKM: ", title="Jasenten LKM")
        text = dialog.get_input()
        self.textbox.insert("0.0", f"Band consist {text} members\n")
        return text

    def _setManagerinYhteystiedot(self):
        dialog = customtkinter.CTkInputDialog(text="Managerin yhteystiedot: ", title="Managerin yhteystiedot")
        text = dialog.get_input()
        self.textbox.insert("0.0", f"Band Contact: {text}\n")
        return text



    def print_bands(self):
        data_processor = DataProcessor(self.db, self.textbox)
        self.textbox.delete("0.0", "end")
        data_processor.print_data("SELECT * FROM bandit")
