from pyfaker import Fake

fake = Fake(lang_code='en')
name=fake.Name.name()
address=fake.Address.street_address()
company=fake.Company.bs()
fake_gb = Fake('en-gb')
phone=fake_gb.PhoneNumber.formats()

print("Name:",name,"\nAddress:",address,"\nCompany:",company,"\nPhone Number:",phone)
