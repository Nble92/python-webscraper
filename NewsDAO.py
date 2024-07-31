class NewsDAO:
    def __init__(self):
        self.title = ""
        self.status = ""

    def set_data(self, title, status):  # Added space after comma
        self.title = title
        self.status = status

    def get_title(self):
        return self.title
    
    def get_status(self):
        return self.status

# Ensure there's a newline here at the end of the file