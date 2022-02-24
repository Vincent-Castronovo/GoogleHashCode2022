def outputer(projects, outputfile="out.txt"):
    with open(outputfile, 'w') as file:
        file.write(str(len(projects)))
        file.write("\n")
        for project in projects :
            file.write(project.pop(0))
            file.write("\n")
            for contrib in project:
                file.write(contrib)
                file.write("\n")

