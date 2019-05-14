import django_filters.rest_framework


class ListOnlyFilterBackend(django_filters.rest_framework.DjangoFilterBackend):
    def filter_queryset(self, request, queryset, view):
        if view.detail:
            return queryset  # do not filter
        
        return super().filter_queryset(request, queryset, view)
