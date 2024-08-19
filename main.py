from copy import deepcopy
from pickle import dump, load
class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
    def __repr__(self):
        return f'"{self.title}" by {self.author} ({self.year})'
def saveBooks(books):
    with open('books.txt', 'wb') as file:
        dump(books, file)
def loadBooks():
    with open('books.txt', 'rb') as file:
        return load(file)

books =  loadBooks()

def printBooks(books):
    for book in books:
        print(book)
def sortBooksByTitle(books):
    if len(books) <= 1:
        return books

    pivot = books[len(books) // 2]
    left = [i for i in books if len(i.title) < len(pivot.title)]
    middle = [i for i in books if len(i.title) == len(pivot.title)]
    right = [i for i in books if len(i.title) > len(pivot.title)]
    return sortBooksByTitle(left) + middle + sortBooksByTitle(right)
def sortBooksByAuthor(books):
    if len(books) <= 1:
        return books

    mid = len(books) // 2
    left = sortBooksByAuthor(books[:mid])
    right = sortBooksByAuthor(books[mid:])
    return merge(left, right)
def merge(left, right):
    sortedBooks = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i].author < right[j].author:
            sortedBooks.append(left[i])
            i += 1
        else:
            sortedBooks.append(right[j])
            j += 1
    while i < len(left):
        sortedBooks.append(left[i])
        i += 1
    while j < len(right):
        sortedBooks.append(right[j])
        j += 1
    return sortedBooks
def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left].year > arr[largest].year:
        largest = left

    if right < n and arr[right].year > arr[largest].year:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)
def sortBooksByYear(arr):
    copyBooks = deepcopy(arr)
    n = len(arr)
    sortedBooks = []
    for i in range(n // 2 - 1, -1, -1):
        heapify(copyBooks, n, i)

    for i in range(n - 1, 0, -1):
        copyBooks[i], copyBooks[0] = copyBooks[0], copyBooks[i]
        sortedBooks.insert(0,copyBooks[i])
        heapify(copyBooks, i, 0)
    return sortedBooks


def searchBook(books):
    title = input('Напишите название, или ее часть, книги: ')
    searchedBooks = []
    for book in books:
        for i in range(len(book.title)):
            if i == len(title):
                searchedBooks.append(book)
                break
            elif book.title[i] != title[i]:
                break
    if len(searchedBooks) == 0:
        return print('Книга не найдена')
    for book in searchedBooks:
        print(book)
def searchBookByAuthor(books):
    author = input('Напишите автора книги: ')
    searchedBooks = []
    for book in books:
        for i in range(len(book.author)):
            if i == len(author):
                searchedBooks.append(book)
                break
            elif book.author[i] != author[i]:
                break
    if len(searchedBooks) == 0:
        return print('Книга не найдена')
    for book in searchedBooks:
        print(book)
def removeBook(books):
    title = input('Напишите название книги, которую хотите удалить: ')
    for book in books:
        if book.title == title:
            books.remove(book)
            saveBooks(books)
            return print('Книга успешно удалена')
    return print('Книга не найдена')
def addBook(books):
    title = input('Введите название книги: ')
    author = input('Введите автора книги: ')
    year = int(input('Введите год издания книги: '))
    books.append(Book(title, author, year))
    saveBooks(books)

actions = {1, 5, 6, 7, 8}
specialActions = {2, 3, 4}
while True:
    actionNumber = int(input('''Выберите действие:
    1.Показать все книги
    2.Сортировать книги по названию
    3.Сортировать книги по автору
    4.Сортировать книги по году издания
    5.Найти книгу по названию
    6.Найти книгу по автору
    7.Добавить книгу
    8.Удалить книгу'''))
    actions = {1: printBooks, 2: sortBooksByTitle, 3: sortBooksByAuthor,4: sortBooksByYear,
               5: searchBook, 6: searchBookByAuthor, 7: addBook, 8: removeBook}
    if actionNumber in specialActions:
        printBooks(actions[actionNumber](books))
    elif actionNumber in actions:
        actions[actionNumber](books)
    else:
        break