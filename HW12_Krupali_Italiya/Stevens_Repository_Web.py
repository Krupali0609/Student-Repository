"""This .py file is all about implementing University, Student, Instructor and major """ 

"""This is importing some of the in-built functions"""
from flask import Flask, render_template
import sqlite3
from typing import Dict
from HW08_Krupali_Italiya import file_reader

app:Flask=Flask(__name__)
"""Take the name from here"""
DB_FILE: str ="C:/Users/0609k/OneDrive/Desktop/Python/HW12_Krupali_Italiya/810_start_k.db"


@app.route("/completed")
def completed_course()->str:
    """Decorator for the route and try and except block"""
    try:
        db: sqlite3.Connection = sqlite3.connect(DB_FILE)
        query: str = "SELECT s.Name, s.CWID, g.Course, g.Grade, i.Name AS 'Instructor' " \
                        "FROM grades2 g JOIN students2 s ON g.StudentCWID = s.CWID " \
                        "JOIN instructors2 i ON g.InstructorCWID = i.CWID ORDER BY s.Name"    
    except sqlite3.OperationalError as e:
        print(e)

    data: Dict[str,str]=\
        [{"name": name,"cwid": cwid,"course": course , "grade":grade, "instructor": instructor}
            for name, cwid, course, grade, instructor in db.execute(query)]
    db.close()
    """Render the template from templates folder"""
    return render_template("student_summary.html",
                            title="Stevens Repository",
                            table_title="Student, Course, Grade and Instructor",
                            students=data )

"""excution starts from here"""
if __name__ == '__main__':    
    app.run(debug=True)

    
