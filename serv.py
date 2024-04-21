from flask import Flask, request, render_template, redirect

import main
from data import db_session
from data.donations import Donations
from data.password_data import Data
from data.users import User

app = Flask(__name__, static_folder='static')
main.main()
db_sess = db_session.create_session()

name_user = None


@app.route('/', methods=['POST', 'GET'])
@app.route('/enter', methods=['POST', 'GET'])
def enter():
    global name_user
    if request.method == 'GET':
        return render_template('enter.html', error='')
    elif request.method == 'POST':
        for user in db_sess.query(User).all():
            if user.name == request.form['Name']:
                for p in db_sess.query(Data).all():
                    if p.name == request.form['Name'] and p.password == request.form['Password']:
                        name_user = request.form['Name']
                        return redirect('/donates/Вы вошли')
        return render_template('enter.html', error='Таких данных нет, зарегистрируйтесь.')


@app.route('/button_load/<int:button_num>', methods=['POST', 'GET'])
def button_load(button_num):
    from add_donate import nums, names
    money = (db_sess.query(User).filter(User.name == name_user).first()).count_money
    if (db_sess.query(User).filter(User.name == name_user).first()).donate == 'Игрок':
        if money > nums[button_num - 1]:
            user = db_sess.query(User).filter(User.name == name_user).first()
            user.donate = names[button_num - 1]
            user.count_money = user.count_money - nums[button_num - 1]
            db_sess.commit()
    elif (db_sess.query(User).filter(User.name == name_user).first()).donate != 'Игрок':
        if money > nums[button_num - 1] and names.index((db_sess.query(User).filter(User.name == name_user).first()).donate) < button_num - 1:
            user = db_sess.query(User).filter(User.name == name_user).first()
            user.donate = names[button_num - 1]
            user.count_money = user.count_money - nums[button_num - 1]
            db_sess.commit()
    else:
        return redirect('/donates/Не хватает денег или ваш донат стоит дороже')
    return redirect('/donates/Спасибо за покупку')


@app.route('/registr', methods=['POST', 'GET'])
def registration():
    global name_user
    if request.method == "GET":
        return render_template('regist.html', error='')
    elif request.method == 'POST':
        for d in db_sess.query(Data).all():
            if request.form['Name'] == d.name or request.form['Password'] == d.password:
                return render_template('regist.html', error='Под такими данными уже зарегистрирован игрок. '
                                                            'Введите другое имя или пароль.')
        user = User()
        data = Data()
        user.name = request.form['Name']
        user.donate = 'Игрок'
        user.count_money = 100000

        data.name = request.form['Name']
        data.password = request.form['Password']
        # data.email = request.form['Email']
        data.telephone = request.form['Tel']
        db_sess.add(user)
        db_sess.add(data)
        db_sess.commit()
        name_user = request.form['Name']
        return redirect('/donates/Вы вошли')


@app.route('/donates/<error>', methods=['POST', 'GET'])
def donates(error=''):
    global name_user
    if request.method == 'GET':

        arr = []
        for i in range(16):
            name = db_sess.query(Donations).filter(Donations.id == i + 1).first()
            text = db_sess.query(Donations).filter(Donations.id == i + 1).first()
            money = db_sess.query(Donations).filter(Donations.id == i + 1).first()
            arr.append([name.donate, text.info, money.money])
        return render_template('donates.html', name1=arr[0][0], text1=arr[0][1], num1=arr[0][2],
                               name2=arr[1][0], text2=arr[1][1], num2=arr[1][2],
                               name3=arr[2][0], text3=arr[2][1], num3=arr[2][2],
                               name4=arr[3][0], text4=arr[3][1], num4=arr[3][2],
                               name5=arr[4][0], text5=arr[4][1], num5=arr[4][2],
                               name6=arr[5][0], text6=arr[5][1], num6=arr[5][2],
                               name7=arr[6][0], text7=arr[6][1], num7=arr[6][2],
                               name8=arr[7][0], text8=arr[7][1], num8=arr[7][2],
                               name9=arr[8][0], text9=arr[8][1], num9=arr[8][2],
                               name10=arr[9][0], text10=arr[9][1], num10=arr[9][2],
                               name11=arr[10][0], text11=arr[10][1], num11=arr[10][2],
                               name12=arr[11][0], text12=arr[11][1], num12=arr[11][2],
                               name13=arr[12][0], text13=arr[12][1], num13=arr[12][2],
                               name14=arr[13][0], text14=arr[13][1], num14=arr[13][2],
                               name15=arr[14][0], text15=arr[14][1], num15=arr[14][2],
                               name16=arr[15][0], text16=arr[15][1], num16=arr[15][2],
                               error=error, don=(db_sess.query(User).filter(User.name == name_user).first()).donate,
                               num=db_sess.query(User).filter(User.name == name_user).first().count_money)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
