import sqlite3

# Database schema and DDL statements for a Question Bank

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('C:\Database\Sqldb\question_bank.db')
cursor = conn.cursor()

# Create tables
cursor.execute('''
CREATE TABLE IF NOT EXISTS Grade (
    grade_id INTEGER PRIMARY KEY,
    grade_section TEXT NOT NULL UNIQUE,
    school TEXT NOT NULL,
    school_board TEXT NOT NULL
);
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Subject (
    subject_name TEXT NOT NULL,
    grade_id INTEGER NOT NULL,
    school_board TEXT NOT NULL,
    PRIMARY KEY (subject_name, grade_id, school_board),
    FOREIGN KEY (grade_id) REFERENCES Grade (grade_id)
);
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Topic (
    topic_name TEXT NOT NULL,
    subject_name TEXT NOT NULL,
    grade_id INTEGER NOT NULL,
    school_board TEXT NOT NULL,
    PRIMARY KEY (topic_name, subject_name, grade_id, school_board),
    FOREIGN KEY (subject_name, grade_id, school_board) REFERENCES Subject (name, grade_id, school_board)
);
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS SubTopic (
    subtopic_name TEXT NOT NULL,
    topic_name TEXT NOT NULL,
    subject_name TEXT NOT NULL,
    grade_id INTEGER NOT NULL,
    school_board TEXT NOT NULL,
    PRIMARY KEY (subtopic_name, topic_name, subject_name, grade_id, school_board),
    FOREIGN KEY (topic_name, subject_name, grade_id, school_board) REFERENCES Topic (name, subject_name, grade_id, school_board)
);
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Question (
    question_id INTEGER PRIMARY KEY AUTOINCREMENT,
    grade_id INTEGER NOT NULL,
    subject_name TEXT NOT NULL,
    school_board TEXT NOT NULL,
    topic_name TEXT NOT NULL,
    subtopic_name TEXT NOT NULL,
    question_text TEXT NOT NULL,
    complexity TEXT NOT NULL CHECK (complexity IN ('Easy', 'Medium', 'Hard')),
    answer TEXT NOT NULL,
    option_a TEXT NOT NULL,
    option_b TEXT NOT NULL,
    option_c TEXT NOT NULL,
    option_d TEXT NOT NULL,
    FOREIGN KEY (grade_id) REFERENCES Grade (grade_id),
    FOREIGN KEY (subject_name, grade_id, school_board) REFERENCES Subject (subject_name, grade_id, school_board),
    FOREIGN KEY (topic_name, subject_name, grade_id, school_board) REFERENCES Topic (topic_name, subject_name, grade_id, school_board),
    FOREIGN KEY (subtopic_name, topic_name, subject_name, grade_id, school_board) REFERENCES SubTopic (subtopic_name, topic_name, subject_name, grade_id, school_board)
);
''')

# Commit changes and close connection
conn.commit()
conn.close()

# Function to randomly select questions based on filters
def get_random_questions(grade, subject, topic, subtopic, num_questions=1):
    conn = sqlite3.connect('question_bank.db')
    cursor = conn.cursor()

    query = '''
    SELECT question_text, complexity, answer
    FROM Question
    WHERE grade_id = (SELECT grade_id FROM Grade WHERE name = ?)
      AND subject_name = ?
      AND topic_name = ?
      AND subtopic_name = ?
    ORDER BY RANDOM()
    LIMIT ?;
    '''
    cursor.execute(query, (grade, subject, topic, subtopic, num_questions))
    questions = cursor.fetchall()

    conn.close()
    return questions