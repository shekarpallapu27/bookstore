from app1.models import BookDetails
from rest_framework import serializers

class BookSerializer(serializers.ModelSerializer):
	class Meta:
		model = BookDetails
		fields = ['book_id','book_name','num_of_books','rack_number','published_date','author_name']
	author_name = serializers.SerializerMethodField('get_author_name')
	def get_author_name(self,obj):
		return obj.author_id.username