from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import Http404, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic
from powerdata.models import SCPMmeasurement
from django.core import serializers
import json

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

def latest(request, n_records=''):
    ''' Returns a json response of the latest measurement '''
    if n_records == '':
        n_records = 1
    try:
        measurement = SCPMmeasurement.objects.order_by('-unix_time')[:n_records]
        # Serialize 'list'
        data = serializers.serialize('json', measurement)
        # Pack list
        struct = json.loads(data)
        if n_records == 1:
            # Unpack list, 1 json obj
            data = json.dumps(struct[0])

    except SCPMmeasurement.DoesNotExist:
        raise Http404
    return HttpResponse(data, content_type='application/json')

def piechart(request):
    #template = loader.get_template('powerdata/piechart/html')
    xdata = ["Apple", "Apricot", "Avocado", "Banana",
             "Boysenberries", "Blueberries", "Dates",
             "Grapefruit", "Kiwi", "Lemon"]
    ydata = [52, 48, 169, 94, 75, 71, 490, 82, 46, 17]
    chartdata = {'x': xdata, 'y': ydata}
    charttype = "pieChart"
    chartcontainer = 'piechart_container'
    data = {
        'charttype': charttype,
        'chartdata': chartdata,
        'chartcontainer': chartcontainer,
        'extra': {
            'x_is_date': False,
            'x_axis_format': '',
            'tag_script_js': True,
            'jquery_on_ready': False,
        }
    }
    return render_to_response('powerdata/piechart.html', data)

