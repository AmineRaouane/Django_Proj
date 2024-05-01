from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import UserSerializer, NoteSerializer
from rest_framework.permissions import IsAuthenticated,AllowAny
from .models import Note
# Create your views here.
class NoteListCreate(generics.ListCreateAPIView):
    """Create and list notes"""
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        """Return the authenticated user's notes"""
        author = self.request.user
        return Note.objects.filter(author=author)
    
    def perform_create(self, serializer):
        """Create a new note"""
        if serializer.is_valid():
            serializer.save(author=self.request.user)
        else:
            print(serializer.errors)

class NoteDelete(generics.DestroyAPIView):
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """Return the authenticated user's notes"""
        author = self.request.user
        return Note.objects.filter(author=author)


class CreateUserView(generics.CreateAPIView):
    """Create a new user in the system"""
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]
