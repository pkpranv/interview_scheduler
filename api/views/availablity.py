from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from rest_framework.permissions import  IsAuthenticated

from ..base_response import HttpErrorResponse,HttpSuccessResponse
from ..permissions import IsHRUser,IsNonHRUser
from ..error_codes import get_error_code
from ..models import Availablity
from ..utils import get_available_slots
from ..serializers.update_availablity_serializer import UpdateAvailablitySerializer




class UpdateAvailablity(CreateAPIView):
    serializer_class = UpdateAvailablitySerializer
    permission_classes = (IsAuthenticated,IsNonHRUser )

    def post(self, request, **kwargs):
        serializer = self.get_serializer(data=request.data, context={'user': request.user})
        if serializer.is_valid():
            serializer.save()
            return HttpSuccessResponse({}, "Updated availablity successefully")
        kwargs_errors = {'error_code': get_error_code(
            serializer.errors.values())}
        return HttpErrorResponse(serializer.errors, **kwargs_errors)

class GetAvailablity(APIView):
    permission_classes = (IsAuthenticated,IsHRUser)

    def get(self, request):
        interviewer_id = request.GET.get('interviewer')
        candidate_id = request.GET.get('candidate')
        date_required = request.GET.get('date')
        interviewer_availablity = Availablity.objects.filter(user_id=interviewer_id,available_date=date_required)
        candidate_availablity = Availablity.objects.filter(user_id=candidate_id, available_date=date_required)
        interviewer_available_slot = get_available_slots(interviewer_availablity)
        candidate_availablity_slot= get_available_slots(candidate_availablity)
        response = { 'slots': interviewer_available_slot.intersection(candidate_availablity_slot)}
        return HttpSuccessResponse(response, "Available time slots are")