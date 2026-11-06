from django import forms

from shopapp.models import Product


# Начиная с Django 4.2 загрузка нескольких файлов через ClearableFileInput(attrs={"multiple": True})
# запрещена: нужны свои виджет и поле, см. документацию "Uploading multiple files"
class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True


class MultipleImageField(forms.ImageField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget", MultipleFileInput())
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        single_file_clean = super().clean
        if isinstance(data, (list, tuple)):
            return [single_file_clean(d, initial) for d in data]
        return [single_file_clean(data, initial)]


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "name", "price", "description", "discount", "preview"

    images = MultipleImageField()


class CSVImportForm(forms.Form):
    csv_file = forms.FileField()
