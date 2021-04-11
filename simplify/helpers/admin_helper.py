from django.contrib import admin
from django.contrib.admin import SimpleListFilter


def __a2z_filter(_field):
    class ModelFilter(SimpleListFilter):
        field = _field
        title = f'alphabet - {_field.replace("_", " ")}'
        parameter_name = f"{field}__alpha"

        def lookups(self, request, model_admin):
            qs = model_admin.get_queryset(request).values_list(self.field, flat=True)
            values = sorted(set(str(x)[0].lower() for x in qs))
            
            for i in values:
                if len(i):
                    yield (i[0], i[0])

        def queryset(self, request, queryset):
            pn = request.GET.dict()
            query_dict = {}
            for k, v in pn.items():
                query_dict[k.replace("__alpha", "__istartswith")] = v

            return queryset.model.objects.filter(**query_dict)

    return ModelFilter



class AlphaNumericFilterAdmin(admin.ModelAdmin):
    def __init__(self, model, admin_site):
        self.model = model
        self.opts = model._meta
        self.admin_site = admin_site

        _filter = [__a2z_filter(x) for x in self.alphanumeric_filter]
        self.list_filter += _filter
