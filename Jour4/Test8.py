def evenodd(number):
    '''Cette fonction prend un entier en argument et affiche pair ou impair'''
    if (number%2) == 0:
        print('Pair')
    else:
        print('impair')
evenodd(5)

print(evenodd.__doc__)