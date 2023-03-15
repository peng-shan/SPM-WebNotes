from django.test import TestCase

# Create your tests here.
from . import views
from django.urls import reverse
from rest_framework import status


# @api_view(['GET', 'POST'])
# def getNotes(request):

#     if request.method == 'GET':
#         return getNotesList(request)

#     if request.method == 'POST':
#         return createNote(request)


# @api_view(['GET', 'PUT', 'DELETE'])
# def getNote(request, pk):

#     if request.method == 'GET':
#         return getNoteDetail(request, pk)

#     if request.method == 'PUT':
#         return updateNote(request, pk)

#     if request.method == 'DELETE':
#         return deleteNote(request, pk)



class NoteTests(TestCase):
    
        def test_get_notes(self):
            url = reverse('notes')
            response = self.client.get(url)
            self.assertEqual(response.status_code, status.HTTP_200_OK)
    
        # def test_get_note_detail(self):
        #     url = reverse('note', args=['1'])
        #     response = self.client.get(url)
        #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    
        def test_create_note(self):
            url = reverse('notes')
            response = self.client.post(url, {'body': 'test'})
            self.assertEqual(response.status_code, status.HTTP_200_OK)
    
        # def test_update_note(self):
        #     url = reverse('note', args=['1'])
        #     response = self.client.put(url, {'body': 'test'})
        #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    
        def test_delete_note(self):
            url = reverse('note', args=['1'])
            response = self.client.delete(url)
            self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
