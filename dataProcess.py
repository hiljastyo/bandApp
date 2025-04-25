class DataProcessor:
    def __init__(self, db_connector, textbox):
        self.db_connector = db_connector
        self.textbox = textbox

    def print_data(self, query):
        data = self.db_connector.fetch_data(query)
        if data:
            self.textbox.delete("0.0", "end")
            for row in data:
                self.textbox.insert("end", f"{row}\n")
        else:
            self.textbox.insert("end", "NO DATA.\n")


    def insert_new_band(self, nimi, genre, jasenet, manager):
        query = "INSERT INTO bandit (nimi, genre, jasenet, managerin_yhteystiedot) VALUES (?, ?, ?, ?)"
        success = self.db_connector.insert_data(query, (nimi, genre, jasenet, manager))
        if success:
            self.textbox.insert("end", f"Band '{nimi}' added to database.\n")


    def insert_new_gig(self, date, showtime, endtime, description):
        query = "INSERT INTO keikat (pvm, aloitusaika, lopetusaika, kuvaus_keikasta) VALUES(?, ?, ?, ?)"
        success = self.db_connector.insert_data(query, (date, showtime, endtime, description))
        if success:
            self.textbox.insert("end", "New gig added!")

    def insert_new_stage(self, name, address, capacity, contact):
        query = "INSERT INTO keikkapaikat (nimi, osoite, kapasiteetti, yhteyshenkilo) VALUES(?, ?, ?, ?)"
        success = self.db_connector.insert_data(query, (name, address, capacity, contact))
        if success:
            self.textbox.insert("end", "New stage added!")

    def insert_new_stage(self, soundcheck, openDoor, showTime, endTime):
        query = "INSERT INTO keikkapaikat (soundcheck, ovet_auki, esityksen_aloitus, esityksen_lopetus) VALUES(?, ?, ?, ?)"
        success = self.db_connector.insert_data(query, (soundcheck, openDoor, showTime, endTime))
        if success:
            self.textbox.insert("end", "New schedule added!")

    def insert_new_expense(self, rent, travel, equipment, other):
        query = "INSERT INTO keikkapaikat (soundcheck, ovet_auki, esityksen_aloitus, esityksen_lopetus) VALUES(?, ?, ?, ?)"
        success = self.db_connector.insert_data(query, (rent, travel, equipment, other))
        if success:
            self.textbox.insert("end", "New schedule added!")