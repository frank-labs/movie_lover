from django import template

register = template.Library()

@register.filter
def format_runtime(value):
    """Convert runtime from minutes to hours and minutes."""
    if value is not None:
        hours = value // 60
        minutes = value % 60
        if hours > 0:
            return f"{hours} h {minutes} min"
        else:
            return f"{minutes} min"
    return value
