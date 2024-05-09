from faker import Faker

fake = Faker()

'''You can generate various types of fake data using the methods provided 
by the fake object. Here are some examples:'''

print('name - ', fake.name())

print('address - ', fake.address())

print('phone number - ', fake.phone_number())

print('email - ', fake.email())

print('company - ', fake.company())

print('job - ', fake.job())

print('country - ', fake.country())

print('credit card number - ', fake.credit_card_number)

print('sentence - ', fake.sentence())