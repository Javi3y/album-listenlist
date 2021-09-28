import sqlite3

conn = sqlite3.connect("albums.sqlite")
c = conn.cursor()
try:
    c.execute(
        """CREATE TABLE albums (
                title TEXT,
                artist TEXT,
                genre TEXT,
                release INTEGER,
                listend BOOL
            )"""
    )
    conn.commit()
except sqlite3.OperationalError:
    pass


def show_albums(albums):
    for i in range(len(albums)):
        if albums[i][4]:
            listend = "listend"
        else:
            listend = "not listend yet"
        print(
            f"no: {i}, title: {albums[i][0]}, artist: {albums[i][1]}, genre: {albums[i][2]}, release: {albums[i][3]}, {listend}"
        )


def select_album(albums):
    while True:
        try:
            inp = int(input("enter the number of the album you want to select: "))
            break
        except (ValueError, IndentationError):
            print("you should enter a number and it should be in the list")
    return albums[inp]


while True:
    print(
        """
        choose one of these options:
        random album: chooses a random album for you(filters included)
        remaining: show remaining albums
        all: show all albums
        listend to: show albums that you've listened to
        add album: add a new album to the list
        quit: you should know what it does :)
    """
    )
    inp = input("enter your option: ")
    if inp == "random album":
        pass
    elif inp == "remaining":
        pass
    elif inp == "all":
        c.execute("SELECT * FROM albums")
        albums = c.fetchall()
        show_albums(albums)
        print(select_album(albums))
    elif inp == "listend to":
        pass
    elif inp == "add album":
        while True:
            try:
                itr = int(
                    input("how many albums do you want to add to the database ?: ")
                )
                break
            except ValueError:
                print("you should add a number")
        for i in range(itr):
            title = input("add the title of the album: ")
            artist = input("add the name of the artist of the album: ")
            genre = input("add the genre of the album: ")
            while True:
                try:
                    release = int(input("enter the realease date of the album: "))
                    break
                except ValueError:
                    print("you should enter a number!!!!")
            c.execute(
                f"INSERT INTO albums VALUES ('{title}', '{artist}', '{genre}', {release}, FALSE)"
            )
            conn.commit()
            print("album added successfully")

    elif inp == "quit":
        break
    else:
        print("enter one of the valid options!!!!")
