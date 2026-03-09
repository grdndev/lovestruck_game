init -1 python:
    def addstory(story_id, story_name, story_book, story_seasonlength, seasons, episodes, nameablecharacters, tags = 0,):
        global books
        books.stories.sid.append(story_id) 
        books.stories.title.append(story_name)
        books.stories.forbook.append(story_book)
        books.stories.seasonlength.append(story_seasonlength)
        books.stories.numseason.append(seasons)
        books.stories.numepisode.append(episodes)
        books.stories.tag.append(tags)
        books.stories.nameablecharacters.append(nameablecharacters)
        for i in range(nameablecharacters):
            firstname = {str(story_id) + "fn" + str(i+1):"             "}
            lastname = {str(story_id) + "ln" + str(i+1):"             "}
            if mcdata.mcnames.get(str(story_id) + "fn" + str(i+1)) != None:
                firstname = {str(story_id) + "fn" + str(i+1):mcdata.mcnames[str(story_id) + "fn" + str(i+1)]}
                books.names.update(firstname)
            else:
                books.names.update(firstname)
            if mcdata.mcnames.get(str(story_id) + "ln" + str(i+1)) != None:
                lastname = {str(story_id) + "ln" + str(i+1):mcdata.mcnames[str(story_id) + "ln" + str(i+1)]}
                books.names.update(lastname)
            else:
                books.names.update(lastname)
