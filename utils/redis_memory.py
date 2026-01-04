import redis

# Redis connection
redis_client = redis.Redis(
    host="127.0.0.1",
    port=6379,
    db=0,
    decode_responses=True
)

CHAT_TTL_SECONDS = 60 * 60 * 24  # 24 hours


def get_conversation(chat_id: str) -> str:
    """
    Fetch full conversation history for a chat.
    """
    key = f"chat:{chat_id}"
    messages = redis_client.lrange(key, 0, -1)
    return "\n".join(messages)


def append_message(chat_id: str, role: str, message: str):
    """
    Append a message to the conversation history.
    """
    key = f"chat:{chat_id}"
    redis_client.rpush(key, f"{role}: {message}")
    redis_client.expire(key, CHAT_TTL_SECONDS)
