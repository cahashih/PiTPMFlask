
import pickle
from flask import Flask,request,jsonify
app = Flask(__name__)




music = []
users = []
# Открываем файл с пользователями
try:
    with open('music.data', 'rb') as filehandle: 
        music = pickle.load(filehandle)
except:
    with open('music.data', 'wb') as filehandle:
        pickle.dump(' ', filehandle)

try:
    with open('users.data', 'rb') as filehandle: 
        users = pickle.load(filehandle)
except:
    with open('users.data', 'wb') as filehandle:
        pickle.dump(' ', filehandle)



#localhost
@app.route('/user',methods=['POST','GET'])
def userPostAndGet():
    if request.method == 'POST':
        data = request.get_json()
        name = None
        email = None
        password = None
        login = None
        if data:
            if 'name' in data:
                name = data['name']
            else:
                return 'Не указано имя', 403
            if 'email' in data:
                email = data['email']
            else:
                return 'Не указана почта', 403
            if 'password' in data:
                password = data['password']
            else:
                return 'Не указан пароль', 403
            if 'login' in data:
                login = data['login']
            else:
                return 'Не указан логин', 403
            
        else:
            return 'Нет данных', 403
        user = []        
        user.append(login)         
        user.append(password) 
        user.append(name)
        user.append(email)
        users.append(user)   
        saveUsers()
        return "Пользователь добавлен",200
    if request.method =="GET":        
        return users,200        
@app.route('/user/<int:id>',methods=['DELETE', 'PUT'])

def userPutAndDelete(id):
    if request.method =='DELETE':
        try:
            del users[id]
            return "Пользователь удалён",200
        except:
            return "Ошибка операции",403

    if request.method =='PUT':
        if len(users) < id:
            return 'Пользователя с таким id нет', 403

        data = request.get_json()
        if data:
            if 'name' in data:
                name = data['name']
            else:
                return 'Не указано имя', 403
            if 'email' in data:
                email = data['email']
            else:
                return 'Не указана почта', 403
            if 'password' in data:
                password = data['password']
            else:
                return 'Не указан пароль', 403
            if 'login' in data:
                login = data['login']
            else:
                return 'Не указан логин', 403
            
        else:
            return 'Нет данных', 403
        user = [] 
        user.append(login)         
        user.append(password) 
        user.append(name)
        user.append(email)
        users[id] = user  
        saveUsers()
        return 'Пользователь изменен', 200
def saveUsers():
    with open('users.data', 'wb') as filehandle:
        pickle.dump(users, filehandle)



@app.route('/music',methods=['POST','GET'])
def musicPostAndGet():
    if request.method == 'POST':
        data = request.get_json()
        name = None
        release = None
        executor = None
        if data:
            if 'name' in data:
                name = data['name']
            else:
                return 'Не указоно название', 403
            if 'release' in data:
                release = data['release']
            else:
                return 'Не указана дата исполнения', 403
            if 'executor' in data:
                executor = data['executor']
            else:
                return 'Не указан исполнитель', 403
            
            
        else:
            return 'Нет данных', 403
        mus = []        
        mus.append(release)         
        mus.append(executor) 
        mus.append(name)
        music.append(mus)   
        saveMusic()
        return "Музыка добавлена",200
    if request.method =="GET":        
        return music,200        
@app.route('/music/<int:id>',methods=['DELETE', 'PUT'])

def musicPutAndDelete(id):
    if request.method =='DELETE':
        try:
            del music[id]
            return "Музыка удалена",200
        except:
            return "Ошибка операции",403

    if request.method =='PUT':
        if len(music) < id:
            return 'Музыки с таким id нет', 403

        data = request.get_json()
        if data:
            if 'name' in data:
                name = data['name']
            else:
                return 'Не указано название', 403
            if 'release' in data:
                release = data['release']
            else:
                return 'Не указана дата исполнения', 403
            if 'executor' in data:
                executor = data['executor']
            else:
                return 'Не указан исполнитель', 403
            
        else:
            return 'Нет данных', 403
            
        mus = []        
        mus.append(release)         
        mus.append(executor) 
        mus.append(name)
        music[id] = mus   
        saveMusic()
        return "Музыка изменена",200



def saveMusic():
    with open('music.data', 'wb') as filehandle:
        pickle.dump(music, filehandle)






app.run(port=3005)


