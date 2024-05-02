from rest_framework_simplejwt.tokens import AccessToken, RefreshToken

class JWTAuthenticationMiddleware:
    
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        access_token_value = request.COOKIES.get("access_token")
        
        if access_token_value:
            try:
                # Access token 디코딩 후 사용자 데이터를 request에 추가
                access_token = AccessToken(access_token_value)
                user = access_token.payload.get("user_id")
                
                # HTTP_AUTHORIZATION 헤더에 JWT ACCESS 헤더 토큰 추가
                request.META['HTTP_AUTHORIZATION'] = f'Bearer {access_token_value}'
            
            except Exception as e:
                pass
        
        response = self.get_response(request)
        
        return response