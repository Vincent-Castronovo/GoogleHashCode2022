


class Contributor:

    name = "Name"
    # {skill, level}
    levels = []

    #class default constructor
    def __init__(self, name, levels): 
        self.name = name
        self.levels = levels

class Project:

    name = "Project name"
    duration = 0
    score = 0
    best_duration = 0
    number_of_roles = 0
    #{roles, level}
    roles = []

    #class default constructor
    def __init__(self, name, duration, score, best_duration, number_of_roles, roles): 
        self.name = name
        self.duration = duration
        self.score = score
        self.best_duration = best_duration
        self.number_of_roles = number_of_roles
        self.roles = roles