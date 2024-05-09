from faker import Faker

fake = Faker()


'''Faker supports different locales, 
allowing you to generate data specific to a certain 
country or language. For example:'''


#GENERATING INDIAN DATA

fake_ind_en = Faker('en_IN')

dict_ind_en = {
    'name' : fake_ind_en.name(),
    'adhar id' : fake_ind_en.aadhaar_id(),
    'address' : fake_ind_en.address(),
    'city' : fake_ind_en.city(),
    'post code' : fake_ind_en.postcode(),
    'country code' : fake_ind_en.country_code()
}

print('---Indian english ---')

for key,value in dict_ind_en.items():
    print(key, ' - ', value)

print('')


# GENERATING DATA IN HINDI

fake_ind_hi = Faker('hi_IN')

dict_ind_hi = {
    'name' : fake_ind_hi.name(),
    'address' : fake_ind_hi.address(),
    'city' : fake_ind_hi.city(),
    'post code' : fake_ind_hi.postcode(),
    'country code' : fake_ind_hi.country_code()
}

print('')

print('---Indian hindi ---')

for key,value in dict_ind_hi.items():
    print(key, ' - ', value)

print('')




# GENERATING DATA for Great Britian

fake_ind_gb = Faker('en_GB')

dict_ind_gb = {
    'name' : fake_ind_gb.name(),
    'address' : fake_ind_gb.address(),
    'city' : fake_ind_gb.city(),
    'post code' : fake_ind_gb.postcode(),
    'country code' : fake_ind_gb.country_code()
}

print('')

print('---Britian english ---')

for key,value in dict_ind_gb.items():
    print(key, ' - ', value)

print('')




# GENERATING DATA French

fake_ind_fr = Faker('fr')

dict_ind_fr = {
    'name' : fake_ind_fr.name(),
    'address' : fake_ind_fr.address(),
    'city' : fake_ind_fr.city(),
    'post code' : fake_ind_fr.postcode(),
    'country code' : fake_ind_fr.country_code()
}

print('')

print('---French english ---')

for key,value in dict_ind_fr.items():
    print(key, ' - ', value)

print('')




# GENERATING DATA Chinese

fake_ind_cn = Faker('zh_CN')

dict_ind_cn = {
    'name' : fake_ind_cn.name(),
    'address' : fake_ind_cn.address(),
    'city' : fake_ind_cn.city(),
    'post code' : fake_ind_cn.postcode(),
    'country code' : fake_ind_cn.country_code()
}

print('')

print('--- Chinese ---')

for key,value in dict_ind_cn.items():
    print(key, ' - ', value)

print('')