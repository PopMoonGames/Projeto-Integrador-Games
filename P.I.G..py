#Importando Bibliotecas Necessárias
import pygame       # Importa a biblioteca pygame, que é usada para desenvolver jogos em Python.
import random       #Importa o módulo random, usado para gerar números aleatórios.
import os           # Importa o módulo os, que fornece funcionalidades relacionadas ao sistema operacional, como manipulação de arquivos.
import sys          #Importa o módulo sys, que fornece acesso a algumas variáveis ​​usadas ou mantidas pelo interpretador Python e funções que interagem fortemente com o interpretador.
from pygame.locals import *     #Importa todos os símbolos do módulo pygame.locals. Isso inclui constantes e eventos pygame.
from pygame import mixer        #Importa o mixer do pygame, usado para controlar a reprodução de sons.

#Criando display da janela do app
SCREEN_HEIGHT = 1000        #Define a altura da tela como 1000 pixels.
SCREEN_WIDTH = 800          #Define a largura da tela como 800 pixels.

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_WIDTH))  #Cria uma tela de exibição com a largura e altura especificadas.
pygame.display.set_caption('PROJETO INTEGRADOR GAMES')          # Define o título da janela do jogo como 'PROJETO INTEGRADOR GAMES'.

# Importando Imagens dos Botões
#Carrega a imagem do botão "flap" (suponho que seja para um jogo de Flappy Bird, por exemplo).
flap_img = pygame.image.load('img/icons/iconflap.png').convert_alpha()
jump_img = pygame.image.load('img/icons/iconjump.png').convert_alpha()
breakoup_img = pygame.image.load('img/icons/iconbreakoup.png').convert_alpha()
space_img = pygame.image.load('img/icons/iconspace.png').convert_alpha()
tkj_img = pygame.image.load('img/icons/icontkj.png').convert_alpha()
fight_img = pygame.image.load('img/icons/iconfight.png').convert_alpha()
exit_img = pygame.image.load('img/icons/sair.png').convert_alpha()
pig_img = pygame.image.load('img/icons/pig_btn.png').convert_alpha()
back_img = pygame.image.load('img/carregamento/telainicial.png').convert_alpha()
dev_img = pygame.image.load('img/carregamento/teladev.png').convert_alpha()


#Criando Classe dos Botões

class Button():
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False
        
    def draw(self, surface):
        action = False
        #Comando para obter posição do mouse
        pos = pygame.mouse.get_pos()
        
        #Verifique as condições do clique do mouse
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
                
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
        
        #Desenha o botão na tela
        surface.blit(self.image, (self.rect.x, self.rect.y))
        
        return action


#Cria instâncias de botão
flap_button = Button(50, 180, flap_img, 0.1)
breakoup_button = Button(30, 320, breakoup_img, 0.15)
space_button = Button(45, 500, space_img, 0.15)
jump_button = Button(630, 180, jump_img, 0.1)
tkj_button = Button(600, 320, tkj_img, 0.15)
fight_button = Button(650, 500, fight_img, 0.2)
exit_button = Button(680, 730, exit_img, 0.8)
pig_button = Button(287, 30, pig_img, 1)

#Configurações para tela carregamento
#criando a janela
width = 600
height = 600
screen_size = (width, height)

#declarando as cores do jogo
black = (0, 0, 0)
green = (33, 94, 33)
red = (200, 0, 0)
white = (255, 255, 255)
yellow = (217, 217, 25)
blue = (20, 20, 200)

score_space = 0
# Criando Tela Inicial

font_path = 'txt/pixel.ttf'

def tela_inicial():
    mixer.init()
    pygame.init()
    
    pygame.mixer.music.load('audio/tela inicial/telainicial.mp3')
    pygame.mixer.music.set_volume(0.2)
    pygame.mixer.music.play(-1, 0.0)
    
    icon = pygame.image.load('img/icons/iconpig.png')
    
    # Limpe a tela
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_WIDTH))
    pygame.display.set_caption('PROJETO INTEGRADOR GAMES')
    pygame.display.set_icon(icon)
    screen.blit(back_img, (0,0))

# Renderizando e exibindo a pontuação com contorno
    font = pygame.font.Font(font_path, 20)
# Renderize o texto principal
    light_text = font.render('FIGHT MORTAL', True, (255, 255, 255))
    light_rect = light_text.get_rect(center=(700, 610))

    #Loop principal da tela inicial
    # Variável para controlar o estado do loop
    run = True
    while run:
        # # Desenhe os botões e execute os jogos correspondentes
        if pig_button.draw(screen):
            pig()
        if flap_button.draw(screen):
            jogo_flap()
        if jump_button.draw(screen):
            jogo_jump()
        if breakoup_button.draw(screen):
            jogo_breakoup()
        if space_button.draw(screen):
            jogo_space()
        if tkj_button.draw(screen):
            jogo_tkr()
        if fight_button.draw(screen):
            jogo_fight()
        if exit_button.draw(screen):
            run = False             # Encerrar o loop e sair
            sys.exit()
            #quit()      

        # Manipulador de eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                #quit()

        # Desenhe o texto principal na tela
        screen.blit(light_text, light_rect)
        # Renderizando e exibindo a pontuação com contorno
        font = pygame.font.Font(font_path, 20)
        # Renderize o texto com uma sombra escura para simular um contorno
        shadow_text = font.render('copyrights PopMoon 2024', True, black)
        shadow_rect = shadow_text.get_rect(center=(132, 772))

        # Desenhe o texto sombreado na tela
        screen.blit(shadow_text, shadow_rect)

        # Renderize o texto principal
        score_text = font.render('copyrights PopMoon 2024', True, white)
        score_rect = score_text.get_rect(center=(130, 770))

        # Desenhe o texto principal na tela
        screen.blit(score_text, score_rect)
        
        pygame.display.update()
        
##############################################################################################################################
# Essa função em questão faz com que exibimos os créditos com os nossos nomes como desenvolvedores do 'Projeto Integrador Games'

def pig():

    pygame.mixer.music.stop()
    mixer.init()
    pygame.init()
    
    pygame.mixer.music.load('audio/tela inicial/pig.mp3')
    pygame.mixer.music.set_volume(0.3)
    pygame.mixer.music.play(-1, 0.0)
    # carregando a imagem da tela inicial
    
    icon = pygame.image.load('img/icons/iconpig.png')
    
    back_img = pygame.image.load('img/carregamento/teladev.png')
    back_img = pygame.transform.scale(back_img, (800, 800))
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_WIDTH))
    pygame.display.set_caption('CRÉDITOS P.I.G.')
    pygame.display.set_icon(icon)
    screen.blit(back_img, (0,0))
    #     screen.blit(back_img, (0, 0))

    # carregando as imagens dos botões
    img_sair = pygame.image.load('img/carregamento/voltar.png')

    # redimensionando os botões
    button_width, button_height = 130, 50
    img_sair = pygame.transform.scale(img_sair, (button_width, button_height))

    # definindo as coordenadas dos botões
    sair_y = 700
    sair_x = 350

    # Definindo os retângulos de colisão dos botões
    
    sair_rect = img_sair.get_rect(topleft=(sair_x, sair_y))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                tela_inicial()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # obtendo a posição do mouse
                mouse_pos = pygame.mouse.get_pos()
                # verificando se clicou em sair
                if sair_rect.collidepoint(mouse_pos) or key[pygame.K_ESCAPE]:
                    #pygame.quit()          esse comando crasha o app se por ventura precisar sair e voltar para a tela
                    tela_inicial()
        #manipuladores de eventos
        
            key = pygame.key.get_pressed()
            if key[pygame.K_ESCAPE]:
                #pygame.quit()
                tela_inicial()
        # denhando os botões na tela
        screen.blit(img_sair, (sair_x, sair_y))

        pygame.display.update()

###############################################################################################################################    
def jogo_flap():

    pygame.init()
    mixer.init()


    pygame.mixer.music.load('audio/flap/flaptheme.mp3')
    pygame.mixer.music.set_volume(0.3)
    pygame.mixer.music.play(-1, 0.0)

    clock = pygame.time.Clock()
    fps = 60
#CRIAR TAMANHO DA TELA DO JOGO
    screen_width = 864
    screen_height = 936
    
    icon = pygame.image.load('img/icons/iconflap.png')
#CRIAR TAMANHO DA TELA DO JOGO
    screen = pygame.display.set_mode((screen_width, screen_height))
#TITULO PARA JANELA      
    pygame.display.set_caption('Flappy Bird')
    pygame.display.set_icon(icon)

    #FONTE
    font = pygame.font.SysFont('Bauhaus 93', 60)
    font_small = pygame.font.SysFont('Lucida Sans', 20)
    font_big = pygame.font.SysFont('Lucida Sans', 24)
    font_path = 'txt/pixel.ttf'
    #CORES
    white = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    PANEL = (153, 217, 234)
#-----------------------define variaveis do jogo-----------------------------------------------
    ground_scroll = 0
    #Velocidade de movimento
    scroll_speed = 4
    flying = False
    game_over = False
    pipe_gap = 150
    pipe_frequency = 1500 #milliseconds
    last_pipe = pygame.time.get_ticks() - pipe_frequency
    score = 0
    pass_pipe = False
    scoreflap = 0
    pontos = 0
    fade_counter = 0
    high_score = 0

    if os.path.exists('txt/scoreflap.txt'):
            with open('txt/scoreflap.txt', 'r') as file:
                high_score = int(file.read())
    else:
        high_score = 0

    # função para carregar a pontuação máxima
    def carregar_pontuacao_maxima():
        try:
            with open('txt/scoreflap.txt', 'r') as file:
                return int(file.read().strip())
        except FileNotFoundError:
            return 0

    # função para salvar a pontuação máxima
    def salvar_pontuacao_maxima(pontuacao):
        with open('txt/scoreflap.txt', 'w') as file:
            file.write(str(pontuacao))

    #IMAGENS
    bg = pygame.image.load('img/flapimg/bg.png')
    ground_img = pygame.image.load('img/flapimg/ground.png')
    button_img = pygame.image.load('img/flapimg/restart.png')

    #Criando imagem de background para game over
    bg_game_over = pygame.image.load('img/flapimg/gameover.png').convert_alpha()
    bg_game_over = pygame.transform.scale(bg_game_over,(864, 936))
    def draw_bg_game_over():
        screen.blit(bg_game_over, (0, 0))

#########################################################################################
    # criando a tela de carregamento
    def tela_carregamento():

        pygame.mixer.music.stop()
        pygame.mixer.music.play(-1)
        
        # carregando a imagem da tela inicial
        back_img = pygame.image.load('img/carregamento/flapcarregamento.png')
        back_img = pygame.transform.scale(back_img, (864, 936))


        # carregando as imagens dos botões
        img_iniciar = pygame.image.load('img/carregamento/iniciar.png')
        img_sair = pygame.image.load('img/carregamento/voltar.png')

        # redimensionando os botões
        button_width, button_height = 130, 50
        img_iniciar = pygame.transform.scale(img_iniciar, (button_width, button_height))
        img_sair = pygame.transform.scale(img_sair, (button_width, button_height))

        # definindo as coordenadas dos botões
        iniciar_x = 250
        iniciar_y = 500
        sair_y = 500
        sair_x = 450

        # Definindo os retângulos de colisão dos botões
        iniciar_rect = img_iniciar.get_rect(topleft=(iniciar_x, iniciar_y))
        sair_rect = img_sair.get_rect(topleft=(sair_x, sair_y))

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    tela_inicial()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # obtendo a posição do mouse
                    mouse_pos = pygame.mouse.get_pos()
                    # verificando se clicou em iniciar
                    if iniciar_rect.collidepoint(mouse_pos):
                        return 'iniciar_jogo'
                    # verificando se clicou em sair
                    elif sair_rect.collidepoint(mouse_pos):
                        pygame.quit()
                        tela_inicial()
                key = pygame.key.get_pressed()
                if key[pygame.K_ESCAPE]:
                    #pygame.quit()
                    tela_inicial()
            screen.blit(back_img, (0, 0))

            # denhando os botões na tela
            screen.blit(img_iniciar, (iniciar_x, iniciar_y))
            screen.blit(img_sair, (sair_x, sair_y))
            
            # Renderizando e exibindo a pontuação com contorno
            font = pygame.font.Font(font_path, 20)
            # Renderize o texto com uma sombra escura para simular um contorno
            shadow_text = font.render('copyrights Andre  Gustavo 2024', True, black)
            shadow_rect = shadow_text.get_rect(center=(152, 782))

            # Desenhe o texto sombreado na tela
            screen.blit(shadow_text, shadow_rect)

            # Renderize o texto principal
            score_text = font.render('copyrights Andre  Gustavo 2024', True, white)
            score_rect = score_text.get_rect(center=(150, 780))
            
            # Desenhe o texto principal na tela
            screen.blit(score_text, score_rect)

            pygame.display.update()
#######################################################################################################
#########################################################################################################
    # tela de gameover
    def tela_final():
        
        pygame.mixer.music.stop()

        background_img = pygame.image.load('img/flapimg/gameover.png')
        background_img = pygame.transform.scale(background_img, (864, 936))

        # carregando os botões
        reiniciar = pygame.image.load('img/carregamento/tkr/tkrreiniciar.png')
        menu = pygame.image.load('img/carregamento/tkr/tkrmenu.png')

        # redimensionando os botões
        button_width, button_height = 130, 50
        reiniciar = pygame.transform.scale(reiniciar, (button_width, button_height))
        menu = pygame.transform.scale(menu, (button_width, button_height))
        
        # coordenadas dos botões
        reiniciar_x = 150
        reiniciar_y = 425
        menu_y = 600
        menu_x = 325

        # colisão dos botões
        reiniciar_rect = reiniciar.get_rect(topleft=(reiniciar_x, reiniciar_y))
        menu_rect = menu.get_rect(topleft=(menu_x, menu_y))

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if menu_rect.collidepoint(mouse_pos):
                        jogo_flap()
            #manipuladores de eventos
            
                key = pygame.key.get_pressed()
                if key[pygame.K_ESCAPE]:
                    jogo_flap()
            
            screen.blit(background_img, (0, 0))
            #screen.blit(reiniciar, reiniciar_rect)
            screen.blit(menu, menu_rect)
            

            # Renderizando e exibindo a pontuação com contorno
            font = pygame.font.Font(font_path, 30)

            # Renderize o texto com uma sombra escura para simular um contorno
            shadow_text = font.render('PONTUACAO   ' + str(score), True, black)
            shadow_rect = shadow_text.get_rect(center=(432, 257))

            # Desenhe o texto sombreado na tela
            screen.blit(shadow_text, shadow_rect)

            # Renderize o texto principal
            score_text = font.render('PONTUACAO   ' + str(score), True, red)
            score_rect = score_text.get_rect(center=(430, 255))

            # Desenhe o texto principal na tela
            screen.blit(score_text, score_rect)

            # Renderizando e exibindo a pontuação com contorno
            font = pygame.font.Font(font_path, 30)

            # Renderize o texto com uma sombra escura para simular um contorno
            shadow_text = font.render('MELHOR PONTUACAO   ' + str(high_score), True, black)
            shadow_rect = shadow_text.get_rect(center=(430, 280))

            # Desenhe o texto sombreado na tela
            screen.blit(shadow_text, shadow_rect)

            # Renderize o texto principal
            score_text = font.render('MELHOR PONTUACAO   ' + str(high_score), True, (197, 173, 55))
            score_rect = score_text.get_rect(center=(428, 278))

            # Desenhe o texto principal na tela
            screen.blit(score_text, score_rect)

            pygame.display.update()
