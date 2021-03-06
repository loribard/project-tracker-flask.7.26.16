from flask import Flask, request, render_template

import hackbright

app = Flask(__name__)


@app.route("/student")
def get_student():
    """Show information about a student."""

    github = request.args.get('github')

    first, last, github = hackbright.get_student_by_github(github)
    project_info = hackbright.get_grades_by_github(github)

    project_info = [{'title': title, 'grade':grade} for title, grade in project_info]
    

    html = render_template('student_info.html',
                            first=first,
                            last=last,
                            github=github,
                            project_info=project_info
                            )
                            

    return html

@app.route("/student-search")
def get_student_form():
    """ Show form for searching for a student."""

    return render_template("student_search.html")

@app.route("/student-add")
def student_add():
    """ Add a new student. """
    
    
    return render_template('add_student.html')
                           
                            
@app.route("/success", methods=['POST'])
def confirm_student_added():
    """Confirm student added to db """

    first = request.form.get('firstname')
    last = request.form.get('lastname')
    github = request.form.get('github')
    
    hackbright.make_new_student(first, last, github)
    
    return render_template('successful_add.html', 
                            github=github)

if __name__ == "__main__":
    hackbright.connect_to_db(app)
    app.run(debug=True)
