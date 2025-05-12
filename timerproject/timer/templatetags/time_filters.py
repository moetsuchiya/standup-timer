from django import template
from datetime import timedelta

register = template.Library()

@register.filter
def format_duration(seconds):
    """秒数を時間:分:秒の形式に変換する"""
    try:
        # 文字列型の場合は数値型に変換
        seconds = float(seconds)
        duration = timedelta(seconds=seconds)
        hours = duration.seconds // 3600 + duration.days * 24
        minutes = (duration.seconds % 3600) // 60
        seconds = duration.seconds % 60

        if hours > 0:
            return f"{hours}時間{minutes}分{seconds}秒"
        elif minutes > 0:
            return f"{minutes}分{seconds}秒"
        else:
            return f"{seconds}秒"
    except (ValueError, TypeError):
        return "0秒"  # エラーの場合は0秒を返す
