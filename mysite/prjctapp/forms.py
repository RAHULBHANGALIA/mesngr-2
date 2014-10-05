from django import forms
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.template.defaultfilters import filesizeformat
from models import Message,User,Upload
   
class FileUploadForm(forms.Form):
    audio_file = forms.FileField(label = _(u"Audio File"))

    def clean(self):
        cleaned_data = self.cleaned_data
        file = cleaned_data.get("audio_file")
        file_exts = ('.mp3',)

        if file is None:
            raise forms.ValidationError('Please select file first')
        if not cotent_type in settings.CONTENT_TYPES:
            raise forms.ValidationError('Audio accepted  only in: %s' % ''.join( file_exts))

        return cleaned_data    
                                            
class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['message_to', 'message_from', 'message_text', 'send_image_or_pdf']
    
##class ProfileForm(forms.ModelForm):
##    class Meta:
##        model = Users
##        fields = ['user_name','user_photo']
        
class SignupForm(forms.ModelForm):
    class Meta:
        model = User
        fields=['user_name','password','user_photo']

class PicuploadForm(forms.ModelForm):    
    #file = Upload.objects.get(id=1).upload.url
    class Meta:
        model = User
        fields = ['user_photo']
