from flask import Flask, render_template, request

app = Flask(__name__) #creates app object from file

@app.route('/')
def landing():
    return render_template('landing.html')

@app.route('/ask', methods=["GET", "POST"])
def my_form_post():
    if request.method == "POST":
        userQ = request.form['userQuestion']
        print(userQ)
        return userQ
    else:
        return render_template('ask.html')
    

@app.route('/info')
def info():
    return render_template('info.html')

#---------------0INFORMATION PAGE ROUTES----------------#
@app.route('/info-generalperiod')
def info_gp():
    return render_template('gp.html')

@app.route('/info-sex')
def info_sx():
    return render_template('sx.html')

@app.route('/info-pregnancy')
def info_pg():
    return render_template('pg.html')

@app.route('/info-contraceptives')
def info_cp():
    return render_template('cp.html')

@app.route('/info-mentalhealth')
def info_mh():
    return render_template('mh.html')

@app.route('/info-menstrualproducts')
def info_mp():
    return render_template('mp.html')

#--------------------------------------------------------#

@app.route('/help_out')
def help():
    return render_template('help.html')

@app.route('/test')
def test():
    return render_template('test3.html') 


if __name__ == "__main__": #'main' is the name of the file
    app.run(debug=True)
