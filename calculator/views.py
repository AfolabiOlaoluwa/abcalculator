# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from calculator.models import LastResult
from django.views.decorators.csrf import csrf_exempt
from scipy.stats import norm
from django.core import serializers

# Create your views here.

def main(request):
    return render(request,'index.html')

@csrf_exempt
def calculate(request):
    """
    This methods takes all parameters from the input boxes
    and calculates the p_value and determines if the result is significant
    or not.
    It also craete or update a database to store values and result of a test
    to make sure that on next text,a user can see the result of the former in
    case their is a need for comparison

    """

    visitors_control = float(request.POST['vcontrol'])
    visitors_variant = float(request.POST['vvariant'])
    conversion_variant = float(request.POST['cvariant'])
    conversion_control = float(request.POST['ccontrol'])

    print p_value(visitors_control,conversion_control,visitors_variant,conversion_variant)
    pvalue = p_value(visitors_control,conversion_control,visitors_variant,conversion_variant)
    print pvalue

    final_pvalue = float(pvalue)
    last_result = LastResult(visitors_control=visitors_control,visitors_variant=visitors_variant,conversion_control=conversion_control,conversion_variant=conversion_variant)
    #To check the significance,you compare the p_value with 0.05,if equal to or less,
    #significance is YES else it is a NO NO
    if final_pvalue <=0.05:
        significance = 'Yes'
    else:
        significance = 'No'
    return JsonResponse({'pvalue':final_pvalue,'significance':significance} )




def getLastResult(request):
    """This function is a get method that returns the most recent result from the table
        return type will be in json format
    """
    data = serializers.serialize('json',LastResult.objects.all())
    return HttpResponse(data,content_type='application/json')


def get_standard_err(input_size,success_rate):
    """This function calculates the standard error which takes
    two arguements """

    temp = success_rate/input_size
    value = temp * (1-temp)/input_size **0.5
    return value

def p_value(visit_control,conv_control,visit_var,conv_var):
    import math
    """This function calculates the p_value and tells if the significance
    is a positive or negative.
    significance is generally measured to be true if the p_value is less equal to or less
    than 0.05 """
    mean_visit = visit_control / conv_control
    mean_conv = visit_var/conv_var
    std_err_control = get_standard_err(visit_control,conv_control)
    std_err_var = get_standard_err(visit_var,conv_var)


    x = (mean_conv - mean_visit)
    y = ( std_err_control**2 + std_err_var**2) **0.5
    print x/y
    return norm.sf(abs(x/y))
