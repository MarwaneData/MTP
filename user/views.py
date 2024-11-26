from django.shortcuts import render ,get_object_or_404, redirect
from django.core.mail import send_mail
from .models import *
from django.contrib import messages
from django.template.loader import render_to_string
from django.http import HttpResponse

def robots_txt(request):
    lines = [
        "User-agent: *",
        "Disallow: /admin/Controle/Content-inserting-modifications", 
        "Allow: /", 
    ]
    return HttpResponse("\n".join(lines), content_type="text/plain")

def custom_404_view(request, exception):
    tours = Tour.objects.filter(is_active=True)  
    excursions = DayTrip.objects.all()
    contact_info = Contact.objects.first() 
    context = {
        'tours': tours,
        'excursions': excursions,
        'contact_info': contact_info,
        'is_contact_page': True,
        'pop': Pop.objects.first() 
    }
    return render(request, '404.html', context, status=404,)


def contact(request):
    tours = Tour.objects.filter(is_active=True)  
    excursions = DayTrip.objects.all()
    contact_info = Contact.objects.first() 
    context = {
        'tours': tours,
        'excursions': excursions,
        'contact_info': contact_info,
        'is_contact_page': True,
        'pop': Pop.objects.first() 
    }
    return render(request, 'contact.html', context)


def contact_email(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        guests = request.POST.get('guests')
        message = request.POST.get('message')
        subject = f"Contact Form Submission from {name}"
        plain_message = f"Name: {name}\nEmail: {email}\nPhone: {phone}\nGuests: {guests}\nMessage:\n{message}"

        html_message = render_to_string('email_template.html', {
            'name': name,
            'email': email,
            'phone': phone,
            'guests': guests,
            'message': message
        })
        from_email = 'noreplay.mtph@gmail.com'
        to_email = ['moroccotoursphotographer@gmail.com']

        try:
            send_mail(
                subject,
                plain_message,  # Plain text message as a fallback
                from_email,
                to_email,
                html_message=html_message  # HTML message
            )
            messages.success(request, "Your message has been sent successfully! We'll respond as soon as possible. Meanwhile, enjoy exploring our gallery!")
        except Exception as e:
            messages.error(request, f"An error occurred while sending your message: {str(e)}")

        return redirect('gallery')
    else:
        return redirect('gallery')

def contact_email2(request):
    if request.method == 'POST':
        check_in = request.POST.get('check_in')
        check_out = request.POST.get('check_out')
        guests = request.POST.get('guests')
        suite = request.POST.get('suite')
        special_requests = request.POST.get('special_requests')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        subject = f"Camp Reservation Request from"
        plain_message = (
            f"Check-in Date: {check_in}\n"
            f"Check-out Date: {check_out}\n"
            f"Guests: {guests}\n"
            f"Suite: {suite}\n"
            f"Phone: {phone}\n"
            f"Email: {email}\n"
            f"Special Requests:\n{special_requests}"
        )

        html_message = render_to_string('email_template_camp.html', {
            'check_in': check_in,
            'check_out': check_out,
            'guests': guests,
            'suite': suite,
            'phone': phone,
            'email': email,
            'special_requests': special_requests
        })
        from_email = 'noreplay.mtph@gmail.com'
        to_email = ['moroccotoursphotographer@gmail.com']

        try:
            send_mail(
                subject,
                plain_message,
                from_email,
                to_email,
                html_message=html_message
            )
            messages.success(request, "Your message has been sent successfully! We'll respond as soon as possible. Meanwhile, enjoy exploring our gallery!")
        except Exception as e:
            messages.error(request, f"An error occurred while sending your message: {str(e)}")

        return redirect('gallery')
    else:
        return redirect('gallery')

def contact_email_tour(request):
    if request.method == 'POST':
        # Capture form data
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        tour_name = request.POST.get('tour_name')
        message = request.POST.get('message')

        # Compose the email subject and body
        subject = f"Contact Form Submission for Tour: {tour_name}"
        plain_message = (
            f"Name: {name}\n"
            f"Email: {email}\n"
            f"Phone: {phone}\n"
            f"Tour Name: {tour_name}\n"
            f"Message:\n{message}"
        )

        html_message = render_to_string('email_template_tour.html', {
            'name': name,
            'email': email,
            'phone': phone,
            'tour_name': tour_name,
            'message': message
        })
        from_email = 'noreplay.mtph@gmail.com'
        to_email = ['moroccotoursphotographer@gmail.com']

        # Send the email
        try:
            send_mail(
                subject,
                plain_message,
                from_email,
                to_email,
                html_message=html_message
            )
            messages.success(request, "Your message has been sent successfully! We'll respond as soon as possible. Meanwhile, enjoy exploring our gallery!")
        except Exception as e:
            messages.error(request, f"An error occurred while sending your message: {str(e)}")

        return redirect('gallery')
    else:
        return redirect('gallery')

def contact_email_trip(request):
    if request.method == 'POST':
        # Capture form data
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        tour_name = request.POST.get('tour_name')
        message = request.POST.get('message')

        # Compose the email subject and body
        subject = f"Contact Form Submission for Trip: {tour_name}"
        plain_message = (
            f"Name: {name}\n"
            f"Email: {email}\n"
            f"Phone: {phone}\n"
            f"Tour Name: {tour_name}\n"
            f"Message:\n{message}"
        )

        html_message = render_to_string('email_template_trip.html', {
            'name': name,
            'email': email,
            'phone': phone,
            'tour_name': tour_name,
            'message': message
        })
        from_email = 'noreplay.mtph@gmail.com'
        to_email = ['moroccotoursphotographer@gmail.com']

        # Send the email
        try:
            send_mail(
                subject,
                plain_message,
                from_email,
                to_email,
                html_message=html_message
            )
            messages.success(request, "Your message has been sent successfully! We'll respond as soon as possible. Meanwhile, enjoy exploring our gallery!")
        except Exception as e:
            messages.error(request, f"An error occurred while sending your message: {str(e)}")

        return redirect('gallery')
    else:
        return redirect('gallery')


def manual_sitemap(request):
    return render(request, 'sitemap.xml', content_type="application/xml")

def index(request):
    homepage = get_object_or_404(HomePage)
    tours = Tour.objects.filter(is_active=True)  if homepage.show_tours_section else []
    excursions = DayTrip.objects.all() if homepage.show_excursions_section else []
    faqs = FAQ.objects.all()
    contact_info = Contact.objects.first()  # Assuming only one contact info entry
    context = {
        'homepage': homepage,
        'tours': tours,
        'excursions': excursions,
        'contact_info': contact_info,
        'faqs': faqs,
        'pop': Pop.objects.first() 

    }
    return render(request, 'index.html', context)

def MoroccoTour(request):
    morocco_tours_page = get_object_or_404(MoroccoToursPage)
    tours = Tour.objects.filter(is_active=True) if morocco_tours_page.show_tours_section else []
    excursions = DayTrip.objects.all() 
    contact_info = Contact.objects.first()
    context = {
        'morocco_tours_page': morocco_tours_page,
        'tours': tours,
        'excursions': excursions,
        'contact_info': contact_info,
        'pop': Pop.objects.first() 

    }
    return render(request, 'MoroccoTour.html', context)


def DayTrips(request):
    day_trips_page = DayTripsPage.objects.first()
    best_daytrips = DayTrip.objects.filter(is_active=True, is_best=True) 
    daytrips = DayTrip.objects.filter(is_active=True) if day_trips_page.show_all_day_trips_section else []
    tours = Tour.objects.filter(is_active=True) 
    excursions = DayTrip.objects.all() 
    contact_info = Contact.objects.first()
    context = {
        'day_trips_page': day_trips_page,
        'best_daytrips': best_daytrips,
        'daytrips': daytrips,
        'tours': tours,
        'excursions': excursions,
        'contact_info': contact_info,
        'pop': Pop.objects.first() 

    }
    return render(request, 'DayTrips.html', context)

def PhotoGraphy(request):
    photographer_tour_page = PhotographerTourPage.objects.first()
    context = {
        'photographer_tour_page': photographer_tour_page,
        'packages': photographer_tour_page.packages.all(),
        'tours': Tour.objects.filter(is_active=True),
        'excursions': DayTrip.objects.all(),
        'contact_info': Contact.objects.first(),
        'pop': Pop.objects.first() 

    }
    return render(request, 'Photography.html', context)

def DesertCamp(request):
    camps = Camp.objects.all()
    desert_camp_page = DesertCampPage.objects.first()
    tours = Tour.objects.filter(is_active=True) 
    excursions = DayTrip.objects.all() 
    contact_info = Contact.objects.first()
    context = {
        'desert_camp_page': desert_camp_page,
        'camps': camps,
        'tours': tours,
        'excursions': excursions,
        'contact_info': contact_info,
        'pop': Pop.objects.first() 

    }
    return render(request, 'LuxuryDesertCamp.html', context)

def about(request):
    about_page = AboutPage.objects.first()  
    tours = Tour.objects.filter(is_active=True) 
    excursions = DayTrip.objects.all() 
    contact_info = Contact.objects.first()
    context = {
        'about_page': about_page,
        'tours': tours,
        'excursions': excursions,
        'contact_info': contact_info,
        'pop': Pop.objects.first() 
    }
    return render(request, 'about.html', context)

def gallery(request):
    gallery_page = GalleryPage.objects.first()
    tours = Tour.objects.filter(is_active=True) 
    excursions = DayTrip.objects.all() 
    context = {
        'gallery_page': gallery_page,
        'tours': tours,
        'excursions': excursions,
        'contact_info' : Contact.objects.first(),
        'pop': Pop.objects.first() 

    }
    return render(request, 'gallery.html', context)

def Blogs(request):
    blog_page = BlogPage.objects.first()
    blogs = Blog.objects.all()  # Fetch all blogs or use a filter if needed
    contact_info = Contact.objects.first()
    context = {
        'blog_page': blog_page,
        'blogs': blogs,
        'tours': Tour.objects.filter(is_active=True),
        'excursions': DayTrip.objects.all(),
        'contact_info': Contact.objects.first(),
        'pop': Pop.objects.first() 
    }
    return render(request, 'blogs.html', context)
def detailBlog(request, slug):
    blog = get_object_or_404(Blog, slug=slug)    
    related_blogs = Blog.objects.exclude(id=blog.id)[:4]
    blog.view_count= blog.view_count+1
    blog.save()
    context = {
        'blog': blog,
        'related_blogs': related_blogs,
        'tours': Tour.objects.filter(is_active=True),
        'excursions': DayTrip.objects.all(),
        'contact_info': Contact.objects.first(),
        'pop': Pop.objects.first() 
    }
    return render(request, "blog-details.html", context)

def tour(request, tour_slug):
    selected_tour = get_object_or_404(Tour, slug=tour_slug)    
    return render(request, 'tour.html', {'tour': selected_tour,'tours': Tour.objects.filter(is_active=True),
        'excursions': DayTrip.objects.all(),
        'contact_info': Contact.objects.first(), 'pop': Pop.objects.first() })

def daytrip_detail(request, slug):
    daytrip = get_object_or_404(DayTrip, slug=slug)
    return render(request, 'day.html', {'daytrip': daytrip,'tours': Tour.objects.filter(is_active=True),
        'excursions': DayTrip.objects.all(),
        'contact_info': Contact.objects.first(), 'pop': Pop.objects.first() })

def camp_detail(request, slug):
    camp = get_object_or_404(Camp, slug=slug)
    suite_additional_features = camp.suite_additional_features.split(',')
    context = {
        'camp': camp,
        'suite_additional_features': suite_additional_features,
        'tours': Tour.objects.filter(is_active=True),
        'excursions': DayTrip.objects.all(),
        'contact_info': Contact.objects.first(),
        'pop': Pop.objects.first() 
    }
    return render(request, 'camp.html', context)
