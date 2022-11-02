import pygame

pygame.init()

########### toutes les classes et fonctions utiliser dans drawe ou setup ############


#classe du joueur
class Player(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.vie = 100
        self.max_vie = 100
        self.attaque = 10
        self.vitesse = 5
        self.sprite_sheet = pygame.image.load('spritesBlond.png')
        self.image = self.get_image(0,0)
        self.image.set_colorkey([255, 0, 202]) # couleur transpatante perso
        self.rect = self.image.get_rect()
        self.position = [x,y]

        self.images = {
            'left1': self.get_image(0, 32),
            'right1': self.get_image(0, 0),
            'dead1': self.get_image(0, 64)
        }  # les étapes d'animation du personnage, ici seulement le 1er sprite de chaque ligne
        self.old_position = self.position.copy()

    def get_image(self, x, y):
        image = pygame.Surface([32,32])# taille d'un perso dans le spitcheet
        image.blit(self.sprite_sheet, (0,0), (x, y, 32, 32))
        return pygame.transform.scale(image,(96,96)) # renvois le srpite à la taille voulus

    def save_location(self): self.old_position = self.position.copy() # utile pour les colision s'il y en a

    def change_animation(self, name):
        self.image = self.images[name]
        self.image.set_colorkey([255, 0, 202])# couleur rgb = transparente à chaque étape de animation

    def move_right(self): self.position[0] += self.vitesse

    def move_left(self): self.position[0] -= self.vitesse

    def move_dead(self): self.position[0] = self.vitesse #self.position[1] bouge de haut en bas , je sais pas bien encore comment on vas faire la mort, légalitée est inutile

    def update(self): #bouge le perso indépendament des obstacles
        self.rect.topleft = self.position

    def handle_input(self):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_LEFT]:  # fleches
            self.move_left()
            self.change_animation('left1')
        elif pressed[pygame.K_RIGHT]:
            self.move_right()
            self.change_animation('right1')



############## mise en place du "setup" ################
#générer la fenaître du jeu
pygame.display.set_caption("The Messager")#titre fenître, titre, img
screen = pygame.display.set_mode((1000,700))#taille fenître

#arriere plans
originalImg = pygame.image.load('village_1.png')
background = pygame.transform.scale(originalImg,(700/128*256,700))

player = Player(500,500)
clock = pygame.time.Clock()



running = True
############## mise en place du "drawe" #############
while running:
    screen.blit(background, (0, 0)) #place le background, le joueur
    screen.blit(player.image,player.rect)
    player.save_location() # en cas de colistion pouvoire retourner en arrière
    player.handle_input() # regerde touche enfoncer
    player.update()
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT: #si croix et cliquer, running est faux et ...
            running = False

clock.tick(60)
pygame.quit()# ... le jeu s'arrete
