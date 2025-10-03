sql="""
create table books(
    id bigserial primary key,
    title varchar(100) not null,
    Author varchar(100) not null

);

INSERT INTO books (title, author) VALUES
('To Kill a Mockingbird', 'Harper Lee'),
('1984', 'George Orwell'),
('Pride and Prejudice', 'Jane Austen'),
('The Great Gatsby', 'F. Scott Fitzgerald'),
('Moby Dick', 'Herman Melville'),
('War and Peace', 'Leo Tolstoy'),
('The Catcher in the Rye', 'J.D. Salinger'),
('Crime and Punishment', 'Fyodor Dostoevsky'),
('The Hobbit', 'J.R.R. Tolkien'),
('Brave New World', 'Aldous Huxley'),
('The Odyssey', 'Homer'),
('The Iliad', 'Homer'),
('Ulysses', 'James Joyce'),
('Don Quixote', 'Miguel de Cervantes'),
('The Brothers Karamazov', 'Fyodor Dostoevsky'),
('Anna Karenina', 'Leo Tolstoy'),
('Fahrenheit 451', 'Ray Bradbury'),
('Jane Eyre', 'Charlotte Brontë'),
('Wuthering Heights', 'Emily Brontë'),
('The Divine Comedy', 'Dante Alighieri'),
('Les Misérables', 'Victor Hugo'),
('The Count of Monte Cristo', 'Alexandre Dumas'),
('Dracula', 'Bram Stoker'),
('Frankenstein', 'Mary Shelley'),
('The Picture of Dorian Gray', 'Oscar Wilde'),
('Hamlet', 'William Shakespeare'),
('Macbeth', 'William Shakespeare'),
('Romeo and Juliet', 'William Shakespeare'),
('A Tale of Two Cities', 'Charles Dickens'),
('Great Expectations', 'Charles Dickens'),
('David Copperfield', 'Charles Dickens'),
('Oliver Twist', 'Charles Dickens'),
('The Old Man and the Sea', 'Ernest Hemingway'),
('For Whom the Bell Tolls', 'Ernest Hemingway'),
('The Sun Also Rises', 'Ernest Hemingway'),
('The Metamorphosis', 'Franz Kafka'),
('The Trial', 'Franz Kafka'),
('The Castle', 'Franz Kafka'),
('The Stranger', 'Albert Camus'),
('The Plague', 'Albert Camus'),
('One Hundred Years of Solitude', 'Gabriel García Márquez'),
('Love in the Time of Cholera', 'Gabriel García Márquez'),
('The Alchemist', 'Paulo Coelho'),
('Veronika Decides to Die', 'Paulo Coelho'),
('Harry Potter and the Philosopher\'s Stone', 'J.K. Rowling'),
('Harry Potter and the Chamber of Secrets', 'J.K. Rowling'),
('Harry Potter and the Prisoner of Azkaban', 'J.K. Rowling'),
('The Lord of the Rings: The Fellowship of the Ring', 'J.R.R. Tolkien'),
('The Lord of the Rings: The Two Towers', 'J.R.R. Tolkien');




select author , count(*) from books group by author having count(*)>1;"""