from django.db import models


class Author(models.Model):
    nid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32,verbose_name='作者')
    age = models.IntegerField(verbose_name="年龄")

    # 与AuthorDetail建立一对一的关系
    authorDetail = models.OneToOneField(to="AuthorDetail", on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class AuthorDetail(models.Model):
    nid = models.AutoField(primary_key=True)
    birthday = models.DateField()
    telephone = models.BigIntegerField()
    addr = models.CharField(max_length=64)


class Publish(models.Model):
    nid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32,verbose_name='出版社')
    city = models.CharField(max_length=32,verbose_name="城市")
    email = models.EmailField(verbose_name='邮箱')

    def __str__(self):
        return self.name


class Book(models.Model):
    nid = models.AutoField(primary_key=True)
    title = models.CharField(max_length=32,verbose_name='书名')
    price = models.DecimalField(max_digits=5, decimal_places=2,verbose_name="价格")
    # 与Publish建立一对多的关系,外键字段建立在多的一方
    publish = models.ForeignKey(to="Publish", to_field="nid", on_delete=models.CASCADE,verbose_name='出版社')
    publishDate = models.DateField(verbose_name="出版日期",auto_created=True)
    # 与Author表建立多对多的关系,ManyToManyField可以建在两个模型中的任意一个，自动创建第三张表
    authors = models.ManyToManyField(to='Author',verbose_name='作者' )

    def __str__(self):
        return self.title
