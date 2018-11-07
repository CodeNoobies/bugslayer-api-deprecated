import hashlib
import urllib
from django import template
from django.utils.safestring import mark_safe
import mistune


register = template.Library()

@register.filter
def gravatar_url(email):
    return "https://www.gravatar.com/avatar/%s" % hashlib.md5(email.encode('utf-8')).hexdigest()


@register.filter()
def markdown(text):
    md = mistune.Markdown()
    return md(text)
