
#To add a new story, add your story details to the end of each line.
#It's very important that any details you add in this screen line up.
#The third entry in each list all refer to story number 3, "The Operative".
init -10 :
    define books.stories.x = 5
    $books.stories.sid = []
    $books.stories.title = []
    $books.stories.forbook = []
    $books.stories.numseason = []
    $books.stories.seasonlength = []
    $books.stories.numepisode = []
    $books.stories.tag = []
    $books.stories.nameablecharacters = []
    $books.names = {"hiflmcfn":"Siobhan", "hiflmcln":"Ryan"}
#Your story id is just a shorter, less pretty version of the actual name that's displayed.
#If your story was called, for example, The Sorceress, then you'd do this:

#define books.stories.id = ["ghost", "djinn", "operative", "sorceress"]
#define books.stories.title = ["The Ghost", "The Djinn", "The Operative", "The Sorceress"]


#forbook is used to determine which UI to use, as well as which menu to place the story in.
#Add the desired book to the end of this list too.


#Havenfall is for Lovers: hifl
#Villainous Nights: VN
#Love & Legends: ll

#The number of seasons you currently have, the number of episodes that will be in each season, and the total episodes you have
#installed.
