import io

def q1():
    r = range(0,5)
    l = [i for i in r]
    l = [[i for i in r] for j in r]
    print (l)

# NB: I had to look this up. I would not have come up with that on my own
def q2():
    l = [[1,2,3],[4,5,6],[7,8,9]]
    out = [j for sub in l for j in sub]
    print (out)

def q3():
    planets = [['Mercury', 'Venus', 'Earth'], ['Mars', 'Jupiter', 'Saturn'], ['Uranus', 'Neptune', 'Pluto']]
    out = [p for sub in planets for p in sub if len(p) < 6]
    print (out)

def q4():
    original={'Name':'iphone5','Brand':'Apple','Color':'silver'}
    out = {v:k for k,v in original.items()}
    print (out)


q1()
q2()
q3()
q4()
