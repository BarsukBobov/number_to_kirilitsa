# Числа в кириллицу
1.1.	Напишите на своём любимом языке функцию преобразованию целого числа в строку прописью.
В любом падеже и в любом роде. Прототип функции:

`string sumProp(int nSum, string sGender, string sCase)`


nSum - целое число менее триллиона (максимум 999 999 999 999)

sGender - род ("М"-мужской, "Ж"-женский, "С"-средний)

sCase - падеж ("И"-именительный, …, "П"-предложный)

![img.png](img.png)

Версия python - 3.7.

1) Создание виртуального окружения:
```
python -m venv venv
```
2) Активация виртуального окружения:
```
# Для Windows
venv\Scripts\activate.bat
# Для Linux
source venv/bin/activate
```

3) Установка библиотек:
```
pip install -r requirements.txt
```

4) Запуск:
```
cd 1_task
python main.py
```

P.s. Тесты из ТЗ проведены в файле tests_with_convert_num.py. Для их запуска необходимо папку task_1 
добавить в source с помощью оболочки Вашего ОС или IDE(mark directory as > sources root).
