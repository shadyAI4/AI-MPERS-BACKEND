import json
from django.http import JsonResponse
from django.views import View
from .views import *
from django.views.decorators.csrf import csrf_exempt



class MessageChannelsView(View):
    def get(self, request):
        # code to process a GET request
        return JsonResponse(data={})

    @csrf_exempt
    def post(self, request):
        try:
            data=json.loads(request.body) 
                  
            # if data['eventName']=='retriveStage':
            #     return JsonResponse(data=RetriveMessageChannels.resolve_approval_stages(data))
                  
            # elif data['eventName']=='resolveFarmerRegistration':
            #     return JsonResponse(data=RetriveMessageChannels.resolve_io_farmer_registration(data))
            
            # elif data['eventName']=='resolveSearchFramer':
            #     return JsonResponse(data=RetriveMessageChannels.resolve_io_farmer_search(data))
            
            # elif data['eventName']=='resolveActivateOrDeactivateFramer':
            #     return JsonResponse(data=RetriveMessageChannels.resolve_activate_or_deactivate(data))
            
            # elif data['eventName']=='genderFarmers':
            #     return JsonResponse(data=RetriveMessageChannels.resolve_farmers_gender(data))
            
            # elif data['eventName']=='resolveSetFarmersPassword':
            #     return JsonResponse(data=RetriveMessageChannels.resolve_send_otp_and_set_password(data))
            
            # elif data['eventName']=='resolveNotification':
            #     return JsonResponse(data=RetriveMessageChannels.resolve_send_notification(data))
            
            # elif data['eventName']=='RequestLocationName':
            #     return JsonResponse(data=RetriveMessageChannels.resolve_location_names(data))
            
            # elif data['eventName']=='RequestUsersDetails':
            #     return JsonResponse(data=RetriveMessageChannels.resolve_request_user_details(data))

        except:
            return JsonResponse(data={})

