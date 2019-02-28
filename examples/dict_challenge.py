################################
#
#  DICT Challenge
#
################################
from modules.utils import banner, nl

locations = {
    0: 'You\'re sitting in front of an iPad learning Python with Tim',
    1: 'You\'re standing at the end of a road in front of a dreary looking brick building.',
    2: 'You\'re at the top of a grassy hill overlooking the valley. The wind occassionally blows gently through.',
    3: 'You\'re inside the old well house beside the babbling brook.',
    4: 'You\'re down in the gully of the valley, walking along the quickly flowing stream.',
    5: 'You\'re in a dark, dark forest. It\'s near impossible to see in front of you.',
}

exits = {
    0: {'q': 0},
    1: {'w': 2, 'e': 3, 'n': 5, 's': 4, 'q': 0},
    2: {'n': 5, 'q': 0},
    3: {'w': 1, 'q': 0},
    4: {'n': 1, 'w': 2, 'q': 0},
    5: {'w': 2, 's': 1, 'q': 0},
}

vocabulary = {
    'north': 'n',
    'south': 's',
    'east': 'e',
    'west': 'w',
    'quit': 'q',
}

loc = 1
while True:
    available_exits = ', '.join(exits[loc].keys()).upper()
    
    nl()
    print(locations[loc])
    nl()
        
    if loc == 0:
        break
    
    direction = input('(' + available_exits + ') ')

    # parse using vocab
    if len(direction) > 1:
        words = direction.split()
        for word in words:
            if word.lower() in vocabulary:
                direction = vocabulary[word.lower()]

    if direction in exits[loc]:
        loc = exits[loc][direction]
    else:
        nl()
        print('*** You can\'t go that way')

