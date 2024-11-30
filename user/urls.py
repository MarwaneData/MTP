from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('about-us', views.about, name='about'),
    path('private-morocco-tours', views.MoroccoTour, name='morocco-tours'),
    path('day-trips', views.DayTrips, name='day-trips'),
    path('morocco-photographer-tours', views.PhotoGraphy, name='PhotoGrapher-tours'),
    path('morocco-luxury-desert-camp', views.DesertCamp, name='DesertCamp'),
    path('morocco-tours-trips-gallery', views.gallery, name='gallery'),
    path('morocco-photographer-blogs', views.Blogs, name='blogs'),
    path('morocco-photographer-blogs/<slug:slug>', views.detailBlog, name='detailBlog'),
    path('tour/<slug:tour_slug>', views.tour, name='tour-detail'),
    path('daytrip/<slug:slug>', views.daytrip_detail, name='daytrip-detail'),
    path('morocco-luxury-desert-camp/<slug:slug>', views.camp_detail, name='camp-detail'),
    path('contact', views.contact, name='contact'),
    path('contact_email', views.contact_email, name='contact_email'),
    path('contact_email2', views.contact_email2, name='contact_email2'),
    path('contact_email3', views.contact_email_tour, name='contact_email_tour'),
    path('contact_email4', views.contact_email_trip, name='contact_email_trip'),
    path('sitemap.xml', views.manual_sitemap, name='manual_sitemap'),
    path("robots.txt", views.robots_txt, name="robots_txt"),
]