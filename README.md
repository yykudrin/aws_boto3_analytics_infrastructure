Есть четыре типа использования

1. Инфраструктура
2. Создание и управление ec2
3. создание superset
4. управление superset

Инфраструктура

1. создаем ключи для своего пользователя в консоли AWS

2. Копируем их в .aws/credentials в следующие переменные соответственно
  aws_access_key_id
  aws_secret_access_key

3. Копируем папку .aws в /User/<username>/

4. Устанавливаем виртуальное окружение
  python3 -m venv env

5. Запускаем виртуальное окружение
  source env/bin/activate
  
6. Устанавливаем  библиотеку boto3 для работы в AWS
  pip3 install boto3

7. Убеждаемся что в регионе меньше 5 VPC и Запускаем файл main.py и ждем создания инфраструктуры
  python3 main.py

8. Заполняем файл для пользователей client_settings.py вносим данные полученные из скипта main.py
  subnet_id
  sg_id 
  
Установка superset

1. после создания инфраструктуры (Пункт Инфраструктура) заполняем файл superset_settings.py
ec2_ami
ec2_instance_size 
subnet_id 
sg_id 
AZ
2. Запускаем create_superset.py
3. Скрипт распечает id superset, нужно заполнить поле superset_instance_id в client_settings.py


Создание и управление  ec2

1. создаем ключи для своего пользователя в консоли AWS

2. Копируем их в .aws/credentials в следующие переменные соответственно
  aws_access_key_id
  aws_secret_access_key

3. Копируем папку .aws в /User/<username>/

4. Устанавливаем виртуальное окружение
  python3 -m venv env

5. Запускаем виртуальное окружение
  source env/bin/activate
  
6. Устанавливаем  библиотеку boto3 для работы в AWS
  pip3 install boto3

7.  Запускаем скрипт create_ec2.py, он выдаст id вашей машины

8. Копируем id машины в файл client_settings.py в переменную instance_id

9. Подключаемся с выданными разрешениями через rdp


Управление superset

1. Запустить start_superset.py
2. Остановить stop_superset.py

Примечание
  
в конце рабочего дня нужно выключить машину, запустив скрипт stop_ec2.py
если вам нужно снова поработать, запустите скрипт start_ec2.py

файлы
  
create_ec2.py - создает виртуальную машину для работы и запускает ее
start_ec2.py - запускает уже существующую виртуальную машину(если вы не создали предварительно машину то запускать будет нечего)
stop_ec2.py - останавливает виртуальную машину


Для пользователей Window
необходимо установить git bash и python 3 версии и в процессе настройки инфраструктуры вместо python3 вводить python и вместо 5 пункта env\scripts\activate.bat
