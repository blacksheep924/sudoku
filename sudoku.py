import pygame
import sys
import random

pygame.init()
WIDTH,HEIGHT = 1280,720
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("SUDOKU")
FPS = 60
BLACK = "black"
WHITE = "white"
CASE_WIDTH,CASE_HEIGHT = 1,60
NUMBER_COLUMNS = 9
NUMBER_CASES = 81
COUNTER = 0
DIFFICULTY = 15
font = pygame.font.Font(None,32)


class Grid:
    def __init__(self,x,y,w,h):
        self.lign_left = pygame.Rect(x,y,w,h)
        self.lign_top = pygame.Rect(x,y,h,w)
        self.lign_bottom = pygame.Rect(x,y+CASE_HEIGHT,h,w)
        self.lign_right = pygame.Rect(x+CASE_HEIGHT,y,w,h)
    def coordinates(self):
        
        top_x = self.lign_top.x 
        left_x = self.lign_left.x 
        bottom_x = self.lign_bottom.x 
        right_x = self.lign_right.x 

        top_y = self.lign_top.y 
        left_y = self.lign_left.y 
        bottom_y = self.lign_bottom.y 
        right_y = self.lign_right.y

        return (top_x,left_x,bottom_x,right_x,top_y,left_y,bottom_y,right_y)
    
class Block:
    def __init__(self):
        ...
        
    def block_number(self):
        
        ...

class Check:
    def __init__(self,list):
        
        self.list = list
    def check_next(self,x,y):
        dx = x
        dy = y
        value_1,value_2 = self.list[dx][1],self.list[dy][1]  
        coord_x_1,coord_x_2 = self.list[dx][0][0],self.list[dy][0][0]
        coord_y_1,coord_y_2 = self.list[dx][0][1],self.list[dy][0][1]
        if value_1 == value_2 and coord_x_1 == coord_x_2 or value_1 == value_2 and coord_y_1 == coord_y_2:
            
            return 1
        elif value_1 == value_2 and coord_x_1 != coord_x_2 or value_1 == value_2 and coord_y_1 != coord_y_2:
            
            return 2
        elif value_1 != value_2:
            
            return 3
        
            
            
        
        
            



def check_grid(my_dict,four_points):
    
    key_list = sorted(my_dict.keys())
    coord_value = []
    new_dict = {}
    index_list = []
    for index, values in enumerate(my_dict):
        
        new_dict.update({index:my_dict[values]})
    key2_list = sorted(new_dict.keys())
    for index, item in enumerate(my_dict):
        if my_dict[item] != " ":
            x = key_list[index],my_dict[item]
            coord_value.append(x)
    for index, item in enumerate(new_dict):
        if new_dict[item] != " ":
            x = key2_list[index],new_dict[item]
            index_list.append(x)

    sorted_coord_value = sorted(coord_value,key=lambda x:x[1])
    sorted_index_list = sorted(index_list,key=lambda x:x[1])
    checky = Check(sorted_coord_value)
    
    x = 0 
    y = 1
    
    while y != len(sorted_coord_value) and x != len(sorted_coord_value)-1:
        
        

        if checky.check_next(x,y) == 1:
            return False
        elif checky.check_next(x,y) == 2:
            y+=1
             
        elif checky.check_next(x,y) == 3:
            
            x += 1
            y = x+1
            
    print(sorted_index_list)        
    return True
            
        
           
    




    
    
    
    
    




def create_grid(four_points,values_in_cases,two_coords,DIFFICULTY):
    
    list_random_cords = random.sample(four_points, DIFFICULTY)
    
    for key in four_points:
        values_in_cases[key[0],key[2],CASE_HEIGHT,CASE_HEIGHT] = str(" ")  
    for key in list_random_cords:
        random_number = random.randint(1, 9)
        values_in_cases[key[0], key[2],CASE_HEIGHT,CASE_HEIGHT] = str(random_number)
    
        
    for cords in list_random_cords:
        var_cord = cords[0],cords[2],CASE_HEIGHT,CASE_HEIGHT
        two_coords.append(var_cord)
            

def number_is_multiple(x):
    global COUNTER
    if x % 9 == 0:
        COUNTER += 1
        
def draw_window(cases,mode,value_in_cases):
    inverse = BLACK
    keylist = list(value_in_cases.keys())
     
    if mode == BLACK:
        WIN.fill(BLACK)
        inverse = WHITE
    else:
        WIN.fill(WHITE)
        inverse = BLACK
    font_mode = font.render("Mode",True,inverse,None)
    text_rect = font_mode.get_rect(topleft=(20,20))
    for index, value in enumerate(value_in_cases):

        font_number = font.render(str(value_in_cases[value][0]),True,inverse,None)
           
        WIN.blit(font_number,(keylist[index][0]+CASE_HEIGHT/2.5,keylist[index][1]+CASE_HEIGHT/3))
    
    WIN.blit(font_mode,text_rect)
    
    for case in cases:
        pygame.draw.rect(WIN,inverse,case.lign_top)
        pygame.draw.rect(WIN,inverse,case.lign_left)
        pygame.draw.rect(WIN,inverse,case.lign_bottom)
        pygame.draw.rect(WIN,inverse,case.lign_right)

    pygame.display.update()


