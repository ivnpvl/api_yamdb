from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ModelViewSet

from reviews.models import Title, Review
from .permissions import IsResponsibleUserOrReadOnly
from .serializers import ReviewSerializer, CommentSerializer


class ReviewViewSet(ModelViewSet):
    http_method_names = [
        'get', 'post', 'patch', 'delete', 'head', 'options', 'trace'
    ]
    serializer_class = ReviewSerializer
    permission_classes = (IsResponsibleUserOrReadOnly,)

    def get_queryset(self):
        title_id = self.kwargs.get('title_id')
        title = get_object_or_404(Title, id=title_id)
        queryset = title.reviews.select_related('author').all()
        return queryset

    def perform_create(self, serializer):
        title_id = self.kwargs.get('title_id')
        title = get_object_or_404(Title, id=title_id)
        serializer.save(
            author=self.request.user,
            title=title
        )


class CommentViewSet(ModelViewSet):
    http_method_names = [
        'get', 'post', 'patch', 'delete', 'head', 'options', 'trace'
    ]
    serializer_class = CommentSerializer
    permission_classes = (IsResponsibleUserOrReadOnly,)

    def get_queryset(self):
        title_id = self.kwargs.get('title_id')
        review_id = self.kwargs.get('review_id')
        review = get_object_or_404(Review, id=review_id, title=title_id)
        queryset = review.comments.select_related('author').all()
        return queryset

    def perform_create(self, serializer):
        title_id = self.kwargs.get('title_id')
        review_id = self.kwargs.get('review_id')
        review = get_object_or_404(Review, id=review_id, title=title_id)
        serializer.save(
            author=self.request.user,
            review=review
        )
