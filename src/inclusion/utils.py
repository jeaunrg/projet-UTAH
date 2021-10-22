
from operator import attrgetter
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from inclusion.models import Patient
from django.db.models import Q



def get_patients_queryset(query=None, **kwargs):
    queryset = []
    queries = query.split(" ")

    ref_patients = Patient.objects.filter(**kwargs)

    for q in queries:
        patients = Patient.objects.filter(
				Q(id__icontains=q) |
				Q(nipp__icontains=q) |
				Q(first_name__icontains=q) |
				Q(last_name__icontains=q)
			).distinct()

        for patient in patients:
            if patient in ref_patients:
                queryset.append(patient)

    return list(set(queryset))


def get_patients_page(request, patients_per_page=10, filter='is_author'):
    # Search
    query = ""
    if request.GET:
        query = str(request.GET.get('q', ''))

    kwargs = {}
    if filter == "is_author":
        kwargs["author"] = request.user

    patients = sorted(get_patients_queryset(query, **kwargs), key=attrgetter('date_updated'), reverse=True)


	# Pagination
    page = request.GET.get('page', 1)
    patients_paginator = Paginator(patients, patients_per_page)
    try:
        patients = patients_paginator.page(page)
    except PageNotAnInteger:
        patients = patients_paginator.page(patients_per_page)
    except EmptyPage:
        patients = patients_paginator.page(patients_paginator.num_pages)

    return query, patients
