
from material.admin.options import MaterialModelAdmin
from material.admin.decorators import register
from .models import Course
# Register your models here.
@register(Course)
class CourseAdmin(MaterialModelAdmin):


    list_display = (
        'course_name',
        'course_description'

    )

    search_fields =(

        'course_name',
    )
    icon_name = 'golf_course'
