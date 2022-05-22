from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .forms import GroupCreateForm
from .models import Group


def create_group(request):
    if request.method == 'GET':
        form = GroupCreateForm()
    else:
        form = GroupCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('groups:list'))

    return render(
        request,
        'groups/create_group.html',
        context={'title': 'Create Group', 'form': form}
    )


def groups(request):
    gp = Group.objects.all()
    return render(
        request,
        'groups/groups.html',
        context={'title': 'List of Groups', 'groups': gp}
    )


def update_group(request, pk):
    group = Group.objects.get(pk=pk)
    if request.method == 'GET':
        form = GroupCreateForm(instance=group)
    else:
        form = GroupCreateForm(request.POST, instance=group)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('groups:list'))

    return render(
        request,
        'groups/update_group.html',
        context={'title': 'Update Grou[', 'form': form}
    )


def delete_group(request, pk):
    group = Group.objects.get(pk=pk)
    if request.method == 'POST':
        group.delete()
        return HttpResponseRedirect(reverse('groups:list'))
    else:
        return render(request, 'confirmation.html', {'object': group})
