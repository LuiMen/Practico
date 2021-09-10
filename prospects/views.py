from django.db.models import Q
from django.shortcuts import render, redirect
from django.utils.translation import ugettext_lazy as _
from django.views.generic import CreateView

from prospects.forms import ProspectsDocumentsFormset, ProspectsEvaluationForm
from prospects.models import Prospects


def prospects_list(request):
    title = _('Prospects List')
    headers = [_('Names'), _('First lastname'), _('Second lastname'), _('Status')]
    q = Q()
    if request.method == 'GET':
        query = request.GET.get('q')
        if query:
            q &= Q(name__icontains=query) | Q(first_lastname__icontains=query) | Q(second_lastname__icontains=query)

        status = request.GET.get('status')
        try:
            int(status)
            if status:
                q &= Q(status=status)
        except:
            pass

    context = {
        'title': title,
        'headers': headers,
        'queryset': Prospects.objects.filter(q),
    }
    return render(request, "list.html", context)


class ProspectsCreateView(CreateView):
    model = Prospects
    fields = ['name', 'first_lastname', 'second_lastname', 'street', 'number', 'suburb', 'zip_code', 'phone', 'rfc']
    template_name = 'register_prospect.html'

    def form_valid(self, form):
        result = super(ProspectsCreateView, self).form_valid(form)

        documents_formset = ProspectsDocumentsFormset(form.data, form.files, instance=self.object,
                                                      prefix='documents_formset')
        if documents_formset.is_valid():
            documents_formset.save()

        return result

    def get_context_data(self, **kwargs):
        context = super(ProspectsCreateView, self).get_context_data(**kwargs)
        context['documents_formset'] = ProspectsDocumentsFormset(prefix='documents_formset')
        return context

    def get_success_url(self):
        return '/'


def prospect_view(request, pk):
    model = Prospects.objects.get(pk=pk)
    fields = {
        _('Street'): model.street,
        _('Number'): model.number,
        _('Suburb'): model.suburb,
        _('Suburb'): model.suburb,
        _('Zip code'): model.zip_code,
        _('Phone'): model.phone,
        _('RFC'): model.rfc,
        _('Status'): model.get_status_value,
    }
    if model.status == Prospects.Status.REJECTED:
        fields.update({
            _('Reject details'): model.reject_details
        })

    form = ProspectsEvaluationForm(request.POST or None, instance=model)
    if form.is_valid():
        prospect = form.save(commit=False)
        prospect.status = Prospects.Status.REJECTED
        prospect.save()
        return redirect("/prospects/")

    context = {
        'title': model,
        'files': model.documents.all(),
        'fields': fields,
        'form': form,
        'evaluated': True if model.status != Prospects.Status.SENT else False
    }
    return render(request, "view.html", context)


def approve_prospect_view(request, pk):
    instance = Prospects.objects.get(pk=pk)
    instance.status = Prospects.Status.AUTHORIZED
    instance.save()
    return redirect("/prospects/")
