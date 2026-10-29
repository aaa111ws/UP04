from rest_framework.views import APIView
from rest_framework.response import Response
from .services import ReportService


class KPIApiView(APIView):
    """GET /api/reports/kpi/?days=30"""

    def get(self, request):
        days = int(request.GET.get("days", 30))
        return Response(ReportService.kpi(days))


class LoansByDayApiView(APIView):
    """GET /api/reports/loans/"""

    def get(self, request):
        days = int(request.GET.get("days", 30))
        return Response(ReportService.loans_by_day(days))


class TopBooksApiView(APIView):
    """GET /api/reports/top-books/"""

    def get(self, request):
        limit = int(request.GET.get("limit", 5))
        return Response(ReportService.top_books(limit))


class LibrarianLoadApiView(APIView):
    """GET /api/reports/librarian-load/"""

    def get(self, request):
        days = int(request.GET.get("days", 30))
        return Response(ReportService.librarian_load(days))


class StockApiView(APIView):
    """GET /api/reports/stock/"""

    def get(self, request):
        return Response(ReportService.stock_status())


class OverdueApiView(APIView):
    """GET /api/reports/overdue/"""

    def get(self, request):
        return Response(ReportService.overdue_list())
