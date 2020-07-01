
##**Objectif**

Construction d'un programme qui lit une suite d'instruction et donne la position finale de B-VZXR.
##**Comment lancer le programme**

 - Modifier le chemin qui stocke les fichiers sources *'instruction_list.txt'* et *'universe.txt'*
*os.chdir("**C:/Users/Dan Vu/Desktop/**")*  (le 1er ligne du partie *Importer les données*)
 - Sélectionner tout le programme et le lancer


----------
#***Le programme***

    import os
    import pandas as pd
    from pandas import DataFrame

##**1. Importer les données**
    os.chdir("C:/Users/Dan Vu/Desktop/")
    InsFile = pd.read_csv('instruction_list.txt', sep=",", header=None, names=['Dir', 'Step'])
    Universe = pd.read_csv('universe.txt', sep=":", header=None, names=['Side', 'Value'])


##**2. Indiquer le score quand robot se tourne vers:** 
**sa droite (+1)** 
**sa gauche(-1)**

    def leftrightscore(dataset):
        score = []
        for val in dataset.values:
            if val == 'right':
                a = 1
            else:
                a = -1
            score.append(a)
        return score

##**3. Indiquer le score quand robot se dirige vers:**
**Le haut (Direction = 0)**
**La droite (*Dir = 1)**
**Le bas (*Dir = 2)**
**La gauche (*Dir = 3)**
***Si la direction < 0 ou > 3*** c.a.d le robot s'est tourné au moins 4 fois d'un quart de tour. Dans ce cas, on le modifie en utilisant le reste de la division de 4 pour assurer qu'il reste toujours 4 uniques valeurs [0,1,2,3] pour exprimer les 4 directions.

    def movement(dataset):
        move =[]
        sum_ = 0
        for val in dataset:
            sum_ += val
            if sum_ < 0 or sum_>3:
                sum_= sum_%4  #sum_ modulo 4
            move.append(sum_)
        return move

##**4. Faire l'instruction pour le déplacement du robot**
Après d'identifier la direction, il va ensuite avancer de k cases selon la valeur du nombre.
**Point départ (x,y) = (0,0)**
Si le robot avance vers **le haut** k cases: **(0,k)**
Si le robot avance vers **la droite** k cases: **(k,0)**
Si le robot avance vers **le bas** k cases: **(0,-k)**
Si le robot avance vers **la gauche** k cases: **(-k,0)**

    def funcX(row):
        if row['Move'] == 0:
            val = 0
        elif row['Move'] == 1:
            val = row['Step']
        elif row['Move'] == 2:
            val = 0
        else:
            val = -row['Step']
        return val

    def funcY(row):
        if row['Move'] == 0:
            val = row['Step']
        elif row['Move'] == 1:
            val = 0
        elif row['Move'] == 2:
            val = - row['Step']
        else:
            val = 0
        return val

## **5. Identifier la dimension de l'espace rectangulaire**

    def sizeuniverse(dataset):
        width = dataset['Value'].loc[0]
        height = dataset['Value'].loc[1]
        return width,height
    
    width, height = sizeuniverse(Universe)

##**6. Impliquer les conditions pour garder le robot dans l'univers indiqué**

    score = leftrightscore(InsFile['Dir'])
    Move = DataFrame(movement(score),columns=['Move'])
    InsFile = pd.concat([InsFile, Move],axis=1)
**Le programme pour trouver la position finale du robot**
  

      def getPositionFinale(dataset):
            cumX =[]
            sumX = 0
            dataX = dataset.apply(funcX, axis=1)
            for val in dataX.values:
                sumX += val
                if sumX >= width:
                    sumX= width -1
                elif sumX < 0:
                    sumX = 0
                else:
                    sumX = sumX
                cumX.append(sumX)
            cumY =[]
            sumY = 0
            dataY = dataset.apply(funcY, axis=1)
            for val in dataY.values:
                sumY += val
                if sumY >= height:
                    sumY = height -1
                elif sumY < 0:
                    sumY = 0
                else:
                    sumY = sumY
                cumY.append(sumY)    
            print("Le robot se trouve sur la case (", cumX[-1],", ", cumY[-1],")")
    
    getPositionFinale(InsFile)


###**Lancer le programme on va trouver le résultat obtenu est:**

    Le robot se trouve sur la case ( 45 ,  83 )






