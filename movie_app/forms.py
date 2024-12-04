from django import forms
from .models import Collection

class CollectionForm(forms.ModelForm):
    class Meta:
        model = Collection
        fields = ['name', 'description']  # Only allow the user to submit these fields

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Optional: Customize field widgets or labels here
        self.fields['name'].widget.attrs.update({'placeholder': 'Enter collection name'})
        self.fields['description'].widget.attrs.update({'placeholder': 'Enter collection description'})
