def show_likes(persons):
    messages={0:"no one  likes",1:"%s likes",2:"%s ,%s likes",3:"%s %s and %s likes",4:"%s,%s and %d likes"}
    likes_quantity=len(persons)
    content=messages.get(likes_quantity,messages[4])
    if(likes_quantity>3):
        return(content %(persons[0],persons[1],len(persons[2:])))
    return(content %(tuple(persons)))
persons=["srinu","prudvi","srinivas","SR"]
print(show_likes(persons))