class ArchiveItem:
    def __init__(self, uid, title, year):
        self.uid = uid
        self.title = title
        self.year = year

    def __str__(self):
        return "User ID: " +str(self.uid) + " Title: " +str(self.title) + " Year: " +str(self.year)

    def __eq__(self, other):
        return self.uid == other.uid

    def is_recent(self, n):
        if self.year >= (2025 - n):
            return True


class Book(ArchiveItem):
    def __init__(self, uid, title, year, author, pages):
        self.author = author
        self.pages = pages
        ArchiveItem.__init__(self, uid, title, year)

    def __str__(self):
        return "Book -> " + "User ID: " +str(self.uid) + " Title: " +str(self.title) + " Year: " +str(self.year) + " Author: " +str(self.author) + " Pages: " +str(self.pages)


class Article(ArchiveItem):
    def __init__(self, uid, title, year, journal, doi):
        self.journal = journal
        self.doi = doi
        ArchiveItem.__init__(self, uid, title, year)

    def __str__(self):
        return "Article -> " + "User ID: " +str(self.uid) + " Title: " +str(self.title) + " Year: " +str(self.year) + " Journal: " +str(self.journal) + " DOI: " +str(self.doi)


class Podcast(ArchiveItem):
    def __init__(self, uid, title, year, host, duration):
        self.host = host
        self.duration = duration
        ArchiveItem.__init__(self, uid, title, year)

    def __str__(self):
        return "Podcast -> " + "User ID: " +str(self.uid) + " Title: " +str(self.title) + " Year: " +str(self.year) + " Host: " +str(self.host) + " Duration: " +str(self.duration)

def save_to_file(items, filename):
    with open(filename, 'w') as f:
        for item in items:
            if isinstance(item, Book):
                f.write(str(item) + "\n")

            elif isinstance(item, Article):
                f.write(str(item) + "\n")

            elif isinstance(item, Podcast):
                f.write(str(item) + "\n")

def load_from_file(filename):
    items = []
    with open(filename, 'r') as f:
        for line in f:
            parts = line.strip().split(',')
            type = parts[0]

            if type == "Book":
                items.append(Book(*parts[1:]))

            elif type == "Article":
                items.append(Article(*parts[1:]))

            elif type == "Podcast":
                items.append(Podcast(*parts[1:]))

    return items

items = [
    Book("B001", "Book1", 2022, "ED", 345) ,
    Book("B002", "Book2", 2003, "ED", 298) ,
    Article("A001", "Article1", 2024, "J1", "DOI1") ,
    Article("A002", "Article2", 2025, "J2", "DOI2") ,
    Podcast("P001", "Podcast1", 2003, "ED", 345) ,
    Podcast("P002", "Podcast2", 2005, "ED", 345)
]

save_to_file(items, "archiveItems.txt")

loaded_items = load_from_file("archiveItems.txt")

for item in loaded_items:
    print(item)


