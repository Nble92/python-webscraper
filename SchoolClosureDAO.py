class SchoolClosureDAO:
    def __init__(self):
        self.url = ""
        self.title = ""
        self.status = ""

    def set_data(self, url, title, status):  # Corrected space after comma
        self.url = url
        self.title = title
        self.status = status

    def get_url(self):
        return self.url

    def get_title(self):
        return self.title
    
    def get_status(self):
        return self.status

# Ensure there's a newline here at the end of the file
