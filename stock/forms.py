from django import forms
from .models import Kstock

class StockCreateForm(forms.ModelForm):

    class Meta:
        model = Kstock
        fields = ['name', 'purchase_data', 'buy_price', 'description']
        #['name', 'purchase_data', 'buy_price', 'description']

    ''' 내부적으로 구현되어 있음 (멤버변수 인스턴스)
		향후 수정 기능 구현시 활용
	def save(self, commit=True):
		self.instance = Post(**self.cleaned_data)
		if commit:
			self.instance.save()
		return self.instance
	'''