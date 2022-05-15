from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from .forms import GroupCreateForm
from .models import Group


def groups(request):
    gp = Group.objects.all()
    return render(
        request,
        'groups/groups.html',
        context={'title': 'List of Groups', 'groups': gp}
    )


@csrf_exempt
def create_group(request):
    if request.method == 'GET':
        form = GroupCreateForm()
    else:
        form = GroupCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('<h1>Group Created!</h1>')

    html_form = f"""
        <form method="post">
            <table>
                {form.as_table()}
            </table>
            <input type="submit" value="Create">
        </form> 
        """

    return HttpResponse(html_form)


@csrf_exempt
def update_group(request, pk):
    group = Group.objects.get(pk=pk)
    if request.method == 'GET':
        form = GroupCreateForm(instance=group)
    else:
        form = GroupCreateForm(request.POST, instance=group)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/groups')

    html_form = f"""
        <form method="post">
            <table>
                {form.as_table()}
            </table>
            <input type="submit" value="Update">
        </form> 
        """

    return HttpResponse(html_form)


def delete_group(request, pk):
    Group.objects.filter(pk=pk).delete()
    return HttpResponseRedirect('/groups')

