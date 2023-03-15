from rest_framework.serializers import ModelSerializer
from .models import Note, NotesUsers


class NoteSerializer(ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'

class NotesUsersSerializer(ModelSerializer):
    class Meta:
        model = NotesUsers
        fields = '__all__'
