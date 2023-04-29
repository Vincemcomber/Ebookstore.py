# I got massive help from my friends Thomas, Mpho and Andile to solve this problem.

# Import sqlite3.
# Utility module for working with Database.  
import sqlite3    

# Create or opens a file called ebookstore with a SQLite3 database.
# Get a cursor object.
db = sqlite3.connect('ebookstore.db')
cur = db.cursor()


# Define a function to add a new book to the database.
def add_book():
    id = input('Please enter the id of the book you want to add: ')  
    title = input('Please enter the Book Title: ')     
    author = input('Please enter the Author Name: ')     
    qty = int(input('Please enter the quantity of {} available: '.format(title)))
    # Insert the values
    cur.execute('INSERT INTO books(title, author, qty) values (?, ?, ?)', (title, author, qty))  
    # Save the changes
    db.commit()      
    

# Define a function to update the details of an existing book in the database.
def update_book():     
    id = input('Please enter the id of book that you want to update: ')     
    title = input('Please enter the new title: ')     
    author = input('Please enter the updated author name: ')     
    qty = int(input('Please enter the new quantity: '))     
    # Set the new values
    cur.execute('UPDATE books SET title=?, author=?, qty=? WHERE id=?', (title, author, qty, id))    
    # Save the changes.
    db.commit()   
    

# Define a function to delete/remove a book from the database.   
def delete_book():     
    id = input('Enter the book id to delete: ')    
    cur.execute('SELECT title from books WHERE id=?', (id,))     
    # Fetch only one entry from above executed statement. 
    results = cur.fetchone()        
    # Print the results.
    print(results)         
    if results:         
        choice = input('Are you sure, you want to delete the book with id {}(1/0): '.format(results[0]))            
    else:         
        print('No book with the given id found')         
        return  
                       
    if choice == '1':         
        cur.execute('DELETE FROM books WHERE id=?', (id,))     
        db.commit()   
            

# Define a function to search/retrieve book data from the database.
def search_book(): 
    author = input('Please input the author name to search book for: ')      
    cur.execute('SELECT * FROM books where author like ?', (author,))     
    # Fetchall results from above statement. 
    results = cur.fetchall()            
    if results:         
        for row in results:             
            print(str(row[0]) + ' | ' + row[1] + ' | ' + row[2] + ' | ' + str(row[3]))                 
    else:         
        print('No books found')   
            

# The main function of the program.           
if __name__ == '__main__':     
    db = sqlite3.connect('ebookstore.db')     
    cur = db.cursor()     
    cur.execute('CREATE TABLE IF NOT EXISTS books(' 'id integer primary key AUTOINCREMENT,' 
                                                     'Title varchar(255),'                
                                                     'Author varchar(30),'                
                                                     'Qty integer)')      

# Using the while loop to  present the user with the following menu:                                                    
while True:         
    choice = input('1. Add Book\n'                        
                   '2. Update Book\n'                        
                   '3. Delete Book\n'                        
                   '4. Search Book\n'                        
                   '0. Exit: ') 
            
    # Get book details from user and add it to the list.         
    if choice == '1':             
        add_book() 

    # Get book id from user, search for the book and update its details.    
    elif choice == '2':             
        update_book() 

    # Get book id from user and delete/remove it from the list.    
    elif choice == '3':             
        delete_book() 

    # Get book id from user and display book details.   
    elif choice == '4':             
        search_book()

    # To break and exit the program.    
    elif choice == '0':             
        break            
    else:             
        print('Wrong Choice, Try again...')

# Print the thank you message.        
print('Thank you for visiting eBookStore!!')
     
# Close the database connection
db.close()

