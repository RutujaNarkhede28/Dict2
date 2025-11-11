students={'anil':23,'sunil':22,'amit':23}
stud=students
print(stud)

d={'A101':'anil','A102':'dinesh','A103':'Sunil'}
#Remove all the element of dict
d.clear()
print(d)
#copy the elements of dict to x
d={'A101':'anil','A102':'dinesh','A103':'Sunil'}
x=d.copy()
print(x)
##Get():-Returns the value of the specified key
d={'A101':'anil','A102':'dinesh','A103':'Sunil'}
x=d.get('keyname')
print(x)
y=d.get('A101')
print(y)
##Items():-
d={'A101':'anil','A102':'dinesh','A103':'Sunil'}
x=d.items()
print(x)
##Keys:-
d={'A101':'anil','A102':'dinesh','A103':'Sunil'}
x=d.keys()
print(x)
##Pop:-
x=d.pop('A101')
print(x)
y=d.pop('A102')
print(y)

##Pop item:- removes the first item of dictionary
d={'A101':'anil','A102':'dinesh','A103':'Sunil'}
x=d.pop('A101')
print(x)


