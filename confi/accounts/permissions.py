from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsAdminRole(BasePermission):
    """دسترسی کامل فقط برای مدیر مدرسه"""
    def has_permission(self, request, view):
        return bool(
            request.user and 
            request.user.is_authenticated and 
            request.user.role == 'admin'
        )

class IsAdminOrDeputyReadOnly(BasePermission):
    """مدیر دسترسی کامل دارد، اما معاون فقط دسترسی خواندن (GET) دارد"""
    def has_permission(self, request, view):
        if not (request.user and request.user.is_authenticated):
            return False
        
        # مدیر همه‌کاره است
        if request.user.role == 'admin':
            return True
            
        # معاون فقط می‌تواند لیست‌ها را ببیند (متدهای امن مثل GET)
        if request.user.role == 'deputy' and request.method in SAFE_METHODS:
            return True
            
        return False

class IsAdminOrDeputy(BasePermission):
    """مدیر و معاون هر دو دسترسی کامل دارند (برای ثبت غیبت و انضباط)"""
    def has_permission(self, request, view):
        return bool(
            request.user and 
            request.user.is_authenticated and 
            request.user.role in ['admin', 'deputy']
        )