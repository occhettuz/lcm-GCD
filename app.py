from flask import Flask, render_template, request
from algo import GCD, lcm

app = Flask(__name__)

@app.route('/', methods=['post', 'get'])
def index():
    NumList=[]
    MCD = 0
    mcm = 0
    error = False
    if request.method == 'POST':
        try:
            Num1 = request.form.get('1st')
            Num2 = request.form.get('2nd')
            Num3 = request.form.get('3rd')
            NumList.extend([Num1, Num2, Num3])
            print(NumList)
            MCD = GCD(NumList)
            mcm = lcm(NumList)
        except ValueError:
            error = True
        except IndexError:
            error = True
    return render_template('index.html', max_com_div=MCD, min_com_mult=mcm, error_result = error)
    del NumList[:]


if __name__ == '__main__':
    app.run(debug=True)