####################################################################


#SAIDA DE TEXTO
    def draw_text(text, font, text_col, x, y):
        img = font.render(text, True, text_col)
        screen.blit(img, (x, y))

    def reset_game():
        pipe_group.empty()
        flappy.rect.x = 100
        flappy.rect.y = int(screen_height / 2)
        score = 0
        return score  
#Função Passaro
    class Bird(pygame.sprite.Sprite):

        def __init__(self, x, y):
            pygame.sprite.Sprite.__init__(self)
            self.images = []
            self.index = 0
            self.counter = 0
            for num in range (1, 4):
                img = pygame.image.load(f"img/flapimg/bird{num}.png")
                self.images.append(img)
            self.image = self.images[self.index]
            self.rect = self.image.get_rect()
            self.rect.center = [x, y]
            self.vel = 0
            self.clicked = False
#game começando a rodar  
        def update(self):

            if flying == True:
                #gravidade
                self.vel += 0.5
                if self.vel > 8:
                    self.vel = 8
                if self.rect.bottom < 768:
                    self.rect.y += int(self.vel)
#game over F
            if game_over == False:
                #PULO
                if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                    self.clicked = True
                    self.vel = -10
                if pygame.mouse.get_pressed()[0] == 0:
                    self.clicked = False

                #handle the animation
                flap_cooldown = 5
                self.counter += 1
                
                if self.counter > flap_cooldown:
                    self.counter = 0
                    self.index += 1
                    if self.index >= len(self.images):
                        self.index = 0
                    self.image = self.images[self.index]


                #ROTAÇÃO/lado bird
                self.image = pygame.transform.rotate(self.images[self.index], self.vel * -2)
            else:
                #APOS FAIL, PASSARO NO CHAO
                self.image = pygame.transform.rotate(self.images[self.index], -90)


#funçao dos tubos
    class Pipe(pygame.sprite.Sprite):

        def __init__(self, x, y, position):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.image.load("img/flapimg/pipe.png")
            self.rect = self.image.get_rect()
            #A variavel position determina se o tubo está vindo de baixo ou de cima
