from faker import Faker

fake = Faker('fa_IR')

print(fake.name())
print(fake.phone_number())