acronym = {'LOL': 'Laugh out loud', 'TBH' : 'To be honest', 'IDK' : 'I dont know'}
print(acronym.get('LOL'))
ac= 'IDK'+ ' what happened '+ 'TBH'
dc = acronym.get('IDK') + 'what happened' + acronym.get('TBH')


print(ac)
print(dc)

