from django.conf import settings
from django.utils.decorators import method_decorator

from rest_framework.views import APIView
from rest_framework.response import Response

from django_ratelimit.decorators import ratelimit

# Create your views here.


@method_decorator(ratelimit(group="api", key="ip", rate="3/s"), name="get")
class EndpointsView(APIView):
    """
    Endpoint: /
    """

    def get(self, request):
        """
        Handle GET request.
        """

        return Response(
            {
                "type": "api-details",
                "id": "1",
                "attributes": {
                    "endpoints": [
                        "/v2",
                        "/v2/images",
                        "/v2/images/:id",
                        "/v2/images/:id/like",
                        "/v2/images/:id/save",
                        "/v2/images/:id/artist",
                        "/v2/images/:id/liked-by",
                        "/v2/images/:id/categories",
                        "/v2/images/:id/characters",
                        "/v2/images/:id/relationships/artist",
                        "/v2/images/:id/relationships/liked-by",
                        "/v2/images/:id/relationships/categories",
                        "/v2/images/:id/relationships/characters",
                        "/v2/artists",
                        "/v2/artists/:id",
                        "/v2/artists/:id/images",
                        "/v2/artists/:id/follow",
                        "/v2/artists/:id/followers",
                        "/v2/artists/:id/relationships/images",
                        "/v2/artists/:id/relationships/followers",
                        "/v2/categories",
                        "/v2/categories/:id",
                        "/v2/categories/:id/images",
                        "/v2/categories/:id/follow",
                        "/v2/categories/:id/followers",
                        "/v2/categories/:id/relationships/images",
                        "/v2/categories/:id/relationships/followers",
                        "/v2/characters",
                        "/v2/characters/:id",
                        "/v2/characters/:id/images",
                        "/v2/characters/:id/follow",
                        "/v2/characters/:id/followers",
                        "/v2/characters/:id/relationships/images",
                        "/v2/characters/:id/relationships/followers",
                        "/v2/lists",
                        "/v2/lists/:id",
                        "/v2/lists/:id/user",
                        "/v2/lists/:id/images",
                        "/v2/lists/:id/followers",
                        "/v2/lists/:id/relationships/user",
                        "/v2/lists/:id/relationships/images",
                        "/v2/lists/:id/relationships/followers",
                        "/v2/users",
                        "/v2/users/@me",
                        "/v2/users/:id",
                        "/v2/users/:id/follow",
                        "/v2/users/:id/discord",
                        "/v2/users/:id/followers",
                        "/v2/users/:id/following",
                        "/v2/users/:id/liked-images",
                        "/v2/users/:id/saved-images",
                        "/v2/users/:id/followed-artists",
                        "/v2/users/:id/followed-characters",
                        "/v2/users/:id/followed-categories",
                        "/v2/users/:id/relationships/discord",
                        "/v2/users/:id/relationships/followers",
                        "/v2/users/:id/relationships/following",
                        "/v2/users/:id/relationships/liked-images",
                        "/v2/users/:id/relationships/saved-images",
                        "/v2/users/:id/relationships/followed-artists",
                        "/v2/users/:id/relationships/followed-characters",
                        "/v2/users/:id/relationships/followed-categories",
                        "/v2/auth/token",
                        "/v2/auth/token/revoke",
                    ],
                    "apiVersion": settings.API_VERSION,
                },
            }
        )
