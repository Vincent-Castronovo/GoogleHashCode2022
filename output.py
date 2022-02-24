def outputer(projects, outputfile="out.txt"):
    with open(outputfile, 'w') as file:
        file.write(str(len(projects)))
        file.write("\n")
        for project in projects :
            file.write(project)
            file.write("\n")
            file.write(' '.join(projects[project]))
            file.write("\n")

