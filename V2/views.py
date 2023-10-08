from django.shortcuts import render, redirect, HttpResponseRedirect
from .forms import *
from django.views.generic.base import TemplateView
from django.views import View
from datetime import datetime


# Create your views here.
def main(request):
    distance_base_price_obj = DistanceBasePrice.objects.all().values(
        'id', 'price', 'km_value', 'day', 'created_time', 'updated_time', 'created_by__username', 'updated_by__username', 'is_enabled')
    distance_addional_price_obj = DistanceAdditionalPrice.objects.all().values(
        'id', 'price', 'km_value', 'created_time', 'updated_time', 'created_by__username', 'updated_by__username', 'is_enabled')
    tmf_obj = TimeMultiplierFactor.objects.all().values(
        'id','price', 'hours', 'created_time', 'updated_time', 'created_by__username', 'updated_by__username', 'is_enabled')
    waiting_charge_obj = WaitingCharge.objects.all().values(
        'id','price', 'per_min', 'created_time', 'updated_time', 'created_by__username', 'updated_by__username', 'is_enabled')
    context = {
        'distance_base_price_obj': distance_base_price_obj,
        'distance_addional_price_obj': distance_addional_price_obj,
        'tmf_obj': tmf_obj,
        'waiting_charge_obj': waiting_charge_obj
    }
    return render(request, 'tables.html', context=context)

################ CRUD on Distance Base Price ##############################

class DistanceBasePriceView(TemplateView):
    template_name = 'distance_base_price.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        distance_base_price_form = DistanceBasePriceForm()
        context = {'distance_base_price_form': distance_base_price_form}
        return context

    def get(self, request):
        if request.GET.get('id'):
            pi = DistanceBasePrice.objects.get(id=request.GET.get('id'))
            distance_base_price_form = DistanceBasePriceForm(instance=pi)
            return render(request, 'distance_base_price.html', {'distance_base_price_form': distance_base_price_form})
        distance_base_price_form = DistanceBasePriceForm()
        return render(request, 'distance_base_price.html', {'distance_base_price_form': distance_base_price_form})

    def post(self, request):
        if request.GET.get('id'):
            DistanceBasePrice.objects.get(id=request.GET.get('id')).delete()
            return HttpResponseRedirect('/')

        distance_base_price_form = DistanceBasePriceForm(request.POST)
        if distance_base_price_form.is_valid():
            DistanceBasePrice.objects.create(
                    price = distance_base_price_form.cleaned_data['price'],
                    km_value = distance_base_price_form.cleaned_data['km_value'],
                    day = distance_base_price_form.cleaned_data['day'],
                    updated_time = datetime.now(),
                    created_by_id = 1,
                    updated_by_id = 1,
                    is_enabled = distance_base_price_form.cleaned_data['is_enabled']
                )
            return HttpResponseRedirect('/')
        else:
            return render(request, 'distance_base_price.html', {'distance_base_price_form': distance_base_price_form})
            
class UpdateDistanceBasePriceView(View):
    def get(self, request):
        pi = DistanceBasePrice.objects.get(id=request.GET.get('id'))
        distance_base_price_form = DistanceBasePriceForm(instance=pi)
        return render(request, 'distance_base_price.html', {'distance_base_price_form': distance_base_price_form})

    def post(self, request):
        if request.GET.get('id'):
            pi = DistanceBasePrice.objects.get(id=request.GET.get('id'))
            distance_base_price_form = DistanceBasePriceForm(request.POST, instance=pi)
            if distance_base_price_form.is_valid():
                DistanceBasePrice.objects.filter(id=request.GET.get('id')).update(
                    price = distance_base_price_form.cleaned_data['price'],
                    km_value = distance_base_price_form.cleaned_data['km_value'],
                    day = distance_base_price_form.cleaned_data['day'],
                    updated_time = datetime.now(),
                    created_by_id = 1,
                    updated_by_id = 1,
                    is_enabled = distance_base_price_form.cleaned_data['is_enabled'],
                    price_type = distance_base_price_form.cleaned_data['price_type']
                )
                return HttpResponseRedirect('/')
            else:
                return render(request, 'distance_base_price.html', {'distance_base_price_form': distance_base_price_form})


################ CRUD on Distance Additonal Price ##############################