def main():
    
    running = True
    
    clock = pygame.time.Clock()
    cases = [Grid((WIDTH-(WIDTH-CASE_HEIGHT*NUMBER_COLUMNS)/2)-CASE_HEIGHT*NUMBER_COLUMNS,(HEIGHT-(HEIGHT+CASE_HEIGHT*NUMBER_COLUMNS)/2),CASE_WIDTH,CASE_HEIGHT) for _ in range(NUMBER_CASES)]
    coordinate_cases = []
    final_coordinates = []
    modes = {"Dark":BLACK,"Light":WHITE}
    mode = modes["Dark"]
    font_mode = font.render("Mode",True,mode,None)
    text_rect = font_mode.get_rect(topleft=(20,20))
    for case in cases:        
        coordinate_cases.append(case.coordinates())
    
    for index, case in enumerate(cases):
        if index != 0:
            number_is_multiple(index)
            case.lign_top.x = coordinate_cases[index-1][0]+(CASE_HEIGHT*index)-(CASE_HEIGHT*(NUMBER_COLUMNS * COUNTER))
            case.lign_bottom.x = coordinate_cases[index-1][1]+(CASE_HEIGHT*index)-(CASE_HEIGHT*(NUMBER_COLUMNS * COUNTER))
            case.lign_right.x = coordinate_cases[index-1][2]+(CASE_HEIGHT*index)-(CASE_HEIGHT*(NUMBER_COLUMNS * COUNTER))
            case.lign_left.x = coordinate_cases[index-1][3]+(CASE_HEIGHT*index)-(CASE_HEIGHT*(NUMBER_COLUMNS * COUNTER))
            case.lign_top.y = coordinate_cases[index-1][4]+CASE_HEIGHT*COUNTER
            case.lign_left.y = coordinate_cases[index-1][5]+CASE_HEIGHT*COUNTER
            case.lign_bottom.y = coordinate_cases[index-1][6]+CASE_HEIGHT*COUNTER
            case.lign_right.y = coordinate_cases[index-1][7]+CASE_HEIGHT*COUNTER
        
    for case in cases:
        final_coordinates.append(case.coordinates())
    
    four_points = []
    x_1 = final_coordinates[0][0]
    x_2 = final_coordinates[0][3]
    y_1 = final_coordinates[0][4]
    y_2 = final_coordinates[0][6]
    var_counter = 1

    for case in cases:
        if var_counter % NUMBER_COLUMNS != 0:
            var_list = (x_1,x_2,y_1,y_2)
            four_points.append(var_list)
            x_1 += CASE_HEIGHT
            x_2 += CASE_HEIGHT
            var_counter += 1
    
        else:
            var_list = (x_1,x_2,y_1,y_2)
            four_points.append(var_list)
            x_1 = final_coordinates[0][0]
            x_2 = final_coordinates[0][3]
            y_1 += CASE_HEIGHT
            y_2 += CASE_HEIGHT
            
            var_counter += 1
       
    case_list = []
    number_chosen = ""
    case_chosen = None   
    values_in_cases = {}
    two_coords = []
    
    
    

    for point in four_points:
        case_list.append(pygame.Rect(point[0],point[2],CASE_HEIGHT,CASE_HEIGHT))
    
    
    start_counter = 0

    while running == True:
        clock.tick(FPS)
        for event in pygame.event.get():
            click = pygame.mouse.get_pos()
            
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if text_rect.collidepoint(event.pos):
                        if mode == WHITE:
                            mode = modes["Dark"]
                            
                        else:
                            mode = modes["Light"]
                
                    else:
                        for case in case_list:
                            if case.collidepoint(event.pos):
                                
                                case_chosen = case[0],case[1],case[2],case[3]
                                
                                                
                      
            if event.type == pygame.KEYDOWN:
                key_pressed = pygame.key.name(event.key)
                try:
                    if int(key_pressed) >= 1 and int(key_pressed) <= 9 and case_chosen not in two_coords:
                        number_chosen = key_pressed
                        values_in_cases[case_chosen] = number_chosen
           
                except ValueError:
                    pass

        if start_counter == 0:
            
            create_grid(four_points,values_in_cases,two_coords,DIFFICULTY)
            check_grid(values_in_cases,four_points)
            while check_grid(values_in_cases,four_points) == False:
                create_grid(four_points,values_in_cases,two_coords,DIFFICULTY)
                if len(two_coords) > DIFFICULTY:
                        two_coords = two_coords[-DIFFICULTY:]
                if check_grid(values_in_cases,four_points) != False:
                        start_counter = 1
               
                
            

        
        
                        
        draw_window(cases,mode,values_in_cases)
        
    
    pygame.quit()

if __name__ == "__main__":
    main()