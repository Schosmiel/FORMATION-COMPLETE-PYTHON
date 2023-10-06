from faker import Faker

fake=Faker(locale="fr_FR")

#print(fake.text())
#print(fake.name())

for _ in range(500):
    #print(fake.unique.random_int())
    #print(fake.unique.first_name())
    #print(fake.unique.job())
    #print(fake.rgb_color())
    #print(fake.hex_color())
    #print(fake.numerify(text="%%%-#-%%%%-%%%%-%%%-##"))
    print(fake.bothify(text="Product Number : ????-########"))
    #print("N° :", fake.credit_card_number(), "Exp :", fake.credit_card_expire(), 
    #      "CVV : ", fake.credit_card_security_code())