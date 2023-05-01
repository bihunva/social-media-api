from rest_framework import serializers

from posts.models import Post


class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source="author.username")

    class Meta:
        model = Post
        fields = ("id", "title", "content", "created_at", "updated_at", "author")
        read_only_fields = ("id", "created_at", "updated_at", "author")
