from faker import Faker
fake = Faker()

# podstawowa wizytówka
class Bussines_Card_Holder:
    def __init__(self, name, surname, company, occupation, email):
        self.name= name
        self.surname = surname
        self.company = company
        self.occupation = occupation
        self.email = email
        self._label_lenght = ""
    
    def __str__(self):
        return f"{self.name} {self.surname} {self.email}"

    #długość imienia i nazwiska
    @property
    def label_lenght(self):
        self._label_lenght = len(self.name + " " + self.surname)
        return f"Lista znaków: {self._label_lenght}"  
##################################################################################
# prywatna wizytówka
class Base_Contact(Bussines_Card_Holder):
    def __init__(self, name, surname, private_number, email):
        self.name = name
        self.surname = surname
        self.private_number = private_number
        self.email = email

    # wybieranie numeru prywatnego
    def contact(self):
        return f"Wybieram numer {self.private_number} i dzwonię do {self.name} {self.surname}"

    # ilość znaków
    @property
    def create_contacts(self):
        card = f"Prywatna wizytówka : {self.label_lenght}"
        return card
#####################################################################################
# służbowa wizytówka
class Business_Contact(Base_Contact):
    def __init__(self,occupation, company, work_number, *args, **kwargs):
        super().__init__(*args,**kwargs)
        self.occupation = occupation
        self.company = company
        self.work_number = work_number

    # wybieranie numeru służbowego
    def contact(self):
        return f"Wybieram numer {self.work_number} i dzwonię do {self.name} {self.surname}"

    # ilość znaków
    @property
    def create_contacts(self):
        card = f"Służbowa wizytówka : {self.label_lenght}"
        return card
#####################################################################################


#tworzenie losowych wizytówek prywatnych

contact_card = Base_Contact(name = fake.first_name(), surname = fake.last_name(), private_number = fake.country_calling_code() + " " + fake.phone_number(),email = fake.company_email())
print(contact_card.contact())
print(contact_card.create_contacts)

#tworzenie losowych wizytówek służbowych

contact_card = Business_Contact(name = fake.first_name(), surname = fake.last_name(), private_number = fake.country_calling_code() + " " + fake.phone_number(),email = fake.company_email(), occupation = fake.job(),company = fake.company(),work_number = fake.country_calling_code() + " " + fake.phone_number())
print(contact_card.contact())
print(contact_card.create_contacts)
