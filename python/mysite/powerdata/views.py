from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import Http404, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic
from powerdata.models import SCPMmeasurement
from django.core import serializers
import json, datetime, time, math

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
        if n_records >= 10000:
            n_records = 10000
        measurement = SCPMmeasurement.objects.order_by('-unix_time')[:n_records]
        measurement = [obj.as_dict() for obj in measurement]
        # Serialize 'list'
        data = json.dumps(measurement)
        # Pack list
        struct = json.loads(data)
        if n_records == 1:
            # Unpack list, 1 json obj
            data = json.dumps(struct[0])

    except SCPMmeasurement.DoesNotExist:
        raise Http404
    return HttpResponse(data, content_type='application/json')

def latest_chart(request, hours=1):
    """
    linewithfocuschart page
    """
    '''
    The rest of this is basically to stop the query
    being super slow as a result of getting tonnes of records.
    We can't plot more than ~ 5000 records anyway without the
    graph being too slow, so we get every $hour record in our
    range which reduces the size of the returned dataset massively.
    '''
    hours = int(hours)
    # Convert to number of records
    n_records = 3600*hours
    # Set up initial filter
    measurements = SCPMmeasurement.objects.filter(unix_time__gte=time.time()-n_records)
    # Extra query for mysql which retrieves only every $hours entry
    measurements = measurements.extra(where=['ROUND(unix_time) %% {0:d} = 0'.format(hours)])

    # Populate data. It's only now (when we iterate) that the query executes.
    xdata = [float(x.unix_time) * 1000 for x in measurements]
    ydata = [float(x.active_power) for x in measurements]
    ydata2 = [float(x.apparent_power) for x in measurements]
    ydata3 = [float(x.voltage) for x in measurements]

    tooltip_date = "%d %b %Y %H:%M:%S %p"
    extra_serie_act = {"tooltip": {"y_start": "Value is ", "y_end": " W"},
                   "date_format": tooltip_date}
    extra_serie_app = {"tooltip": {"y_start": "Value is ", "y_end": " VA"},
                       "date_format": tooltip_date}
    extra_serie_V = {"tooltip": {"y_start": "Value is ", "y_end": " V"},
                       "date_format": tooltip_date}
    chartdata = {
        'x': xdata,
        'name1': 'Active Power', 'y1': ydata, 'extra1': extra_serie_act,
        'name2': 'Apparent Power', 'y2': ydata2, 'extra2': extra_serie_app,
        'name3': 'Voltage', 'y3': ydata3, 'extra3': extra_serie_V
    }
    charttype = "lineWithFocusChart"
    chartcontainer = 'linewithfocuschart_container'  # container name
    data = {
        'charttype': charttype,
        'chartdata': chartdata,
        'chartcontainer': chartcontainer,
        'extra': {
            'x_is_date': True,
            'x_axis_format': '%d %b %H:%M',
            'tag_script_js': True,
            'jquery_on_ready': True,
        }
    }
    return render_to_response('powerdata/linewithfocuschart.html', data)


def livechart(request, last_minutes=10):
    # get last minute of data initially
    last_minutes = int(last_minutes)
    initial_data = [obj.as_dict() for obj in reversed(SCPMmeasurement.objects.order_by('-unix_time')[:last_minutes*60])]
    initial_data = json.dumps(initial_data)
    return render(request, 'powerdata/livechart.html', {"my_data": initial_data})
