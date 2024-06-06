from rest_framework.throttling import UserRateThrottle

class mehedithrottle(UserRateThrottle):
    scope = 'mehedi'