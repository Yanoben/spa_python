from django import forms


COLUM_CHOICES = [
    ('name', 'Название'),
    ('count', 'Количество'),
    ('distance', 'Расстояние')]
CONDITIONS = [
    ('=', 'равно'),
    ('in', 'содержит'),
    ('more', 'больше'),
    ('less', 'меньше')]


class FilterForm(forms.Form):
    colum = forms.MultipleChoiceField(
        required=False,
        widget=forms.Select,
        choices=COLUM_CHOICES,
        label='Столбец')
    condition = forms.MultipleChoiceField(
        required=False,
        widget=forms.Select,
        choices=CONDITIONS,
        label='Условие')
    text = forms.CharField(required=False, label='Текст')
