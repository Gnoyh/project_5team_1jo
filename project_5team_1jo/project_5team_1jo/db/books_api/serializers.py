from rest_framework import serializers
from books.models import RecomBooks

class RecomBooksSerializer(serializers.Serializer):
    #필드 정의
    id = serializers.IntegerField(read_only = True)
    title = serializers.CharField(max_length=50)
    author = serializers.CharField(max_length=20)
    recomment = serializers.CharField(max_length=2000)
    isbn = serializers.CharField(max_length=13)
    publisher = serializers.CharField(max_length=8)
    recomno = serializers.CharField(max_length=20)
    drcode = serializers.IntegerField()

    #신규 생성
    def create(self, validated_data):
        return RecomBooks.objects.create(**validated_data)
    
    #인스턴스 갱신
    def update(self, instance, validated_data):
        #OrderedDict type
        instance.title = validated_data.get('title', instance.title)
        instance.author = validated_data.get('author', instance.author)
        instance.recomment = validated_data.get('recomment', instance.recomment)
        instance.isbn = validated_data.get('isbn', instance.isbn)
        instance.publisher = validated_data.get('publisher', instance.publisher)
        instance.recomno = validated_data.get('recomno', instance.recomno)
        instance.drcode = validated_data.get('drcode', instance.drcode)
        instance.save()
        return instance