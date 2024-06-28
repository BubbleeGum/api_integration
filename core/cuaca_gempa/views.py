from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status 
import requests
from .serializers import CuacaGempaSerializer

class CuacaGempaAPIView(APIView):
    def get(self, request):
        api_url = 'https://cuaca-gempa-rest-api.vercel.app/weather/jawa-barat/bandung'
        
        try:
            response = requests.get(api_url)
            if response.status_code == 200:
                response = response.json()
                data = {
                    'status':'success',
                    'message':'Data Berhasil Diperoleh',
                    'meta':{
                        'id': response['data']['id'],
                        'latitude': response['data']['latitude'],
                        'longitude': response['data']['longitude'],
                        'coordinate': response['data']['coordinate'],
                        'type': response['data']['type'],
                        'region': response['data']['region'],
                        'level': response['data']['level'],
                        'description': response['data']['description'],
                        'domain': response['data']['domain'],
                        'tags': response['data']['tags'],
                    },
                    'data': CuacaGempaSerializer(response['data']['params'], many=True).data, 
                }
                return Response(data, status=status.HTTP_200_OK)
            else:
                return Response({'message': 'not found'}, status=status.HTTP_404_NOT_FOUND)
            
        except requests.exceptions.HTTPError as e:
            return Response({'error':e})


