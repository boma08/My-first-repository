class Logic:

    def write_data(self, website_entry, username_entry, password_entry):
        with open("data.txt", "a") as file:
            file.write(website_entry.input)