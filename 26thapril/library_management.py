class Library:
    book=["The fault in our stars","Abang","Citadel"]
    author_book={
        "Pablo":["escobar","escobar returns","escobar part 3"]
    }
    def getAllBooks():
        for i in book:
            print(i)
    def addBook():
        book.append("oops")
    def getBookByAuthorName(authorName):
        for key in author_book:
            if key==authorName:
                print(author_book[key])
    def sortBooksInTopologicalOrder():
        book.sort()
        print(book)
    def getAllSubcribers():
        pass
    def getAllEarnings():
        pass
    def getUnavailableBooks():
        pass
class MyLibrary(Library):
    def getFaviourtBook():
        pass

