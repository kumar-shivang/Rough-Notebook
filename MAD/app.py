from csv import reader as read_csv
from jinja2 import Template
from sys import argv
import matplotlib.pyplot as plt
def main_template():
    return """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{title}}</title>
    <style>
        table,td,th{
            border:1px solid black;
        }
    </style>
</head>
<body>
    {% if title=="Course Data" %}
        <h1>Course Data</h1>
        <table>
            <tr><th>Average Marks</th><th>Maximum Marks</th></tr>
            <tr><td>{{mean}}</td><td>{{max_marks}}</td></tr>
        </table>
        <img src="./histogram.png" alt="histogram">

    {% elif title=="Student Data" %}
    <table>
        <tr><th>Student id</th>
        <th>Course id</th>
        <th>Marks</th></tr>
        {% for i in student_data %}
    <tr>
        <td>{{i[0]}}</td>
        <td>{{i[1]}}</td>
        <td>{{i[2]}}</td>
    </tr>
        {% endfor %}
        <tr><td>Total Marks</td><td colspan="2">{{total_marks}}</td></tr>
    </table>

    {% else %}
    <h1>Wrong Inputs</h1>
    <p>
        Something went wrong
    </p>
    {% endif %}
</body>
</html>
"""
def collect_data():
    data = []
    with open("./data.csv","r") as f:
        csvfile = read_csv(f)
        next(csvfile)
        for i in csvfile:
            data.append(i)
        for i in range(len(data)):
            data[i] = list(map(int,data[i]))
        return data

def create_plot(marks):
        plt.hist(marks)
        plt.xlabel("Marks")
        plt.ylabel("Probability")
        plt.savefig("histogram.png")

def write_course_template(course_id,data):
        course_data = list(filter(lambda i:i[1]==course_id,data))
        marks = [i[2] for i in course_data]
        create_plot(marks)
        title = "Course Data"
        mean = sum(marks)/len(marks)
        max_marks = max(marks)
        content = Template(main_template()).render(title=title,mean=mean,max_marks=max_marks)
        with open("./output.html","w") as f:
            f.write(content)
    
def write_student_template(student_id,data):
    student_data = list(filter(lambda i:i[0]==student_id,data))
    marks = [i[2] for i in student_data]
    total_marks = sum(marks)
    title = "Student Data"
    content = Template(main_template()).render(title=title,student_data=student_data,total_marks=total_marks)
    with open("./output.html","w") as f:
        f.write(content)

def write_error_template():
        content = Template(main_template()).render(title="Something Went Wrong")
        with open("./output.html","w") as f:
            f.write(content)


def main(argv):
    if argv[1]=="-c" and int(argv[2]) in {2001,2002,2003,2004}:
        course_id = int(argv[2])
        write_course_template(course_id,collect_data())
    elif argv[1]=="-s" and int(argv[2]) in {1001, 1002, 1003, 1004, 1005, 1009, 1007, 1008, 1000, 1060, 1090, 1080, 1030}:
        student_id = int(argv[2])
        write_student_template(student_id,collect_data())
    else:
        write_error_template()

if __name__ == "__main__":
    main(argv)

