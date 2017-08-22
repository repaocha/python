alien_0={'color':'green','points':5}
print(alien_0['color'])
print(alien_0['points'])

alien_0['x_position']=0
alien_0['y_position']=25
print(alien_0)

alien_0={'color':'green'}
print("The alien is "+alien_0['color']+'.')


alien_0={'x_position':0,'y_position':25,'speed':'medium'}
print("Original x-position: "+str(alien_0['x_position']))

if alien_0['speed']=='slow':
     x_increment=1
elif alien_0['speed']=='medium':
     x_increment=2
else:
     x_increment=3

alien_0['x_position']=alien_0['x_position']+x_increment
print("New x-position:" +str(alien_0['x_position']))


alien_0={'color':'green','points':5}
print(alien_0)

del alien_0['points']
print(alien_0)


favorite_languages={
    'jen':'python',
    'sarah':'c',
    'Tom':'ruby',
    'phil':'python'
}
print("sarah's favorite language is "+favorite_languages['sarah'].title()+".")
for name,language in favorite_languages.items():
     print("Name: "+name)
     print("Language: "+language)
for name in favorite_languages.keys():
     print(name.title())
friends=['phil','sarah']
for name in favorite_languages.keys():
     print(name.title())
     
     if name in friends:
     	   print("Hi "+name.title()+",I see your favorite language is "+favorite_languages[name].title()+".")
for name in sorted(favorite_languages.keys()):
     print(name.title()+",thank you for taking the poll.")
print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
     print(language.title())
     

user_0={
       'username':'yangchen',
       'first':'yang',
       'last':'chen'
}
for key,value in user_0.items():
     print("key: "+key)
     print("Value: "+value)


alien_0={'color':'green','points':5}
alien_1={'color':'yellow','points':10}
alien_2={'color':'red','points':15}

aliens=[alien_0,alien_1,alien_2]

for alien in aliens:
     print(alien)


aliens=[]

for alien_number in range(30):
     new_alien={'color':'green','points':5,'speed':'slow'}
     aliens.append(new_alien)
     #print(aliens)

for alien in aliens[0:3]:
     if alien['color']=='green':
         alien['color']='yellow'
         alien['speed']='medium'
         alien['points']=10

for alien in aliens[:5]:
     print(alien)
print("...")

print("Total number of aliens:"+str(len(aliens)))


pizza={
         'crust':'thick',
         'toppings':['mushrooms','extra cheese']
        }
print("You ordered a "+pizza['crust']+"-crust pizza with the following toppings:")

for topping in pizza['toppings']:
      print ("\t"+topping)


favorite_languages={
        'jen':['python','ruby'],
        'sarah':['c'],
        'tom':['ruby','go'],
        'phil':['python','haskell']
}
for name,languages in favorite_languages.items():
     print("\n"+name.title()+"'s favorite languages are:")
     for language in languages:
     	        print("\t"+language.title())



users={
      'aeinstein':{
      'first':'albert',
      'last':'einstein',
      'location':'princeton',
      },

      'mcurie':{
      'first':'marie',
      'last':'curie',
      'location':'paris',
      },
}

for username,user_info in users.items():
     print("\nUsername:"+username)
     full_name=user_info['first']+" "+user_info['last']
     location=user_info['location']

     print("\tfull_name:"+full_name.title())
     print("\tlocation:"+location.title())