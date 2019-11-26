from material.admin.options import MaterialModelAdmin
from material.admin.decorators import register
from headlines import models
# Register your models here.
@register(models.Headline)
class HeadlineAdmin(MaterialModelAdmin):

    list_display = ['headline', 'dateposted']
    icon_name = 'view_headline'
