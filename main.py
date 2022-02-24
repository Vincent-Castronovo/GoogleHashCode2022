from parse import readFile
from output import outputer

output_projects = {}
#["name", contributeur1, 2, 3], [], []

def firstRun():

    for i in range(len(projects)):
        output_projects[projects[i][0]] = []

    lvlup = True

    #while(lvlup):
        #print("---------------------------------")
    lvlup = False
    #For each project
    for i in range(len(projects)):
        if (projects[i][4] == 0):
            continue
        #print("Looking at project " + projects[i][0])
        #Look for each roles needed
        for j in range(len(projects[i][5])):
            skill_name = projects[i][5][j][0]
            skill_level = projects[i][5][j][1]

            #If an available contributor with sufficient skills can do it
            for k in range(len(contributors)):
                #if contributor is available and not already in the project
                if contributors[k][2] == 0 and contributors[k][0] not in projects[i][7]:
                    #look for the needed skill
                    for l in range(len(contributors[k][1])):
                        #print(str(contributors[k][1][l][0]) + str(projects[i][5][j][0]) + str(contributors[k][1][l][1]) + str(projects[i][5][j][1]))
                        if contributors[k][1][l][0] == skill_name and contributors[k][1][l][1] >= skill_level:
                            #print("Found contributor: " + contributors[k][0])

                            #changed current project and days of the contributor
                            contributors[k][2] += projects[i][1]
                            contributors[k][3] = projects[i][0]
                            

                            output_projects[projects[i][0]].append(contributors[k][0])
                            projects[i][7].append(contributors[k][0])

                            projects[i][4] -= 1
                            #change skill needed to 9000 because not needed anymore
                            projects[i][5][j][1] = 9000

                            #print("Number of skills still needed: " + str(projects[i][4]))

                            #level up
                            #ontributors[k][1][l][1] = contributors[k][1][l][1] + 1
                            #lvlup = True
                            break

            #If not, look if someone already on this project can do mentoring
            #print(contributors)
            #print(projects)
            #Else, wait for someone to be available if possible
            
            for k in range(len(contributors)):
                if contributors[k][2] != 0 and contributors[k][0] not in projects[i][7]:
                    #possible
                    #if projects[i][3] - (contributors[k][2] + projects[i][1]) > 0:
                    #look for the needed skill
                    #print(str(contributors[k][1][l][0]) + str(projects[i][5][j][0]) + str(contributors[k][1][l][1]) + str(projects[i][5][j][1]))
                    for l in range(len(contributors[k][1])):
                        #print(contributors[l][0])
                        if contributors[k][1][l][0] == projects[i][5][j][0] and contributors[k][1][l][1] >= projects[i][5][j][1]:
                            #print("Found contributor: " + contributors[k][0])

                            #changed current project and days of the contributor
                            contributors[k][2] += projects[i][1]
                            contributors[k][3] = projects[i][0]
                            

                            output_projects[projects[i][0]].append(contributors[k][0])
                            projects[i][7].append(contributors[k][0])

                            projects[i][4] -= 1
                            #change skill needed to 9000 because not needed anymore
                            projects[i][5][j][1] = 9000


                            #print("Number of skills still needed: " + str(projects[i][4]))

                            #level up
                            #if (contributors[k][1][l][1] == projects[i][5][j][1] or contributors[k][1][l][1] == projects[i][5][j][1] - 1):
                            #    contributors[k][1][l][1] = contributors[k][1][l][1] + 1
                            #    lvlup = True
                            break
                        
    for i in range(len(projects)):
        if projects[i][4] != 0:
            output_projects.pop(projects[i][0], None)



if __name__ == "__main__":
    print("Start")

    nbrContributeurs, nbProjects, contributors, projects = readFile("input_data/d_dense_schedule.in.txt")
    #print(projects)
    firstRun()
    projects_done = 0
    for i in range(len(projects)):
        if (projects[i][4] == 0):
            projects_done += 1
    print(""+ str(projects_done) + " projects completed")
    outputer(output_projects, 'd_out.txt')


