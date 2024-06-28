import pygame
import colores
from datos import lista
from funciones import *
pygame.init()
ANCHO_VENTANA = 858
ALTO_VENTANA = 715

pregunta = ""
tema = ""
score = 0
respuesta_a = ""
respuesta_b = ""
respuesta_c = ""
lista_preguntas = []
lista_temas = []
lista_respuesta_a = []
lista_respuesta_b = []
lista_respuesta_c = []
lista_correctas=[]
contador = 0
contador_respuestas_apretadas = 0
respuesta_apretada = ""
flag_siguiente_pregunta = False
flag_primera_ejecucion = True

for e_lista in lista:
    lista_preguntas.append(e_lista["pregunta"])
    lista_temas.append(e_lista["tema"])
    lista_respuesta_a.append(e_lista["a"])
    lista_respuesta_b.append(e_lista["b"])
    lista_respuesta_c.append(e_lista["c"])
    lista_correctas.append(e_lista["correcta"])
   
#cargar logo
imagen = pygame.image.load("logo_carrera_de_mente.png")
imagen = pygame.transform.scale(imagen,(200,200))

#crear una fuente
fuente = pygame.font.SysFont("Arial",30)
fuente_respuestas = pygame.font.SysFont("Arial",20)
TEXTO_SCORE = fuente.render(str("SCORE"),True,colores.COLOR_GRIS)
TEXTO_SIGUIENTE_PREGUNTA = fuente.render(str("Siguiente pregunta"),True,colores.COLOR_GRIS)
TEXTO_REINICIAR = fuente.render(str("REINICIAR"),True,colores.COLOR_GRIS)
texto_tema = fuente.render(str("tema"),True,colores.COLOR_AMARILLO)
texto_pregunta = fuente.render(str("pregunta"),True,colores.COLOR_GRIS)
texto_score_variable = fuente.render(str(score),True,colores.COLOR_GRIS)
texto_respuesta_a = fuente_respuestas.render(str("A"),True,colores.COLOR_AMARILLO)
texto_respuesta_b = fuente_respuestas.render(str("B"),True,colores.COLOR_AMARILLO)
texto_respuesta_c = fuente_respuestas.render(str("C"),True,colores.COLOR_AMARILLO)

respuesta_a_visible = False
respuesta_b_visible = False
respuesta_c_visible = False
#posiciones botones
    
pos_siguiente_pregunta = (300,20,300,100)
pos_reiniciar = (ANCHO_VENTANA*0.5-100,570,200,100)
ANCHO_RESPUESTA = ANCHO_VENTANA / 3
pos_respuesta_A = (0,400,ANCHO_RESPUESTA-10,100)
pos_respuesta_B = (ANCHO_RESPUESTA,400,ANCHO_RESPUESTA-10,100)
pos_respuesta_C = (ANCHO_RESPUESTA*2,400,ANCHO_RESPUESTA-10,100)

#crear la pantalla
pantalla = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA))
pygame.display.set_caption("Carrera de Mente")

flag_correr = True

