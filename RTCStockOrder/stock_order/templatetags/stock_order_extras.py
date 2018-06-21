from django.template.defaulttags import register


@register.filter
def make_readable(value):
    # Replaces underscores and captilises text
    value = value.replace('_',' ')
    value = value.title()
    value = value.replace('Rtc ', 'RTC ')
    return value

