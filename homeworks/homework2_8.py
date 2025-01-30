import sqlite3

def high_grade_views():
    try:
        conn = sqlite3.connect('UsersGrades.db')
        cursor = conn.cursor()

        cursor.execute("SELECT MAX(grade) FROM grades")
        highest_grade = cursor.fetchone()[0]

        conn.close()

        if highest_grade is not None:
            return {'highest_grade': highest_grade}
        else:
            return {'error': 'No grades available'}

    except sqlite3.Error as e:
        return {'error': f'Database error: {e}'}

print(high_grade_views())
