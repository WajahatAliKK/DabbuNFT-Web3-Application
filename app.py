from flask import Flask, render_template, request, redirect, url_for, flash, session
import pandas as pd
from utils import *
import openpyxl

app = Flask(__name__, template_folder='templates', static_url_path='/static')
app.secret_key = "AhmedProjectNFT"


# ------------------------------------ Main Pages Routes------------------------------------


@app.route("/")
def index():
    Christmasdata = get_coloured(changing=True)
    Standarddata = get_data_ForStandar(changing=True)
    Characterdata = get_Character(changing=True)
    return render_template('index.html', data=Christmasdata, stddata=Standarddata, chardata=Characterdata)


@app.route("/single_product/<name>/<tknno>/<price>/<tkntype>/<tkndesc>/<pageno>/<rarity>", methods=['GET', 'POST'])
def single_product(name, tknno, price, tkntype, tkndesc, pageno, rarity):
    img_path = request.args.get('image_path')
    selected_category = request.args.get('category')
    temp = tkndesc[tkndesc.find('('):len(tkndesc)]
    minted = get_minted()
    tknno = get_Digits(tknno)
    if selected_category and selected_category == "Standard Token":
        relevant_images = get_data_ForStandar(changing=True, image_version=pageno[:len(pageno) - 1])[:8]


    else:
        relevant_images = get_data_ForSimilar(True, pageno, img_path)
        # print("Eroor")
    return render_template('single-product.html', name=str(name), tknno=str(tknno), price=str(price),
                           image_path=str(img_path),
                           tkntype=str(tkntype), tkndesc=temp, relevant_images=relevant_images, pageno=float(pageno),
                           selected_category=selected_category, rarity=str(rarity), mint=minted)


@app.route("/product")
def product():
    datas = get_data_final(changing=True)
    return render_template('products.html', datas=datas)


@app.route("/original")
def original():
    datas = get_Orignial(changing=True)
    return render_template('products.html', datas=datas)


@app.route("/earth")
def earth():
    datas = get_Eatrth(changing=True)
    return render_template('products.html', datas=datas)


@app.route("/water")
def water():
    datas = get_Water(changing=True)
    return render_template('products.html', datas=datas)


@app.route("/fire")
def fire():
    datas = get_Fire(changing=True)
    return render_template('products.html', datas=datas)


@app.route("/air")
def air():
    datas = get_Air(changing=True)
    return render_template('products.html', datas=datas)


@app.route("/space")
def space():
    datas = get_Space(changing=True)
    return render_template('products.html', datas=datas)


@app.route("/manuscript")
def manuscript():
    datas = get_Manuscript(changing=True)
    return render_template('products.html', datas=datas)


@app.route("/metaverse")
def metaverse():
    datas = get_mataverse(changing=True)
    return render_template('products.html', datas=datas)


@app.route("/christmassy")
def christmassy():
    datas = get_Christmas(changing=True)
    return render_template('products.html', datas=datas)


@app.route("/coloured")
def coloured():
    datas = get_coloured(changing=True)
    return render_template('products.html', datas=datas)


@app.route("/character")
def character():
    name = request.args.get('page')
    datas = get_Character(changing=True, typea=name)
    return render_template('products.html', datas=datas)


@app.route("/about")
def about():
    return render_template('about.html')


@app.route("/contact")
def contact():
    return render_template('contact.html')


@app.route("/Dabbu_Characters")
def Dabbu_Characters():
    return render_template('character.html')


@app.route("/Roadmap")
def Roadmap():
    return render_template('roadmap.html')


@app.route("/terms")
def terms():
    return render_template('terms.html')


@app.route("/privacy")
def privacy():
    return render_template('privacy.html')


if __name__ == "__main__":
    app.debug = True
    app.run('0.0.0.0', 5000, debug=True, threaded=True)
