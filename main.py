class library:
  no_of_books = 5
  books = ["Python", "Java", "C++", "CSS", "HTMl"]

  def isbooks(self):
    print(f"Total books are {self.no_of_books} which are given below:-\n")
    for i in self.books:
      print(i)
    print("\n\n\n")
    # print(len(self.books))
    # print(self.no_of_books)

  def addbooks(self, bookname):
    self.books.append(bookname)
    if (len(self.books) > self.no_of_books):
      self.no_of_books += 1
      print(f"Total books are {len(self.books)} which are given below:-\n")
      for i in self.books:
        print(i)
    print("\n\n\n")
    # print(len(self.books))
    # print(self.no_of_books)

  def check(self):
    if (self.no_of_books == len(self.books)):
      print(f"Length of Books:{len(self.books)} are Equal to No of Books: {self.no_of_books}.")
    else:
      print(f"Length of Books:{len(self.books)} are Not Equal to No of Books:{self.no_of_books}.")


obj = library()
obj.isbooks()
obj.addbooks("C")
obj.addbooks("Webdevlopment")
obj.check()


