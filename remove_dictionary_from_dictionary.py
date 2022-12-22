a = {
        'data' : 
        [
            {'name' : 'ashish1','address':'abc'},
            {'name' : 'ashish2','address':'abc'},
            {'name' : 'ashish3','address':'abc'},
            {'name' : 'ashish4','address':'abc'}
        ]
}
for ct,i in enumerate(a.get('data')):
    if i.get('name') == 'ashish4':
        # print("delete : ",i)
        del a.get('data')[ct] 

print(a)
