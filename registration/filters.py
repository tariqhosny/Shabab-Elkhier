from django.contrib.admin import SimpleListFilter
from django.db.models import Count

class DuplicateNameFilter(SimpleListFilter):
    title = 'Duplicate Names'
    parameter_name = 'duplicate_names'

    def lookups(self, request, model_admin):
        return (
            ('duplicates', 'Duplicates'),
        )

    def queryset(self, request, queryset):
        if self.value() == 'duplicates':
            duplicates = (queryset
                          .values('name')
                          .annotate(name_count=Count('name'))
                          .filter(name_count__gt=1)
                          .values_list('name', flat=True))
            return queryset.filter(name__in=duplicates)
        return queryset
    
class DuplicateNationalIDFilter(SimpleListFilter):
    title = 'Duplicate National IDs'
    parameter_name = 'duplicate_national_ids'

    def lookups(self, request, model_admin):
        return (
            ('duplicates', 'Duplicates'),
        )

    def queryset(self, request, queryset):
        if self.value() == 'duplicates':
            duplicates = (queryset
                          .values('national_id')
                          .annotate(national_id_count=Count('national_id'))
                          .filter(national_id_count__gt=1)
                          .values_list('national_id', flat=True))
            return queryset.filter(national_id__in=duplicates)
        return queryset