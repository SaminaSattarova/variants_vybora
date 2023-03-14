from flask import Flask, request, url_for

app = Flask(__name__)


@app.route('/choice/<planet_name>')
def return_sample_page(planet_name):
    slov = {'Меркурий': 'Первая планета,' 'Там очень жарко', 'Венера': 'Вторая планета,' 'Там жарко и Марс недалеко',
            'Земля': 'Наша третья планета,' 'Самая комфортная планета', 'Нептун': 'Восьмая планета,' 'Синяя планета',
            'Марс': 'Четвертая планета,' 'Тебя там не хватает!', 'Юпитер': 'Пятая планета,' 'Самая большая в СС',
            'Сатурн': 'Шестая планета,' 'У него есть кольца', 'Уран': 'Седьмая планета,' 'Голубая планета'}
    countdown_list = slov[planet_name].split(',')
    return f'''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <link rel="stylesheet"
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                            crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style_mars.css')}" />
                    <title>Привет, {planet_name}!</title>
                  </head>
                  <body>
                    <h2>Мое предложение: {planet_name}!</h2>
                    <br><label>Вы можите посмотреть предложение по любой из восьми возможных планет</label>
                    <br><label class="green">{countdown_list[0]}</label>
                    <br><label class="yellow">{countdown_list[1]}</label>
                  </body>
                </html>'''


if __name__ == '__main__':
    app.run(port=8076, host='127.0.0.1')