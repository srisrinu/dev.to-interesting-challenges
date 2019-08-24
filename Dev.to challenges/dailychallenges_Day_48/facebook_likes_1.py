from collections import defaultdict
def show_likes(persons):
    messages=defaultdict(lambda:"%s,%s and %d likes",{0:"no one likes",1:"%s likes",2:"%s amd %s likes",3:"%s,%s and %s likes"})
    likes_quantity=len(persons)
    content=messages[likes_quantity]
    if(likes_quantity>3):
        return(content %(persons[0],persons[1],len(persons[2:])))
    return(content %(tuple(persons)))
persons=["srinu","prudvi","SR","srinivas"]
print(show_likes(persons))
    