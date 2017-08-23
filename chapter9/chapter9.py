class Dog(object):
      def __init__(self,name,age):
            self.name=name
            self.age=age

      def sit(self):
            print(self.name.title()+"is now sitting.")

      def roll_over(self):
            print(self.name.title()+"rolled over!")

my_dog=Dog('willie',6)
you_dog=Dog('lucy',3)

print("My dog's name is "+my_dog.name.title()+".")
print("My dog is "+str(my_dog.age)+" years old.")
my_dog.sit()
my_dog.roll_over()

print("Your dog's name is "+you_dog.name.title()+".")
print("Your dog is "+str(you_dog.age)+" years old.")


from collections import OrderedDict

favorite_languages=OrderedDict()

favorite_languages['jen']='python'
favorite_languages['sarah']='c'
favorite_languages['tom']='ruby'
favorite_languages['phil']='python'

for name ,language in favorite_languages.items():
     print(name.title()+"'s favorite language is:"+language.title()+'.')
