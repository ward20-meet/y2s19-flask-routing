from databases import *
from flask import Flask, render_template, url_for
app = Flask(__name__)

@app.route('/')
def home():
	id_number=4
	return render_template('home.html')

add_student("Ward", 2003, False)


@app.route('/student/<int:student_id>')
def display_student(student_id):
	student = query_by_id(student_id)
	return render_template('student.html', id_number = student_id , student=student)

if __name__ == '__main__':
    app.run(debug=True)
