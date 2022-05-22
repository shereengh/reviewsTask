from django.shortcuts import render
from api.serializers import ReviewListSerializer
from reviews.models import Review
from rest_framework.generics import ListAPIView,CreateAPIView

class ReviewListView(ListAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewListSerializer

class CreateView(CreateAPIView):
    serializer_class = ReviewListSerializer