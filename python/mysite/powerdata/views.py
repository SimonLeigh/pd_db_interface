from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.core.urlresolvers import reverse
from django.views import generic
from powerdata.models import SCPMmeasurement

# Create your views here.

class IndexView(generic.ListView):
    ''' Returns the index page with latest 10 measurements '''
    template_name = 'powerdata/index.html'
    context_object_name = 'latest_measurement_list'

    def get_queryset(self):
        ''' Return the last 30 measurements '''
        return SCPMmeasurement.objects.order_by('-unix_time')[:30]
 
class DetailView(generic.DetailView):
    ''' Returns the detailed information for the measurement at $unix_epoch'''
    model = SCPMmeasurement
    template_name = 'powerdata/detail.html'
    context_object_name = 'measurement'

    #def get_context_data(self, **kwargs):
    #    context = super(SCPMmeasurement, self).get_context_data(**kwargs)
    #    return context
    #measurement = get_object_or_404(SCPMmeasurement, pk=float(unix_epoch))
    #context = {'measurement': measurement, 'unix_epoch': unix_epoch}
    #return render(request, 'powerdata/detail.html', context)

