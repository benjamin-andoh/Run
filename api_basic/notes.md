>>>from api_basic.models import Article
>>> from api_basic.serializers import ArticleSerializer
>>> a = Article(title='java', author='papa', email='papa@gmail.com')
>>> a.save()
>>> b = Article.objects.all()
>>> b
<QuerySet [<Article: python>, <Article: java>]>
>>> s = ArticleSerializer(a)
>>> s.data
{'title': 'java', 'author': 'papa', 'email': 'papa@gmail.com', 'date': '2020-07-13T19:06:58.123044Z'}
>>> from rest_framework.renderers import JSONRenderer
>>> from rest_framework.parsers import JSONParser
>>> c = JSONRenderer().render(s.data)
>>> c
b'{"title":"java","author":"papa","email":"papa@gmail.com","date":"2020-07-13T19:06:58.123044Z"}'
>>>


When passing a query set
>>> s = ArticleSerializer(Article.objects.all(), many=True)
>>> s.data
[OrderedDict([('title', 'python'), ('author', 'benjamin andoh'), ('email', 'benoo.andoh@gmail.com'), ('date', '2020-07-13T18:37:17.175781Z')]), OrderedDict([('title
', 'java'), ('author', 'papa'), ('email', 'papa@gmail.com'), ('date', '2020-07-13T19:06:58.123044Z')])]
>>>

>>> s = ArticleSerializer()
>>> print(repr(s))
ArticleSerializer():
    title = CharField(max_length=100)
    author = CharField(max_length=100)
    email = EmailField(max_length=100)
    date = DateTimeField()
>>>
