<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Polls首页</title>
</head>
<body>
<h1>Polls首页</h1>
{{ questions }}
<hr>
<ul>
    {% for q in questions %}
        <li>{{ q.question_text }} {{ q.pub_date }}</li>
    {% endfor %}
</ul>
<hr>
<ul>
    {% for q in questions %}
        {% if q.was_publish_recently %}
            <li>{{ q.question_text }} {{ q.pub_date }}</li>
        {% endif %}
    {% endfor %}
</ul>
</body>
</html>