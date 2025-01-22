keys = ['a', 'b', 'c']
default_dict = dict.fromkeys(keys, [])
default_dict['a'].append(1)

print(default_dict)  
# Output: {'a': [1], 'b': [1], 'c': [1]}


keys = ['a', 'b', 'c']
default_dict = {key: [] for key in keys}
default_dict['a'].append(1)

print(default_dict)  
# Output: {'a': [1], 'b': [], 'c': []}
