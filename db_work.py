from flask import Flask
import datetime

from data import db_session
from data.users import User
from data.news import News


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/blogs.db")
    # app.run()
    # user = User()
    # user.name = "Пользователь 3"
    # user.about = "биография пользователя 3"
    # user.email = "email3@email.ru"
    db_sess = db_session.create_session()
    # db_sess.add(user)
    # db_sess.commit()
    # user = db_sess.query(User).first()
    # print(user.name)
    users = db_sess.query(User).all()
    #print(users)
    for user in users:
        print(user)
    # print("----------------------------------------")
    # for user in db_sess.query(User).filter(User.id > 1, User.email.notilike("%1%")):
    #     print(user)

    print("----------------------------------------")
    # user = db_sess.query(User).filter(User.id == 1).first()
    # print(user)
    # user.name = "Измененное имя пользователя"
    # user.created_date = datetime.datetime.now()
    # db_sess.commit()
    # db_sess.query(User).filter(User.id >= 3).delete()
    # db_sess.commit()
    # user = db_sess.query(User).filter(User.id == 2).first()
    # db_sess.delete(user)
    # db_sess.commit()
    # news = News(title="Первая новость", content="Привет блог!",
    #             user_id=1, is_private=False)
    # db_sess.add(news)
    # db_sess.commit()
    # user = db_sess.query(User).filter(User.id == 1).first()
    # news = News(title="Вторая новость", content="Уже вторая запись!",
    #             user=user, is_private=False)
    # db_sess.add(news)
    # db_sess.commit()
    # user = db_sess.query(User).filter(User.id == 1).first()
    # news = News(title="Личная запись", content="Эта запись личная",
    #             is_private=True)
    # user.news.append(news)
    # db_sess.commit()

    for news in user.news:
        print(news)

if __name__ == '__main__':
    main()
