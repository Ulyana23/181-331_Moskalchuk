# Статический анализ

Представленный модуль был реализован в рамках дисциплины «Программирование криптографических алгоритмов». Он осуществляет шифрование и расшифровку поданного на вход сообщения, используя алгоритм шифрования RSA. В качестве анализатора был выбран Pylint.

После статического анализа были получены результаты следующего вида:
**имя_файла:номер_строки:номер_символа: код_ошибки: описание_ошибки**

В результате анализа кода было выявлено 47 ошибок:

![до_1](https://user-images.githubusercontent.com/43664758/214790478-5ab27997-63be-4a8d-a131-7cfedef204ad.JPG)
![до_2](https://user-images.githubusercontent.com/43664758/214790635-3468f908-6732-42bc-810c-8aea66441c77.JPG)


Я решила исправить 2 из них:
1. ```main.py:47:0: C0103: Function name "errorMessageN" doesn't conform to snake_case naming style (invalid-name)```
2. ```main.py:80:14: R1734: Consider using [] instead of list() (use-list-literal)```

Первая ошибка говорит о том, что функция errorMessageN должна быть переминована в соответствии со стилем snake_case.
Код до изменений:
```python
def errorMessageN(_maxElem, _n):
    if _n < _maxElem:
        print("Вы выбрали слишком маленькие значения P и Q, попробуйте ещё раз.")
        sys.exit()
```

После изменений:

```python
def error_message_n(_maxElem, _n):
    if _n < _maxElem:
        print("Вы выбрали слишком маленькие значения P и Q, попробуйте ещё раз.")
        sys.exit()
```

Вторая ошибка говорит о том, что для объявления списка вместо конструкции list() лучше использовать [].
Код до изменений:
```python
def textToNum(_string):
    numList = list()  
    for letter in _string:
        numList.append(ord(letter))

    return numList
```
Код после изменений:
```python
def textToNum(_string):
    numList = []
    for letter in _string:
        numList.append(ord(letter))

    return numList
```

После изменения ошибки пропали:
![image](https://user-images.githubusercontent.com/43664758/214791411-89a715dd-800a-4303-833f-c052d80327d2.png)
![image](https://user-images.githubusercontent.com/43664758/214791563-fcfb2eda-a41b-4106-a57d-2bf7ae6daa01.png)


# Модульное тестирование

Представленный модуль был реализован в рамках дисциплины «Программирование криптографических алгоритмов». Для проведения модульного тестирования была выбрана функция Эйлера.

Для написания юниттеста был создан файл ```test.py```
Далее был импортирован фреймворк для модульного тестирования и файл main.py.

В классе MyTestCase и функции test_something подаю входное значение в функцию euler() и результат записываю в переменную result. 
Далее вызывается функция, срвнивающая значение, которое вернула функция euler() с верным выходным значением.

### Результат:
Позитивный модульный тест:
![image](https://user-images.githubusercontent.com/43664758/214800439-c8047791-6196-4aa8-a4bd-ed252c889e11.png)

Негативный модульный тест:
![image](https://user-images.githubusercontent.com/43664758/214800844-00d319aa-dcdf-4cf4-b413-676e976ebbe3.png)



