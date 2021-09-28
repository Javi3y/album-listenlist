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


def filter_albums(albums):
    def release_filter(release, start, end):
        if start <= release <= end:
            return True

    while True:
        try:
            start = int(
                input(
                    "enter the start of the year you want to filter by(enter nothing for none): "
                )
            )
            end = int(
                input(
                    "enter the end of the year you want to filter by(enter nothing for none): "
                )
            )
        except ValueError:
            print("you should enter a number!!!!")
            
        if start:
            albums = list(
                filter(
                    lambda date: release_filter(date[3], start, float("inf")), albums
                )
            )
        if end:
            albums = list(filter(lambda date: release_filter(date[3], 0, end), albums))

        artist = input(
            "enter the name of the artist you want to filter by(enter nothing for none): "
        )
        if artist:
            albums = list(filter(lambda item: item[1] == artist), albums)

        genre = input(
            "enter the name of the genre you want to filter by(enter nothing for none): "
        )
        if genre:
            albums = list(filter(lambda item: item[2] == genre), albums)

        return albums


def show_albums(albums):
    if albums:
        for i in range(len(albums)):
            if albums[i][4]:
                listend = "listend"
            else:
                listend = "not listend yet"
            print(
                f"no: {i}, title: {albums[i][0]}, artist: {albums[i][1]}, genre: {albums[i][2]}, release: {albums[i][3]}, {listend}"
            )
        else:
            print("no albums available!!!!")


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
        show_albums(filter_albums(albums))
        if albums:
            print(select_album((albums)))
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
                    release = int(input("enter the release date of the album: "))
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
