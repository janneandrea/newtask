
max_chapters = -1
book_with_max = ""

with open("books_and_chapters.txt") as books_file:

    # Iterate through the file one line at a time
    for line in books_file:
        # Split up the line based on the ":"
        parts = line.split(":")

        # Get the book and strip off any leading/trailing whitespace
        book = parts[0].strip()

        # Get the number of chapters as an integer
        chapters = int(parts[1])

        # Get the volume of scripture and strip off any leading/trailing whitespace
        scripture = parts[2].strip()

        print(f"Scripture: {scripture}, Book: {book}, Chapters: {chapters}")
