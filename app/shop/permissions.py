from rest_framework import permissions


class ShopAccessPermission(permissions.BasePermission):
    """Allowing/Restricting user to update their profile"""

    def has_permission(self, request, obj):
        try:
            if request.user.is_superuser:
                return True

            if request.user.is_owner and request.method in [
                "GET",
                "PUT",
                "PATCH",
            ]:
                return True
        except:
            return False


class WarehouseAccessPermission(permissions.BasePermission):
    """Allowing/Restricting user to access warehouse"""

    def has_permission(self, request, obj):
        try:
            if request.user.is_owner:
                return True

            if (
                request.user.is_salesman or request.user.is_manager
            ) and request.method in permissions.SAFE_METHODS:
                return True

        except:
            return False


class ProductAccessPermission(permissions.BasePermission):
    """Allowing/Restricting user to access Product"""

    def has_permission(self, request, obj):
        try:
            if request.user.is_owner:
                return True

            if request.user.is_manager and request.method in [
                "POST",
                "GET",
                "PUT",
                "PATCH",
            ]:
                return True

            if request.user.is_salesman and request.method in permissions.SAFE_METHODS:
                return True

        except:
            return False


class CustomerAccessPermission(permissions.BasePermission):
    """Allowing/Restricting user to access Customer"""

    def has_permission(self, request, obj):
        try:
            if request.user.is_owner:
                return True

            if (
                request.user.is_salesman or request.user.is_manager
            ) and request.method in permissions.SAFE_METHODS:
                return True

        except:
            return False


class VendorAccessPermission(permissions.BasePermission):
    """Allowing/Restricting user to access Customer"""

    def has_permission(self, request, obj):
        try:
            if request.user.is_owner:
                return True

            if (
                request.user.is_salesman or request.user.is_manager
            ) and request.method in permissions.SAFE_METHODS:
                return True

        except:
            return False


class CustomerTransactionPermission(permissions.BasePermission):
    """Allowing/Restricting user to access the transactions"""

    def has_permission(self, request, obj):
        try:
            if request.user.is_owner:
                return True

            if (
                request.user.is_manager or request.user.is_salesman
            ) and request.method in ["POST", "GET", "PUT", "PATCH"]:
                return True
        except:
            pass