# exam
Online Exam Web App


## Dump Data
Create Fixtures
```bash
python manage.py dumpdata <app>.<Model> --indent=4 --format=json > <app>/fixtures/<Model>.json
```

Load Fixtures
```bash
python manage.py loaddata <app>/fixtures/<Model>.json
```