def readFile(filename):
    file = open(filename, 'r')
    lines = file.readlines()
    nbDeContributeurs, nbDeProjets = lines[0].split()
    nbContributeurs = int(nbDeContributeurs)
    nbProjets = int(nbDeProjets)

    contributeurs = []
    i = 1
    k = 0
    while k < nbContributeurs:
        line1 = lines[i].split()
        nom = line1[0]
        nbskills = int(line1[1])
        skills = []
        for j in range(nbskills):
            tmp = lines[i+j+1].split()
            skills.append([tmp[0], int(tmp[1])])
        contributeurs.append([nom,skills,0])
        i += nbskills + 1
        k += 1

    projets = []
    k = 0
    while k < nbProjets:
        line1 = lines[i].split()
        nom = line1[0]
        days = int(line1[1])
        score = int(line1[2])
        bbday = int(line1[3])
        nbroles = int(line1[4])
        skills = []
        for j in range(nbroles):
            tmp = lines[i+j+1].split()
            skills.append([tmp[0], int(tmp[1])])
        projets.append([nom, days, score, bbday, nbroles, skills, 0])
        i += nbroles + 1
        k += 1

    return nbContributeurs, nbProjets, contributeurs, projets

print(readFile("input_data/b_better_start_small.in.txt"))