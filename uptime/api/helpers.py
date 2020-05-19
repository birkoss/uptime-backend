from django.db.models import Q


def apiGetUserFilters(**kwargs):
    filters = Q()

    if not kwargs['user'].is_staff:
        filters.add(Q(user=kwargs['user']), Q.AND)

    return filters
