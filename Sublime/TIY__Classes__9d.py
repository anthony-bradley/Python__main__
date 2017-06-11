#python3 TIY__Classes__9d.py

#Imported Restaurant: 9-10:

from restaurant import Restaurant

bistro_1 = Restaurant('guacamole 61', 'mexican')

bistro_1.describe_restaurant()
bistro_1.open_restaurant()


#Imported Admin: 9-11:

#from user_module import User, Privileges, Admin

#me = Admin('anthony', 'thudium', str(24), 'berkeley', 'berkeley')

#me.describe_user()

#my_privileges = ['Add post.', 'Delete post.', 'Ban user.',]

#me.privileges.privileges = my_privileges # [1] This makes it work.

#me.privileges.show_privileges() # [2] This makes it work.


#Multiple Modules: 9-12:

from privileges_admin import User, Privileges, Admin

me = Admin('anthony', 'thudium', str(24), 'berkeley', 'berkeley')

me.describe_user()

my_privileges = ['Add post.', 'Delete post.', 'Ban user.',]

me.privileges.privileges = my_privileges # [1] This makes it work.

me.privileges.show_privileges() # [2] This makes it work.


