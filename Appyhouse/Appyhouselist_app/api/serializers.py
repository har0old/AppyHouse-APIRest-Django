from rest_framework import serializers
from Appyhouselist_app.models import Company, Property, Comment

class CommentSerializer(serializers.ModelSerializer):
    comment_user = serializers.StringRelatedField(read_only=True)
    class Meta: 
        model = Comment
        exclude = ["property"]
        #fields = "__all__"

class CommentAllSerializer(serializers.ModelSerializer):
    comment_user = serializers.StringRelatedField(read_only=True)
    class Meta: 
        model = Comment
        fields = "__all__"
    
class PropertySerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    longigitude_address = serializers.SerializerMethodField()
    class Meta:
        model = Property
        fields = "__all__"
        #fields = ['id', 'address', 'image']
        #exclude = ["id"]
    
    def get_longigitude_address(self, object):
        number_of_characters = len(object.address)
        return number_of_characters
         
    def validate(self, data):
        if data['address'] == data['country']:
            raise serializers.ValidationError("El valor para la dirección y el País deben ser diferentes")
        else:
            return data
        
    def validate_image(self, data):
        if len(data)<7:
            raise serializers.ValidationError("La url de la imagen es demasiado corta")
        else:
            return data

#class CompanySerializer(serializers.HyperlinkedModelSerializer): 
class CompanySerializer(serializers.ModelSerializer):
    properties = PropertySerializer(many=True, read_only=True)
    #properties = serializers.StringRelatedField(many=True, read_only=True)
    #properties = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    #properties = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='property-detail' )
    class Meta: 
        model = Company
        fields = "__all__"

