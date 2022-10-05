***Тестирование API***

1. POST <http://127.0.0.1:3005/user>

Body: JSON

{

`    `"name":"Sur",

`    `"login":"SurLog",

`    `"password":"Password",

`    `"email": "email@mail.ru"

}

` `![](https://github.com/cahashih/PiTPMFlask/blob/main/Screens/screen001.png)

Выдаваемая информация: Пользователь добавлен, 200

2. GET <http://127.0.0.1:3005/user>

![](https://github.com/cahashih/PiTPMFlask/blob/main/Screens/screen002.png)

Выдаваемая информация: Все пользователи, 200

3. DELETE <http://127.0.0.1:3005/user>/0

![](https://github.com/cahashih/PiTPMFlask/blob/main/Screens/screen003.png)

Выдаваемая информация: Пользователь удален, 200

4. PUT <http://127.0.0.1:3005/user/0>

Body: JSON

{

`    `"name":"SurEdit",

`    `"login":"SurLogEdit",

`    `"pqssword":"PasswordEdit",

`    `"email": "email@mail.ruEdit"

}

![](https://github.com/cahashih/PiTPMFlask/blob/main/Screens/screen004.png)

Выдаваемая информация: Пользователь изменен, 200

5. POST <http://127.0.0.1:3005/music>

Body: JSON

{

`    `"name":"SurMusic",

`    `"release":"ReleaseA",

`    `"executor":"ExecutorA"

}

![](https://github.com/cahashih/PiTPMFlask/blob/main/Screens/screen005.png)

Выдаваемая информация: Музыка добавлена, 200

6. GET <http://127.0.0.1:3005/music>

![](https://github.com/cahashih/PiTPMFlask/blob/main/Screens/screen006.png)

Выдаваемая информация: Вся музыка, 200

7. DELETE <http://127.0.0.1:3005/music/0>

![](https://github.com/cahashih/PiTPMFlask/blob/main/Screens/screen007.png)

Выдаваемая информация: Музыка удалена, 200

8. PUT <http://127.0.0.1:3005/music/0>

Body: JSON

{

`    `"name":"SurMusicEdit",

`    `"release":"ReleaseEdit",

`    `"executor":"ExecutorEdit"

}

![](https://github.com/cahashih/PiTPMFlask/blob/main/Screens/screen008.png)

Выдаваемая информация: Музыка изменена, 200




