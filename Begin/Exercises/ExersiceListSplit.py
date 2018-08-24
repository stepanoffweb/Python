#"bob | Robert | Gringo | 8-921-007-1637 | robert@mail.sru"  To create a list of subjects and to convert it into dictionary and split/ print those subjects.  


data = "bob | Robert | Gringo | 8-921-007-1637 | robert@mail.sru"
my_list = data.split('|')
print(my_list)
'''
nickname = my_list[0]
firstname = my_list[1]
secondname = my_list[2]
phonenumber = my_list[3]
email = my_list[4]

print(nickname, firstname, secondname, phonenumber, email)'''
nickname, firstname, secondname, phonenumber, email = data.split('|')
print(nickname, firstname, secondname, phonenumber, email )
