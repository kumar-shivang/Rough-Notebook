from flask import Flask
from flask import render_template
from flask import request
import matplotlib.pyplot as plt
from csv import reader as read_csv
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
        plt.clf()
        plt.hist(marks)
        plt.xlabel("Marks")
        plt.ylabel("Probability")
        plt.savefig("static/histogram.png")

app = Flask(__name__)
@app.route('/',methods = ["GET","POST"])
def hello_world():
    if request.method == "GET":
        return render_template("form.html")
    elif request.method == "POST":
        dict = request.form
        data = collect_data()
        course_id_set = set([i[1] for i in data])
        student_id_set = set([i[0] for i in data])
        if dict["ID"] == "student_id" and int(dict["id_value"]) in student_id_set:
            student_id = int(dict["id_value"])
            title = "Student Data"
            student_data = list(filter(lambda i:i[0]==student_id,data))
            marks = [i[2] for i in student_data]
            total_marks = sum(marks)
            return render_template("template.html",title=title,student_data=student_data,total_marks=total_marks)

        elif dict["ID"] == "course_id" and int(dict["id_value"]) in course_id_set:
            title = "Course Data"
            course_id = int(dict["id_value"])
            course_data = list(filter(lambda i:i[1]==course_id,data))
            marks = [i[2] for i in course_data]
            create_plot(marks)
            title = "Course Data"
            mean = sum(marks)/len(marks)
            max_marks = max(marks)
            return render_template("template.html",title=title,mean=mean,max_marks=max_marks)
            
        else:
            return render_template("template.html",title = "Something went wrong")
    else:
        return render_template("template.html",title = "Something went wrong")
    
if __name__=="__main__":
    app.debug = True
    app.run()