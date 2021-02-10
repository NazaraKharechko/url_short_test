from django import forms
from .models import Link


class LinkSubmitForm(forms.Form):
    url = forms.URLField(
        label='URL to be shortened', )
    custom = forms.CharField(
        label='Custom shortened name',
        required=False, )

    def clean_custom(self):
        custom = self.cleaned_data['custom']
        if not custom:
            return

        try:
            if Link.objects.filter(id=id).exists():
                raise forms.ValidationError('"%s" is already taken' % custom)
        except OverflowError:
            raise forms.ValidationError(too_long_error)
        return custom
