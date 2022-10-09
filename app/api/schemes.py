from drf_yasg import openapi

from config import settings


request_body = openapi.Schema(
    type=openapi.TYPE_OBJECT, 
    properties={
        'relative_news': openapi.Schema(description='Role', type=openapi.TYPE_STRING, enum=[role for role in settings.ROLES]),
    }
)

response_ok = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'relative_news': openapi.Schema(
            type=openapi.TYPE_ARRAY, 
            items=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'url': openapi.Schema(description='Url', type=openapi.TYPE_STRING),
                    'date_time': openapi.Schema(description='Date and Time', type=openapi.TYPE_STRING),
                    'category': openapi.Schema(description='Category', type=openapi.TYPE_STRING),
                    'title': openapi.Schema(description='Title', type=openapi.TYPE_STRING),
                    'description': openapi.Schema(description='Description', type=openapi.TYPE_STRING)
                }
            ),
        )
    }
)