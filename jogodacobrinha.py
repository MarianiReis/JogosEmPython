import pygame
import random

pygame.init()



largura, altura = 600, 400
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Jogo da Cobrinha")



preto = (0, 0, 0)
verde = (0, 255, 0)
vermelho = (255, 0, 0)
branco = (255, 255, 255)


tamanho_bloco = 20
velocidade = 10


fonte = pygame.font.SysFont("arial", 25)

def desenhar_cobra(cobra):
    for segmento in cobra:
        pygame.draw.rect(tela, verde, [segmento[0], segmento[1], tamanho_bloco, tamanho_bloco])

def mostrar_pontuacao(pontos):
    texto = fonte.render(f"Pontos: {pontos}", True, branco)
    tela.blit(texto, [10, 10])

def jogo():
    rodando = True
    game_over = False

    
    x, y = largura // 2, altura // 2
    dx, dy = 0, 0

    
    cobra = [[x, y]]
    comprimento = 1

    
    comida_x = random.randrange(0, largura - tamanho_bloco, tamanho_bloco)
    comida_y = random.randrange(0, altura - tamanho_bloco, tamanho_bloco)

    relogio = pygame.time.Clock()

    while rodando:
        while game_over:
            tela.fill(preto)
            texto = fonte.render("Game Over! Pressione R para reiniciar.", True, vermelho)
            tela.blit(texto, [largura // 6, altura // 3])
            pygame.display.update()

            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    rodando = False
                    game_over = False
                if evento.type == pygame.KEYDOWN and evento.key == pygame.K_r:
                    jogo()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT and dx == 0:
                    dx, dy = -tamanho_bloco, 0
                elif evento.key == pygame.K_RIGHT and dx == 0:
                    dx, dy = tamanho_bloco, 0
                elif evento.key == pygame.K_UP and dy == 0:
                    dx, dy = 0, -tamanho_bloco
                elif evento.key == pygame.K_DOWN and dy == 0:
                    dx, dy = 0, tamanho_bloco

     
        x += dx
        y += dy
        cobra.append([x, y])

        if len(cobra) > comprimento:
            del cobra[0]

        
        if x < 0 or x >= largura or y < 0 or y >= altura or [x, y] in cobra[:-1]:
            game_over = True

        
        if x == comida_x and y == comida_y:
            comprimento += 1
            comida_x = random.randrange(0, largura - tamanho_bloco, tamanho_bloco)
            comida_y = random.randrange(0, altura - tamanho_bloco, tamanho_bloco)

        
        tela.fill(preto)
        pygame.draw.rect(tela, vermelho, [comida_x, comida_y, tamanho_bloco, tamanho_bloco])
        desenhar_cobra(cobra)
        mostrar_pontuacao(comprimento - 1)

        pygame.display.update()
        relogio.tick(velocidade + (comprimento // 5)) 

    pygame.quit()

jogo()