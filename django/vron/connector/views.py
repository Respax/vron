"""
Connector Views

These are the views that control the requests received
"""

##########################
# Imports
##########################
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from vron.connector.api.api import Api
import requests






######################
# API Views
#######################
@csrf_exempt
def api( request ):
    """
    Receives and handles a request from VIATOR

    :param: request
    :return: String
    """

    # Reads XML content
    if 'debug' in request.GET:
        response = requests.get( "https://vron-test.respax.com/static/viator_booking_tw.xml" )
        #http://localhost:8000/static/viator_booking_tw.xml
        xml_raw = response.content
    elif request.method == 'POST':
        xml_raw = request.body
    else:
        xml_raw = ''

    # Checks if it's test or live
    if 'config' in request.GET and request.GET['config'] in ['train', 'live']:
        config = request.GET['config']
    else:
        config = 'train'

    # Handles API request
    api = Api( xml_raw, config )

    # Returns XML response
    return HttpResponse( api.process(), content_type = "application/xml" )