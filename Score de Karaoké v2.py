#*******Partie B**************************************
class Player:
    def __init__(self,username):  #initialisation de la classe avec ses options
        self.__pseudo=username

    def getPsuedo(self):
        return self.__pseudo    #creation d'une fonction renvoyant le pseudo du joueur

class Karaoke:
    def __init__(self,nameSong,ListeScoreMusic):                #initialisation de la classe Karaoke
        self.__nommusic=nameSong
        self.__listescoreM=ListeScoreMusic                          #deux entrée, les noms et la liste des scores

    def nameSong(self,idS):
        print(self.__nommusic[idS])                     # fonction test  permettant de renvoyer le nom d'une music via son id

    def ScoreAddMusic(self,idS,ScoretoAdd,PseudoPlayer):            #fonction permettant de rajouter une score avec le nom du joueur a la musique choisis
        ScoreL[ids]+= PseudoPlayer + ScoretoAdd
        print(ScoreL[ids])


#*******************Initialisation des valeurs**************************

ScoreL={0:[],2:[],3:[],4:[],5:[]}
PauloV2=Player("PauloLeBO")         #creation de PauloV2 qui est donc le joueur avec son pseudo
Karaok=Karaoke({0:"My World",1:"Never Say Never",2:"Believe",3:"La Mauvaise Réputation",4:"Les Amoureux Des Bancs Publics",5:"Le Gorille"},ScoreL) #creation de karaok regroupant des musics et une liste de score
Karaok.nameSong(2)
Karaoke.ScoreAddMusic(1,50,PauloV2.getPsuedo())

#***********************************************************************