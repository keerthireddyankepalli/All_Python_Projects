1. Game Development/TicTacToe
Tic Tac Toe - Python Game
A simple command-line based Tic Tac Toe game written in Python, where two players take turns to place their mark (X or O) in a 3x3 grid. The game ends when one player wins or the board is full (draw).

 Features
- Two-player mode (Player 1 and Player 2)
- 3x3 game board
- Win condition checking (horizontal, vertical, diagonal)
- Draw detection
- Input validation (prevents overwriting cells)

 Game Rules
- The game is played on a 3x3 grid.
- Player 1 uses X, Player 2 uses O.
- Players take turns to choose a position (1 to 9).
- The first player to align three symbols in a row (horizontally, vertically, or diagonally) wins.
- If all spots are filled with no winner, the game ends in a draw.

 How to Run
1. Make sure you have Python 3.x installed.
2. Open terminal/command prompt.
3. Navigate to the folder:
bash
cd Game_Development

4. Run the script:
bash
python TicTacToe.py

 Requirements
- Python 3.x  
(No external libraries needed)

Sample Output
   |   |   
-----------
   |   |   
-----------
   |   |   

Player 1, enter your move (1-9): 5

   |   |   
-----------
   | X |   
-----------
   |   |   

----------------------------------------------------------------------------

2-To-Do List
Here’s a complete README for your To-Do List Python project that includes an overview, features, usage, and technical details—all combined clearly:

---

 To-Do List (Python CLI App)

A simple command-line To-Do List application written in Python that helps users manage tasks efficiently. It allows you to add, view, mark, and remove tasks, while also saving your progress using JSON for persistence.

---

Features

- Add a new task with:
  - Title
  - Description
  - Due Date (in YYYY-MM-DD format)
- Remove existing tasks by title
- Mark tasks as completed
- View all current tasks along with their status
- Save and load tasks using a JSON file (data persistence)

---

 How It Works

Core Classes:
- *Task*: Represents each individual task with details like title, description, due date, and completion status.
- *TaskManager*: Maintains a list of all tasks, and supports operations like add, remove, mark complete, save, and load.

Main Flow:
- Loads tasks at startup (manager.load_tasks())
- Displays an interactive menu to the user
- Takes input to perform task operations
- Saves tasks before exiting (manager.save_tasks())

 Sample Menu
---- TO-DO LIST MENU ----
1. Add Task
2. Remove Task
3. Mark Task as Completed
4. Show All Tasks
5. Save and Exit
Data Storage (JSON)

Tasks are stored in a JSON file for persistence between runs. Each task is saved with:
json
{
  "title": "Sample Task",
  "description": "Do something important",
  "due_date": "2025-06-30",
  "completed": false
}
---
How to Run
Make sure Python is installed.
bash
python ToDoList.py

-----------------------------------------------------------------------------------------------
Thanks! Now that I’ve seen all parts of your chatbot, here’s a complete summary (README) combining everything:

---

 Simple NLTK Chatbot – Aneka

A basic Python chatbot named Aneka built using Natural Language Toolkit (NLTK). It reads a .txt file for responses and simulates conversation using tokenization, lemmatization, and simple matching.

 Features

- Greets users with custom inputs
- Understands and replies using a knowledge base (Act1Scene1.txt)
- Handles:
  - Greetings (hi, hello, etc.)
  - Thanks (thanks, thank you)
  - Exit (bye)
- Preprocesses text (tokenization, punctuation removal, lemmatization)
- Dynamic responses using sentence matching

How It Works

1. Text Loading: Reads a .txt file and stores sentences
2. Preprocessing:
   - Lowercasing
   - Removing punctuation
   - Lemmatizing
3. User Interaction Loop:
   - Matches greeting words
   - Otherwise, selects a suitable sentence from text file (not shown but expected to use similarity logic)
4. Custom Response:
   - “You're welcome” for thanks
   - “Bye!” on exit

 File Used
- Act1Scene1.txt: Source of all chatbot replies (loaded and tokenized)

How to Run
bash
pip install nltk


Then run:

bash
python chatbots.py

 Example
You: hi
Aneka: hello

You: who are you?
Aneka: [response from the text file]

You: bye
Aneka: Bye! Have a great time!

----------------------------------------------------------------------------------------------

Web Scraping Project - Book Data Extraction

This Python script scrapes book information from the website [books.toscrape.com](https://books.toscrape.com) and saves the extracted data into a CSV file.

Features

- Scrapes multiple pages (pages 1 to 4) of the book catalogue.
- Extracts the following details for each book:
  - Title
  - Star Rating
  - Price
- Saves the collected data into a CSV file named books.csv.

Requirements

Make sure you have the following Python libraries installed:

- requests — for sending HTTP requests
- beautifulsoup4 — for parsing HTML content
- pandas — for handling data and exporting to CSV

You can install these using pip:

bash
pip install requests beautifulsoup4 pandas

How to Run

Run the script using Python:

bash
python Webscraping.py

The script will create a file called books.csv in the same directory with the extracted book details.

Code Overview
- Sends requests to each page of the book catalogue.
- Parses the HTML content using BeautifulSoup.
- Finds all book articles and extracts the title, star rating, and price.
- Appends the data to a list and converts it into a pandas DataFrame.
- Exports the DataFrame to a CSV file.





