import random

def roll_dice(*args, **kwargs):
    results = []

    for arg in args:
        results.append(random.randint(1, arg))

    total = 0
    for result in results:
        total += result
    
    total += kwargs.get('modifier', 0)

    print(kwargs.get('player_name', 'guest'))

    if kwargs.get('verbose'):
        for result in results:
            print(result)

    return total


print(f"Total: {roll_dice(16,16,16,16,16, player_name='Spotty', verbose=True)}")