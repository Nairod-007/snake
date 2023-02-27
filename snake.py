from time import sleep
import pygame
from random import randrange

class Jeu:
    def __init__(self):
        self.largeur_limit = 5
        self.taille = 20
        self.dimension = (800,600)
        self.ecran = pygame.display.set_mode(self.dimension)
        pygame.display.set_caption("Jeu snake")
        self.dimension_jeu=(40,40,self.dimension[0]-40,self.dimension[1]-40)
        self.partie = True

        #Serpent
        self.serpent_position = [self.dimension_jeu[0], self.dimension_jeu[1]] #Départ
        self.serpent_direction = [0, 0]
        self.serpent_taille = self.taille
        self.serpent_longueur = 1
        self.vitesse = 1
        self.serpent_positions = []

        #Pomme
        self.pomme_taille = self.taille
        self.pomme_position = [randrange(self.dimension_jeu[0],self.dimension_jeu[2]-self.pomme_taille,self.taille),
                               randrange(self.dimension_jeu[1],self.dimension_jeu[3]-self.pomme_taille,self.taille)]


    def main(self):
        # Permet de gerer les évenements, d'afficher certains composants du jeu grace au while loop
        while self.partie:
            pygame.time.Clock().tick(60) #Permet de gérer les fps du jeu
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.partie=False # Fin de la partie

                #Donne la direction du serpent
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        self.serpent_direction[0]= self.vitesse
                        self.serpent_direction[1]= 0
                    if event.key == pygame.K_LEFT:
                        self.serpent_direction[0]= -self.vitesse
                        self.serpent_direction[1]= 0
                    if event.key == pygame.K_UP:
                        self.serpent_direction[0]= 0
                        self.serpent_direction[1]= -self.vitesse
                    if event.key == pygame.K_DOWN:
                        self.serpent_direction[0]= 0
                        self.serpent_direction[1]= self.vitesse

            #Si le Serpent touche la Pomme
            self.contact()

            #Corps du serpent
            tete_serpent = []
            tete_serpent.append(self.serpent_position[0])
            tete_serpent.append(self.serpent_position[1])
            direction_serpent=[]
            direction_serpent.append(self.serpent_direction[0])
            direction_serpent.append(self.serpent_direction[1])
            tete_serpent.append(direction_serpent)
            self.serpent_positions.append(tete_serpent)

            if len(self.serpent_positions) > self.serpent_longueur:
                self.serpent_positions.pop(0)


            #Stop si serpent en dehors des limites
            if not (self.dehors_limite()):
                pass
            else:
                self.deplacement()

            self.ecran.fill((0,0,0))#attribut la couleur noir à l'écran
            self.dessin_pomme()
            self.dessin_serpent()
            for corps_serpent in self.serpent_positions:
                pygame.draw.rect(self.ecran,(0,255,0),(corps_serpent[0],corps_serpent[1],self.taille,self.taille))
            self.delimiter()
            self.actualiser()

    def contact(self):
        if self.serpent_position == self.pomme_position:
            self.pomme_position = [randrange(self.dimension_jeu[0],self.dimension_jeu[2]-self.pomme_taille,self.taille),
                                   randrange(self.dimension_jeu[1],self.dimension_jeu[3]-self.pomme_taille,self.taille)]
            self.serpent_longueur+=1

    def deplacement(self):
        for i in range(self.taille//self.vitesse):
            #Mise a jour de la position du serpent
            if self.serpent_direction[0] != 0:
                self.serpent_position[0] += self.serpent_direction[0]
            elif self.serpent_direction[1] != 0:
                self.serpent_position[1] += self.serpent_direction[1]

            #if self.serpent_longueur>:

            if self.serpent_positions[0][-1][0]!=0:
                self.serpent_positions[0][0] += self.serpent_positions[0][-1][0]
            elif self.serpent_positions[0][-1][1]!=0:
                self.serpent_positions[0][1] += self.serpent_positions[0][-1][1]

            sleep(0.002)
            self.ecran.fill((0,0,0))#attribut la couleur noir à l'écran
            self.dessin_pomme()
            self.dessin_serpent()
            self.delimiter()
            self.actualiser()

    def dehors_limite(self):
        if self.serpent_direction[0] == -self.vitesse and self.serpent_position[0] <= self.dimension_jeu[0] :
            return False
        elif self.serpent_direction[1] == -self.vitesse and self.serpent_position[1] <= self.dimension_jeu[1] :
            return False
        elif self.serpent_direction[0] == self.vitesse and self.serpent_position[0]+self.taille >= self.dimension_jeu[2]:
            return False
        elif self.serpent_direction[1] == self.vitesse and self.serpent_position[1]+self.taille >= self.dimension_jeu[3]:
            return False
        else:
            return True

    def actualiser(self):
        pygame.display.flip()

    def dessin_pomme(self):
        pygame.draw.rect(self.ecran,(255,0,0),(self.pomme_position[0],self.pomme_position[1],self.pomme_taille,self.pomme_taille))

    def dessin_serpent(self):
        pygame.draw.rect(self.ecran,(0,255,0),(self.serpent_position[0],self.serpent_position[1],self.serpent_taille,self.serpent_taille))
        for corps_serpent in self.serpent_positions:
            pygame.draw.rect(self.ecran,(0,255,0),(corps_serpent[0],corps_serpent[1],self.taille,self.taille))

    def delimiter(self):
        pygame.draw.rect(self.ecran,(255,255,255),
                        (self.dimension_jeu[0]-self.largeur_limit,self.dimension_jeu[1]-self.largeur_limit,
                         self.dimension_jeu[2]-40+2*self.largeur_limit,self.dimension_jeu[3]-40+2*self.largeur_limit),
                         self.largeur_limit)



if __name__=='__main__':
    pygame.init()
    Jeu().main()
    pygame.quit()

