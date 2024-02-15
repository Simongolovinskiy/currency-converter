# Currency Converter
![Python](https://img.shields.io/badge/-Python-3776AB?style=flat&logo=python&logoColor=white)
![Docker](https://img.shields.io/badge/-Docker-092E20?style=flat&logo=docker&logoColor=white)
![Aiogram](https://img.shields.io/badge/-Aiogram%20-ff9900?style=flat&logo=bot&logoColor=white)
## Описание проекта
Данный проект является тестовым заданием. Инструкции указаны ниже.


## Запуск проекта
- Клонировать репозиторий и перейти в него в командной строке:
```
git clone https://github.com/Simongolovinskiy/currency-converter.git
```
```
```
- Cоздать и активировать виртуальное окружение
```
python3 -m venv venv # Для Linux и macOS
python -m venv venv # Для Windows
```
```
venv/Scripts/activate # Для Windows
source venv/bin/activate # Для Linux и macOS
```
- Установите зависимости из файла requirements.txt
```
pip install -r requirements.txt
``` 
- Осталось запустить проект одной командой
```
python run.py
```
```
## Запуск из Docker:
```
-Чтобы запустить проект из докера, перейдите в директорию проекта и воспользуйтесь данными командами
```
docker build -t test .
```

```
docker run --rm --name Prod -p 8080:8080 test
```