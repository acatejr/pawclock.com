from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import DayCareSession

# Create your views here.
# def index(request):
#     """
#     Render the index page.
#     """
#     return render(request, "index1.html")

class IndexView(ListView):
    """
    Render the index page.
    """
    model = DayCareSession
    template_name = "index.html"

    def get_queryset(self, *args, **kwargs):
        qs = super(IndexView, self).get_queryset(*args, **kwargs)
        qs = DayCareSession.objects.filter(check_out__isnull=True)
        # qs = qs.order_by("-id")
        return qs

    # def get_context_data(self, **kwargs):
    #     context = super(IndexView, self).get_context_data(**kwargs)
    #     #filter_set = DayCareSession.objects.all()

        # filter_set = Gauges.objects.all()
        # if self.request.GET.get('gauge_id'):
        #     gauge_id = self.request.GET.get('gauge_id')
        #     filter_set = filter_set.filter(gauge_id=gauge_id)


# class BookListView(ListView):
#     model = Book

#     def head(self, *args, **kwargs):
#         last_book = self.get_queryset().latest("publication_date")
#         response = HttpResponse(
#             # RFC 1123 date format.
#             headers={
#                 "Last-Modified": last_book.publication_date.strftime(
#                     "%a, %d %b %Y %H:%M:%S GMT"
#                 )
#             },
#         )
#         return response
def about(request):
    """
    Render the about page.
    """
    return render(request, "about.html")

def contact(request):
    """
    Render the contact page.
    """
    return render(request, "contact.html")

def privacy(request):
    """
    Render the privacy policy page.
    """
    return render(request, "privacy.html")
