
# 2. Write a Python program to replace dictionary values(V,VI)and with their average.
# Input:-
# student_details= [{'id' : 1, 'subject' : 'math', 'V' : 70, 'VI' : 82},
# {'id' : 2, 'subject' : 'math', 'V' : 73, 'VI' : 74},
# {'id' : 3, 'subject' : 'math', 'V' : 75, 'VI' : 86}]
# Expected Output:
# [{'subject': 'math', 'id': 1, 'V+VI': 76.0}, {'subject': 'math', 'id': 2, 'V+VI': 73.5},
# {'subject': 'math', 'id': 3, 'V+VI': 80.5}]

student_details= [
    {'id' : 1, 'subject' : 'math', 'V' : 70, 'VI' : 82},
    {'id' : 2, 'subject' : 'math', 'V' : 73, 'VI' : 74},    
    {'id' : 3, 'subject' : 'math', 'V' : 75, 'VI' : 86}
    
    ]

for key in student_details:
    key['V+VI']=key['VI']+key['VI'] /2
    key.pop('V')
    key.pop('VI')

print(student_details)