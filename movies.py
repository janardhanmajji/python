current_movies = {'Temper' : '11:00am', 'ASVR' : '1:00pm', 'Rakhi': '4:00pm', 'YD' : '6:00pm'}
print('We are playing the following movies\n')
for movie in current_movies:
    print(movie)
ice = input('Which movie do you want to watch\n')
st = current_movies.get(ice)

if st==None:
    print('The movie is not present')
else:
    print('The movie is at ', st)    


