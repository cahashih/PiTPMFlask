**Тестирование API**

1. POST <http://127.0.0.1:3005/user>

Body: JSON

{

`    `"name":"Sur",

`    `"login":"SurLog",

`    `"password":"Password",

`    `"email": "email@mail.ru"

}

` `![](Aspose.Words.1c2f0b59-7c44-4afd-8a8b-32f6a223fc7e.001.png)

Выдаваемая информация: Пользователь добавлен, 200

1. GET <http://127.0.0.1:3005/user>

![](Aspose.Words.1c2f0b59-7c44-4afd-8a8b-32f6a223fc7e.002.png)

Выдаваемая информация: Все пользователи, 200

1. DELETE <http://127.0.0.1:3005/user>/0

![](Aspose.Words.1c2f0b59-7c44-4afd-8a8b-32f6a223fc7e.003.png)

Выдаваемая информация: Пользователь удален, 200

1. PUT <http://127.0.0.1:3005/user/0>

Body: JSON

{

`    `"name":"SurEdit",

`    `"login":"SurLogEdit",

`    `"pqssword":"PasswordEdit",

`    `"email": "email@mail.ruEdit"

}

![](Aspose.Words.1c2f0b59-7c44-4afd-8a8b-32f6a223fc7e.004.png)

Выдаваемая информация: Пользователь изменен, 200

1. POST <http://127.0.0.1:3005/music>

Body: JSON

{

`    `"name":"SurMusic",

`    `"release":"ReleaseA",

`    `"executor":"ExecutorA"

}

![](Aspose.Words.1c2f0b59-7c44-4afd-8a8b-32f6a223fc7e.005.png)

Выдаваемая информация: Музыка добавлена, 200

1. GET <http://127.0.0.1:3005/music>

![](Aspose.Words.1c2f0b59-7c44-4afd-8a8b-32f6a223fc7e.006.png)

Выдаваемая информация: Вся музыка, 200

1. DELETE <http://127.0.0.1:3005/music/0>

![](Aspose.Words.1c2f0b59-7c44-4afd-8a8b-32f6a223fc7e.007.png)

Выдаваемая информация: Музыка удалена, 200

1. PUT <http://127.0.0.1:3005/music/0>

Body: JSON

{

`    `"name":"SurMusicEdit",

`    `"release":"ReleaseEdit",

`    `"executor":"ExecutorEdit"

}

![](Aspose.Words.1c2f0b59-7c44-4afd-8a8b-32f6a223fc7e.008.png)

Выдаваемая информация: Музыка изменена, 200




