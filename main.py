# Задание 1
def get_books(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.read().strip().split('\n')[1:]
    parse_line = lambda parts: [
        parts[0],              # isbn
        parts[1],              # title
        parts[2],              # author
        int(parts[3]),         # quantity
        float(parts[4])        # price
    ]
    return list(map(lambda line: parse_line(line.split('|')), lines))

# Задание 2
def filtered_books(books, search_str):
    filtered = filter(lambda b: search_str.lower() in b[1].lower(), books)
    transform = lambda b: [
        b[0],                  # isbn
        f"{b[1]}, {b[2]}",     # title, author вместе
        b[3],                  # quantity
        b[4]                   # price
    ]
    return list(map(transform, filtered))

# Задание 3
def get_totals(books):
    return list(map(lambda b: (b[0], round(b[2] * b[3], 2)), books))

# Проверка
if __name__ == "__main__":

    books = get_books("books.csv")
    print("Все книги")
    print(*books, sep="\n")
    
    print("\n Книги с Python")
    py_books = filtered_books(books, "python")
    print(*py_books, sep="\n")
    
    print("\n Общая стоимость книг по отдельности")
    totals_py = get_totals(py_books)
    print(*totals_py, sep="\n")

    total_sum_all = sum(map(lambda b: b[3] * b[4], books))
    print("\n")
    print(f"Итого за все книги: {round(total_sum_all, 2)}")