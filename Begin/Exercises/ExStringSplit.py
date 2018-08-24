#"bob | Robert | Gringo | 8-921-007-1637 | robert@mail.sru"  To  split/ print those subjects.  

data = "bob | Robert | Gringo | 8-921-007-1637 | robert@mail.sru"


for i in range(4)
	new_data = data[:data.index('|')+1]
	print(i, new_data)
	data = new_data


