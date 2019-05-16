from django.core import validators


validate_slug_with_spaces = validators.RegexValidator(
    r'^[\s\w\-]+$', 
    'It only allows letters, numbers, whitespaces, underscores or hyphens.', 
)
