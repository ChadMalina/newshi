class car:
    def __init__(self,brand,model,year):
        self.brand=brand
        self.model=model
        self.year=year
    def display_info(self):
        print(f"ThIS Car's brand is {self.brand} and the Model is {self.model} and finally it was made in {self.year}")
    def __str__(self):
        return f"{self.brand}, {self.model}, {self.year}"

Display_info=car("BMW","M3 GTR","2007")
print(Display_info)