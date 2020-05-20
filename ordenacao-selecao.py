from turtle import forward, left, setworldcoordinates, done, position, setposition, speed, tracer, color, pendown, penup, dot, begin_fill, end_fill, hideturtle
from random import randint
BAR_WIDTH_CONST = 6
def draw_bar(bar_width, bar_height, pos_x, pos_y, color_param='black'):
    color(color_param)
    setposition(pos_x, pos_y)
    pendown()
    begin_fill()
    forward(bar_width)
    left(90)
    forward(bar_height)
    left(90)
    forward(bar_width)
    left(90)
    forward(bar_height)
    left(90)
    end_fill()
    penup()
    return None
def draw_bar_list(list_of_bars, pos_x, pos_y):
    hideturtle()
    speed(0)
    for target_list in list_of_bars:
        draw_bar(BAR_WIDTH_CONST, target_list, pos_x, pos_y)
        pos_x += BAR_WIDTH_CONST
    return None
def busca_menor(arr):
    menor = arr[0]
    menor_indice = 0
    for i in range(1, len(arr)):
        if arr[i] < menor:
            menor = arr[i]
            menor_indice = i
    return menor_indice
# def draw_dot(pos_x, pos_y):
#     setposition(pos_x, pos_y)
#     dot(5)
def ordenacao_por_selecao(arr):
    speed(0)
    novo_arr = []
    pos_y = 400
    pos_x = 0
    arr_copy = arr[:]
    for i in range(len(arr)):
        menor = busca_menor(arr)
        index = arr_copy.index(arr[menor])
        draw_bar(BAR_WIDTH_CONST, arr_copy[index], index* BAR_WIDTH_CONST, 0, 'blue')
        arr_copy[index] = 101
        # arr_copy.remove(arr[menor])
        novo_arr.append(arr.pop(menor))
        # draw_dot((index + 1) * BAR_WIDTH_CONST - 3, 1)
        draw_bar(BAR_WIDTH_CONST, novo_arr[len(novo_arr)-1], pos_x, pos_y, 'blue')
        pos_x+=BAR_WIDTH_CONST
    return novo_arr
setworldcoordinates(-1, -1, 800, 800)
# disable screen refresh
# tracer(0, 0)
list_of_bars = [randint(1,100) for i in range(1,101)]
draw_bar_list(list_of_bars, 0 ,0)
ordenacao_por_selecao(list_of_bars)
done()