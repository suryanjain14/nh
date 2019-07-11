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

    class Meta:
        model = Group

        fields = {'image', 'name', 'bio', 'status', 'admin'}

    '''
    def __init__(self, user, *args, **kwargs):
        temp = user
        groups =Group.objects.all()
        for group in groups:
            grp1 = group.users.all()
            print('wlkahdkhskajhdkjshajk')
            print(grp1)
            for user in grp1:
                if user == temp:
                    id = group.id

        group = Group.objects.filter(pk=id)
        self.admin = forms.ModelChoiceField(queryset=group.users)
        super(groupedit, self).__init__(*args, **kwargs)
'''
