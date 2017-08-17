ten_things = "apples oranges crows telephone light sugar"

print "wai there's not 10 things in that list,let's fix that."

stuff = ten_things.split(' ')
more_stuf = ["day","night","song","frisbee","frisbee","corn","banana","girl","boy"]

while len(stuff) != 10:
    next_one =more_stuf.pop()
    print "adding: ",next_one
    stuff.append(next_one)
    print "there's %d items now." %len(stuff)

print "there we go :",stuff

print "let's do some things with stuff."

print stuff[1]
print stuff[-1]
print stuff.pop(2)
print ' '.join(stuff)
print stuff
print '#'.join(stuff[3:5])