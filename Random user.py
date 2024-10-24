#Esta libreria es especial para recibir información con el metodo GET desde la API random user
from randomuser import RandomUser
import pandas as pd

r = RandomUser()
some_list = r.generate_users(10)

name = r.get_full_name()

for user in some_list:
    print(user.get_full_name(),"",user.get_email())

#invocamos el metodo get_picture para generar fotos
for user in some_list:
    print (user.get_picture())

def get_users():
    users = []

    for user in RandomUser.generate_users(10):
        users.append({"Name": user.get_full_name(), "Gender": user.get_gender(), "City": user.get_city(),
                      "State": user.get_state(), "Email": user.get_email(), "DOB": user.get_dob(),
                      "Picture": user.get_picture()})

    return pd.DataFrame(users)

pd.set_option('display.max_columns', None)
pd.set_option('display.max_colwidth', None)
df1 = pd.DataFrame(get_users())
print(df1)