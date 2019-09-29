from rest_framework import serializers
from .models import Article, Category, Tag
from users.models import User


class CategorySubSerializer(serializers.ModelSerializer):
    """子分类序列化"""

    class Meta:
        model = Category
        fields = ('id', 'name')


class CategorySerializer(serializers.ModelSerializer):
    """文章分类序列化"""
    subs = CategorySubSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ('id', 'name', 'parent', 'owner', 'subs')
        extra_kwargs = {
            'parent': {'write_only': True},
            'owner': {'write_only': True}
        }


class TagSerializer(serializers.ModelSerializer):
    """标签序列化类"""

    class Meta:
        model = Tag
        fields = ('id', 'name', 'owner')


class ArticleCreateSerializer(serializers.ModelSerializer):
    """创建文章序列化类"""

    class Meta:
        model = Article
        fields = ('title', 'body', 'pub_time', 'author', 'category', 'tags')


class AuthorSerializer(serializers.ModelSerializer):
    """文章作者序列化类"""

    class Meta:
        model = User
        fields = ('id', 'username')


class CategoryArticleSerializer(serializers.ModelSerializer):
    """文章所属类序列化类"""

    class Meta:
        model = Category
        fields = ('name',)


class TagArticleSerializer(serializers.ModelSerializer):
    """文章标签序列化类"""

    class Meta:
        model = Tag
        fields = ('name',)


class ArticleListSerializer(serializers.ModelSerializer):
    """文章列表序列化类"""
    author = AuthorSerializer()
    category = CategoryArticleSerializer()
    tags = TagArticleSerializer(many=True)

    class Meta:
        model = Article
        fields = ('title', 'pub_time', 'author', 'category', 'tags')


class ArticleDetailSerializer(serializers.ModelSerializer):
    """文章详情序列化类"""
    author = AuthorSerializer()
    category = CategoryArticleSerializer()
    tags = TagArticleSerializer(many=True)

    class Meta:
        model = Article
        fields = ('title', 'body', 'pub_time', 'author', 'category', 'tags')