class DistanceAdditionalPriceView(TemplateView):
    template_name = 'distance_additional_price.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        distance_additional_price_form = DistanceAdditionalPriceForm()
        context = {'distance_additional_price_form': distance_additional_price_form}
        return context

    def get(self, request):
        if request.GET.get('id'):
            pi = DistanceAdditionalPrice.objects.get(id=request.GET.get('id'))
            distance_additional_price_form = DistanceAdditionalPriceForm(instance=pi)
            return render(request, 'distance_additional_price.html', {'distance_additional_price_form': distance_additional_price_form})
        distance_additional_price_form = DistanceAdditionalPriceForm()
        return render(request, 'distance_additional_price.html', {'distance_additional_price_form': distance_additional_price_form})

    def post(self, request):
        if request.GET.get('id'):
            DistanceAdditionalPrice.objects.get(id=request.GET.get('id')).delete()
            return HttpResponseRedirect('/')

        distance_additional_price_form = DistanceAdditionalPriceForm(request.POST)
        if distance_additional_price_form.is_valid():
            DistanceAdditionalPrice.objects.create(
                    price = distance_additional_price_form.cleaned_data['price'],
                    km_value = distance_additional_price_form.cleaned_data['km_value'],
                    updated_time = datetime.now(),
                    created_by_id = 1,
                    updated_by_id = 1,
                    is_enabled = distance_additional_price_form.cleaned_data['is_enabled']
                )
            return HttpResponseRedirect('/')
        else:
            return render(request, 'distance_additional_price.html', {'distance_additional_price_form': distance_additional_price_form})
            
class UpdateDistanceAdditionalPriceView(View):
    def get(self, request):
        pi = DistanceAdditionalPrice.objects.get(id=request.GET.get('id'))
        distance_additional_price_form = DistanceAdditionalPriceForm(instance=pi)
        return render(request, 'distance_additional_price.html', {'distance_additional_price_form': distance_additional_price_form})

    def post(self, request):
        if request.GET.get('id'):
            pi = DistanceAdditionalPrice.objects.get(id=request.GET.get('id'))
            distance_additional_price_form = DistanceAdditionalPriceForm(request.POST, instance=pi)
            if distance_additional_price_form.is_valid():
                DistanceAdditionalPrice.objects.filter(id=request.GET.get('id')).update(
                    price = distance_additional_price_form.cleaned_data['price'],
                    km_value = distance_additional_price_form.cleaned_data['km_value'],
                    updated_time = datetime.now(),
                    created_by_id = 1,
                    updated_by_id = 1,
                    is_enabled = distance_additional_price_form.cleaned_data['is_enabled']
                )
                return HttpResponseRedirect('/')
            else:
                return render(request, 'distance_additional_price.html', {'distance_additional_price_form': distance_additional_price_form})



################# CRUD on TMF  ########################################


class TMFView(TemplateView):
    template_name = 'tmf.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        tmf_form = TMFForm()
        context = {'tmf_form': tmf_form}
        return context

    def get(self, request):
        if request.GET.get('id'):
            pi = TimeMultiplierFactor.objects.get(id=request.GET.get('id'))
            tmf_form = TMFForm(instance=pi)
            return render(request, 'tmf.html', {'tmf_form': tmf_form})
        tmf_form = TMFForm()
        return render(request, 'tmf.html', {'tmf_form': tmf_form})

    def post(self, request):
        if request.GET.get('id'):
            TimeMultiplierFactor.objects.get(id=request.GET.get('id')).delete()
            return HttpResponseRedirect('/')

        tmf_form = TMFForm(request.POST)
        if tmf_form.is_valid():
            TimeMultiplierFactor.objects.create(
                    price = tmf_form.cleaned_data['price'],
                    hours = tmf_form.cleaned_data['hours'],
                    updated_time = datetime.now(),
                    created_by_id = 1,
                    updated_by_id = 1,
                    is_enabled = tmf_form.cleaned_data['is_enabled']
                )
            return HttpResponseRedirect('/')
        else:
            return render(request, 'tmf.html', {'tmf_form': tmf_form})
            
class UpdateTMFView(View):
    def get(self, request):
        pi = TimeMultiplierFactor.objects.get(id=request.GET.get('id'))
        tmf_form = TMFForm(instance=pi)
        return render(request, 'tmf.html', {'tmf_form': tmf_form})

    def post(self, request):
        if request.GET.get('id'):
            pi = TimeMultiplierFactor.objects.get(id=request.GET.get('id'))
            tmf_form = TMFForm(request.POST, instance=pi)
            if tmf_form.is_valid():
                TimeMultiplierFactor.objects.filter(id=request.GET.get('id')).update(
                    price = tmf_form.cleaned_data['price'],
                    hours = tmf_form.cleaned_data['hours'],
                    updated_time = datetime.now(),
                    created_by_id = 1,
                    updated_by_id = 1,
                    is_enabled = tmf_form.cleaned_data['is_enabled']
                )
                return HttpResponseRedirect('/')
            else:
                return render(request, 'tmf.html', {'tmf_form': tmf_form})


################## CRUD on Waiting Charge #############################

