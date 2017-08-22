def greet_user():
     print("Hello")
greet_user()


def greet_user(username):
     print("Hello,"+username.title()+"!")
greet_user('jesse')


def describe_pet(pet_name,animal_type='dog'):
      print("\nI have a "+animal_type+".")
      print("My "+animal_type+"'s name is "+pet_name.title()+".")
describe_pet('hamster','harry')
describe_pet('dog','willie')
describe_pet('tom','cat')
describe_pet(pet_name='tom',animal_type='cat')
describe_pet(pet_name='willie')
describe_pet('willie')


def get_formatted_name(first_name,last_name,middle_name=''):
     if middle_name:
           full_name=first_name+' '+middle_name+' '+last_name
     else:
           full_name=first_name+' '+middle_name+' '+last_name 
     return full_name.title()
musician=get_formatted_name('jimi','hendrix')
print(musician)
musician=get_formatted_name('jimi','hendrix','lee')
print(musician)


def build_person(first_name,last_name,age=' '):
      person={'first':first_name,'last':last_name}
      if age:
          person['age']=age
      return person
musician=build_person('jimi','hendrix',age=20)
print(musician)


def greet_users(names):
     for name in names:
           msg="Hello, "+name.title()+"!"
           print(msg)
usernames=['hannah','ty','margot']
greet_users(usernames)


unprinted_designs=['iphone case','robot pendant','dodecahedron']
completed_models=[]
while unprinted_designs:
      current_design=unprinted_designs.pop()

      print("Printing model: "+current_design)
      completed_models.append(current_design)

print("\nThe following models have been printed:")
for completed_model in completed_models:
     print(completed_model)


def print_models(unprinted_designs,completed_models):
     while unprinted_designs:
     	      current_design=unprinted_designs.pop()

     	      print("Printing model: "+current_design)
     	      completed_models.append(current_design)
def show_completed_models(completed_models):
     print("\nThe following models have been printed:")
     for completed_model in completed_models:
     	     print(completed_model)

unprinted_designs=['ipone case','robot pendant','dodecahedron']
completed_models=[]
print_models(unprinted_designs,completed_models)
show_completed_models(completed_models)


def make_pizza(size,*toppings):
     print("\nMaking a "+str(size)+"-inch pizza with the following toppings:")
     for topping in toppings:
     	     print("- "+topping)
make_pizza(16,'pepperoni')
make_pizza(12,'mushrooms','green peppers','extra cheese')


def build_profile(first,last,**user_info):
     profile={}
     profile['first name']=first
     profile['last_name']=last
     for key,value in user_info.items():
     	     profile[key]=value
     return profile
user_profile=build_profile('albert','einstein',
                                 location='princeton',
                                 field='physics')
print(user_profile)