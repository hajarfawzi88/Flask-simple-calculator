from flask import Flask , render_template,url_for,request
from math import sin,cos,tan,sqrt,pow
 

app=Flask(__name__)

##creating roots=links=URL
#main route
@app.route("/")

def main():
    return render_template("index.html")

@app.route("/advanced")
def advanced():
    return render_template("advanced.html")
@app.route("/calculate_advanced",methods=["post"])
def calculate_advanced():
    first=int(request.form["first_number"])
    operat=request.form["operations"]
    if operat=="cosine":
        result=cos(first) 
    elif operat=="sin":
        result=sin(first) 
    elif operat=="tan":
        result=tan(first) 
    elif operat=="^2":
        result=pow(first,2)
    elif operat=="sqrt":
        result=sqrt(first)
    else:
        return "Sorry Something went wrong"
    return render_template("advanced.html",result=result)

@app.route("/simple")
def simple():
    return render_template("simple.html")

@app.route("/calculate",methods=["post"])
def calculate():
    first=int(request.form["first_number"])
    second=int(request.form["second_number"])
    operat=request.form["operations"]
    if operat=="add":
        result=first + second
    elif operat=="subtract":
        result=first - second
    elif operat=="multiply":
        result=first * second
    elif operat=="divide":
        result=first / second
    else:
        return "Sorry Something went wrong"
    return render_template("simple.html",result=result)



if __name__=="__main__":
    app.run(debug=True)