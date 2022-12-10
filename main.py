from flask import Flask, request, render_template_string, render_template, flash
import os
import numpy as np
from draw import *

TEMPLATE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
app = Flask(__name__, template_folder=TEMPLATE_DIR, static_folder=TEMPLATE_DIR)
app = Flask(__name__, static_url_path="/images", static_folder="images")

app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods = ['GET', 'POST'])
def result():
    if request.method == "POST":
        vecto_cp_d1 = (request.form.get("n1",type=int), request.form.get("n2",type=int), request.form.get("n3",type=int))
        vecto_cp_d2 = (request.form.get("n4",type=int), request.form.get("n5",type=int), request.form.get("n6",type=int))
        A_d1 = (request.form.get("n7",type=int), request.form.get("n8",type=int), request.form.get("n9",type=int))
        B_d2 = (request.form.get("n10",type=int), request.form.get("n11",type=int), request.form.get("n12",type=int))

        # [vtcp1,vtcp2]
        u1 = vecto_cp_d1[1] * vecto_cp_d2[2] - vecto_cp_d1[2] * vecto_cp_d2[1]
        u2 = vecto_cp_d1[2] * vecto_cp_d2[0] - vecto_cp_d1[0] * vecto_cp_d2[2]
        u3 = vecto_cp_d1[0] * vecto_cp_d2[1] - vecto_cp_d1[1] * vecto_cp_d2[0]
        Tich_co_huong_2vtcp = (u1, u2, u3)

        #VectoAB
        vectoAB = (B_d2[0] - A_d1[0], B_d2[1] - A_d1[1], B_d2[2] - A_d1[2])

        #[vtcp1,vtcp2].VectoAB
        Tich_hon_tap = np.dot(Tich_co_huong_2vtcp, vectoAB)

        #[vtcp1,VectoAB]
        u4 = vecto_cp_d1[1] * vectoAB[2] - vecto_cp_d1[2] * vectoAB[1]
        u5 = vecto_cp_d1[2] * vectoAB[0] - vecto_cp_d1[0] * vectoAB[2]
        u6 = vecto_cp_d1[0] * vectoAB[1] - vecto_cp_d1[1] * vectoAB[0]
        Tich_co_huong_vtcp1_va_vtAB = (u4, u5, u6)

        #vtcp1.vtcp2
        Tich_vo_huong_2vtcp = np.dot(vecto_cp_d1, vecto_cp_d2)
        
        draw_line(vecto_cp_d1, A_d1, vecto_cp_d2, B_d2)
        path_image = os.path.join('images', 'result.png')
        
        return render_template('result.html',
                                vecto_cp_d1=vecto_cp_d1,
                                vecto_cp_d2= vecto_cp_d2,
                                A_d1=A_d1,
                                B_d2=B_d2,
                                Tich_co_huong_2vtcp= Tich_co_huong_2vtcp,
                                vectoAB=  vectoAB,
                                Tich_hon_tap= Tich_hon_tap,
                                Tich_co_huong_vtcp1_va_vtAB = Tich_co_huong_vtcp1_va_vtAB,
                                Tich_vo_huong_2vtcp= Tich_vo_huong_2vtcp, 
                                user_img = path_image
                                )
if __name__ == '__main__':
    app.run(debug = True, host='127.0.0.1', port=5000)
