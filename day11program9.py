employees = ['Manohar', 'prasad', 'manasa']
defaults = {"designation": 'Developer', "Salary":80000}

data = dict.fromkeys(employees,defaults)
print(data)

#individual data
print(data["manasa"])