#posição 1 é de cima, -1 é de baixo
            if position == 1:
                self.image = pygame.transform.flip(self.image, False, True)
                self.rect.bottomleft = [x, y - int(pipe_gap / 2)]
                #usado para fazer com que o outro tubo reapareça em cima
            elif position == -1:
                self.rect.topleft = [x, y + int(pipe_gap / 2)]


        def update(self):
            self.rect.x -= scroll_speed
            if self.rect.right < 0:
                self.kill()



    class Button():
        def __init__(self, x, y, image):
            self.image = image
            self.rect = self.image.get_rect()
            self.rect.topleft = (x, y)

        def draw(self):
            action = False

            #posição mouse
            pos = pygame.mouse.get_pos()

            #click do mouse
            if self.rect.collidepoint(pos):
                if pygame.mouse.get_pressed()[0] == 1 or K_SPACE:
                    action = True

            #draw button
            screen.blit(self.image, (self.rect.x, self.rect.y))

            return action



    pipe_group = pygame.sprite.Group()
    bird_group = pygame.sprite.Group()
    
    #distancia entre o passaro e o inicio da tela
    flappy = Bird(100, int(screen_height / 2))

    bird_group.add(flappy)

    #botao restart
    button = Button(screen_width // 2 - 50, screen_height // 2 - 100, button_img)

#############################################################################################
#loop infinito do jogo
#REUNE TODOS OS CONJUNTOS DE VARIAVEIS PARA FAZER COM QUE O JOGO SE CRIE  PERFEITAMENE
    tela_carregamento()
    run = True
    while run:

        clock.tick(fps)
        
        #Formando fundo
        screen.blit(bg, (0,0))

        pipe_group.draw(screen)
        bird_group.draw(screen)
        bird_group.update()

        #fazer o fundo e animar
        screen.blit(ground_img, (ground_scroll, 768))

        #mostrar os pontos
        if len(pipe_group) > 0:
            if bird_group.sprites()[0].rect.left > pipe_group.sprites()[0].rect.left\
                and bird_group.sprites()[0].rect.right < pipe_group.sprites()[0].rect.right\
                and pass_pipe == False:
                pass_pipe = True
            if pass_pipe == True:
                if bird_group.sprites()[0].rect.left > pipe_group.sprites()[0].rect.right:
                    score += 1
                    pass_pipe = False
        draw_text(str(score), font, white, int(screen_width / 2), 20)


        #MOSTRAR COLISAO
        if pygame.sprite.groupcollide(bird_group, pipe_group, False, False) or flappy.rect.top < 0:
            game_over = True
        #uma vez que o pássaro atinge o solo, o jogo termina e não voa mais if flappy.rect.bottom >= 768:

        if flappy.rect.bottom >= 768:
            game_over = True
            flying = False


        if flying == True and game_over == False:
            #GERAR NOVOS TUBOS  
            time_now = pygame.time.get_ticks()
            if time_now - last_pipe > pipe_frequency:
                pipe_height = random.randint(-100, 100)
                btm_pipe = Pipe(screen_width, int(screen_height / 2) + pipe_height, -1)
                top_pipe = Pipe(screen_width, int(screen_height / 2) + pipe_height, 1)
                pipe_group.add(btm_pipe)
                pipe_group.add(top_pipe)
                last_pipe = time_now

            pipe_group.update()

            ground_scroll -= scroll_speed
            if abs(ground_scroll) > 35:
                ground_scroll = 0
            #Atualização do Recorde
            if score > high_score:
                high_score = score
                salvar_pontuacao_maxima(high_score)
                with open('txt/scoreflappy.txt', 'w') as file:
                    file.write(str(high_score))
        

        #verificar se houve game over e resetar
        if game_over == True:
            tela_final()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN and flying == False and game_over == False:
                flying = True
            key = pygame.key.get_pressed()
            if key[pygame.K_ESCAPE]:
                #pygame.quit()
                tela_carregamento()
        pygame.display.update()
    
    
############################################################################################################################ 
#Créditos a Lucas Sena para a elaboração de retorno ao menu inicial.

        
def jogo_jump():
    
    mixer.init()
    pygame.init()

    #Dimensões da janela do jogo
    SCREEN_WIDTH = 400
    SCREEN_HEIGHT = 600

    icon = pygame.image.load('img/icons/iconjump.png')
    #Criando janela do jogo
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('JumpFrog')
    pygame.display.set_icon(icon)

    #Carregar músicas e sons
    pygame.mixer.music.load('audio/jump/music.mp3')
    pygame.mixer.music.set_volume(0.2)
    pygame.mixer.music.play(-1, 0.0)
    jump_fx = pygame.mixer.Sound('audio/jump/jump.mp3')
    jump_fx.set_volume(0.5)
    death_fx = pygame.mixer.Sound('audio/jump/death.mp3')
    death_fx.set_volume(0.5)


    #Variavéis do jogo
    SCROLL_THRESH = 200
    GRAVITY = 1
    MAX_PLATFORMS = 10
    scroll = 0
    bg_scroll = 0
    game_over = False
    score = 0
    fade_counter = 0
    scorejump = 0

    if os.path.exists('txt/scorejump.txt'):
        with open('txt/scorejump.txt', 'r') as file:
            high_score = int(file.read())
    else:
        high_score = 0

    # Definição de cores
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    PANEL = (153, 217, 234)

    #Definições de Fonte
    font_small = pygame.font.SysFont('Lucida Sans', 20)
    font_big = pygame.font.SysFont('Lucida Sans', 24)
    
#########################################################################################
    # criando a tela inicial
    def tela_carregamento():

        pygame.mixer.music.stop()
        pygame.mixer.music.play(-1)
        
        # carregando a imagem da tela inicial
        back_img = pygame.image.load('img/carregamento/jumpcarregamento.png')
        back_img = pygame.transform.scale(back_img, (400, 600))


        # carregando as imagens dos botões
        img_iniciar = pygame.image.load('img/carregamento/iniciar.png')
        img_sair = pygame.image.load('img/carregamento/voltar.png')

        # redimensionando os botões
        button_width, button_height = 130, 50
        img_iniciar = pygame.transform.scale(img_iniciar, (button_width, button_height))
        img_sair = pygame.transform.scale(img_sair, (button_width, button_height))

        # definindo as coordenadas dos botões
        iniciar_x = 50
        iniciar_y = 400
        sair_y = 400
        sair_x = 200

        # Definindo os retângulos de colisão dos botões
        iniciar_rect = img_iniciar.get_rect(topleft=(iniciar_x, iniciar_y))
        sair_rect = img_sair.get_rect(topleft=(sair_x, sair_y))

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    tela_inicial()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # obtendo a posição do mouse
                    mouse_pos = pygame.mouse.get_pos()
                    # verificando se clicou em iniciar
                    if iniciar_rect.collidepoint(mouse_pos):
                        
                        return 'iniciar_jogo'
                    # verificando se clicou em sair
                    elif sair_rect.collidepoint(mouse_pos):
                        # pygame.quit()
                        tela_inicial()
                key = pygame.key.get_pressed()
                if key[pygame.K_ESCAPE]:
                    #pygame.quit()
                    tela_inicial()
            screen.blit(back_img, (0, 0))

            # denhando os botões na tela
            screen.blit(img_iniciar, (iniciar_x, iniciar_y))
            screen.blit(img_sair, (sair_x, sair_y))
            
            # Renderizando e exibindo a pontuação com contorno
            font = pygame.font.Font(font_path, 20)
            # Renderize o texto com uma sombra escura para simular um contorno
            shadow_text = font.render('copyrights Igor  Leao 2024', True, black)
            shadow_rect = shadow_text.get_rect(center=(132, 592))

            # Desenhe o texto sombreado na tela
            screen.blit(shadow_text, shadow_rect)

            # Renderize o texto principal
            score_text = font.render('copyrights Igor  Leao 2024', True, white)
            score_rect = score_text.get_rect(center=(130, 590))

            # Desenhe o texto principal na tela
            screen.blit(score_text, score_rect)

            pygame.display.update()
#######################################################################################################

    #Definir Taxa de Quadros
    clock = pygame.time.Clock()
    FPS = 60
    #CÓDIGO ENEMY(inimigos)
    class Enemy(pygame.sprite.Sprite):
        def __init__(self, SCREEN_WIDTH, y, sprite_sheet, scale):
            pygame.sprite.Sprite.__init__(self)
            #define variaveis
            self.animation_list = []
            self.frame_index = 0
            self.update_time = pygame.time.get_ticks()
            self.direction = random.choice([-1, 1])
            if self.direction == 1:
                self.flip = True
            else:
                self.flip = False

            #Carregar imagens da spritesheet
            animation_steps = 8
            for animation in range(animation_steps):
                image = sprite_sheet.get_image(animation, 32, 32, scale, (0, 0, 0))
                image = pygame.transform.flip(image, self.flip, False)
                image.set_colorkey((0, 0, 0))
                self.animation_list.append(image)
            
             #Seleciona a imagem inicial e cria um retângulo a partir dela, isso faz com  que facilite na colisão dos componentes do jogo
            self.image = self.animation_list[self.frame_index]
            self.rect = self.image.get_rect()

            if self.direction == 1:
                self.rect.x = 0
            else:
                self.rect.x = SCREEN_WIDTH
            self.rect.y = y

        def update(self, scroll, SCREEN_WIDTH):
            #Atualização da animação
            ANIMATION_COOLDOWN = 50
            #Atualiza a imagem dependendo do quadro atual
            self.image = self.animation_list[self.frame_index]
            #Verifica se já passou tempo suficiente desde a última atualização
            if pygame.time.get_ticks() - self.update_time > ANIMATION_COOLDOWN:
                self.update_time = pygame.time.get_ticks()
                self.frame_index += 1
            #Se a animação acabar, volta ao inicio
            if self.frame_index >= len(self.animation_list):
                self.frame_index = 0

            #Move os inimigos
            self.rect.x += self.direction * 2
            self.rect.y += scroll

            #Verifica se saiu da tela
            if self.rect.right < 0 or self.rect.left > SCREEN_WIDTH:
                self.kill()

    #CÓDIGO SPRITES
    class SpriteSheet():
        def __init__(self, image):
            self.sheet = image

        def get_image(self, frame, width, height, scale, colour):
            image = pygame.Surface((width, height)).convert_alpha()
            image.blit(self.sheet, (0, 0), ((frame * width), 0, width, height))
            image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
            image.set_colorkey(colour)

            return image
    
    #Carrega imagens
    jumpy_image = pygame.image.load('img/jumpimg/jump.png').convert_alpha()
    bg_image = pygame.image.load('img/jumpimg/bg.png').convert_alpha()
    platform_image = pygame.image.load('img/jumpimg/wood.png').convert_alpha()
    bg_game_over = pygame.image.load('img/jumpimg/gameover.png').convert_alpha()
    bg_game_over = pygame.transform.scale(bg_game_over,(400, 600))
    #Sprite do Passaro
    bird_sheet_img = pygame.image.load('img/jumpimg/bird.png').convert_alpha()
    bird_sheet = SpriteSheet(bird_sheet_img)
    
    #Função para saída de texto na tela
    def draw_text(text, font, text_col, x, y):
        img = font.render(text, True, text_col)
        screen.blit(img, (x, y))

    #Função para desenhar o painel de informações, no caso o placar
    def draw_panel():
        pygame.draw.rect(screen, PANEL, (0, 0, SCREEN_WIDTH, 30))
        pygame.draw.line(screen, WHITE, (0, 30), (SCREEN_WIDTH, 30), 2)
        draw_text(str(score), font_small, RED, 10, 0)
        draw_text('Metros', font_small, RED, 65, 0)

    #Função para desenhar o background do jogo
    def draw_bg(bg_scroll):
        screen.blit(bg_image, (0, 0 + bg_scroll))
        screen.blit(bg_image, (0, -600 + bg_scroll))
        
    def draw_bg_game_over():
        screen.blit(bg_game_over, (0, 0))


    #Classe do Player(jogador)
    class Player():
        def __init__(self, x, y):
            self.image = pygame.transform.scale(jumpy_image, (45, 45))
            self.width = 25
            self.height = 40
            self.rect = pygame.Rect(0, 0, self.width, self.height)
            self.rect.center = (x, y)
            self.vel_y = 0
            self.flip = False

        def move(self):
            #Reseta Variaveis
            scroll = 0
            dx = 0
            dy = 0

            #Processar o precionamento de teclas, entender o comando dado pelas teclas selecionadas no código
            key = pygame.key.get_pressed()
            if key[pygame.K_a] or key[pygame.K_LEFT]:
                dx = -10
                self.flip = True
            if key[pygame.K_d] or key[pygame.K_RIGHT]:
                dx = 10
                self.flip = False

            #Gravidade
            self.vel_y += GRAVITY
            dy += self.vel_y

            #Certifique-se de que o player não saia da borda da tela
            if self.rect.left + dx < 0:
                dx = -self.rect.left
            if self.rect.right + dx > SCREEN_WIDTH:
                dx = SCREEN_WIDTH - self.rect.right


            #Verifica colisão com as plataformas
            for platform in platform_group:
                #Colisão na direção 'Y' (subindo)
                if platform.rect.colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                     #Verifica se o player esta acima da plataforma
                    if self.rect.bottom < platform.rect.centery:
                        if self.vel_y > 0:
                            self.rect.bottom = platform.rect.top
                            dy = 0
                            self.vel_y = -20
                            jump_fx.play()

            #veifica se o jogador saltou para o topo da tela
            if self.rect.top <= SCROLL_THRESH:
                #if player is jumping
                if self.vel_y < 0:
                    scroll = -dy

            #Atualizar posição do retângulo
            self.rect.x += dx
            self.rect.y += dy + scroll

            #Atualiza a máscara
            self.mask = pygame.mask.from_surface(self.image)

            return scroll

        def draw(self):
            screen.blit(pygame.transform.flip(self.image, self.flip, False), (self.rect.x - 12, self.rect.y - 5))

    #Classe das Plataformas
    class Platform(pygame.sprite.Sprite):
        def __init__(self, x, y, width, moving):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.transform.scale(platform_image, (width, 10))
            self.moving = moving
            self.move_counter = random.randint(0, 50)
            self.direction = random.choice([-1, 1])
            self.speed = random.randint(1, 2)
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y

        def update(self, scroll):
            #Mover a plataforma de um lado para o outro se for uma paltaforma móvel
            if self.moving == True:
                self.move_counter += 1
                self.rect.x += self.direction * self.speed

            #Muda a direção da plataforma se ela mover totalmente ou bater no final da tela
            if self.move_counter >= 100 or self.rect.left < 0 or self.rect.right > SCREEN_WIDTH:
                self.direction *= -1
                self.move_counter = 0

            #Atualiza a posição vertical da plataforma
            self.rect.y += scroll

            #Verifica se a platorma saiu da tela
            if self.rect.top > SCREEN_HEIGHT:
                self.kill()

    #Instância do player
    jumpy = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 150)

    #Cria os sprites dos seguintes grupos
    platform_group = pygame.sprite.Group()
    enemy_group = pygame.sprite.Group()

    #Cria a plataforma inicial
    platform = Platform(SCREEN_WIDTH // 2 - 50, SCREEN_HEIGHT - 50, 100, False)
    platform_group.add(platform)
###################################################################################################
    #Loop do jogo
    
    tela_carregamento()
    run = True
    while run:

        clock.tick(FPS)

        if game_over == False:
            scroll = jumpy.move()

            #Desenha o background
            bg_scroll += scroll
            if bg_scroll >= 600:
                bg_scroll = 0
            draw_bg(bg_scroll)

            #Gerando as plataformas
            if len(platform_group) < MAX_PLATFORMS:
                p_w = random.randint(40, 60)
                p_x = random.randint(0, SCREEN_WIDTH - p_w)
                p_y = platform.rect.y - random.randint(80, 120)
                p_type = random.randint(1, 2)
                if p_type == 1 and score > 500:
                    p_moving = True
                else:
                    p_moving = False
                platform = Platform(p_x, p_y, p_w, p_moving)
                platform_group.add(platform)

            #Atualiza as plataformas
            platform_group.update(scroll)

            #Gerando inimigos
            if len(enemy_group) == 0 and score > 1500:
                enemy = Enemy(SCREEN_WIDTH, 100, bird_sheet, 1.5)
                enemy_group.add(enemy)

            #Atualiza os inimigos
            enemy_group.update(scroll, SCREEN_WIDTH)

            #Atualiza a pontuação
            if scroll > 0:
                score += scroll

            #Desenha a linha na pontuação mais alta, onde consta o atual recorde
            pygame.draw.line(screen, RED, (0, score - high_score + SCROLL_THRESH), (SCREEN_WIDTH, score - high_score + SCROLL_THRESH), 3)
            draw_text('RECORDE', font_small, RED, SCREEN_WIDTH - 130, score - high_score + SCROLL_THRESH)

            #Desenha as Sprites
            platform_group.draw(screen)
            enemy_group.draw(screen)
            jumpy.draw()

            #Desenha o painel de placar
            draw_panel()

            #Checa o Game Over
            if jumpy.rect.top > SCREEN_HEIGHT:
                game_over = True
                pygame.mixer.music.stop()
                death_fx.play()
            #Checagem para colisão com os inimigos
            if pygame.sprite.spritecollide(jumpy, enemy_group, False):
                if pygame.sprite.spritecollide(jumpy, enemy_group, False, pygame.sprite.collide_mask):
                    game_over = True
                    death_fx.play()
        else:
            if fade_counter < SCREEN_WIDTH:
                fade_counter += 5
                for y in range(0, 6, 2):
                    pygame.draw.rect(screen, BLACK, (0, y * 100, fade_counter, 100))
                    pygame.draw.rect(screen, BLACK, (SCREEN_WIDTH - fade_counter, (y + 1) * 100, SCREEN_WIDTH, 100))
            else:
                draw_bg_game_over()
                draw_text('VOCÊ SUBIU:  ', font_big, PANEL, 30, 250)
                draw_text('VOCÊ SUBIU:  ', font_big, BLACK, 28, 248)
                if score == 0 or score <= 999:
                    draw_text(str(score), font_big, PANEL, 200, 250)
                    draw_text('METROS', font_big, PANEL, 250, 250)
                    draw_text(str(score), font_big, BLACK, 198, 248)
                    draw_text('METROS', font_big, BLACK, 248, 248)
                if score > 999:
                    draw_text(str(score), font_big, PANEL, 180, 250)
                    draw_text('METROS', font_big, BLACK, 248, 248)
                    
                
                
                if score <= high_score:
                        pontos = high_score
                        if pontos == high_score:	
                            draw_text('RECORDE ATUAL: '+ str(pontos), font_big, RED, 10, 300)
                            draw_text('Metros', font_big, RED, 300, 300)
                            draw_text('TENTE NOVAMENTE', font_big, RED, 80, 350)
                            draw_text('RECORDE ATUAL: '+ str(pontos), font_big, BLACK, 8, 298)
                            draw_text('Metros', font_big, BLACK, 298, 298)
                            draw_text('TENTE NOVAMENTE', font_big, BLACK, 78, 348)
                        if score > high_score:
                            pontos = score
                            draw_text('RECORDE ATUAL: '+ str(pontos), font_big, PANEL, 10, 300)
                            draw_text('Metros', font_big, PANEL, 300, 300)
                            draw_text('PARABÉNS', font_big, PANEL, 90, 350)
                            #
                            draw_text('RECORDE ATUAL: '+ str(pontos), font_big, PANEL, 8, 298)
                            draw_text('Metros', font_big, PANEL, 298, 298)
                            draw_text('PARABÉNS', font_big, PANEL, 88, 348)
                    
                draw_text('Aperte ESPAÇO para jogar novamente', font_small, RED, 20, 500)
                draw_text('Aperte ESC para sair do jogo', font_small, RED, 60, 550)
                draw_text('Aperte ESPAÇO para jogar novamente', font_small, BLACK, 18, 498)
                draw_text('Aperte ESC para sair do jogo', font_small, BLACK, 58, 548)
                
                
                #Atualização do Recorde
                if score > high_score:
                    high_score = score
                    with open('txt/scorejump.txt', 'w') as file:
                        file.write(str(high_score))
                key = pygame.key.get_pressed()
                if key[pygame.K_SPACE] or key[pygame.K_KP_ENTER]:
                    #Reseta Variaveis
                    pygame.mixer.music.play(-1)
                    game_over = False
                    score = 0
                    scroll = 0
                    fade_counter = 0
                    #Reposiciona o player
                    jumpy.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT - 150)
                    #Reseta os inimigos
                    enemy_group.empty()
                    #reseta as plataformas
                    platform_group.empty()
                    #Cria plataforma inicial
                    platform = Platform(SCREEN_WIDTH // 2 - 50, SCREEN_HEIGHT - 50, 100, False)
                    platform_group.add(platform)
                    
                key = pygame.key.get_pressed()
                if key[pygame.K_ESCAPE]:
                    
                    tela_carregamento()
                    
        #Manipulador de eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                #Atualiza o recorde
                if score > high_score:
                    high_score = score
                    with open('txt/scorejump.txt', 'w') as file:
                        file.write(str(high_score))
                run = False

        #Atualiza janela de exibição
        pygame.display.update()

##############################################################################################################################################  
def jogo_breakoup():
    
    pygame.init()

    # Carrega a música
    pygame.mixer.music.load('audio/breakout/breackouttheme.mp3')
    pygame.mixer.music.play(-1) # Reproduz a música continuamente
    pygame.mixer.music.set_volume(0.5)  # Ajusta o volume para metade
    
    screen_width = 600
    screen_height = 600
    
    icon = pygame.image.load('img/icons/iconbreakoup.png')
    
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('Breakout')
    pygame.display.set_icon(icon)
    
    #define fonte
    font = pygame.font.SysFont('Constantia', 30)
    
    # Definição da fonte que será usada para exibir os números nos blocos
    block_font = pygame.font.SysFont('Constantia', 24)
    
    #define colours (definição de cores)
    bg = (234, 218, 184)
    #block colours (bloquear cores)
    block_red = (242, 84, 96)
    block_green = (86, 174, 87)
    block_blue = (69, 177, 232)
    black = (0, 0, 0)
    #paddle colours (cores de plataforma)
    paddle_col = (142, 135, 123)
    paddle_outline = (100, 100, 100)
    #text colour (cor do texto)
    text_col = (78, 81, 139)
    
    #define game variables (definir variáveis do jogo)
    cols = 6
    rows = 6
    clock = pygame.time.Clock()
    fps = 60
    live_ball = False
    #game_over = 0
    score = 0
    check_game_over = 0
    breakhigh_score = 0
    game_over = False
# função para carregar a pontuação máxima
    def carregar_pontuacao_maxima():
        try:
            with open('txt/breakhigh_score.txt', 'r') as file:
                return int(file.read().strip())
        except FileNotFoundError:
            return 0

    # função para salvar a pontuação máxima
    def salvar_pontuacao_maxima(pontuacao):
        with open('txt/break_score.txt', 'w') as file:
            file.write(str(pontuacao))
            
    breakhigh_score = carregar_pontuacao_maxima()
#########################################################################################
    # criando a tela inicial
    def tela_carregamento():

        pygame.mixer.music.stop()
        pygame.mixer.music.play(-1)
        
        # carregando a imagem da tela inicial
        back_img = pygame.image.load('img/carregamento/breakoutcarregamento.png')
        back_img = pygame.transform.scale(back_img, (600, 600))


        # carregando as imagens dos botões
        img_iniciar = pygame.image.load('img/carregamento/iniciar.png')
        img_sair = pygame.image.load('img/carregamento/voltar.png')

        # redimensionando os botões
        button_width, button_height = 130, 50
        img_iniciar = pygame.transform.scale(img_iniciar, (button_width, button_height))
        img_sair = pygame.transform.scale(img_sair, (button_width, button_height))

        # definindo as coordenadas dos botões
        iniciar_x = 150
        iniciar_y = 300
        sair_y = 300
        sair_x = 325

        # Definindo os retângulos de colisão dos botões
        iniciar_rect = img_iniciar.get_rect(topleft=(iniciar_x, iniciar_y))
        sair_rect = img_sair.get_rect(topleft=(sair_x, sair_y))

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    tela_inicial()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # obtendo a posição do mouse
                    mouse_pos = pygame.mouse.get_pos()
                    # verificando se clicou em iniciar
                    if iniciar_rect.collidepoint(mouse_pos):
                        return 'iniciar_jogo'
                    # verificando se clicou em sair
                    elif sair_rect.collidepoint(mouse_pos):
                        pygame.quit()
                        tela_inicial()
                key = pygame.key.get_pressed()
                if key[pygame.K_ESCAPE]:
                    tela_inicial()
            screen.blit(back_img, (0, 0))

            # denhando os botões na tela
            screen.blit(img_iniciar, (iniciar_x, iniciar_y))
            screen.blit(img_sair, (sair_x, sair_y))
            
            # Renderizando e exibindo a pontuação com contorno
            font = pygame.font.Font(font_path, 20)
            # Renderize o texto com uma sombra escura para simular um contorno
            shadow_text = font.render('copyrights Fabio  Augusto 2024', True, black)
            shadow_rect = shadow_text.get_rect(center=(152, 592))

            # Desenhe o texto sombreado na tela
            screen.blit(shadow_text, shadow_rect)

            # Renderize o texto principal
            score_text = font.render('copyrights Fabio  Augusto 2024', True, (65, 105, 225))
            score_rect = score_text.get_rect(center=(150, 590))

            # Desenhe o texto principal na tela
            screen.blit(score_text, score_rect)

            pygame.display.update()
#######################################################################################################

#########################################################################################################
    # tela de gameover
    def tela_final():
        
        pygame.mixer.music.stop()

        background_img = pygame.image.load('img/carregamento/gameover.png')
        background_img = pygame.transform.scale(background_img, (width, height))

        # carregando os botões
        reiniciar = pygame.image.load('img/carregamento/tkr/tkrreiniciar.png')
        menu = pygame.image.load('img/carregamento/tkr/tkrmenu.png')

        # redimensionando os botões
        button_width, button_height = 130, 50
        reiniciar = pygame.transform.scale(reiniciar, (button_width, button_height))
        menu = pygame.transform.scale(menu, (button_width, button_height))
        
        # coordenadas dos botões
        reiniciar_x = 150
        reiniciar_y = 425
        menu_y = 425
        menu_x = 325

        # colisão dos botões
        reiniciar_rect = reiniciar.get_rect(topleft=(reiniciar_x, reiniciar_y))
        menu_rect = menu.get_rect(topleft=(menu_x, menu_y))

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if reiniciar_rect.collidepoint(mouse_pos):
                        # música de quando estiver jogando
                        pygame.mixer.music.set_volume(0.2)
                        pygame.mixer.music.load("audio/breakout/breackouttheme.mp3")
                        pygame.mixer.music.play(-1)
                        return 'reiniciar jogo'
                    elif menu_rect.collidepoint(mouse_pos):
                        return tela_carregamento()
            #manipuladores de eventos
            
                key = pygame.key.get_pressed()
                if key[pygame.K_ESCAPE]:
                    tela_carregamento()
            
            screen.blit(background_img, (0, 0))
            screen.blit(reiniciar, reiniciar_rect)
            screen.blit(menu, menu_rect)
            

            # Renderizando e exibindo a pontuação com contorno
            font = pygame.font.Font(font_path, 30)

            # Renderize o texto com uma sombra escura para simular um contorno
            shadow_text = font.render('PONTUACAO   ' + str(score), True, black)
            shadow_rect = shadow_text.get_rect(center=(width / 2 + 2, 392))

            # Desenhe o texto sombreado na tela
            screen.blit(shadow_text, shadow_rect)

            # Renderize o texto principal
            score_text = font.render('PONTUACAO   ' + str(score), True, red)
            score_rect = score_text.get_rect(center=(width / 2, 390))

            # Desenhe o texto principal na tela
            screen.blit(score_text, score_rect)

            # Renderizando e exibindo a pontuação com contorno
            font = pygame.font.Font(font_path, 30)

            # Renderize o texto com uma sombra escura para simular um contorno
            shadow_text = font.render('MELHOR PONTUACAO   ' + str(breakhigh_score), True, black)
            shadow_rect = shadow_text.get_rect(center=(width / 2 + 2, 412))

            # Desenhe o texto sombreado na tela
            screen.blit(shadow_text, shadow_rect)

            # Renderize o texto principal
            score_text = font.render('MELHOR PONTUACAO   ' + str(breakhigh_score), True, (197, 173, 55))
            score_rect = score_text.get_rect(center=(width / 2, 410))

            # Desenhe o texto principal na tela
            screen.blit(score_text, score_rect)

            pygame.display.update()
########################################################################################################## 
    #function for outputting text onto the screen (função para saída de texto na tela)
    def draw_text(text, font, text_col, x, y):
        img = font.render(text, True, text_col)
        screen.blit(img, (x, y))
    
    #brick wall class (Classe da parede de tijolos)
    class wall():
        def __init__(self):
            self.width = screen_width  // cols
            self.height = 50
    
        def create_wall(self):
            self.blocks = []
            for row in range(rows):
                block_row =[]
                for col in range(cols):
                    block_x = col * self.width
                    block_y = row * self.height
                    rect = pygame.Rect(block_x, block_y, self.width, self.height)
                    if row < 2:
                        strength = 3
                    elif row < 4:
                        strength = 2
                    elif row < 6:
                        strength = 1
                    block_individual = [rect, strength]
                    if strength == 1:
                        number_text = block_font.render("10", True, (255, 255, 255))
                    elif strength == 2:
                        number_text = block_font.render("20", True, (255, 255, 255))
                    elif strength == 3:
                        number_text = block_font.render("30", True, (255, 255, 255))
                    block_individual.append(number_text)
                    block_row.append(block_individual)
                self.blocks.append(block_row)
    
        def draw_wall(self):
            for row in self.blocks:
                for block in row:
                    if block[1] == 3:
                        block_col = block_blue
                    elif block[1] == 2:
                        block_col = block_green
                    elif block[1] == 1:
                        block_col = block_red
                    pygame.draw.rect(screen, block_col, block[0])
                    pygame.draw.rect(screen, bg, (block[0]), 2)
                    number_rect = block[2].get_rect()
                    number_rect.center = (block[0][0] + self.width // 2, block[0][1] + self.height // 2)
                    screen.blit(block[2], number_rect)
    
    #paddle class (classe da plataforma)
    class paddle():
        def __init__(self):
            self.reset()
    
        def move(self, score):
            self.direction = 0
            key = pygame.key.get_pressed()
            if key[pygame.K_LEFT] and self.rect.left > 0:
                self.rect.x -= self.speed
                self.direction = -1
            if key[pygame.K_RIGHT] and self.rect.right < screen_width:
                self.rect.x += self.speed
                self.direction = 1
    
            for row in range(rows):
                for col in range(cols):
                    block_rect = wall.blocks[row][col][0]
                    block_strength = wall.blocks[row][col][1]
                    if self.rect.colliderect(block_rect) and block_strength > 1:
                        wall.blocks[row][col][1] -= 1
                        if wall.blocks[row][col][1] == 0:
                        # global score
                            score += 10
    
            return score
    
        def draw(self):
            pygame.draw.rect(screen, paddle_col, self.rect)
            pygame.draw.rect(screen, paddle_outline, self.rect, 3)
    
        def reset(self):
            self.height = 20
            self.width = int(screen_width / cols)
            self.x = int((screen_width / 2) - (self.width / 2))
            self.y = screen_height - (self.height * 2)
            self.speed = 10
            self.rect = Rect(self.x, self.y, self.width, self.height)
            self.direction = 0
    
    #ball class (classe da bola)
    class game_ball():
        def __init__(self, x, y):
            self.reset(x, y)
    
        def move(self, score):
            collision_thresh = 5
            wall_destroyed = 1
            row_count = 0
            for row in wall.blocks:
                item_count = 0
                for item in row:
                    if self.rect.colliderect(item[0]):
                        score += 10  # Adiciona 10 pontos a cada colisão com um bloco
                        if abs(self.rect.bottom - item[0].top) < collision_thresh and self.speed_y > 0:
                            self.speed_y *= -1
                        if abs(self.rect.top - item[0].bottom) < collision_thresh and self.speed_y < 0:
                            self.speed_y *= -1
                        if abs(self.rect.right - item[0].left) < collision_thresh and self.speed_x > 0:
                            self.speed_x *= -1
                        if abs(self.rect.left - item[0].right) < collision_thresh and self.speed_x < 0:
                            self.speed_x *= -1
                        if wall.blocks[row_count][item_count][1] > 1:
                            wall.blocks[row_count][item_count][1] -= 1
                        else:
                            wall.blocks[row_count][item_count][0] = (0, 0, 0, 0)
                    if wall.blocks[row_count][item_count][0] != (0, 0, 0, 0):
                        wall_destroyed = 0
                    item_count += 1
                row_count += 1
            if wall_destroyed == 1:
                self.game_over = 1
    
            if self.rect.left < 0 or self.rect.right > screen_width:
                self.speed_x *= -1
            if self.rect.top < 0:
                self.speed_y *= -1
            if self.rect.bottom > screen_height:
                self.game_over = -1
            if self.rect.colliderect(player_paddle):
                if abs(self.rect.bottom - player_paddle.rect.top) < collision_thresh and self.speed_y > 0:
                    self.speed_y *= -1
                    self.speed_x += player_paddle.direction
                    if self.speed_x > self.speed_max:
                        self.speed_x = self.speed_max
                    elif self.speed_x < 0 and self.speed_x < -self.speed_max:
                        self.speed_x = -self.speed_max
                else:
                    self.speed_x *= -1        
            self.rect.x += self.speed_x
            self.rect.y += self.speed_y
            return score
    
        def draw(self):
            pygame.draw.circle(screen, paddle_col, (self.rect.x + self.ball_rad, self.rect.y + self.ball_rad), self.ball_rad)
            pygame.draw.circle(screen, paddle_outline, (self.rect.x + self.ball_rad, self.rect.y + self.ball_rad), self.ball_rad, 3)
    
        def reset(self, x, y):
            self.ball_rad = 10
            self.x = x - self.ball_rad
            self.y = y
            self.rect = Rect(self.x, self.y, self.ball_rad * 2, self.ball_rad * 2)
            self.speed_x = 4
            self.speed_y = -4
            self.speed_max = 5
            self.game_over = 0
    
    #create a wall (cria a parede)
    wall = wall()
    wall.create_wall()
    
    #create paddle (criar plataforma)
    player_paddle = paddle()
    
    #create a wall (criar uma parede)
    ball = game_ball(player_paddle.x + (player_paddle.width // 2), player_paddle.y - player_paddle.height)
    
    def check_game_over():
        for row in wall.blocks:
            for block in row:
                if block[0] != (0, 0, 0, 0):
                    return 0  # Retorna 0 se ainda houver blocos na parede
        return 1  # Retorna 1 se todos os blocos foram destruídos e o jogo acabou
    
    #Criando imagem de background para game over
    bg_game_over = pygame.image.load('img/carregamento/gameover.png').convert_alpha()
    bg_game_over = pygame.transform.scale(bg_game_over,(600, 600))
    
 ##################################################################################   
    tela_carregamento()
    run = True
    while run:
        clock.tick(fps)
        screen.fill(bg)
    
        wall.draw_wall()
        player_paddle.draw()
        ball.draw()
    
        
        if live_ball:
            if live_ball:
                score = player_paddle.move(score)
                score = ball.move(score)  # Passando a pontuação como parâmetro
            
            game_over = check_game_over()  # Aqui você pode verificar o término do jogo
            if ball.game_over == -1:  # Verifica se a bola atingiu a parte inferior da tela
                
                tela_final()
                live_ball = False
                pygame.mixer.music.stop()
                
        if not live_ball:
            if game_over == 0:
                draw_text('APERTE ESPAÇO PARA INICIAR', font, text_col, 80, 400)
            
   
            if score > breakhigh_score:
                breakhigh_score = score
                salvar_pontuacao_maxima(breakhigh_score) 

            # Mostrando a tela de fim de jogo
            if game_over:
                tela_final()
                #screen.blit(0, 0)
                
        draw_text(f'Pontuação: {score}', font, text_col, 5, 570)
    
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE or event.key == pygame.K_KP_ENTER:
                        if not live_ball:
                            live_ball = True
                            ball.reset(player_paddle.x + (player_paddle.width // 2), player_paddle.y - player_paddle.height)
                            player_paddle.reset()
                            wall.create_wall()
                            score = 0
                            pygame.mixer.music.play(-1)
                    elif event.key == pygame.K_ESCAPE:
                        #pygame.quit()
                        tela_carregamento()
                
        pygame.display.update()
 
##################################################################################################################################################################  
#Créditos a Vinitrap para habilitar o Score_Space com o novo posicionamento do global
def jogo_space():
    
    global score_space
    pygame.mixer.pre_init(44100, -16, 2, 512)
    mixer.init()
    pygame.init() #inicializa todos os módulos importados do pygame.
    pygame.mixer.music.load('audio/space/themespace.mp3')
    pygame.mixer.music.play(-1) # Reproduz a música continuamente
    pygame.mixer.music.set_volume(0.5)  # Ajusta o volume para metade
    
    icon = pygame.image.load('img/icons/iconspace.png')
    
    #define fps
    clock = pygame.time.Clock() #Cria um objeto `Clock` que será usado para controlar a taxa de quadros (FPS) do jogo. Isso permite que o jogo seja executado a uma velocidade consistente em diferentes sistemas.
    fps = 60 #Define a taxa de quadros desejada para o jogo como 60 FPS (frames por segundo). Isso determina com que frequência a tela será atualizada.
    
    #Essencialmente, esta parte do código configura a janela principal do jogo com uma taxa de quadros desejada e um título apropriado.
    screen_width = 600 #Define as dimensões da janela do jogo como 600 pixels de largura por 800 pixels de altura. Essas dimensões são usadas para determinar o tamanho da área de jogo.
    screen_height = 800
    #Cria a janela do jogo com as dimensões especificadas (`screen_width` e `screen_height`). A função `set_mode()` da biblioteca Pygame cria uma janela com as dimensões fornecidas e retorna um objeto `Surface` que representa a área desenhável da janela.
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('Space Invanders') #Define o título da janela do jogo como 'Space Invaders'. Este título aparecerá na barra de título da janela do jogo.
    pygame.display.set_icon(icon)
    
    
    #define fontes
    font30 = pygame.font.SysFont('Constantia', 30) #`font30`: É o nome da variável que armazenará o objeto de fonte criado. `pygame.font` é o módulo de fontes do Pygame, e `SysFont` é um método desse módulo que cria um objeto de fonte do sistema.
    font40 = pygame.font.SysFont('Constantia', 40) #'Constantia'`: É o nome da fonte a ser usada. `30`: É o tamanho da fonte. `font40`: É outra variável para um segundo objeto de fonte, criado de forma semelhante ao primeiro, mas com um tamanho maior.
    
    score_space = 0
    spacehigh_score = 0
    
    # função para carregar a pontuação máxima
    def carregar_pontuacao_maxima():
        try:
            with open('txt/score_space.txt', 'r') as file:
                return int(file.read().strip())
        except FileNotFoundError:
            return 0

    # função para salvar a pontuação máxima
    def salvar_pontuacao_maxima(pontuacao):
        with open('txt/score_space.txt', 'w') as file:
            file.write(str(pontuacao))
            
    spacehigh_score = carregar_pontuacao_maxima()
    
    
    
    #carregar sons
    
    explosion_fx = pygame.mixer.Sound("audio/space/explosion.wav") # `explosion_fx`: É o nome da variável que armazenará o objeto de som criado. #`pygame.mixer.Sound`: Este método cria um novo objeto de som. #`pygame.mixer` é o módulo do Pygame usado para carregar e reproduzir sons. O método `Sound` é usado para carregar um arquivo de som e criar um objeto de som correspondente. #`"img/explosion.wav"`: É o caminho para o arquivo de som que será carregado. Este arquivo deve estar no formato WAV e localizado na pasta `img`.
    explosion_fx.set_volume(0.25) #`.set_volume(0.25)`: Este método ajusta o volume do som. O volume é especificado como um valor flutuante entre `0.0` (silencioso) e `1.0` (volume máximo). Aqui, o volume é definido para `0.25`, o que significa que o som será reproduzido a 25% do volume máximo.
    
    explosion2_fx = pygame.mixer.Sound("audio/space/explosion2.wav")
    explosion2_fx.set_volume(0.25)
    
    laser_fx = pygame.mixer.Sound("audio/space/laser.wav")
    laser_fx.set_volume(0.25)
    
    
    
    #define variáveis do jogo #Essas variáveis são fundamentais para controlar a lógica e o fluxo do jogo, como a geração de inimigos, o gerenciamento de tiros, e o encerramento do jogo. Elas trabalham juntas para garantir que o jogo progrida de maneira ordenada e para fornecer feedback apropriado ao jogador com base em suas ações e no estado do jogo.
    rows = 5 #rows e cols: Essas variáveis determinam o número de linhas (rows) e colunas (cols) para a formação de alienígenas no jogo. Aqui, ambos são definidos como 5, criando uma grade de alienígenas 5x5.
    cols = 5
    alien_cooldown = 1000 #Define o cooldown (em milissegundos) entre os tiros disparados pelos alienígenas. Neste caso, 1000 milissegundos (ou 1 segundo) é o tempo que deve passar antes que outro alien possa disparar novamente.
    last_alien_shot = pygame.time.get_ticks() #Armazena o momento (em milissegundos) em que o último tiro foi disparado por um alienígena.
    countdown = 3
    last_count = pygame.time.get_ticks() #Semelhante a last_alien_shot, esta variável armazena o momento em que a contagem regressiva foi atualizada pela última vez. É usada para controlar o tempo entre as atualizações da contagem regressiva.
    game_over = 0 #Esta variável controla o estado do jogo. Seu valor determina se o jogo terminou e, em caso afirmativo, se o jogador ganhou ou perdeu. Um valor de 0 significa que o jogo está em andamento, 1 indica que o jogador ganhou, e -1 significa que o jogador perdeu.
    score = 0
    
    check_game_over = 0
    #definir cores
    red = (255, 0, 0) #`red`: Define a cor vermelha com o máximo de vermelho (255) e nenhum verde ou azul (0, 0). O resultado é um vermelho puro e vibrante.
    green = (0, 255, 0) #`green`: Define a cor verde com o máximo de verde (255) e nenhum vermelho ou azul (0, 0). O resultado é um verde puro e vibrante.
    white = (255, 255, 255) #`white`: Define a cor branca com o máximo de vermelho, verde e azul (255, 255, 255). Quando todas as componentes de cor são maximizadas, o resultado é branco.
    
    
    
    #carregar imagem
    bg = pygame.image.load("img/spaceimg/bg.png") #`bg`: Esta é uma variável que armazena a imagem de fundo carregada.  `pygame.image.load`: Este é o método usado para carregar uma imagem do disco. O argumento `"img/bg.png"` especifica o caminho para o arquivo de imagem que será usado como fundo. Esta imagem deve estar localizada na pasta `img` no mesmo diretório que o script Python, e o arquivo deve ser chamado `bg.png`.
    
    def draw_bg(): #Define uma função chamada `draw_bg`. Esta função, quando chamada, executa o bloco de código indentado abaixo dela.
        screen.blit(bg, (0, 0)) #`screen.blit(bg, (0, 0))`: Este é o comando que efetivamente desenha a imagem de fundo na tela. #`screen`: Este é o objeto de tela onde a imagem será desenhada. Ele é criado anteriormente no código com uma chamada a `pygame.display.set_mode()`, que define a dimensão da janela do jogo. `.blit`: É um método que "cola" uma superfície sobre outra. Neste caso, ele está colando a imagem de fundo (`bg`) na superfície da tela (`screen`). #`bg`: A superfície (neste caso, a imagem de fundo) a ser colada. #`(0, 0)`: A posição na tela onde o canto superior esquerdo da imagem de fundo será colocado. Neste caso, a imagem será colocada no canto superior esquerdo da tela.
    
    
    #define função para criar texto
    def draw_text(text, font, text_col, x, y): #`def`: Palavra-chave usada para definir uma função em Python. #`draw_text`: Nome da função. Este nome é usado para chamar a função em outras partes do código. #`(text, font, text_col, x, y)`: Lista de parâmetros que a função requer para executar. Esses parâmetros incluem: - `text`: O texto que será renderizado. #`font`: A fonte usada para renderizar o texto. - `text_col`: A cor do texto, especificada como uma tupla RGB (por exemplo, `(255, 255, 255)` para branco). #`x`, `y`:As coordenadas na tela onde o texto será posicionado, com `x` representando a posição horizontal e `y` a posição vertical.
        img = font.render(text, True, text_col) #`font.render`: Método para renderizar o texto. `font` é o objeto de fonte passado para a função, e `render` é o método usado para criar uma imagem do texto. #`text`: O texto a ser renderizado. #`True`: Ativa o anti-aliasing do texto, o que suaviza as bordas das letras para uma aparência mais polida. #`text_col`: A cor do texto. #`img`: A imagem renderizada do texto é armazenada na variável `img`.
        screen.blit(img, (x, y)) # `screen.blit`: Método usado para desenhar uma superfície (neste caso, o texto renderizado) em outra superfície (a tela do jogo). #`img`: A superfície do texto renderizado que será desenhada. #`(x, y)`: As coordenadas onde o texto será desenhado na tela. `x` e `y` definem a posição do canto superior esquerdo da imagem do texto. Usando esta função, é possível adicionar texto ao jogo em diferentes posições, cores e fontes, o que é útil para mostrar informações ao jogador, como pontuações, mensagens de estado do jogo, e instruções.
    

######################## Definição da função tela_inicial() ##########################################

#########################################################################################
    # criando a tela inicial
    def tela_carregamento():

        pygame.mixer.music.stop()
        pygame.mixer.music.play(-1)
        
        # carregando a imagem da tela inicial
        back_img = pygame.image.load('img/carregamento/spacecarregamento.png')
        back_img = pygame.transform.scale(back_img, (600, 800))


        # carregando as imagens dos botões
        img_iniciar = pygame.image.load('img/carregamento/start.png')
        img_sair = pygame.image.load('img/carregamento/exit.png')

        # redimensionando os botões
        button_width, button_height = 130, 50
        img_iniciar = pygame.transform.scale(img_iniciar, (button_width, button_height))
        img_sair = pygame.transform.scale(img_sair, (button_width, button_height))

        # definindo as coordenadas dos botões
        iniciar_x = 150
        iniciar_y = 600
        sair_y = 600
        sair_x = 325

        # Definindo os retângulos de colisão dos botões
        iniciar_rect = img_iniciar.get_rect(topleft=(iniciar_x, iniciar_y))
        sair_rect = img_sair.get_rect(topleft=(sair_x, sair_y))

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    tela_inicial()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # obtendo a posição do mouse
                    mouse_pos = pygame.mouse.get_pos()
                    # verificando se clicou em iniciar
                    if iniciar_rect.collidepoint(mouse_pos):
                        return 'iniciar_jogo'
                    # verificando se clicou em sair
                    elif sair_rect.collidepoint(mouse_pos):
                        pygame.quit()
                        tela_inicial()
                key = pygame.key.get_pressed()
                if key[pygame.K_ESCAPE]:
                    tela_inicial()
            screen.blit(back_img, (0, 0))

            # denhando os botões na tela
            screen.blit(img_iniciar, (iniciar_x, iniciar_y))
            screen.blit(img_sair, (sair_x, sair_y))
            
            # Renderizando e exibindo a pontuação com contorno
            font = pygame.font.Font(font_path, 20)
            # Renderize o texto com uma sombra escura para simular um contorno
            shadow_text = font.render('copyrights Erik  Daniel 2024', True, black)
            shadow_rect = shadow_text.get_rect(center=(152, 772))

            # Desenhe o texto sombreado na tela
            screen.blit(shadow_text, shadow_rect)

            # Renderize o texto principal
            score_text = font.render('copyrights Erik  Daniel 2024', True, green)
            score_rect = score_text.get_rect(center=(150, 770))

            # Desenhe o texto principal na tela
            screen.blit(score_text, score_rect)

            pygame.display.update()
#######################################################################################################

#########################################################################################################
    # tela de gameover
    def tela_final():
        
        pygame.mixer.music.stop()

        background_img = pygame.image.load('img/spaceimg/gameover.png')
        background_img = pygame.transform.scale(background_img, (600, 800))

        # carregando os botões
       
        exit = pygame.image.load('img/carregamento/tkr/tkrmenu.png')

        # redimensionando os botões
        button_width, button_height = 130, 50
        exit = pygame.transform.scale(exit, (button_width, button_height))
        
        # coordenadas dos botões
        
        exit_y = 600
        exit_x = 250

        # colisão dos botões
       
        exit_rect = exit.get_rect(topleft=(exit_x, exit_y))

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()                     
                        
                    if exit_rect.collidepoint(mouse_pos):                
                        jogo_space()
            #manipuladores de eventos
            
                key = pygame.key.get_pressed()
                if key[pygame.K_ESCAPE]:
                    jogo_space()
            
            screen.blit(background_img, (0, 0))
            screen.blit(exit, exit_rect)
            

            # Renderizando e exibindo a pontuação com contorno
            font = pygame.font.Font(font_path, 30)

            # Renderize o texto com uma sombra escura para simular um contorno
            shadow_text = font.render('PONTUACAO   ' + str(score_space), True, black)
            shadow_rect = shadow_text.get_rect(center=(width / 2 + 2, 392))

            # Desenhe o texto sombreado na tela
            screen.blit(shadow_text, shadow_rect)

            # Renderize o texto principal
            score_text = font.render('PONTUACAO   ' + str(score_space), True, red)
            score_rect = score_text.get_rect(center=(width / 2, 390))

            # Desenhe o texto principal na tela
            screen.blit(score_text, score_rect)

            # Renderizando e exibindo a pontuação com contorno
            font = pygame.font.Font(font_path, 30)

            # Renderize o texto com uma sombra escura para simular um contorno
            shadow_text = font.render('MELHOR PONTUACAO   ' + str(spacehigh_score), True, black)
            shadow_rect = shadow_text.get_rect(center=(width / 2 + 2, 412))

            # Desenhe o texto sombreado na tela
            screen.blit(shadow_text, shadow_rect)

            # Renderize o texto principal
            score_text = font.render('MELHOR PONTUACAO   ' + str(spacehigh_score), True, (197, 173, 55))
            score_rect = score_text.get_rect(center=(width / 2, 410))

            # Desenhe o texto principal na tela
            screen.blit(score_text, score_rect)

            pygame.display.update()
########################################################################################################## 

    #Esta seção de código define uma classe chamada `Spaceship`, que representa a nave espacial do jogador no jogo. A classe herda de `pygame.sprite.Sprite`, que é uma classe base em Pygame usada para representar tudo o que pode ser desenhado em um jogo (como personagens, inimigos, etc.).
    #criar classe de nave espacial
    class Spaceship(pygame.sprite.Sprite): #`class Spaceship`: Define uma nova classe chamada `Spaceship`. #`pygame.sprite.Sprite`, permitindo que ela use funcionalidades definidas na classe Sprite de Pygame.
        def __init__(self, x, y, health): #`def __init__`: É o construtor da classe. Este método especial é chamado automaticamente quando um novo objeto `Spaceship` é criado. #`(self, x, y, health)`: `self` refere-se à instância da classe; `x` e `y` são as coordenadas iniciais da nave espacial na tela; `health` é a saúde inicial da nave.
            pygame.sprite.Sprite.__init__(self) #Esta linha é necessária para inicializar corretamente a parte da superclasse (`pygame.sprite.Sprite`) do objeto. Isso garante que a nave espacial se comporte como um Sprite do Pygame, incluindo funcionalidades como agrupamento com outros Sprites e detecção de colisões.
            self.image = pygame.image.load("img/spaceimg/spaceship.png") #######`self.image`: Este atributo armazena a imagem da nave espacial. #`pygame.image.load` é usado para carregar a imagem do disco. #
            self.rect = self.image.get_rect() # `self.rect`: Este atributo armazena um retângulo (`pygame.Rect`) que representa a posição e tamanho da nave espacial na tela. #`get_rect()` é um método que cria um novo retângulo com o tamanho da imagem.
            self.rect.center = [x, y] # `self.rect.center = [x, y]`: Define o centro do retângulo (e, portanto, da nave espacial) nas coordenadas `x` e `y` fornecidas. Isso posiciona a nave espacial na tela.
            self.health_start = health #```python self.health_start = health e self.health_remaining = health ``` #Estas linhas inicializam a saúde da nave. `health_start` armazena a saúde inicial da nave espacial para referência, e `health_remaining` armazena a saúde atual, que pode diminuir ao longo do jogo.
            self.health_remaining = health
            self.last_shot = pygame.time.get_ticks() #`self.last_shot`: Armazena o tempo (em milissegundos desde a inicialização do Pygame) quando a nave espacial disparou pela última vez. Isso é usado para controlar o intervalo entre os disparos. Essa classe fornece a base para criar e manipular a nave espacial do jogador no jogo, incluindo renderização, posicionamento e gestão de saúde.
    
    
        def update(self):
            #definir velocidade de movimento
            speed = 8 #`speed`: Esta variável define a velocidade de movimento da nave espacial. O valor `8` indica a quantidade de pixels que a nave se move a cada atualização. Um valor maior resultaria em uma nave mais rápida, enquanto um valor menor a faria mover-se mais devagar.
            #definir uma variável de resfriamento
            cooldown = 500 #milissegundos #`cooldown`: Define um intervalo de tempo (em milissegundos) que deve passar antes que a nave espacial possa disparar novamente. Este mecanismo previne que a nave dispare de maneira contínua, adicionando um elemento estratégico ao jogo. Neste caso, o jogador deve esperar 500 milissegundos entre cada disparo.
            game_over = 0 #`game_over`: Esta linha inicializa uma variável local chamada `game_over` com o valor `0`. Dentro deste contexto específico, a variável parece ser usada para indicar o estado do jogo (embora seu uso não seja completamente claro apenas com este trecho de código). Tipicamente, `game_over` pode ser usado para determinar se o jogo acabou, onde `0` pode indicar que o jogo está em andamento, `1` que o jogador ganhou, e `-1` que o jogador perdeu. No entanto, sem ver o restante do método `update`, não está claro como essa variável é usada posteriormente. Este método `update` provavelmente contém mais lógica relacionada ao movimento da nave espacial baseado nas entradas do usuário (como pressionar teclas para mover para esquerda ou direita e disparar), além de verificar colisões ou outras condições que podem alterar o estado de `game_over`. A combinação destes elementos permite que a nave espacial responda a interações do jogador e mude de acordo com o estado do jogo.
    
    
            #get pressionamento de tecla
            key = pygame.key.get_pressed() #`pygame.key.get_pressed()`: Este método retorna um dicionário que mapeia cada tecla para um estado booleano, indicando se a tecla está atualmente pressionada (`True`) ou não (`False`). O objeto `key` armazena o estado de todas as teclas.
            if key[pygame.K_LEFT] and self.rect.left > 0: #`if key[pygame.K_LEFT]`: Verifica se a tecla esquerda (`K_LEFT`) está pressionada. #`and self.rect.left > 0`: Garante que a nave não se mova para fora da tela pelo lado esquerdo. `self.rect.left > 0` verifica se a borda esquerda da nave (`self.rect.left`) ainda está dentro da área visível da tela (`> 0`).
                self.rect.x -= speed #`self.rect.x -= speed`: Se ambas as condições forem verdadeiras, a posição `x` da nave é decrementada pela `speed` definida anteriormente, movendo a nave para a esquerda.
            if key[pygame.K_RIGHT] and self.rect.right < screen_width: #`if key[pygame.K_RIGHT]`: Verifica se a tecla direita (`K_RIGHT`) está pressionada.
                self.rect.x += speed #`self.rect.x -= speed`: Se ambas as condições forem verdadeiras, a posição `x` da nave é decrementada pela `speed` definida anteriormente, movendo a nave para a esquerda.
    
            #gravar hora atual
            time_now = pygame.time.get_ticks() #`time_now`: A variável `time_now` armazena o valor retornado por `pygame.time.get_ticks()`, representando o momento atual em milissegundos. #`pygame.time.get_ticks()`: Retorna o número de milissegundos desde que o pygame foi inicializado. Esta função é muito útil para medir o tempo decorrido e controlar eventos baseados em tempo no jogo.
            #atirar
            if key[pygame.K_SPACE] and time_now - self.last_shot > cooldown: #`if key[pygame.K_RIGHT]`: Verifica se a tecla direita (`K_RIGHT`) está pressionada. #`time_now - self.last_shot > cooldown`: Calcula a diferença de tempo entre o momento atual (`time_now`, obtido por `pygame.time.get_ticks()`) e o momento do último disparo (`self.last_shot`). Se essa diferença for maior que o período de cooldown especificado, significa que o jogador pode disparar novamente.
                laser_fx.play() #`laser_fx.play()`: Reproduz o efeito sonoro de disparo (`laser_fx`), que foi previamente carregado. Isso adiciona feedback auditivo ao ato de disparar, aumentando a imersividade do jogo.
                bullet = Bullets(self.rect.centerx, self.rect.top) #`Bullets(self.rect.centerx, self.rect.top)`: Cria uma nova instância da classe `Bullets`, usando a posição central no eixo x (`centerx`) da nave espacial e a posição superior (`top`) como ponto de origem do projétil. Isso assegura que o projétil seja disparado da posição correta da nave.
                bullet_group.add(bullet) #bullet_group.add(bullet)`: Adiciona o novo projétil ao grupo `bullet_group`. Em Pygame, os grupos de sprites são usados para organizar e gerenciar múltiplos objetos de forma eficiente, permitindo realizar operações como desenhar todos os sprites do grupo ou detectar colisões de forma coletiva.
                self.last_shot = time_now #Após um disparo ser realizado, o momento do último disparo (`self.last_shot`) é atualizado para o momento atual (`time_now`). Isso garante que o intervalo de cooldown seja respeitado antes que o próximo disparo possa ser feito. Essa lógica permite que o jogador controle a nave espacial e dispare projéteis ao pressionar a tecla de espaço, com um intervalo mínimo entre os disparos, tornando o jogo mais desafiador e estratégico.
    
    
            #atualizar máscara
            self.mask = pygame.mask.from_surface(self.image) #`self.mask`: Este atributo armazena a máscara de colisão criada para o objeto. #`pygame.mask.from_surface`: Este método cria uma nova máscara de colisão a partir de uma superfície Pygame. A máscara de colisão é essencialmente uma grade de pontos booleanos que representam os pixels da superfície: `True` para pixels opacos e `False` para pixels transparentes. #`self.image`: É a superfície Pygame (neste caso, a imagem da nave espacial) a partir da qual a máscara é criada.
    
    
            #Desenhar barra de saúde
            pygame.draw.rect(screen, red, (self.rect.x, (self.rect.bottom + 10), self.rect.width, 15)) #Esta linha desenha um retângulo vermelho na tela, que serve como a barra de saúde de fundo da nave espacial. O retângulo é posicionado logo abaixo da nave (`self.rect.bottom + 10`), com a mesma largura que a nave (`self.rect.width`) e uma altura de 15 pixels.
            if self.health_remaining > 0: #Se a nave ainda tiver saúde (`self.health_remaining > 0`), um retângulo verde é desenhado sobre o retângulo vermelho. A largura deste retângulo verde é proporcional à saúde restante da nave, calculada como uma fração da saúde inicial (`self.health_remaining / self.health_start`) vezes a largura total da barra.
                pygame.draw.rect(screen, green, (self.rect.x, (self.rect.bottom + 10), int(self.rect.width * (self.health_remaining / self.health_start)), 15))
            elif self.health_remaining <= 0:
                explosion = Explosion(self.rect.centerx, self.rect.centery, 3)
                explosion_group.add(explosion)
                self.kill()
                game_over = -1
            return game_over
    
      
    #create Classe de marcadores
    class Bullets(pygame.sprite.Sprite):
        def __init__(self, x, y):
            pygame.sprite.Sprite.__init__(self) #Chama o construtor da classe base `Sprite` para realizar a inicialização necessária.
            self.image = pygame.image.load("img/spaceimg/bullet.png") #self.image`: Carrega a imagem que representa o projétil. Assume-se que há um arquivo chamado `bullet.png` na pasta `img`.
            self.rect = self.image.get_rect() #`self.rect`: Obtém um retângulo que envolve a imagem. Esse retângulo é usado para posicionamento, detecção de colisão e outras operações relacionadas ao sprite.
            self.rect.center = [x, y] #`self.rect.center = [x, y]`: Define a posição inicial do projétil. Os parâmetros `x` e `y` são passados para o construtor e determinam onde o projétil aparecerá na tela quando for criado.
    
        def update(self, score_a):
            global score_space  # Adiciona esta linha
            self.rect.y -= 5 #Move o projétil para cima na tela. Cada chamada ao método `update` diminui a posição `y` do retângulo em 5 pixels, fazendo com que o projétil se mova verticalmente.
            if self.rect.bottom < 0: #Verifica se o projétil saiu da tela. Se a parte inferior (`bottom`) do retângulo for menor que 0 (ou seja, o projétil saiu da parte superior da tela), o projétil é removido.
                self.kill() #Remove o projétil do(s) grupo(s) de sprites ao qual pertence, efetivamente "deletando-o" do jogo.
            if pygame.sprite.spritecollide(self, alien_group, True): #Verifica se houve colisão entre o projétil e qualquer um dos alienígenas (`alien_group`). O parâmetro `True` indica que os alienígenas atingidos devem ser removidos (destruídos).
                ############ ACRECENTANDO 1 PONTO A CADA COLISSÃO ENTRE O TIRO E A NAVE #############
                score_space += 1
                self.kill()
                explosion_fx.play() #Reproduz um efeito sonoro de explosão quando um alienígena é atingido.
                explosion = Explosion(self.rect.centerx, self.rect.centery, 2) # Cria uma nova explosão na posição onde o projétil atingiu o alienígena.
                explosion_group.add(explosion) #Adiciona a nova explosão ao grupo de sprites de explosões para que seja renderizada.
    #Essa classe permite criar e gerenciar os projéteis disparados pela nave do jogador, incluindo movê-los na tela, detectar colisões com inimigos e tratar as consequências dessas colisões, como destruir o inimigo e criar uma animação de explosão.
    
            
    
    #criar aula de Alienígenas
    class Aliens(pygame.sprite.Sprite):
        def __init__(self, x, y): #Define o construtor com parâmetros `x` e `y`, que são as coordenadas iniciais do alienígena na tela.
            pygame.sprite.Sprite.__init__(self) #Chama o construtor da classe base `Sprite` para realizar a inicialização necessária.
            self.image = pygame.image.load("img/spaceimg/alien" + str(random.randint(1, 5)) + ".png") #Carrega uma imagem aleatória para o alienígena, escolhendo aleatoriamente entre imagens nomeadas `alien1.png` a `alien5.png` na pasta `img`. Isso adiciona variedade visual aos inimigos.
            self.rect = self.image.get_rect() #Obtém um retângulo que envolve a imagem carregada. Este retângulo é usado para posicionamento e detecção de colisão.
            self.rect.center = [x, y] #Define a posição inicial do alienígena com base nos parâmetros `x` e `y`.
            self.move_counter = 0 #Inicializa um contador usado para controlar o movimento do alienígena.
            self.move_direction = 1 ##Define a direção inicial do movimento do alienígena. `1` indica movimento para a direita; `-1` indicaria movimento para a esquerda.
    
        def update(self): #Define o método que atualiza o estado do alienígena a cada frame do jogo.
            self.rect.x += self.move_direction #Move o alienígena horizontalmente na direção especificada por `self.move_direction`
            self.move_counter += 1 #Incrementa o contador de movimento.
            if abs(self.move_counter) > 75: #Verifica se o contador de movimento excedeu o valor `75`, indicando que é hora de mudar de direção.
                self.move_direction *= -1 #Inverte a direção do movimento multiplicando `self.move_direction` por `-1`.
                self.move_counter *= self.move_direction #Ajusta o `move_counter` para continuar a contagem na nova direção. Esta linha parece ter um comportamento um pouco inusual ao multiplicar o contador pela direção, o que pode não ser o comportamento esperado para simplesmente inverter a direção do movimento. Tipicamente, você poderia reiniciar `self.move_counter` para `0` ou um valor fixo na direção oposta para manter o controle consistente.
    
    
    
    #criar classe Alien Bullets
    class Alien_Bullets(pygame.sprite.Sprite):
        def __init__(self, x, y): #Este método inicializa um novo projétil alienígena. `x` e `y` são as coordenadas iniciais do projétil.
            pygame.sprite.Sprite.__init__(self) #Chama o construtor da classe base `Sprite` para realizar a inicialização necessária.
            self.image = pygame.image.load("img/spaceimg/alien_bullet.png") #Carrega a imagem que será usada para o projétil alienígena. Assume-se que existe um arquivo chamado `alien_bullet.png` na pasta `img`.
            self.rect = self.image.get_rect() #Cria um retângulo ao redor da imagem do projétil. Este retângulo é usado para posicionamento, detecção de colisão, e outras operações relacionadas ao sprite.
            self.rect.center = [x, y] #Posiciona o centro do retângulo (e, portanto, da imagem do projétil) nas coordenadas fornecidas (`x`, `y`).
    
        def update(self): #Este método é chamado a cada frame do jogo para atualizar o estado do projétil.
            self.rect.y += 2 #Move o projétil para baixo aumentando a posição `y` do retângulo em 2 pixels. Isso simula o projétil sendo disparado para baixo em direção à nave do jogador.
            if self.rect.top > screen_height: #Verifica se o projétil saiu da tela (ou seja, se a parte superior do retângulo é maior que a altura da tela). Se sim, o projétil é removido do jogo usando `self.kill()`.
                self.kill()
            if pygame.sprite.spritecollide(self, spaceship_group, False, pygame.sprite.collide_mask): #Verifica colisões entre o projétil e a nave do jogador (`spaceship_group`). `pygame.sprite.collide_mask` permite detecção de colisão pixel-perfect, se ambos os sprites (projétil e nave) tiverem uma "máscara" definida. Se houver uma colisão, o seguinte acontece:
                self.kill() #Remove o projétil do jogo
                explosion2_fx.play() #Reproduz um efeito sonoro de explosão.
                #reduzir a saúde da nave espacial
                spaceship.health_remaining -= 1 #Cria uma nova instância de `Explosion` na posição do impacto.
                explosion = Explosion(self.rect.centerx, self.rect.centery, 1) #Cria uma nova instância de `Explosion` na posição do impacto.
                explosion_group.add(explosion) #Adiciona a nova explosão ao grupo de sprites para que seja renderizada.
                #Essa classe implementa a lógica para criar, mover e gerenciar as colisões dos projéteis alienígenas, incluindo a remoção da nave do jogador quando atingida e a criação de efeitos visuais e sonoros para simular a explosão resultante do impacto.
    
    
    
    #cria classe Explosão
    class Explosion(pygame.sprite.Sprite):
        def __init__(self, x, y, size): #Este método inicializa uma nova instância de `Explosion` com uma localização (`x`, `y`) e um tamanho (`size`). A localização determina onde a explosão aparecerá na tela, e o tamanho afeta as dimensões da animação da explosão.
            pygame.sprite.Sprite.__init__(self) #Chama o construtor da classe base para realizar inicializações necessárias para que o objeto se comporte como um sprite.
            self.images = [] #Inicia uma lista vazia que armazenará as imagens usadas para animar a explosão.
            for num in range(1, 6): #Um loop que carrega 5 imagens de explosão (assumindo que os arquivos são nomeados `exp1.png` a `exp5.png`) para a lista `self.images`.
                img = pygame.image.load(f"img/spaceimg/exp{num}.png") #Carrega uma imagem de explosão.
                if size == 1:
                    img = pygame.transform.scale(img, (20, 20)) ###Escala a imagem para o tamanho especificado, baseado no parâmetro `size` passado para o construtor. Isso permite que a explosão seja exibida em diferentes escalas, dependendo da necessidade (por exemplo, uma explosão pequena para projéteis, média para naves alienígenas, ou grande para a nave do jogador).
                if size == 2:
                    img = pygame.transform.scale(img, (40, 40))
                if size == 3:
                    img = pygame.transform.scale(img, (160, 160))
                #adicione a imagem à lista
                self.images.append(img) #Adiciona a imagem escalada à lista `self.images`
            self.index = 0 #Inicializa o índice da imagem atual na animação da explosão.
            self.image = self.images[self.index] #Define a imagem atual da explosão como a primeira imagem na lista `self.images`.
            self.rect = self.image.get_rect() #Cria um retângulo ao redor da imagem atual. Esse retângulo é usado para posicionamento e detecção de colisão.
            self.rect.center = [x, y] #Posiciona o centro do retângulo (e, portanto, da explosão) nas coordenadas fornecidas.
            self.counter = 0 #Posiciona o centro do retângulo (e, portanto, da explosão) nas coordenadas fornecidas.
            #A classe `Explosion` permite criar uma animação de explosão no jogo, alterando a imagem da explosão ao longo do tempo para criar um efeito visual dinâmico. Isso é tipicamente usado para melhorar a resposta visual quando objetos são destruídos ou danificados.
    
        def update(self):
            explosion_speed = 3
            #atualizar animação de explosão
            self.counter += 1
    
            if self.counter >= explosion_speed and self.index < len(self.images) - 1:
                self.counter = 0
                self.index += 1
                self.image = self.images[self.index]
    
            #se a animação estiver completa, exclua a explosão
            if self.index >= len(self.images) - 1 and self.counter >= explosion_speed:
                self.kill()
    
    
    
    
    #criar grupos de sprites
    spaceship_group = pygame.sprite.Group()
    bullet_group = pygame.sprite.Group()
    alien_group = pygame.sprite.Group()
    alien_bullet_group = pygame.sprite.Group()
    explosion_group = pygame.sprite.Group()
    
    
    def create_aliens():
        #gerar alienígenas
        for row in range(rows):
            for item in range(cols):
                alien = Aliens(100 + item * 100, 100 + row * 70)
                alien_group.add(alien)
    
    create_aliens()
    
    #Criando imagem de background para game over
    bg_game_over = pygame.image.load('img/spaceimg/gameover.png').convert_alpha()
    bg_game_over = pygame.transform.scale(bg_game_over,(600, 800))
    
    #criar jogador
    spaceship = Spaceship(int(screen_width / 2), screen_height - 100, 3)
    spaceship_group.add(spaceship)
    
    ################# DECLARANDO O VALOR INICIAL A VARIAVEL SCORE #####################
    #score_space = 0

    # Chamada da tela de inicialização antes do loop do jogo
    tela_carregamento()

    ################# INICIO DO LOOP ###############
    run = True
    while run:
    
        clock.tick(fps)
    
        #desenhar fundo
        draw_bg()

    
    ################## MOSTRANDO PONTUAÇÃO ##################
    
        font = pygame.font.Font(pygame.font.get_default_font(), 16)
        text = font.render('Pontuação: ' + str(score_space), True, white)
        text_rect = text.get_rect()
        text_rect.center = (510, 40)
        screen.blit(text, text_rect)
    
        if countdown == 0:
            #criar balas alienígenas aleatórias
            #gravar hora atual
            time_now = pygame.time.get_ticks()
            #atirar
            if time_now - last_alien_shot > alien_cooldown and len(alien_bullet_group) < 5 and len(alien_group) > 0:
                attacking_alien = random.choice(alien_group.sprites())
                alien_bullet = Alien_Bullets(attacking_alien.rect.centerx, attacking_alien.rect.bottom)
                alien_bullet_group.add(alien_bullet)
                last_alien_shot = time_now
    
            #verifique se todos os alienígenas foram mortos
            if len(alien_group) == 0:
                game_over = 1
    
            if game_over == 0:
                #atualizar nave espacial
                game_over = spaceship.update()
                
                #atualizar grupos de sprites
                bullet_group.update(score_space)
                alien_group.update()
                alien_bullet_group.update()
                
                
            else:
                if game_over == -1:
                   tela_final()
                if game_over == 1:
                    draw_text('YOU WIN!', font40, white, int(screen_width / 2 - 100), int(screen_height / 2 + 50))
            
        if countdown > 0:
            draw_text('GET READY!', font40, white, int(screen_width / 2 - 110), int(screen_height / 2 + 50))
            draw_text(str(countdown), font40, white, int(screen_width / 2 - 10), int(screen_height / 2 + 100))
            count_timer = pygame.time.get_ticks()
            if count_timer - last_count > 1000:
                countdown -= 1
                last_count = count_timer
    
    
        #atualizar grupo de explosão    
        explosion_group.update()         
    
        #desenha grupos de sprites
        spaceship_group.draw(screen)
        bullet_group.draw(screen)
        alien_group.draw(screen)
        alien_bullet_group.draw(screen)
        explosion_group.draw(screen)
    
        if score_space > spacehigh_score:
            spacehigh_score = score_space
            salvar_pontuacao_maxima(spacehigh_score)
                    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE or event.key == pygame.K_KP_ENTER:
                    if explosion_group.update():
                        score_space = 0
                        pygame.mixer.music.play(-1)
        key = pygame.key.get_pressed()
        if key[pygame.K_ESCAPE]:
            tela_carregamento()   
    
        pygame.display.update()
    
################################################################################################################################################          
def jogo_tkr():

    pygame.init()

    font_path = 'txt/pixel.ttf'

    # Definindo a largura e altura da tela do jogo
    width = 800
    height = 800

    icon = pygame.image.load('img/carregamento/tkr/tkrinicial.png')

    # Criando a janela
    screen_size = (width, height)
    pygame.display.set_icon(icon)
    screen = pygame.display.set_mode(screen_size)
    pygame.display.set_caption('The Kanjo Racing')

    # declarando as cores do jogo
    black = (0, 0, 0)
    green = (33, 94, 33)
    red = (200, 0, 0)
    white = (255, 255, 255)
    yellow = (217, 217, 25)
    blue = (20, 20, 200)
    gray = (50,50,50)

    # cofigurações do jogo
    speed = 2
    score = 0
    gameover = False
    gameover_time = 0

    # marcando a pista
    marker_width = 10
    marker_height = 50

    # marcação da rua e pistas
    road = (100, 0, 300, height)
    left_edge_marker = (95, 0, marker_width, height)
    right_edge_marker = (395, 0, marker_width, height)

    # coordenadas das pistas
    left_lane = 150
    center_lane = 250
    right_lane = 350
    lanes = [left_lane, center_lane, right_lane]

    # função para carregar a pontuação máxima
    def carregar_pontuacao_maxima():
        try:
            with open('txt/tkrhigh_score.txt', 'r') as file:
                return int(file.read().strip())
        except FileNotFoundError:
            return 0

    # função para salvar a pontuação máxima
    def salvar_pontuacao_maxima(pontuacao):
        with open('txt/tkrhigh_score.txt', 'w') as file:
            file.write(str(pontuacao))

    # carrega a pontuação máxima
    tkrhigh_score = carregar_pontuacao_maxima()

#########################################################################################
    # criando a tela inicial
    def tela_carregamento():
        pygame.mixer.music.stop()

        # música tela inicial
        pygame.mixer.music.set_volume(0.2)
        pygame.mixer.music.load("audio/tkr/tkrtheme.mp3")
        pygame.mixer.music.play(-1)

        # carregando a imagem da tela inicial
        back_img = pygame.image.load('img/carregamento/tkr/tkrcarregamento.png')
        back_img = pygame.transform.scale(back_img, (800, 800))

        # texto da tela inicial
        titulo_txt = pygame.image.load('img/carregamento/tkr/tkrinicial.png')
        titulo_txt = pygame.transform.scale(titulo_txt, (800, 500))

        # carregando as imagens dos botões
        img_iniciar = pygame.image.load('img/carregamento/tkr/tkriniciar.png')
        img_sair = pygame.image.load('img/carregamento/tkr/tkrsair.png')

        # redimensionando os botões
        button_width, button_height = 130, 50
        img_iniciar = pygame.transform.scale(img_iniciar, (button_width, button_height))
        img_sair = pygame.transform.scale(img_sair, (button_width, button_height))

        # definindo as coordenadas dos botões
        iniciar_x = 225
        iniciar_y = 450
        sair_y = 450
        sair_x = 425

        # Definindo os retângulos de colisão dos botões
        iniciar_rect = img_iniciar.get_rect(topleft=(iniciar_x, iniciar_y))
        sair_rect = img_sair.get_rect(topleft=(sair_x, sair_y))

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # obtendo a posição do mouse
                    mouse_pos = pygame.mouse.get_pos()
                    # verificando se clicou em iniciar
                    if iniciar_rect.collidepoint(mouse_pos):
                        return 'iniciar_jogo'
                    # verificando se clicou em sair
                    elif sair_rect.collidepoint(mouse_pos):
                        tela_inicial()
                    
                #manipuladores de eventos
                                    
                key = pygame.key.get_pressed()
                if key[pygame.K_ESCAPE]:
                    tela_inicial()

            screen.blit(back_img, (0, 0))
            screen.blit(titulo_txt, (0, 0))

            # denhando os botões na tela
            screen.blit(img_iniciar, (iniciar_x, iniciar_y))
            screen.blit(img_sair, (sair_x, sair_y))

            # Renderizando e exibindo a pontuação com contorno
            font = pygame.font.Font(font_path, 20)

            # Renderize o texto com uma sombra escura para simular um contorno
            shadow_text = font.render('copyrights Clayton  Moura 2024', True, black)
            shadow_rect = shadow_text.get_rect(center=(152, 772))

            # Desenhe o texto sombreado na tela
            screen.blit(shadow_text, shadow_rect)

            # Renderize o texto principal
            light_text = font.render('copyrights Clayton  Moura 2024', True, (65, 105, 225))
            light_rect = light_text.get_rect(center=(150, 770))

            # Desenhe o texto principal na tela
            screen.blit(light_text, light_rect)

            pygame.display.update()
#########################################################################################################
    # tela de gameover
    def tela_final():
        fim_txt = pygame.image.load('img/carregamento/tkr/tkrfim.png')
        fim_txt = pygame.transform.scale(fim_txt, (700, 700))
        pygame.mixer.music.stop()

        background_img = pygame.image.load('img/carregamento/tkr/tkrgameover.png')
        background_img = pygame.transform.scale(background_img, (width, height))

        # carregando os botões
        reiniciar = pygame.image.load('img/carregamento/tkr/tkrreiniciar.png')
        menu = pygame.image.load('img/carregamento/tkr/tkrmenu.png')

        # redimensionando os botões
        button_width, button_height = 130, 50
        reiniciar = pygame.transform.scale(reiniciar, (button_width, button_height))
        menu = pygame.transform.scale(menu, (button_width, button_height))
        
        # coordenadas dos botões
        reiniciar_x = 225
        reiniciar_y = 700
        menu_y = 700
        menu_x = 425

        # colisão dos botões
        reiniciar_rect = reiniciar.get_rect(topleft=(reiniciar_x, reiniciar_y))
        menu_rect = menu.get_rect(topleft=(menu_x, menu_y))

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if reiniciar_rect.collidepoint(mouse_pos):
                        # música de quando estiver jogando
                        pygame.mixer.music.set_volume(0.2)
                        pygame.mixer.music.load("audio/tkr/tkrrace.mp3")
                        pygame.mixer.music.play(-1)
                        return 'reiniciar jogo'
                    elif menu_rect.collidepoint(mouse_pos):
                        return tela_carregamento()
            #manipuladores de eventos
            
                key = pygame.key.get_pressed()
                if key[pygame.K_ESCAPE]:
                    tela_carregamento()
            
            screen.blit(background_img, (0, 0))
            screen.blit(reiniciar, reiniciar_rect)
            screen.blit(menu, menu_rect)
            screen.blit(fim_txt, (70, 0))

            # Renderizando e exibindo a pontuação com contorno
            font = pygame.font.Font(font_path, 30)

            # Renderize o texto com uma sombra escura para simular um contorno
            shadow_text = font.render('PONTUACAO   ' + str(score), True, black)
            shadow_rect = shadow_text.get_rect(center=(width / 2 + 2, 612))

            # Desenhe o texto sombreado na tela
            screen.blit(shadow_text, shadow_rect)

            # Renderize o texto principal
            score_text = font.render('PONTUACAO   ' + str(score), True, red)
            score_rect = score_text.get_rect(center=(width / 2, 610))

            # Desenhe o texto principal na tela
            screen.blit(score_text, score_rect)

            # Renderizando e exibindo a pontuação com contorno
            font = pygame.font.Font(font_path, 30)

            # Renderize o texto com uma sombra escura para simular um contorno
            shadow_text = font.render('MELHOR PONTUACAO   ' + str(tkrhigh_score), True, black)
            shadow_rect = shadow_text.get_rect(center=(width / 2 + 2, 632))

            # Desenhe o texto sombreado na tela
            screen.blit(shadow_text, shadow_rect)

            # Renderize o texto principal
            score_text = font.render('MELHOR PONTUACAO   ' + str(tkrhigh_score), True, (197, 173, 55))
            score_rect = score_text.get_rect(center=(width / 2, 630))

            # Desenhe o texto principal na tela
            screen.blit(score_text, score_rect)

            pygame.display.update()
#############################################################################################################                        
    # para a animação das faixas divisórias
    lane_marker_move_y = 0


    class Vehicle(pygame.sprite.Sprite):
        def __init__(self, image, x, y):
            pygame.sprite.Sprite.__init__(self)

            # escala dos carros
            image_scale = 100 / image.get_rect().width
            new_width = image.get_rect().width * image_scale
            new_height = image.get_rect().height * image_scale
            self.image = pygame.transform.scale(image, (new_width, new_height))

            self.rect = self.image.get_rect()
            self.rect.center = [x, y]


    class PlayerVehicle(Vehicle):
        def __init__(self, x, y):
            image = pygame.image.load('img/tkrimg/player.png')
            super().__init__(image, x, y)


    # localização de início do jogador
    player_x = 250
    player_y = 725

    # criando o carro do jogador
    player_group = pygame.sprite.Group()
    player = PlayerVehicle(player_x, player_y)
    player_group.add(player)

    # carregando as imagens dos outros carros
    image_filenames = ['ambulance.png', 'car.png', 'minitruck.png', 'police.png', 'taxi.png', 'truck.png', 'van.png',
                    'viper.png']
    vehicle_images = []
    for image_filename in image_filenames:
        image = pygame.image.load('img/tkrimg/' + image_filename)
        vehicle_images.append(image)

    # sprite grupo de veículos
    vehicle_group = pygame.sprite.Group()

    # carregando a imagem da batida
    crash = pygame.image.load('img/tkrimg/crash.png')
    crash_rect = crash.get_rect()

    # efeito sonoro de colisão
    collision_sound = pygame.mixer.Sound('audio/tkr/tkrcollision.mp3')
#################################################################################
    # exibindo a tela inicial
    tela_carregamento()

    # loop do jogo
    clock = pygame.time.Clock()
    fps = 120
    running = True

    # música de quando estiver jogando
    pygame.mixer.music.set_volume(0.2)
    pygame.mixer.music.load("audio/tkr/tkrrace.mp3")
    pygame.mixer.music.play(-1)
    while running:

        clock.tick(fps)

        if gameover:
                gameover = False
                speed = 2
                score = 0
                vehicle_group.empty()
                player.rect.center = [player_x, player_y]
                pygame.mixer.music.set_volume(0.09)
        else:
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
            
                # movimentação do jogador
                if event.type == KEYDOWN:
                    if event.key == K_a and player.rect.center[0] > left_lane or event.key == K_LEFT and player.rect.center[0] > left_lane:
                        player.rect.x -= 100
                    elif event.key == K_d and player.rect.center[0] < right_lane or event.key == K_RIGHT and player.rect.center[0] < right_lane:
                        player.rect.x += 100


                    # checando se há colisão após mudar de pista
                    for vehicle in vehicle_group:
                        if pygame.sprite.collide_rect(player, vehicle):
                            collision_sound.play()
                            gameover = True
                            gameover_time = pygame.time.get_ticks()

                            # colocando o jogador próximo a outros veículos
                            # e determinando onde colocar a imagem de batida
                            if event.key == K_LEFT:
                                player.rect.left = vehicle.rect.right
                                crash_rect.center = [player.rect.left,
                                                    (player.rect.center[1] + vehicle.rect.center[1]) / 2]
                            elif event.key == K_RIGHT:
                                player.rect.right = vehicle.rect.left
                                crash_rect.center = [player.rect.right,
                                                    (player.rect.center[1] + vehicle.rect.center[1]) / 2]

            # desenhando a grama
            screen.fill(gray)

            # desenhando a rua
            pygame.draw.rect(screen, black, road)

            # desenhando o acostamento
            pygame.draw.rect(screen, yellow, right_edge_marker)
            pygame.draw.rect(screen, yellow, left_edge_marker)

            # desenhando as faixas
            lane_marker_move_y += speed * 2
            if lane_marker_move_y >= marker_height * 2:
                lane_marker_move_y = 0
            for y in range(marker_height * -2, height, marker_height * 2):
                pygame.draw.rect(screen, white, (left_lane + 45, y + lane_marker_move_y, marker_width, marker_height))
                pygame.draw.rect(screen, white, (center_lane + 45, y + lane_marker_move_y, marker_width, marker_height))

            # desenhando o jogador
            player_group.draw(screen)

            # adicionando mais dois veículos acima
            if len(vehicle_group) < 2:

                # checando que há espaço entre os veículos
                add_vehicle = True
                for vehicle in vehicle_group:
                    if vehicle.rect.top < vehicle.rect.height * 1.5:
                        add_vehicle = False

                if add_vehicle:

                    # selecionando uma pista aleatória
                    lane = random.choice(lanes)

                    # selecionando um veículo aleatório
                    image = random.choice(vehicle_images)
                    vehicle = Vehicle(image, lane, height / -2)
                    vehicle_group.add(vehicle)

            # fazendo os veículos se moverem
            for vehicle in vehicle_group:
                vehicle.rect.y += speed

                # removendo os veículos após deixarem a tela
                if vehicle.rect.top >= height:
                    vehicle.kill()

                    # adicionando a pontuação
                    score += 1

                    # aumentando a velocidade depois de ultrapassar 5 carros
                    if score > 0 and score % 5 == 0:
                        speed += 1

            # Desenhando os outros veículos
            vehicle_group.draw(screen)

            # Mostrando a pontuação
            font = pygame.font.Font(pygame.font.get_default_font(), 16)
            text = font.render('Pontuação: 0' + str(score), True, white)
            text_rect = text.get_rect()
            text_rect.center = (600, 400)
            screen.blit(text, text_rect)

            # Checando se houve colisão frontal
            if pygame.sprite.spritecollide(player, vehicle_group, True):
                collision_sound.play()
                gameover = True
                gameover_time = pygame.time.get_ticks()
                crash_rect.center = [player.rect.center[0], player.rect.top]

            # Atualizando a maior pontuação
            if score > tkrhigh_score:
                tkrhigh_score = score
                salvar_pontuacao_maxima(tkrhigh_score) 

            # Mostrando a tela de fim de jogo
            if gameover:
                tela_final()
                screen.blit(crash, crash_rect)

        pygame.display.update()

##########################################################################################################################################
def jogo_fight():
    mixer.init()
    pygame.init()

    #create game window
    SCREEN_WIDTH = 1000
    SCREEN_HEIGHT = 600

    icon = pygame.image.load('img/icons/iconfight.png')
    #Cria janela do jogo
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Fight Mortal")
    pygame.display.set_icon(icon)

    #definir taxa de quadros
    clock = pygame.time.Clock()
    FPS = 60

    #Definir cores
    RED = (255, 0, 0)
    YELLOW = (255, 255, 0)
    WHITE = (255, 255, 255)

    #Definir variavéis do jogo
    intro_count = 3
    last_count_update = pygame.time.get_ticks()
    score1 = 0  #pontuação do player 1. [P1]
    score2 = 0  #pontuação do player 2. [P2]
    round_over = False
    victory = False
    ROUND_OVER_COOLDOWN = 2000

    #define variavéis dos lutadores
    WARRIOR_SIZE = 162
    WARRIOR_SCALE = 4
    WARRIOR_OFFSET = [72, 56]
    WARRIOR_DATA = [WARRIOR_SIZE, WARRIOR_SCALE, WARRIOR_OFFSET]
    WIZARD_SIZE = 250
    WIZARD_SCALE = 3
    WIZARD_OFFSET = [112, 107]
    WIZARD_DATA = [WIZARD_SIZE, WIZARD_SCALE, WIZARD_OFFSET]

    #carregar músiccas e sons
    pygame.mixer.music.load("audio/fight/fighttheme.mp3")
    pygame.mixer.music.set_volume(0.2)
    pygame.mixer.music.play(-1, 0.0, 5000)
    sword_fx = pygame.mixer.Sound("audio/fight/sword.wav")
    sword_fx.set_volume(0.5)
    magic_fx = pygame.mixer.Sound("audio/fight/magic.wav")
    magic_fx.set_volume(0.75)

    #carregar imagens de background
    bg_image = pygame.image.load("img/fightimg/background.jpg").convert_alpha()

    #carregar sprites
    warrior_sheet = pygame.image.load("img/fightimg/jogador_1/warrior.png").convert_alpha()
    wizard_sheet = pygame.image.load("img/fightimg/jogador_2/wizard.png").convert_alpha()

    #carregar imagem de vitória
    victory_img = pygame.image.load("img/fightimg/victory.png").convert_alpha()
    finish_img = pygame.image.load('img/fightimg/finish.png')
    player1win = pygame.image.load('img/fightimg/player1win.png').convert_alpha()
    player1win = pygame.transform.scale(player1win, (250, 150))
    player2win = pygame.image.load('img/fightimg/player2win.png').convert_alpha()
    player2win = pygame.transform.scale(player2win, (250, 150))
    #definir o número de etapas em cada animação
    WARRIOR_ANIMATION_STEPS = [10, 8, 1, 7, 7, 3, 7]
    WIZARD_ANIMATION_STEPS = [8, 8, 1, 8, 8, 3, 7]

    #define fonte
    count_font = pygame.font.Font("txt/turok.ttf", 80)
    score_font = pygame.font.Font("txt/turok.ttf", 30)
    
    #########################################################################################
    # criando a tela inicial
    def tela_carregamento():

        pygame.mixer.music.stop()
        pygame.mixer.music.play(-1)
        
        # carregando a imagem da tela inicial
        back_img = pygame.image.load('img/carregamento/bgfight.png')
        back_img = pygame.transform.scale(back_img, (1000, 600))
        
        # carregando as imagens dos botões
        img_iniciar = pygame.image.load('img/carregamento/iniciar.png')
        img_sair = pygame.image.load('img/carregamento/voltar.png')

        # redimensionando os botões
        button_width, button_height = 130, 50
        img_iniciar = pygame.transform.scale(img_iniciar, (button_width, button_height))
        img_sair = pygame.transform.scale(img_sair, (button_width, button_height))

        # definindo as coordenadas dos botões
        iniciar_x = 300
        iniciar_y = 500
        sair_y = 500
        sair_x = 500

        # Definindo os retângulos de colisão dos botões
        iniciar_rect = img_iniciar.get_rect(topleft=(iniciar_x, iniciar_y))
        sair_rect = img_sair.get_rect(topleft=(sair_x, sair_y))

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    tela_inicial()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # obtendo a posição do mouse
                    mouse_pos = pygame.mouse.get_pos()
                    # verificando se clicou em iniciar
                    if iniciar_rect.collidepoint(mouse_pos):
                        return 'iniciar_jogo'
                    # verificando se clicou em sair
                    elif sair_rect.collidepoint(mouse_pos):
                        # pygame.quit()
                        tela_inicial()
                key = pygame.key.get_pressed()
                if key[pygame.K_ESCAPE]:
                    #pygame.quit()
                    tela_inicial()
            screen.blit(back_img, (0, 0))

            # denhando os botões na tela
            screen.blit(img_iniciar, (iniciar_x, iniciar_y))
            screen.blit(img_sair, (sair_x, sair_y))
            
            # Renderizando e exibindo a pontuação com contorno
            font = pygame.font.Font(font_path, 20)
            # Renderize o texto com uma sombra escura para simular um contorno
            shadow_text = font.render('copyrights Fabio  Augusto 2024', True, black)
            shadow_rect = shadow_text.get_rect(center=(152, 592))

            # Desenhe o texto sombreado na tela
            screen.blit(shadow_text, shadow_rect)

            # Renderize o texto principal
            score_text = font.render('copyrights Fabio  Augusto 2024', True, RED)
            score_rect = score_text.get_rect(center=(150, 590))

            # Desenhe o texto principal na tela
            screen.blit(score_text, score_rect)

            pygame.display.update()
#######################################################################################################
#########################################################################################################
    # tela de gameover
    def tela_final():
        

        background_img = pygame.image.load('img/fightimg/finish.png')
        background_img = pygame.transform.scale(background_img, (1000, 800))

        # carregando os botões
        reiniciar = pygame.image.load('img/carregamento/tkr/tkrreiniciar.png')
        menu = pygame.image.load('img/carregamento/tkr/tkrmenu.png')

        # redimensionando os botões
        button_width, button_height = 130, 50
        reiniciar = pygame.transform.scale(reiniciar, (button_width, button_height))
        menu = pygame.transform.scale(menu, (button_width, button_height))
        
        # coordenadas dos botões
        reiniciar_x = 300
        reiniciar_y = 500
        menu_y = 500
        menu_x = 500

        # colisão dos botões
        reiniciar_rect = reiniciar.get_rect(topleft=(reiniciar_x, reiniciar_y))
        menu_rect = menu.get_rect(topleft=(menu_x, menu_y))

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if reiniciar_rect.collidepoint(mouse_pos):
                        # música de quando estiver jogando
                        pygame.mixer.music.set_volume(0.2)
                        pygame.mixer.music.load("audio/fight/fighttheme.mp3")
                        pygame.mixer.music.play(-1)
                        return 'reiniciar jogo'
                    elif menu_rect.collidepoint(mouse_pos):
                        return tela_carregamento()
            #manipuladores de eventos
            
                key = pygame.key.get_pressed()
                if key[pygame.K_ESCAPE]:
                    tela_carregamento()
            
            screen.blit(background_img, (0, 0))
            screen.blit(reiniciar, reiniciar_rect)
            screen.blit(menu, menu_rect)
            

            # Renderizando e exibindo a pontuação com contorno
            font = pygame.font.Font(font_path, 30)

            # Renderize o texto com uma sombra escura para simular um contorno
            shadow_text = font.render('PLAYER 1   ' + str(score1), True, black)
            shadow_rect = shadow_text.get_rect(center=(80 , 40))

            # Desenhe o texto sombreado na tela
            screen.blit(shadow_text, shadow_rect)

            # Renderize o texto principal
            score_text = font.render('PLAYER 1   ' + str(score1), True, red)
            score_rect = score_text.get_rect(center=(82, 42))

            # Desenhe o texto principal na tela
            screen.blit(score_text, score_rect)

            # Renderizando e exibindo a pontuação com contorno
            font = pygame.font.Font(font_path, 30)

            # Renderize o texto com uma sombra escura para simular um contorno
            shadow_text = font.render('PLAYER 2   ' + str(score2), True, black)
            shadow_rect = shadow_text.get_rect(center=(80, 60))

            # Desenhe o texto sombreado na tela
            screen.blit(shadow_text, shadow_rect)

            # Renderize o texto principal
            score_text = font.render('PLAYER 2   ' + str(score2), True, (197, 173, 55))
            score_rect = score_text.get_rect(center=(82, 62))

            # Desenhe o texto principal na tela
            screen.blit(score_text, score_rect)

            pygame.display.update()
#############################################################################################################

    ##################### Classe dos Lutadores ###################################

    class Fighter():
        def __init__(self, player, x, y, flip, data, sprite_sheet, animation_steps, sound):
            self.player = player
            self.size = data[0]
            self.image_scale = data[1]
            self.offset = data[2]
            self.flip = flip
            self.animation_list = self.load_images(sprite_sheet, animation_steps)
            self.action = 0#0:idle #:run #2:jump #3:attack1 #4:attack2 #5:hit #6:death
            self.frame_index = 0
            self.image = self.animation_list[self.action][self.frame_index]
            self.update_time = pygame.time.get_ticks()
            self.rect = pygame.Rect((x, y, 80, 180))
            self.vel_y = 0
            self.running = False
            self.jump = False
            self.attacking = False
            self.attack_type = 0
            self.attack_cooldown = 0
            self.attack_sound = sound
            self.hit = False
            self.health = 100
            self.alive = True


        def load_images(self, sprite_sheet, animation_steps):
            #extrair imagens da spritesheet
            animation_list = []
            for y, animation in enumerate(animation_steps) : 
                temp_img_list = []
                for x in range (animation):
                    temp_img = sprite_sheet.subsurface(x * self.size, y * self.size, self.size, self.size)
                    temp_img_list.append( pygame.transform.scale(temp_img, (self.size * self.image_scale, self.size * self.image_scale)))
                animation_list.append(temp_img_list)
            return animation_list


        def move(self, screen_width, screen_height, surface, target, round_over):
            SPEED = 10
            GRAVITY = 2
            dx = 0
            dy = 0
            self.running = False
            self.attack_type = 0

            #obter pressionamentos de tecla
            key = pygame.key.get_pressed()

             #só pode realizar outras ações se não estiver atacando no momento
            if self.attacking == False and self.alive == True and round_over == False:
                #Checar controles do Player 1
                if self.player == 1:
                    #Movimentos
                    if key[pygame.K_a]:
                        dx = -SPEED
                        self.running = True
                    if key[pygame.K_d]:
                        dx = SPEED
                        self.running = True
                    #Pulo
                    if key[pygame.K_w] and self.jump == False:
                        self.vel_y = -30
                        self.jump = True
                    #Ataque 
                    if key[pygame.K_b] or key[pygame.K_m]:
                        self.attack(target)
                        #determinar qual tipo de ataque foi usado
                        if key[pygame.K_b]:
                            self.attack_type = 1
                        if key[pygame.K_m]:
                            self.attack_type = 2


                #Checar controles do Player 2
                if self.player == 2:
                    #Movimento
                    if key[pygame.K_LEFT]:
                        dx = -SPEED
                        self.running = True
                    if key[pygame.K_RIGHT]:
                        dx = SPEED
                        self.running = True
                    #Pulo
                    if key[pygame.K_UP] and self.jump == False:
                        self.vel_y = -30
                        self.jump = True
                    #Ataque
                    if key[pygame.K_KP_0] or key[pygame.K_KP_ENTER]:
                        self.attack(target)
                        #determinar qual tipo de ataque foi usado
                        if key[pygame.K_KP_0]:
                            self.attack_type = 1
                        if key[pygame.K_KP_ENTER]:
                            self.attack_type = 2

            #aplicar gravidade
            self.vel_y += GRAVITY
            dy += self.vel_y

            #garantir que o plaer permaneça na tela
            if self.rect.left + dx < 0:
                dx = -self.rect.left
            if self.rect.right + dx > screen_width:
                dx = screen_width - self.rect.right
            if self.rect.bottom + dy > screen_height - 110:
                self.vel_y = 0
                self.jump = False
                dy = screen_height - 110 - self.rect.bottom

            # garantir que os jogadores fiquem de frente um para o outro
            if target.rect.centerx > self.rect.centerx:
                self.flip = False
            else:
                self.flip = True

            #aplicar tempo de ataque
            if self.attack_cooldown > 0:
                self.attack_cooldown -= 1

            #atualizar posição do player
            self.rect.x += dx
            self.rect.y += dy


        #Manipulador de atualizações de animação
        def update(self):
            #verifique qual ação o jogador está realizando
            if self.health <= 0:
                self.health = 0
                self.alive = 0
                self.update_action(6)#6:morte
            elif self.hit == True:
                self.update_action(5)#5:hit
            elif self.attacking == True:
                if self.attack_type == 1:
                    self.update_action(3)#3:ataque 1
                elif self.attack_type == 2:
                    self.update_action(4)#4:ataque 2
            elif self.jump == True:
                self.update_action(2)#2:pulo
            elif self.running == True:
                self.update_action(1)#1:corrida
            else:
                self.update_action(0)#0:parado

            animation_cooldown = 50
            #atualização de imagem
            self.image = self.animation_list[self.action][self.frame_index]
            #verifique se já passou tempo suficiente desde a última atualização
            if pygame.time.get_ticks() - self.update_time > animation_cooldown:
                self.frame_index +=1
                self.update_time = pygame.time.get_ticks()
            #verifique se a animação terminou
            if self.frame_index >= len(self.animation_list[self.action]):
                #se o jogador estiver morto, encerre a animação
                if self.alive == False:
                    self.frame_index = len(self.animation_list[self.action]) - 1
                else:
                    self.frame_index = 0
                    #verificar se um ataque foi executado
                    if self.action == 3 or self.action == 4:
                        self.attacking = False
                        self.attack_cooldown = 20
                    #verifique se o dano foi sofrido
                    if self.action == 5:
                        self.hit = False
                        #se o jogador estava no meio de um ataque, então o ataque é interrompido
                        self.attacking = False
                        self.attack_cooldown = 20


        def attack(self, target):
            if self.attack_cooldown == 0:
            #Execute o ataque
                self.attacking = True
                self.attack_sound.play()
                attacking_rect = pygame.Rect(self.rect.centerx - (2 * self.rect.width * self.flip), self.rect.y, 2 * self.rect.width, self.rect.height)
                if attacking_rect.colliderect(target.rect):
                    target.health -= 10
                    target.hit = True


        def update_action(self, new_action):
            #verifique se a nova ação é diferente da anterior
            if new_action != self.action:
                self.action = new_action
                #atualize as novas configurações de animação
                self.frame_index = 0
                self.update_time = pygame.time.get_ticks()

        def draw(self, surface):
            img = pygame.transform.flip(self.image, self.flip, False)
            surface.blit(img, (self.rect.x - (self.offset[0] * self.image_scale), self.rect.y - (self.offset[1] * self.image_scale)))

    ######################################################

    #Função de desenhar os textos
    def draw_text(text, font, text_col, x, y):
        img = font.render(text, True, text_col)
        screen.blit(img, (x, y))

    #função de desennhar o background
    def draw_bg():
        scaled_bg = pygame.transform.scale(bg_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
        screen.blit(scaled_bg, (0, 0))

    #função para desenhar background
    def draw_health_bar(health, x, y):
        ratio = health / 100
        pygame.draw.rect(screen, WHITE, (x - 2, y - 2, 404, 34))
        pygame.draw.rect(screen, RED, (x, y, 400, 30))
        pygame.draw.rect(screen, YELLOW, (x, y, 400 * ratio, 30))

        
    #crie duas instâncias de lutadores
    fighter_1 = Fighter(1, 200, 310, False, WARRIOR_DATA, warrior_sheet, WARRIOR_ANIMATION_STEPS, sword_fx)
    fighter_2 = Fighter(2, 700, 310, True, WIZARD_DATA, wizard_sheet, WIZARD_ANIMATION_STEPS, magic_fx)

#####################################################################
    #loop do jogo
    tela_carregamento()
    run = True
    while run:

        clock.tick(FPS)

        #desenha o background
        draw_bg()

        #apresenta os estatus dos players
        draw_health_bar(fighter_1.health, 20, 20)
        draw_health_bar(fighter_2.health, 580, 20)
        draw_text("P1: " + str(score1), score_font, RED, 20, 60)
        draw_text("P2: " + str(score2), score_font, RED, 580, 60)

        #atualização do contador
        if intro_count <= 0:
            #movimento dos lutadores
            fighter_1.move(SCREEN_WIDTH, SCREEN_HEIGHT, screen, fighter_2, round_over)
            fighter_2.move(SCREEN_WIDTH, SCREEN_HEIGHT, screen, fighter_1, round_over)
        else:
            #temporizador de contagem de exibição
            draw_text(str(intro_count), count_font, RED, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 3)
            #atualizar temporizador de contagem
            if (pygame.time.get_ticks() - last_count_update) >= 1000:
                intro_count -= 1
                last_count_update = pygame.time.get_ticks()

        #Atualização dos lutadores
        fighter_1.update()
        fighter_2.update()

        #desenha os lutadores
        fighter_1.draw(screen)
        fighter_2.draw(screen)

        #verifique a derrota do jogador
        if round_over == False:
            if fighter_1.alive == False:
                score2 += 1
                round_over = True
                round_over_time = pygame.time.get_ticks()
                if score2 == 2:
                    tela_final()
            elif fighter_2.alive == False:
                score1 += 1
                round_over = True
                round_over_time = pygame.time.get_ticks()
                if score1 == 2:
                    tela_final()
        else:
            #Tela de imagem de vitória
            screen.blit(victory_img, (360, 150))
            if pygame.time.get_ticks() - round_over_time > ROUND_OVER_COOLDOWN:
                round_over = False
                intro_count = 0#3
                fighter_1 = Fighter(1, 200, 310, False, WARRIOR_DATA, warrior_sheet, WARRIOR_ANIMATION_STEPS, sword_fx)
                fighter_2 = Fighter(2, 700, 310, True, WIZARD_DATA, wizard_sheet, WIZARD_ANIMATION_STEPS, magic_fx)

        #manipulador de eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                tela_final()
        key = pygame.key.get_pressed()
        if key[pygame.K_ESCAPE]:
            tela_carregamento()

        #Atualização da tela
        pygame.display.update()

##########################################################################################################################
def main():
    tela_inicial()

main()            

'''
Desenvolvedores:
Andre
Clayton
Erik
Fabio
Igor
'''
 