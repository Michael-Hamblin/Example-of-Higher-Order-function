# Example of a higher order function that displays a employee's base salary and name
def base_salary(x):
    def employee(full_name):
        # concatenation of the strings
        return full_name + " : " + str(x)

        # return the function (no parenthesis needed)

    return employee


# instance of base_salary with 10k as argument
salary_10k = base_salary(10000)

print(salary_10k("Michael Hamblin"))

print(salary_10k("Victor Deltoro"))

print(salary_10k("Simon lane"))
