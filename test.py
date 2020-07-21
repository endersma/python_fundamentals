students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterateDictionary(user_list):
    
    for i in range(0, len(user_list), 1):
        for key, value in user_list[i].items():
            print(key, value)

iterateDictionary(students)