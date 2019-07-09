from .models import Group
from django import forms

STATUS = (
    (0, "Active"),
    (1, "Closed"),
)


class groupedit(forms.ModelForm):
    image = forms.ImageField(widget=forms.ClearableFileInput(
        attrs={'class': 'custom-file-input', 'id': 'file', 'type': 'file', })
    )
    name = forms.CharField()
    bio = forms.CharField()
    status = forms.ChoiceField(choices=STATUS)

    entrykey = forms.IntegerField()

    def __init__(self, *args, **kwargs):
        self.admin = forms.ModelChoiceField(queryset=Group.objects.get(pk=pk))

    class Meta:
        model = Group.objects
        fields = {'image', 'name', 'bio', 'status', 'admin'}
