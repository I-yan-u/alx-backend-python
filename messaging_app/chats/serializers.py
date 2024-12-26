from rest_framework import serializers
from .models import CustomUser, Conversation, Message


class CustomUserSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()

    class Meta:
        model = CustomUser
        fields = [
            "user_id",
            "username",
            "email",
            "first_name",
            "last_name",
            "phone_number",
            "role",
            "full_name",
        ]

    def get_full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}"


class MessageSerializer(serializers.ModelSerializer):
    sender_name = serializers.CharField(
        source="sender.username", read_only=True
    )

    class Meta:
        model = Message
        fields = [
            "message_id",
            "sender",
            "sender_name",
            "message_body",
            "sent_at",
        ]

    def validate_message_body(self, value):
        if len(value) < 1:
            raise serializers.ValidationError("Message body can not be empty.")
        return value


class ConversationSerializer(serializers.ModelSerializer):
    participants = CustomUserSerializer(many=True, read_only=True)
    messages = MessageSerializer(many=True, read_only=True)
    message_count = serializers.SerializerMethodField()

    class Meta:
        model = Conversation
        fields = [
            "conversation_id",
            "participants_id",
            "messages",
            "message_count",
            "created_at",
        ]

    def get_message_count(self, obj):
        return obj.messages.count()