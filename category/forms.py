from django import form
from .models import Category


class CategoryForm(form.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'