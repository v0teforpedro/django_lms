from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from students.models import Student

from .forms import GroupCreateForm, GroupUpdateForm
from .models import Group


# def create_group(request):
#     if request.method == 'GET':
#         form = GroupCreateForm()
#     else:
#         form = GroupCreateForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('groups:list'))
#
#     return render(
#         request,
#         'groups/create_group.html',
#         context={'title': 'Create Group', 'form': form}
#     )


class CreateGroupView(CreateView):
    model = Group
    success_url = reverse_lazy('groups:list')
    template_name = 'groups/create_group.html'
    form_class = GroupCreateForm
    extra_context = {'title': 'Create Group'}


# def groups(request):
#     gp = Group.objects.all()
#     return render(
#         request,
#         'groups/groups.html',
#         context={'title': 'List of Groups', 'groups': gp}
#     )


class ListGroupView(ListView):
    model = Group
    template_name = 'groups/groups.html'
    extra_context = {'title': 'List of Groups'}


# def update_group(request, pk):
#     group = get_object_or_404(Group, pk=pk)
#     if request.method == 'GET':
#         form = GroupCreateForm(instance=group)
#     else:
#         form = GroupCreateForm(request.POST, instance=group)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('groups:list'))
#
#     return render(
#         request,
#         'groups/update_group.html',
#         context={'title': 'Update Group', 'form': form, 'group': group}
#     )


class UpdateGroupView(UpdateView):
    model = Group
    success_url = reverse_lazy('groups:list')
    template_name = 'groups/update_group.html'
    form_class = GroupUpdateForm
    extra_context = {'title': 'Update Group'}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['students'] = self.get_object().students.prefetch_related('headman_group')

        return context

    def get_initial(self):
        initial = super().get_initial()
        try:
            initial['headman_field'] = self.object.headman.pk
        except AttributeError:
            pass
        return initial

    def form_valid(self, form):
        response = super().form_valid(form)
        try:
            form.instance.headman = Student.objects.get(pk=form.cleaned_data['headman_field'])
            form.instance.save()
        except ValueError:
            pass
        return response


# def delete_group(request, pk):
#     group = Group.objects.get(pk=pk)
#     if request.method == 'POST':
#         group.delete()
#         return HttpResponseRedirect(reverse('groups:list'))
#     else:
#         return render(request, 'confirmation.html', {'object': group})


class DeleteGroupView(DeleteView):
    model = Group
    success_url = reverse_lazy('groups:list')
    template_name = 'confirmation.html'
