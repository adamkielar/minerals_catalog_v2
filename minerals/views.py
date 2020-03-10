from django.shortcuts import get_object_or_404, render
from django.db.models import Q
from .models import Mineral
from .filters import MineralFilter


def mineral_list(request):
    minerals = Mineral.objects.all()
    mineral_filter = MineralFilter(request.GET, queryset=minerals)
    minerals = mineral_filter.qs
    active_letter = "A"

    return render(
        request,
        "minerals/minerals_list.html",
        {
            "minerals": minerals,
            "mineral_filter": mineral_filter,
            "active_letter": active_letter,
        },
    )


def mineral_detail(request, pk):
    mineral = get_object_or_404(Mineral, pk=pk)
    mineral_values = Mineral.objects.values().filter(pk=pk).first()

    return render(
        request,
        "minerals/mineral_detail.html",
        {"mineral": mineral, "mineral_values": mineral_values,},
    )


def mineral_letter(request, letter="A"):
    minerals = Mineral.objects.filter(Q(name__istartswith=letter))

    active_letter = letter

    return render(
        request,
        "minerals/minerals_list.html",
        {"minerals": minerals, "active_letter": letter,},
    )


def mineral_search(request):
    query = request.GET.get("q")

    if query:
        minerals = Mineral.objects.filter(
            Q(name__icontains=query)
            | Q(image_filename__icontains=query)
            | Q(image_caption__icontains=query)
            | Q(category__icontains=query)
            | Q(formula__icontains=query)
            | Q(strunz_classification__icontains=query)
            | Q(crystal_system__icontains=query)
            | Q(unit_cell__icontains=query)
            | Q(color__icontains=query)
            | Q(crystal_symmetry__icontains=query)
            | Q(cleavage__icontains=query)
            | Q(mohs_scale_hardness__icontains=query)
            | Q(luster__icontains=query)
            | Q(streak__icontains=query)
            | Q(diaphaneity__icontains=query)
            | Q(optical_properties__icontains=query)
            | Q(refractive_index__icontains=query)
            | Q(group__icontains=query)
            | Q(crystal_habit__icontains=query)
            | Q(specific_gravity__icontains=query)
        )

    return render(request, "minerals/minerals_list.html", {"minerals": minerals})
