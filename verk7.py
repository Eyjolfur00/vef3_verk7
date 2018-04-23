from bottle import *

@route("/")
def index():
    return template("verk7.tpl")


@get("/data")
def data():
    nafn = request.query.get("nafn")
    lykilord = request.query.get("lykilord")
    nafn = nafn.lower()
    lykilord = lykilord.lower()
    if nafn == "admin" and lykilord == "admin":
        response.set_cookie("admin","ok")
    else:
        return template("villa.tpl")

    if request.get_cookie("admin"):
        return template("admin_site.tpl")





    
@route("/setcookie")
def index():
    response.set_cookie("Kaka","nammikaka")
    return "búa til köku"

@route("/deletecookie")
def index():
    response.set_cookie("Kaka","", expires=0)
    return "Kakan er farin"






@route('/Myndir/<filename>')
def server_static(filename):
    return static_file(filename, root="./Myndir")

run()
