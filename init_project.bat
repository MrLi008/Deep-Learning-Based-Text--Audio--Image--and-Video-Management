

chcp 65001

python -m pip install --upgrade pip -i https://pypi.tuna.tsinghua.edu.cn/simple

pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple

echo "若提示缺包,请执行: pip install -r requirements.txt"
@REM pip install -r requirements.txt

python manage.py makemigrations

python manage.py migrate

python manage.py collectstatic --noinput > log.txt

python manage.py createsuperuser --username=123456 --email=


python add_管理员.py
@REM start python manage.py runserver
@REM start http://localhost:9100