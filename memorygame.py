# implementation of card game - Memory

import simpleguitk as simplegui
import random
deck=[]             #emptylist1
turns=0
exposed=[]          #emptylist2
card_exposed=[]     #emptylist3
card_width=70
# helper function to initialize globals
def new_game():
    global turns,deck,clicks,exposed,card_exposed
    deck=[i for i in range(0,8)]+[ i for i in range(0,8)] #deck list contains numbers from 0 to 7 (2 times each)
    random.shuffle(deck)                                  #Numbers are placed randomly
    exposed=[False for i in range(16)]                    #No card is exposed yet(false state for every card)
    card_exposed=[]                                       #emptylist
    clicks=0
    turns=0

# define event handlers
def mouseclick(pos):
    global turns,clicks
    if clicks==0:
        card_exposed.append(pos[0]//card_width)           #storing the index of exposed card(clicked card) to end of the card_exposed list one by one.
        exposed[pos[0]//card_width]=True                  #the state becomes true for the this index in exposed list.
        clicks=1
        turns+=1
    elif clicks==1:
        if not (pos[0]//card_width in card_exposed):      #if index of exposed card(clicked card) is different than previous.
            card_exposed.append(pos[0]//card_width)       #then this index is stored at the end of card_exposed list.
            exposed[pos[0]//card_width]=True              #exposed state becomes true for this index as well.
            clicks+=1
    else:
        if not (pos[0]//card_width in card_exposed):           #if index of exposed card(clicked card) is not in card_exposed.
            if deck[card_exposed[-1]]!=deck[card_exposed[-2]]: #we compare the value at the indexes stored in card_exposed list in the main deck
                exposed[card_exposed[-1]]=False                #if not same values, exposed state becomes false for that index
                exposed[card_exposed[-2]]=False                #if not same values, exposed state becomes false for that index
                card_exposed.pop()                             #index stored is removed from list(card_exposed)
                card_exposed.pop()                             #index stored is removed from list(card_exposed)
            clicks=1
            turns+=1
            exposed[pos[0]//card_width]=True                   #if values are equal then the exposed state for those indexes become true.
            card_exposed.append(pos[0]//card_width)            # and that index is added to end of list card_exposed.





# cards are logically 50x100 pixels in size
def draw(canvas):
    label.set_text("Turns= " + str(turns))   #printing turns used
    for i in range(16):
        canvas.draw_line([card_width * (i % 15 + 1) , 0],[card_width * (i % 15 +1), 141], 1.8,"gold")   #drawing lines on canvas.
        if exposed[i]:  #if state is true for index i.
            canvas.draw_text(str(deck[i]) , [15 + card_width * i,100] ,70, "gold")  #exposing the number of the card.



# create frame and add a button and labels
frame = simplegui.create_frame("Memory", card_width * 16, 120)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")
frame.set_canvas_background("black")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()
