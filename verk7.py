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


run(host="0.0.0.0", port=os.environ.get("PORT"))
