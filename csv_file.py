import csv

# fields = ['Name', 'Email']

# rows = [ ['Nikhil', 'nikhil.gfg@gmail.com'],
#         ['Sanchit', 'sanchit.gfg@gmail.com'],
#         ['Aditya', 'aditya.gfg@gmail.com'],
#         ['Sagar', 'sagar.gfg@gmail.com'],
#         ['Prateek', 'prateek.gfg@gmail.com'],
#         ['Sahil', 'sahil.gfg@gmail.com']]

mydict =[{'branch': 'COE', 'cgpa': '9.0',
          'name': 'Nikhil', 'year': '2'},
        {'branch': 'COE', 'cgpa': '9.1',
         'name': 'Sanchit', 'year': '2'},
        {'branch': 'IT', 'cgpa': '9.3',
         'name': 'Aditya', 'year': '2'},
        {'branch': 'SE', 'cgpa': '9.5',
         'name': 'Sagar', 'year': '1'},
        {'branch': 'MCE', 'cgpa': '7.8',
         'name': 'Prateek', 'year': '3'},
        {'branch': 'EP', 'cgpa': '9.1',
         'name': 'Sahil', 'year': '2'}]

fields = ['name', 'branch', 'year', 'cgpa']

# filename = "email_records.csv"
filename = "university_records.csv"
 

with open(filename, "w") as csvfile:
    csvwriter = csv.DictWriter(csvfile, fieldnames= fields)

    csvwriter.writeheader()
    csvwriter.writerows(mydict)