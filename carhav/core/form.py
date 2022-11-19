from django import forms

from carhav.core.models import UserCourseApplicationModel, UserInterviewSchedule

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

class SpecializeCourseForm(forms.ModelForm):
    # add options to a time_to_join field
    time_to_join = forms.ChoiceField(
        choices=[
            ("ASAP", "ASAP"),
            ("1 Month", "1 Month"),
            ("3 Months", "3 Months"),
            ("6 Months", "6 Months"),
            ("1 Year", "1 Year"),
        ]
    )
    # country_of_residence should be a choice field with options from a list of countries
    country_of_residence = forms.ChoiceField(
        choices=[
            ("Canada", "Canada"),
            ("United States", "United States"),
            ("United Kingdom", "United Kingdom"),
            ("Nigeria", "Nigeria"),
            ("Ghana", "Ghana"),
            ("Kenya", "Kenya"),
            ("South Africa", "South Africa"),
            ("Australia", "Australia"),
            ("Germany", "Germany"),
            ("France", "France"),
            ("Spain", "Spain"),
            ("Italy", "Italy"),
            ("Russia", "Russia"),
            ("China", "China"),
            ("Japan", "Japan"),
            ("India", "India"),
            ("Brazil", "Brazil"),
            ("Mexico", "Mexico"),
            ("Argentina", "Argentina"),
            ("Chile", "Chile"),
            ("Colombia", "Colombia"),
            ("Peru", "Peru"),
            ("Venezuela", "Venezuela"),
            ("Other", "Other"),
        ]
    )
    class Meta:
        model = UserCourseApplicationModel
        fields = "__all__"
        exclude = ["slug", "created_at", "updated_at", "bootCamp"]

    def __str__(self):
        return self.name

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get("name")
        email = cleaned_data.get("email")
        phone = cleaned_data.get("phone")
        message = cleaned_data.get("message")
        country_of_residence = cleaned_data.get("country_of_residence")
        city_of_residence = cleaned_data.get("city_of_residence")
        if not name and not email and not phone and not message:
            raise forms.ValidationError("We need your name, email, phone and message!")

    # action on form submission
    def save(self):
        super().save()
        
        
class UserInterviewScheduleForm(forms.ModelForm):
    # add options to a time_to_join field
    time_to_join = forms.ChoiceField(
        choices=[
            ("ASAP", "ASAP"),
            ("1 Month", "1 Month"),
            ("3 Months", "3 Months"),
            ("6 Months", "6 Months"),
            ("1 Year", "1 Year"),
        ]
    )
    # country_of_residence should be a choice field with options from a list of countries
    country_of_residence = forms.ChoiceField(
        choices=[
            ("Canada", "Canada"),
            ("United States", "United States"),
            ("United Kingdom", "United Kingdom"),
            ("Nigeria", "Nigeria"),
            ("Ghana", "Ghana"),
            ("Kenya", "Kenya"),
            ("South Africa", "South Africa"),
            ("Australia", "Australia"),
            ("Germany", "Germany"),
            ("France", "France"),
            ("Spain", "Spain"),
            ("Italy", "Italy"),
            ("Russia", "Russia"),
            ("China", "China"),
            ("Japan", "Japan"),
            ("India", "India"),
            ("Brazil", "Brazil"),
            ("Mexico", "Mexico"),
            ("Argentina", "Argentina"),
            ("Chile", "Chile"),
            ("Colombia", "Colombia"),
            ("Peru", "Peru"),
            ("Venezuela", "Venezuela"),
            ("Other", "Other"),
        ]
    )
    class Meta:
        model = UserInterviewSchedule
        fields = "__all__"
        exclude = ["slug", "created_at", "updated_at"]

    def __str__(self):
        return self.name

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get("name")
        email = cleaned_data.get("email")
        phone = cleaned_data.get("phone")
        message = cleaned_data.get("message")
        country_of_residence = cleaned_data.get("country_of_residence")
        city_of_residence = cleaned_data.get("city_of_residence")
        if not name and not email and not phone and not message:
            raise forms.ValidationError("We need your name, email, phone and message!")

    # action on form submission
    def save(self):
        super().save()