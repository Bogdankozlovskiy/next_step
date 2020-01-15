from django import forms
from .models import Comment


class CommentForm(forms.Form):
	text = forms.CharField(max_length=50)
	text.widget.attrs.update({'class':'form-control'})

	# class Meta:                  # if forms.ModelForm
	# 	model = Comment
	# 	fields = ['text']
	# 	widgets = {'text': forms.TextInput(attrs={'class':'form-control'})}

	def save(self, idd, user):
		new_comment = Comment.objects.create(
			text = self.cleaned_data['text'],
			video_id = idd,
			user_id = user.id,
		)
		return new_comment