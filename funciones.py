
def chequear_click_en_rect(posicion_click:tuple,item_rect:tuple):
    if ((posicion_click[0]>item_rect[0] and 
         posicion_click[0]<item_rect[0]+item_rect[2])
        and (posicion_click[1]>item_rect[1] and 
             posicion_click[1]<item_rect[1]+item_rect[3])):
               return True
    return False