while flag_correr:
    lista_eventos = pygame.event.get()
    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            flag_correr = False
        if evento.type == pygame.MOUSEBUTTONDOWN:

            if chequear_click_en_rect(evento.pos,pos_respuesta_A):
                if respuesta_a_visible:
                    respuesta_apretada = 'a'
                    respuesta_a_visible = False
                    contador_respuestas_apretadas += 1
            elif chequear_click_en_rect(evento.pos,pos_respuesta_B):
                if respuesta_b_visible:
                    respuesta_apretada = 'b'
                    respuesta_b_visible = False
                    contador_respuestas_apretadas += 1
            elif chequear_click_en_rect(evento.pos,pos_respuesta_C):
                if respuesta_c_visible:
                    respuesta_apretada = 'c'
                    respuesta_c_visible = False
                    contador_respuestas_apretadas += 1     
            if lista_correctas[contador] == respuesta_apretada:
                flag_siguiente_pregunta = True
                score += 10           
                contador_respuestas_apretadas = 0
            # print(contador_respuestas_apretadas)
            if contador_respuestas_apretadas >= 2:
                flag_siguiente_pregunta = True
                contador_respuestas_apretadas = 0
                        
            if chequear_click_en_rect(evento.pos,pos_reiniciar):
                respuesta_a_visible = True
                respuesta_b_visible = True
                respuesta_c_visible = True
                contador = 0
                contador_respuestas_apretadas = 0
                flag_siguiente_pregunta = False
                respuesta_apretada = ""
                score = 0
            if chequear_click_en_rect(evento.pos,pos_siguiente_pregunta) or flag_siguiente_pregunta:
                if flag_primera_ejecucion:
                    flag_primera_ejecucion = False

                else:
                    if contador == len(lista_preguntas)-1:
                        contador = 0
                    else:
                        contador += 1
                    respuesta_apretada = "" 
                    flag_siguiente_pregunta = False
                respuesta_a_visible = True
                respuesta_b_visible = True
                respuesta_c_visible = True
                # print("correcta:"+lista_correctas[contador],respuesta_apretada)
            
        

                
            # print(respuesta_apretada)
        respuesta_apretada = ""            
    pantalla.fill(colores.BLUE)

        #realizar todos los cambios de texto
    if not flag_primera_ejecucion:
        pregunta = lista_preguntas[contador]
        tema = lista_temas[contador]
        respuesta_a = lista_respuesta_a[contador]
        respuesta_b = lista_respuesta_b[contador]
        respuesta_c = lista_respuesta_c[contador]
        texto_tema = fuente.render(str(tema),True,colores.COLOR_AMARILLO)
        texto_pregunta = fuente.render(str(pregunta),True,colores.COLOR_GRIS)
        texto_respuesta_a = fuente_respuestas.render(str(respuesta_a),True,colores.COLOR_AMARILLO)
        texto_respuesta_b = fuente_respuestas.render(str(respuesta_b),True,colores.COLOR_AMARILLO)
        texto_respuesta_c = fuente_respuestas.render(str(respuesta_c),True,colores.COLOR_AMARILLO)
        texto_score_variable = fuente.render(str(score),True,colores.COLOR_GRIS)
    
    #botones
        #fijos    
    pygame.draw.rect(pantalla,colores.COLOR_AMARILLO,pos_siguiente_pregunta)
    pygame.draw.rect(pantalla,colores.COLOR_AMARILLO,pos_reiniciar)
        
    #Fundir textos
    pantalla.blit(TEXTO_SCORE,(pos_siguiente_pregunta[0]+20,
                               pos_siguiente_pregunta[1]+110))
    pantalla.blit(texto_score_variable,
                                (pos_siguiente_pregunta[0]+20,
                                pos_siguiente_pregunta[1]+140))
    pantalla.blit(texto_tema,(20,220))
    pantalla.blit(texto_pregunta,(20,260))
    pantalla.blit(TEXTO_SIGUIENTE_PREGUNTA,(pos_siguiente_pregunta[0]+20,
                                           pos_siguiente_pregunta[1]+30))
    pantalla.blit(TEXTO_REINICIAR,(pos_reiniciar[0]+20,
                                           600))
    if respuesta_a_visible:
        pygame.draw.rect(pantalla,colores.COLOR_AMARILLO,pos_respuesta_A,5)
        pantalla.blit(texto_respuesta_a,(pos_respuesta_A[0]+15
                                     ,pos_respuesta_A[1]+35))
    if respuesta_b_visible:
        pygame.draw.rect(pantalla,colores.COLOR_AMARILLO,pos_respuesta_B,5)
        pantalla.blit(texto_respuesta_b,(pos_respuesta_B[0]+15
                                     ,pos_respuesta_B[1]+35))
    if respuesta_c_visible:
        pygame.draw.rect(pantalla,colores.COLOR_AMARILLO,pos_respuesta_C,5)  
        pantalla.blit(texto_respuesta_c,(pos_respuesta_C[0]+15
                                     ,pos_respuesta_C[1]+35))
    
    pantalla.blit(imagen,(10,10))
    
    pygame.display.flip()
    
pygame.quit()

