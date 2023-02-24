from rest_framework import serializers
from .models import *
class CountrySerializer(serializers.ModelSerializer):
  class Meta:
    model=Country
    fields='__all__'
    
class CitySerializer(serializers.ModelSerializer):
  select_type=serializers.SerializerMethodField()
  class Meta:
    model=City
    fields='__all__'
    
  def to_representation(self, instance):
    data = super().to_representation(instance)
    data['country_name']=Country.objects.filter(id=instance.country_id).first().country_name
    return data

  def get_select_type(self, obj):
    # import pdb;pdb.set_trace()
    if self.context:
      if str(obj.id) in  self.context['city_id']:
        return True
    return False
     