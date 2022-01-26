#*******Partie A**************************************
class Player:
    def __init__(self,username,listepoint):  #initialisation de la classe avec ses options
        self.__pseudo=username
        self.__scores=listepoint

    def ScoreSend(self,musique):
        print(self.__scores[musique])   #Fonction qui permet de renvoyer le score d'une musique

    def NewScore(self,nvscore,songname):                    #fonction ajoutant un score a une musique
        self.nvxscore=nvscore
        self.songid=songname
        if self.nvxscore>=self.__scores[self.songid]:                       #verifie que le score qui veut etre ajouter n'est pas inferieur au score existant
            self.__scores[self.songid]=nvscore
            print("votre nouveau score est de", self.__scores[self.songid])
        else:
            print("Vous n'avez pas battu votre record, retenter votre chance!")

    def MeilleurScore(self):                                    #Fonction renvoyant le meilleur score du joueur
        BestScore=self.__scores[0]
        BestScoreSongid=0
        for i in range(1,5):
            if self.__scores[i-1]>=self.__scores[i]:                        # on parcours le dico du score
                if self.__scores[i-1]>BestScore:                #on compare la valeur avec la valeur qui la precede pour savoir laquelle est superieur
                    BestScore=self.__scores[i-1]
                    BestScoreSongid=i-1                                         #ajout de l'info sur le score est l'identifiant de la musique
            else:
                if self.__scores[i]>BestScore:                                  # on ajoute le resultat selon la reponse donné par le comparateur
                    BestScore=self.__scores[i]              #ajout de l'info sur le score est l'identifiant de la musique
                    BestScoreSongid=i
        print("Votre meilleur score est ",BestScore,"sur la musique",BestScoreSongid)       #on return l'info au joueur

    def PireScore(self):                                #Fonction renvoyant le pire score du joueur
        WorstScore=self.__scores[0]
        WorstScoreSongid=0
        for i in range(1,5):
            if self.__scores[i-1]<=self.__scores[i]:                            #on parcours le dico du score
                if self.__scores[i-1]<WorstScore:                       #on compare la valeur avec la valeur qui la precede pour savoir laquelle est inferieur
                    WorstScore=self.__scores[i-1]
                    WorstScoreSongid=i-1                                #ajout de l'info sur le score est l'identifiant de la musique
            else:
                if self.__scores[i]<WorstScore:                         #on ajoute le resultat selon la reponse donné par le comparateur
                    WorstScore=self.__scores[i]
                    WorstScoreSongid=i                                      #ajout de l'info sur le score est l'identifiant de la musique
        print("Votre pire score est ",WorstScore,"sur la musique",WorstScoreSongid)   #on return l'info au joueur


    def ScoreTotal(self):                   #fonction renvoyant le score total
        ScoreMax=0
        for i in self.__scores:                       #parcours le dico score en entier
            ScoreMax+=self.__scores[i]              #ajoute tout les scores a une valeur
        print (self.__pseudo,"a un score total de", ScoreMax)                        #retourne cette valeur max

#***************************Initialisation des valeurs*************************************
SongScore={0:0, 1:50, 2:100, 3:60, 4:75}        #creation d'un dico avec les musiques et les scores

Paulo=Player("Paulo",SongScore)
Paulo.ScoreSend(2)
Paulo.NewScore(50,2)
Paulo.NewScore(65,3)
Paulo.MeilleurScore()
Paulo.PireScore()
Paulo.ScoreTotal()

#******************************************************************************************
