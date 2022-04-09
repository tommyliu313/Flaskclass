Flask Install
```bash
pip install flask-wtf flask-sqlalchemy flask-migrate flask-login email_validator flask-email pyjwt hashlib flask-bootstrap
```

想知道安裝了甚麼套件?
```bash
pip3 freeze > requirements.txt
pip3 install -r requirements.txt
```
重複使用的
```python
{% if user %}{% endif %}
```
```bash
flask db init
flask db migrate -m "users table"
flask db upgrade
```
表單
```html
<form action="" method="post" novalidate>
    
    <p>{{ form.remember_me() }}{{ form.remember_me.label }}</p>
        <p>{{ form.submit() }}</p>
</form>
```

Python表單的欄位設計(pip install flask-wtf)
```python

```
引用
from x import y