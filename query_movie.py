import sqlite3

def run_query():
    conn = sqlite3.connect('movies.db')
    c = conn.cursor()

    print("\n🎬 Welcome to Movie Selector!\n")
    print("Choose your filter:")
    print("1. By Year\n2. By Genre\n3. By Director\n4. By Rating\n5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        year = input("Enter year: ")
        c.execute("SELECT * FROM movies WHERE year=?", (year,))
    elif choice == '2':
        genre = input("Enter genre: ")
        c.execute("SELECT * FROM movies WHERE genre LIKE ?", ('%' + genre + '%',))
    elif choice == '3':
        director = input("Enter director name: ")
        c.execute("SELECT * FROM movies WHERE director LIKE ?", ('%' + director + '%',))
    elif choice == '4':
        rating = input("Enter minimum rating: ")
        c.execute("SELECT * FROM movies WHERE rating >= ?", (rating,))
    elif choice == '5':
        print("Goodbye!")
        return
    else:
        print("Invalid choice")
        return

    results = c.fetchall()
    if results:
        print("\nResults:\n")
        for row in results:
            print(f"{row[1]} ({row[2]}) - {row[3]} - {row[4]} - Rating: {row[5]}")
    else:
        print("No results found.")
    
    conn.close()

run_query()
