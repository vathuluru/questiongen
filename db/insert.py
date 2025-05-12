import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('C:\\Database\\Sqldb\\question_bank.db')
cursor = conn.cursor()

# Insert data into Grade table
cursor.execute('''
INSERT OR IGNORE INTO Grade (grade_id, grade_section, school, school_board)
VALUES
    (7, 'Grade 7', 'ABC School', 'CBSE'),
    (8, 'Grade 8', 'ABC School', 'CBSE'),
    (9, 'Grade 9', 'XYZ School', 'ICSE'),
    (10, 'Grade 10', 'XYZ School', 'ICSE');
''')

# Insert data into Subject table
cursor.execute('''
INSERT OR IGNORE INTO Subject (subject_name, grade_id, school_board)
VALUES
    ('Math', 7, 'CBSE'),
    ('Physics', 7, 'CBSE'),
    ('Chemistry', 8, 'CBSE'),
    ('Math', 9, 'ICSE'),
    ('Physics', 10, 'ICSE'),
    ('Chemistry', 10, 'ICSE');
''')

# Insert data into Topic table
cursor.execute('''
INSERT OR IGNORE INTO Topic (topic_name, subject_name, grade_id, school_board)
VALUES
    ('Algebra', 'Math', 7, 'CBSE'),
    ('Newton Laws', 'Physics', 7, 'CBSE'),
    ('Periodic Table', 'Chemistry', 8, 'CBSE'),
    ('Geometry', 'Math', 9, 'ICSE'),
    ('Thermodynamics', 'Physics', 10, 'ICSE'),
    ('Organic Chemistry', 'Chemistry', 10, 'ICSE');
''')

# Insert data into SubTopic table
cursor.execute('''
INSERT OR IGNORE INTO SubTopic (subtopic_name, topic_name, subject_name, grade_id, school_board)
VALUES
    ('Linear Equations', 'Algebra', 'Math', 7, 'CBSE'),
    ('First Law of Motion', 'Newton Laws', 'Physics', 7, 'CBSE'),
    ('Elements and Symbols', 'Periodic Table', 'Chemistry', 8, 'CBSE'),
    ('Triangles', 'Geometry', 'Math', 9, 'ICSE'),
    ('Heat Transfer', 'Thermodynamics', 'Physics', 10, 'ICSE'),
    ('Hydrocarbons', 'Organic Chemistry', 'Chemistry', 10, 'ICSE');
''')

# Insert data into Question table
cursor.execute('''
INSERT OR IGNORE INTO Question (question_id, grade_id, subject_name, school_board, topic_name, subtopic_name, question_text, complexity, answer, option_a, option_b, option_c, option_d)
VALUES
    (NULL, 7, 'Math', 'CBSE', 'Algebra', 'Linear Equations', 'Solve for x: 2x + 3 = 7', 'Easy', '2', '1', '2', '3', '4'),
    (NULL, 7, 'Physics', 'CBSE', 'Newton Laws', 'First Law of Motion', 'What does the first law of motion state?', 'Medium', 'Inertia', 'Force', 'Inertia', 'Acceleration', 'Momentum'),
    (NULL, 8, 'Chemistry', 'CBSE', 'Periodic Table', 'Elements and Symbols', 'What is the symbol for Sodium?', 'Easy', 'Na', 'Na', 'S', 'N', 'So'),
    (NULL, 9, 'Math', 'ICSE', 'Geometry', 'Triangles', 'What is the sum of angles in a triangle?', 'Easy', '180', '90', '180', '360', '270'),
    (NULL, 10, 'Physics', 'ICSE', 'Thermodynamics', 'Heat Transfer', 'What is the SI unit of heat?', 'Medium', 'Joule', 'Calorie', 'Joule', 'Watt', 'Newton'),
    (NULL, 10, 'Chemistry', 'ICSE', 'Organic Chemistry', 'Hydrocarbons', 'What is the simplest hydrocarbon?', 'Easy', 'Methane', 'Methane', 'Ethane', 'Propane', 'Butane');
''')

# Commit changes and close connection
conn.commit()
conn.close()