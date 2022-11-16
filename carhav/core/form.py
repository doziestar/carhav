from django import forms

class ContactForm(forms.Form):
    pass

class ResumeRevampForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    phone = forms.CharField(max_length=100)
    resume = forms.FileField()
    message = forms.CharField(widget=forms.Textarea)

    def __str__(self):
        return self.name
    
    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get("name")
        email = cleaned_data.get("email")
        phone = cleaned_data.get("phone")
        resume = cleaned_data.get("resume")
        message = cleaned_data.get("message")

        if not name and not email and not phone and not resume and not message:
            raise forms.ValidationError("You have to write something!")
    
    # action on form submission
    def save(self):
        super().save()

class InterviewPrepForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    phone = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)

    def __str__(self):
        return self.name
    
    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get("name")
        email = cleaned_data.get("email")
        phone = cleaned_data.get("phone")
        message = cleaned_data.get("message")

        if not name and not email and not phone and not message:
            raise forms.ValidationError("You have to write something!")
    
    # action on form submission
    def save(self):
        super().save()

class BootcampForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    phone = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)

    def __str__(self):
        return self.name
    
    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get("name")
        email = cleaned_data.get("email")
        phone = cleaned_data.get("phone")
        message = cleaned_data.get("message")

        if not name and not email and not phone and not message:
            raise forms.ValidationError("You have to write something!")
    
    # action on form submission
    def save(self):
        super().save()

class AppointmentForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    phone = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)

    def __str__(self):
        return self.name
    
    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get("name")
        email = cleaned_data.get("email")
        phone = cleaned_data.get("phone")
        message = cleaned_data.get("message")

        if not name and not email and not phone and not message:
            raise forms.ValidationError("You have to write something!")
    
    # action on form submission
    def save(self):
        super().save()

class PartnersForm(forms.Form):
    pass

class SpecializeCourseForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    phone = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)

    def __str__(self):
        return self.name
    
    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get("name")
        email = cleaned_data.get("email")
        phone = cleaned_data.get("phone")
        message = cleaned_data.get("message")

        if not name and not email and not phone and not message:
            raise forms.ValidationError("You have to write something!")
    
    # action on form submission
    def save(self):
        super().save()