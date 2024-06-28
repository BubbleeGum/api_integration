from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import NewsSerializer
import requests

class NewsAPIView(APIView):
    def get(self, request, channel):
        api_url = f'https://nodejs-rss-feed-berita-indonesia-api.vercel.app/api/{channel}'
        
        try:
            response = requests.get(api_url)
            if response.status_code == 200:
                response = response.json()
                data = {
                    'status':'success',
                    'message':'Data Berhasil Diperoleh',
                    'meta':{
                        'title': response['data']['title'],
                        'description': response['data']['description'],
                        'link': response['data']['link'],
                    },
                    'data': NewsSerializer(response['data']['item'], many=True).data,
                }
                return Response(data, status=status.HTTP_200_OK)
            else:
                return Response({'message': 'not found'}, status=status.HTTP_404_NOT_FOUND)       
        
        except requests.exceptions.HTTPError as e:
            return Response({'error':e})

        
        
        

