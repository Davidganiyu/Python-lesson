def library_management_system(book):
    if book == "Available":
        return "The book is available for borrowing."
    else:
        return "The book is currently unavailable."
    
book = "Available"
status = library_management_system(book)
print(status)