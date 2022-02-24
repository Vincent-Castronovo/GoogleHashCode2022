


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
    best_duration = 0
    #{roles, level}
    roles = []