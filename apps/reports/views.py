from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .models import MissingPerson
from .serializers import MissingPersonSerializer
# from .kafka_producer import publish_missing_person_event

from apps.auth import *

class ReportMissingPersonView(APIView):
    # permission_classes = [IsAuthenticated]

    def post(self, request):
        print("||||||||||||||",request.user)  # 🔥🔥🔥 gives current user

        """Add a new record and link it to the logged-in user"""
        # request.data["created_by"] = request.user.id  # 🔥🔥🔥 Auto-assign user

        serializer = MissingPersonSerializer(data=request.data)
        if serializer.is_valid():
            missing_person = serializer.save()

            # Publish event to Kafka
            event_data = {
                "id": missing_person.id,
                "name": missing_person.name,
                "last_seen_location": missing_person.last_seen_location,
                "status": "reported",
                # "user": missing_person.username
            }
            # publish_missing_person_event(event_data) # 🔥🔥🔥.....

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        missing_persons = MissingPerson.objects.all()
        """🔥🔥🔥Display only records added by the logged-in user🔥🔥🔥"""
        # missing_persons = MissingPerson.objects.filter(created_by=request.user)
        serializer = MissingPersonSerializer(missing_persons, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)



















