#DICTIONARY


#dictionary in phyton is used to store Information
# Creation of  dictionary
dictionary = {}
print(dictionary)

#another way of creation of dictionary is
 
dictionary = dict()
print(dictionary, type(dictionary))

# To add something in the dictionary 
xyz = {'name' : 'Abbas '  , 'nationality' : 'pakistan' ,'place' : 'UAE '}
print (xyz)


# To add some value in dictionary 

my_data  = {'name' : 'Abbas '  , 'nationality' : 'pakistan' ,'place' : 'UAE '}
print(my_data,type(my_data))
 # Name , age and nationality are keys , abbas,19  and pakistan are values

#if we want a specific value from the dictionary

dictionary  = {'name' : 'Abbas '  , 'nationality' : 'pakistan' ,'place' : 'United Arab Emirates '} 
print(dictionary["name"],type(dictionary))


# items METHOD in dictionary


dictionary  =  {'name' : 'Abbas '  , 'nationality' : 'pakistan' ,'place' : 'United arab emirates '}
print(dictionary.items())
#this is the way we can get all the items stored in dictionary  


 # if we want the only the keys in the dictionary 

dictionary  =  {'name' : 'Abbas '  , 'nationality' : 'pakistan' ,'place' : 'United arab emirates '}
print(dictionary.keys())

# Delete method 
#with the help of delete method we could delete a specific data from the dictionary

dictionary  = {'name' : 'jhon '  , 'nationality' : 'UK' ,'place' : 'UAE '}
del dictionary ["place"]
print(dictionary.items())
#the output will be only the name and nationality

# POP METHOD
#with the help of this method we can make one value prominent by adding .pop with the dictionary

dictionary  = { 'ame' : 'Abbas' ,
                'age' :  '19' , 
                'nationality ': 'pakistan' } 
print(dictionary.pop("name"))
print(dictionary.keys())
print(dictionary.values())