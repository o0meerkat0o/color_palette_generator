from flask import Flask, render_template, request
#from flask_mysqldb import MySQL  
from datetime import datetime
import colorsys

app = Flask(__name__)

# If you ever want MySQL again, uncomment these:
# app.config['MYSQL_HOST'] = 'mysql.2324.lakeside-cs.org'
# app.config['MYSQL_USER'] = 'student2324'
# app.config['MYSQL_PASSWORD'] = 'm545CS42324'
# app.config['MYSQL_DB'] = '2324playground'
# app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
# mysql = MySQL(app)

@app.route('/')
def index():
    return render_template('index.html.j2')

def hex_to_rgb(hex):
    return tuple(int(hex[i:i+2], 16) for i in (0, 2, 4))

def complementary_rgb_255(r, g, b):
    cr = 255 - r
    cg = 255 - g
    cb = 255 - b
    return cr, cg, cb

@app.route('/results', methods=['POST'])
def results():
    colorHex = request.values.get("color")
    if colorHex is None:
        return render_template('error.html.j2')
    colorRGB = hex_to_rgb(colorHex.lstrip('#'))
    colorHLS = colorsys.rgb_to_hls(colorRGB[0]/255, colorRGB[1]/255, colorRGB[2]/255)

    tricolor1_hue = (colorHLS[0] + 120 / 360) % 1.0
    tricolor2_hue = (colorHLS[0] + 240 / 360) % 1.0
    tricolor1 = tuple(int(x * 255) for x in colorsys.hls_to_rgb(tricolor1_hue, colorHLS[1], colorHLS[2]))
    tricolor2 = tuple(int(x * 255) for x in colorsys.hls_to_rgb(tricolor2_hue, colorHLS[1], colorHLS[2]))

    anacolor1_hue = (colorHLS[0] + 30 / 360) % 1.0
    anacolor2_hue = (colorHLS[0] + 60 / 360) % 1.0
    anacolor3_hue = (colorHLS[0] + 90 / 360) % 1.0
    anacolor1 = tuple(int(x * 255) for x in colorsys.hls_to_rgb(anacolor1_hue, colorHLS[1], colorHLS[2]))
    anacolor2 = tuple(int(x * 255) for x in colorsys.hls_to_rgb(anacolor2_hue, colorHLS[1], colorHLS[2]))
    anacolor3 = tuple(int(x * 255) for x in colorsys.hls_to_rgb(anacolor3_hue, colorHLS[1], colorHLS[2]))

    tetracolor1_hue = (colorHLS[0] + 270 / 360) % 1.0
    tetracolor1 = tuple(int(x * 255) for x in colorsys.hls_to_rgb(tetracolor1_hue, colorHLS[1], colorHLS[2]))

    compRGB = complementary_rgb_255(colorRGB[0], colorRGB[1], colorRGB[2])

    return render_template(
        'results.html.j2',
        color1=colorRGB, color2=compRGB, color3=tricolor1, color4=tricolor2,
        color5=anacolor1, color6=anacolor2, color7=anacolor3, color8=tetracolor1
    )

if __name__ == '__main__':
    app.run(debug=True)
