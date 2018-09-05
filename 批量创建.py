import os
import random
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myadmin.settings")

if __name__ == "__main__":
    import django
    django.setup()
    from app01 import models


    # def create():
    #     obj_list = [models.Book(
    #         title = f"老男孩{i}",
    #         publish_id=random.choice([1,2,3,4]),
    #         price=random.randint(1,100),
    #         publishDate = random.choice(['2016-10-8','2017-9-8','2018-7-8'])
    #     )
    #         for i in range(160)]
    #     models.Book.objects.bulk_create(obj_list)
    #
    # create()

    # def create():
    #     book_obj_list = models.Book.objects.all()
    #
    #
    #     for book_obj in book_obj_list:
    #         book_obj.authors.add(*random.sample([1,2,3],2))
    #
    # create()



    # def delete():
    #     models.Book.objects.all().delete()

    # delete()

    # list = [1,2,3,4,5]
    # print(random.sample(list,2))