class waitingChargeView(TemplateView):
    template_name = 'waiting_charge.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        waiting_charge_form = WaitingChargeForm()
        context = {'waiting_charge_form': waiting_charge_form}
        return context

    def get(self, request):
        if request.GET.get('id'):
            pi = WaitingCharge.objects.get(id=request.GET.get('id'))
            waiting_charge_form = WaitingChargeForm(instance=pi)
            return render(request, 'waiting_charge.html', {'waiting_charge_form': waiting_charge_form})
        waiting_charge_form = WaitingChargeForm()
        return render(request, 'waiting_charge.html', {'waiting_charge_form': waiting_charge_form})

    def post(self, request):
        if request.GET.get('id'):
            WaitingCharge.objects.get(id=request.GET.get('id')).delete()
            return HttpResponseRedirect('/')

        waiting_charge_form = WaitingChargeForm(request.POST)
        print("waiting_charge_form.is_valid()==>", waiting_charge_form.is_valid())
        if waiting_charge_form.is_valid():
            WaitingCharge.objects.create(
                    price = waiting_charge_form.cleaned_data['price'],
                    per_min = waiting_charge_form.cleaned_data['per_min'],
                    updated_time = datetime.now(),
                    created_by_id = 1,
                    updated_by_id = 1,
                    is_enabled = waiting_charge_form.cleaned_data['is_enabled']
                )
            return HttpResponseRedirect('/')
        else:
            return render(request, 'waiting_charge.html', {'waiting_charge_form': waiting_charge_form})
            
class UpdatewaitingChargeView(View):
    def get(self, request):
        pi = WaitingCharge.objects.get(id=request.GET.get('id'))
        waiting_charge_form = WaitingChargeForm(instance=pi)
        return render(request, 'waiting_charge.html', {'waiting_charge_form': waiting_charge_form})

    def post(self, request):
        if request.GET.get('id'):
            pi = WaitingCharge.objects.get(id=request.GET.get('id'))
            waiting_charge_form = WaitingChargeForm(request.POST, instance=pi)
            if waiting_charge_form.is_valid():
                WaitingCharge.objects.filter(id=request.GET.get('id')).update(
                    price = waiting_charge_form.cleaned_data['price'],
                    per_min = waiting_charge_form.cleaned_data['per_min'],
                    updated_time = datetime.now(),
                    created_by_id = 1,
                    updated_by_id = 1,
                    is_enabled = waiting_charge_form.cleaned_data['is_enabled']
                )
                return HttpResponseRedirect('/')
            else:
                return render(request, 'waiting_charge.html', {'waiting_charge_form': waiting_charge_form})


################## API Section ##################################

from rest_framework.response import Response
from rest_framework import viewsets
from django.db.models import Q

class GetPriceView(viewsets.ModelViewSet):
    def create(self, request):
        Dn = request.data['distance_traveled_in_km']
        Tn = request.data['time_taken']
        day = request.data['day']
        wt = request.data['waiting_time']

        dbp_object = DistanceBasePrice.objects.get(Q(day=day))
        dap_first_object = DistanceAdditionalPrice.objects.first()

        dbp_amount = 0
        dap_amount = 0
        hour_amount = 0
        wating_time_amount = 0

        if Dn > dbp_object.km_value:
            extra_travlled = Dn - dbp_object.km_value
            extra_travlled_charge = extra_travlled * dap_first_object.price
            actual_charge = dbp_object.price + extra_travlled_charge
            dbp_amount = actual_charge
        else:
            dbp_amount = dbp_object.price
        dap_last_object = DistanceAdditionalPrice.objects.last()
        if Dn > dap_last_object.km_value:
            extra_km_travelled = Dn - dap_last_object.km_value
            extra_charges = extra_km_travelled * dap_last_object.price
            dap_amount = (dap_last_object.km_value * dap_first_object.price) + extra_charges
        else:
            dap_amount = Dn * dap_first_object.price

        tmf_obj = TimeMultiplierFactor.objects.last()

        if "min" in Tn and 'hour' not in Tn:
            minutes = float(Tn.split()[0])
            hours = minutes / 60
            hour_amount = hours * tmf_obj.price
        elif "hour" in Tn and "min" not in Tn:
            hours = float(Tn.split()[0])
            if hours > 1 and hours <= 2:
                hour_amount = tmf_obj.price * 1.25
            elif hours > 2 and hours <= 3:
                hour_amount = tmf_obj.price * 2.2
            else:
                hour_amount = tmf_obj.price
        else:
            hours, minutes = Tn.split(' hour ')
            hours = float(hours)
            minutes = float(minutes.split(' min')[0])

            total_hours = hours + (minutes / 60)

            if total_hours > 1 and total_hours <= 2:
                hour_amount = tmf_obj.price * 1.25
            elif total_hours > 2 and total_hours <= 3:
                hour_amount = tmf_obj.price * 2.2
            else:
                hour_amount = tmf_obj.price

        wt_obj = WaitingCharge.objects.last()

        wt_minutes = float(wt.split()[0])
        if wt_minutes > wt_obj.per_min:
            per_minute_charge = wt_obj.price / wt_obj.per_min
            waiting_min = wt_minutes - wt_obj.per_min
            wating_time_amount = waiting_min * per_minute_charge
        else:
            wating_time_amount = 0

        Price = dbp_amount + dap_amount + hour_amount + wating_time_amount
        return Response({
            "total_price": Price
        })