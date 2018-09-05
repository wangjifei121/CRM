from stark.servers.site import ModelStark
from stark.servers.site import site
from app01 import models


class BookConfig(ModelStark):
    list_display = ['title', 'price', 'publish','authors']
    list_display_links = ["title"]
    search_fields = ['title']
    list_filter = ['publish','authors']


site.register(models.Book, BookConfig)
class PublishConfig(ModelStark):
    list_display = ['name', 'city', 'email']

site.register(models.Publish, PublishConfig)
site.register(models.Author)
site.register(models.AuthorDetail)
