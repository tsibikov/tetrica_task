### Тестовое задание

- 1 Задача

find_index.py
```
Дан массив чисел, состоящий из некоторого количества подряд идущих единиц, за которыми следует какое-то количество подряд идущих нулей: 111111111111111111111111100000000. 
Найти индекс первого нуля (то есть найти такое место, где заканчиваются единицы, и начинаются нули)
```

- 2 Задача

wiki_animals.py

Требует установки библиотеки Wikipedia-API
```
pip install Wikipedia-API==0.5.4
```

```
В нашей школе мы не можем разглашать персональные данные пользователей, но чтобы преподаватель и ученик смогли объяснить нашей поддержке, кого они имеют в виду (у преподавателей, например, часто учится несколько Саш), мы генерируем пользователям уникальные и легко произносимые имена. Имя у нас состоит из прилагательного, имени животного и двузначной цифры. В итоге получается, например, "Перламутровый лосось 77". Для генерации таких имен мы и решали следующую задачу:
Получить с русской википедии список всех животных (Категория:Животные по алфавиту) и вывести количество животных на каждую букву алфавита. Результат должен получиться в следующем виде:
А: 642
Б: 412
В:....

```


- 3 Задача

lesson_time.py
```
Мы сохраняем время присутствия каждого пользователя на уроке  виде интервалов. В функцию передается словарь, содержащий три списка с таймстемпами (время в секундах): — lesson – начало и конец урока 
— pupil – интервалы присутствия ученика 
— tutor – интервалы присутствия учителя 
Интервалы устроены следующим образом – это всегда список из четного количества элементов. Под четными индексами (начиная с 0) время входа на урок, под нечетными - время выхода с урока.
Нужно написать функцию, которая получает на вход словарь с интервалами и возвращает время общего присутствия ученика и учителя на уроке (в секундах). 

```