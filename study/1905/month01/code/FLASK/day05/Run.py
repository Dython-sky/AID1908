from flask import Flask,render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import or_

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']="mysql://root:584023982@127.0.0.1:3306/flask"
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN']=True
db = SQLAlchemy(app)
# 根据现有的表结构构建模型类
class Users(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(80),unique=True)
    age = db.Column(db.Integer)
    email = db.Column(db.String(120),unique=True)
    def __init__(self,username,age,email):
        self.username = username
        self.age = age
        self.email = email
    def __repr__(self):
        return "<Users %r>"%self.username
class Course(db.Model):
    __tablename__ = "course"
    id = db.Column(db.Integer,primary_key=True)
    cname = db.Column(db.String(60))
    # 反向引用,返回与当前课程相关的teacher列表
    # backref定义反向关系，本质上会向Teacher实体中增加一个course属性，该属性可替代course_id访问course模型,此时获得的是模型对象，不是外键值
    teachers = db.relationship('Teacher',backref='course')
    def __init__(self,cname):
        self.cname = cname
class Teacher(db.Model):
    __tablename__ = "teacher"
    id = db.Column(db.Integer,primary_key=True)
    tname = db.Column(db.String(30))
    tage = db.Column(db.Integer)
    # 增加一列:course_id,外键列，要引用自主键表(course)的主键列(id)
    course_id = db.Column(db.Integer,db.ForeignKey("course.id"))
    def __init__(self,tname,tage):
        self.tname = tname
        self.tage = tage
    def __repr__(self):
        return "<Teacher %r>"%self.tname

db.drop_all()
db.create_all()
@app.route('/insert')
def insert_views():
    users = Users("陈欢",23,"chenhuan@163.com")
    db.session.add(users)
    return "Insert OK"
@app.route('/query')
def query_views():
    # 测试查询
    # print(db.session.query(Users))
    # print(db.session.query(Users.username,Users.email))
    # print(db.session.query(Users,Course))

    # 通过查询执行函数获得最终查询结果
    # all():得到查询结果中所有的结果
    # users = db.session.query(Users).all()
    # for user in users:
    #     print(user.username,user.age,user.email)

    # first():得到查询结果中的第一个查询结果
    # user = db.session.query(Users).first()
    # print(user.username,user.age,user.email)
    # course = db.session.query(Course).first()
    # print(course)

    # 使用查询过滤器函数对数据进行筛选
    # 查询年龄大于22的Users信息
    # users = db.session.query(Users).filter(Users.age > 22).all()
    # print(users)

    # 查询年龄大于22且id大于2的Users信息
    # users = db.session.query(Users).filter(Users.age>22,Users.id>2).all()
    # print(users)

    # 查询年龄大于22或id大于2的Users信息
    # users = db.session.query(Users).filter(or_(Users.age > 22,Users.id > 2)).all()
    # print(users)

    # 查询email中包含字符'd'的用户信息
    # users = db.session.query(Users).filter(Users.email.like('%d%')).all()
    # print(users)

    # 查询id在1,2,3之间的用户信息
    # users = db.session.query(Users).filter(Users.id.in_([1,2,3])).all()
    # print(users)

    # 查询Users表中所有数据的前3条
    # users = db.session.query(Users).limit(3).all()
    # users = db.session.query(Users).limit(3).offset(1).all()
    # print(users)

    # 查询Users表中所有的数据，并按照id倒序排序
    # users = db.session.query(Users).order_by(Users.id.desc(),Users.age.asc()).all()
    # print(users)

    # 查询Users表中所有数据，并按照age进行分组排序
    # users = db.session.query(Users).group_by('age').all()
    # print(users)

    # 基于models实现的查询:查询id>3的所有用户的信息
    users = Users.query.filter(Users.id>3).all()
    print(users)
    return "Query OK"
@app.route('/query_all')
def query_all():
    # 查询Users表中所有的数据
    users = db.session.query(Users).all()
    return render_template('01-users.html',params=locals())
# @app.route('/query_by_id/<int:id>')
# def query_by_id(id):
#     user = db.session.query(Users).filter_by(id=id).first()
#     return render_template('02-user.html',params=locals())
@app.route('/query_by_id')
def query_by_id():
    # 接收前端通过地址栏传递过来的查询字符串
    id = request.args.get('id')
    # 根据id获取user的信息
    user = db.session.query(Users).filter_by(id=id).first()
    # 将user对象发送的02-user.html模板上进行显示
    return render_template('02-user.html', params=locals())
@app.route('/delete_user')
def delete_user():
    user = Users.query.filter_by(id=2).first()
    db.session.delete(user)
    return "Delete OK"
@app.route('/update_user')
def update_user():
    user = Users.query.filter_by(id=4).first()
    user.username = "张乐乐"
    user.age = 23
    db.session.add(user)
    return "Update OK"
@app.route('/delete')
def delete_views():
    # 接收请求过来的id值
    id = request.args.get('id')
    user = Users.query.filter_by(id=id).first()
    # 将模型对象删除
    db.session.delete(user)
    url = request.headers.get('referer','/query_all')
    return redirect(url)
@app.route('/update',methods=['GET','POST'])
def update_views():
    if request.method == 'GET':
        # 获取前端传递过来的id
        id = request.args.get('id')
        # 根据id查询出对应的实体对象
        user = Users.query.filter_by(id=id).first()
        # 将实体对象方到03-update.html模板中显示
        return render_template('03-update.html',params=locals())
    else:
        # 接收前端传递过来的四个参数
        id = request.form['id']
        username = request.form['username']
        age = request.form['age']
        email = request.form['email']
        # 查
        user = Users.query.filter_by(id=id).first()
        # 改
        user.username = username
        user.age = age
        user.email = email
        # 保存
        db.session.add(user)
        return redirect('/query_all')
if __name__ == '__main__':
    app.run(debug=True)