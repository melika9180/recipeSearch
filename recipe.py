import requests
import json

# Define function to search for books
def search_books(title):
    url = f"https://www.googleapis.com/books/v1/volumes?q={title}"
    response = requests.get(url)
    data = json.loads(response.text)
    return data['items']

# Define function to save book results to file
def save_to_file(books):
    with open("book_results.txt", "w") as file:
        for book in books:
            file.write(f"Title: {book['volumeInfo']['title']}\n")
            file.write(f"Author(s): {', '.join(book['volumeInfo']['authors'])}\n")
            file.write(f"Published Date: {book['volumeInfo']['publishedDate']}\n")
            file.write(f"Description: {book['volumeInfo']['description']}\n\n")


# Prompt user for book title to search
title = input("Enter book title to search: ")

# Call search_books function and print results to console
books = search_books(title)
for book in books:
    print(f"Title: {book['volumeInfo']['title']}")
    print(f"Author(s): {', '.join(book['volumeInfo']['authors'])}")
    print(f"Published Date: {book['volumeInfo']['publishedDate']}")
    print(f"Description: {book['volumeInfo']['description']}\n")

# Call save_to_file function to save results to file
save_to_file(books)
