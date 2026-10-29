from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    # Админка Django (HTML только здесь, но это готовое)
    path("admin/", admin.site.urls),

    # === МОДУЛЬ 1: АВТОРИЗАЦИЯ ===
    path("api/auth/", include("apps.accounts.urls")),

    # === МОДУЛЬ 2: КНИЖНЫЙ ФОНД ===
    path("api/", include("apps.catalog.urls")),

    # === МОДУЛЬ 3: ЧИТАТЕЛИ ===
    path("api/readers/", include("apps.readers.urls")),

    # === МОДУЛЬ 4: ВЫДАЧИ ===
    path("api/loans/", include("apps.loans.urls")),

    # === МОДУЛЬ 5: ОТЧЁТЫ ===
    path("api/reports/", include("apps.reports.urls")),

    # DRF-вход через браузер (для тестирования)
    path("api/drf-login/", include("rest_framework.urls")),
]

admin.site.site_header = "Библиотека — система учёта книг"
admin.site.site_title = "Библиотека"
admin.site.index_title = "Управление фондом, читателями и выдачами"
