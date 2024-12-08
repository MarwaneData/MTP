from django.contrib import admin
from .models import *
from .models import MoroccoToursPage

class TourAdmin(admin.ModelAdmin):
    list_display = ('name', 'prices', 'departure_city', 'duration_days', 'created_at', 'updated_at')
    search_fields = ('name', 'departure_city', 'end_city')
    list_filter = ('updated_at', 'created_at')
    prepopulated_fields = {'slug': ('name',)}
class DayDetailAdmin(admin.ModelAdmin):
    list_display = ('tour', 'day_number', 'title')
class TourImageAdmin(admin.ModelAdmin):
    list_display = ('image', 'alt_text')
class DayTripAdmin(admin.ModelAdmin):
    list_display = ('name','departure_city', 'duration_hours', 'is_active', 'created_at', 'updated_at')
    search_fields = ('name', 'departure_city', 'end_city')
    list_filter = ('updated_at', 'created_at')
    prepopulated_fields = {'slug': ('name',)}
class ActionDetailAdmin(admin.ModelAdmin):
    list_display = ('day_trip', 'action_number', 'title')
class DayTripImageAdmin(admin.ModelAdmin):
    list_display = ('image', 'alt_text')
admin.site.register(Tour, TourAdmin)
admin.site.register(Pop)
admin.site.register(DayDetail, DayDetailAdmin)
admin.site.register(TourImage, TourImageAdmin)
admin.site.register(DayTrip, DayTripAdmin)
admin.site.register(ActionDetail, ActionDetailAdmin)
admin.site.register(DayTripImage, DayTripImageAdmin)
admin.site.site_header = 'Morocco Tours Photographers'                    # default: "Django Administration"
admin.site.index_title = 'Controling your tours, daytrips, and more'                 # default: "Site administration"
admin.site.site_title = 'Administrations'
class CampAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name', 'heroDescription', 'meta_title')
    search_fields = ('name', 'location')

admin.site.register(Camp, CampAdmin)
@admin.register(HomePage)
class HomePageAdmin(admin.ModelAdmin):
    list_display = (
        'meta_title', 
        'show_tours_section', 
        'show_excursions_section', 
        'satisfaction_rate', 
        'years_experience', 
        'destinations', 
        'happy_travelers'
    )
    fieldsets = (
        ('SEO', {
            'fields': ('meta_title', 'meta_description', 'meta_keywords')
        }),
        ('Hero Section', {
            'fields': ('hero_title', 'hero_paragraph', 'hero_image','mobile_hero_image', 'display_hero_button', 'hero_button_text')
        }),
        ('Tours Section', {
            'fields': ('show_tours_section', 'tours_section_title')
        }),
        ('Excursions Section', {
            'fields': ('show_excursions_section', 'excursions_section_title')
        }),
        ('About Section', {
            'fields': ('show_about_section', 'about_title', 'about_paragraph', 'about_image')
        }),
        ('Comfort Section', {
            'fields': ('show_comfort_section', 'comfort_title', 'comfort_paragraph', 'comfort_image')
        }),
        ('Statistics Section', {
            'fields': ('satisfaction_rate', 'years_experience', 'destinations', 'happy_travelers'),
            'description': 'Enter values for customer satisfaction, experience years, destinations, and happy travelers statistics.'
        }),
    )


@admin.register(MoroccoToursPage)
class MoroccoToursPageAdmin(admin.ModelAdmin):
    list_display = ('meta_title', 'hero_title', 'tours_section_title')
    
    fieldsets = (
        ('SEO Settings', {
            'fields': ('meta_title', 'meta_description', 'meta_keywords')
        }),
        ('Hero Section', {
            'fields': ('hero_title', 'hero_paragraph', 'hero_image', 'display_hero_button', 'hero_button_text')
        }),
        ('Tours Section', {
            'fields': ('show_tours_section', 'tours_section_title')
        }),
        ('Services Section', {
            'fields': (
                'show_services_section',
                'service_title1', 'service_image1', 
                'service_title2', 'service_image2', 
                'service_title3', 'service_image3', 
            )
        }),
        ('Why Choose Us Section', {
            'fields': ('show_why_choose_section', 'why_choose_title', 'why_choose_paragraphs', 'why_choose_image')
        }),
        ('Our Strengths Section', {
            'fields': (
                'show_strengths_section', 'strengths_title',
                'strength_title1', 'strength_image1',
                'strength_title2', 'strength_image2',
                'strength_title3', 'strength_image3',
                'strength_title4', 'strength_image4',
                'strength_title5', 'strength_image5',
                'strength_title6', 'strength_image6'
            )
        }),
        ('Steps Section', {
            'fields': (
                'show_steps_section', 'steps_title',
                'step1_title', 'step1_description',
                'step2_title', 'step2_description',
                'step3_title', 'step3_description',
                'steps_image',
            )
        }),
    )

@admin.register(DayTripsPage)
class DayTripsPageAdmin(admin.ModelAdmin):
    list_display = ('meta_title', 'hero_title', 'best_day_trips_title', 'all_day_trips_title')
    
    fieldsets = (
        ('SEO Settings', {
            'fields': ('meta_title', 'meta_description', 'meta_keywords')
        }),
        ('Hero Section', {
            'fields': ('hero_title', 'hero_paragraph', 'hero_image', 'display_hero_button', 'hero_button_text')
        }),
        ('Services Section', {
            'fields': (
                'show_services_section',
                'service_title1', 'service_image1', 
                'service_title2', 'service_image2', 
                'service_title3', 'service_image3'
            )
        }),
        ('Best Day Trips Section', {
            'fields': ('show_best_day_trips_section', 'best_day_trips_title')
        }),
        ('All Day Trips Section', {
            'fields': ('show_all_day_trips_section', 'all_day_trips_title')
        }),
        ('Blog Section', {
            'fields': ('show_blog_section', 'blog_title', 'blog_paragraph', 'blog_image')
        }),
        ('Unique Experiences Section', {
            'fields': ('show_unique_experiences_section', 'unique_experiences_title', 'unique_experiences_paragraph', 'unique_experiences_image')
        }),
    )


class PackageInline(admin.StackedInline):
    model = Package
    extra = 1
    fieldsets = (
        (None, {
            'fields': (
                'title',
                'old_price',
                'current_price',
                'duration',
                'retouched_photos',
                'color_corrected_photos',
                'editing_time',
            ),
        }),
        ('Calculated Fields', {
            'fields': ('discount_percentage',),
            'classes': ('collapse',),
        }),
    )
    readonly_fields = ('discount_percentage',)

    def discount_percentage(self, obj):
        # Return the discount percentage as a read-only field
        return obj.discount_percentage if obj else 'N/A'
    discount_percentage.short_description = 'Discount %'

@admin.register(PhotographerTourPage)
class PhotographerTourPageAdmin(admin.ModelAdmin):
    list_display = ('meta_title', 'hero_title')
    inlines = [PackageInline]
    fieldsets = (
        ('SEO', {
            'fields': ('meta_title', 'meta_description', 'meta_keywords')
        }),
        ('Hero Section', {
            'fields': ('hero_title', 'hero_paragraph', 'hero_image_large', 'hero_image_medium', 'hero_image_small')
        }),
        ('Content Section', {
            'fields': ('section_title', 'paragraphs', 'image', 'Second_section', 'section_paragraphs', 'image_section')
        }),
        ('Package Section', {
            'fields': ('package_section_title',)
        }),
        
    )



@admin.register(DesertCampPage)
class DesertCampPageAdmin(admin.ModelAdmin):
    fieldsets = (
        ('SEO', {
            'fields': ('meta_title', 'meta_description', 'meta_keywords')
        }),
        ('Hero Section', {
            'fields': ('hero_title', 'hero_paragraph', 'hero_image')
        }),
        ('First Text/Image Section', {
            'fields': ('first_section_title', 'first_section_text', 'first_section_image')
        }),
        ('Camps Section', {
            'fields': ('camps_section_title',)  # Only the title, no relation to camps
        }),
        ('Small Info Section', {
            'fields': ('small_info_title', 'small_info_text', 'small_info_image')
        }),
        ('Second Text/Image Section', {
            'fields': ('second_section_title', 'second_section_text', 'second_section_image')
        }),
    )


@admin.register(AboutPage)
class AboutPageAdmin(admin.ModelAdmin):
    fieldsets = (
        ('SEO Information', {
            'fields': ('meta_title', 'meta_description', 'meta_keywords')
        }),
        ('Hero Section', {
            'fields': ('hero_title', 'hero_paragraph', 'hero_image')
        }),
        ('Video Section', {
            'fields': ('video_section_title', 'video_section_description', 'video_url')
        }),
        ('First Section', {
            'fields': ('first_section_title', 'first_section_text', 'first_section_image')
        }),
        ('Services Section', {
            'fields': (
                'services_title', 
                'service_title1', 'service_description1', 'service_image1',
                'service_title2', 'service_description2', 'service_image2',
                'service_title3', 'service_description3', 'service_image3',
            )
        }),
        ('Client Care Section', {
            'fields': ('client_care_title', 'client_care_text', 'client_care_image')
        }),
        ('Testimonials Section', {
            'fields': (
                'testimonials_title',
                'testimonial1_content', 'testimonial1_image', 'testimonial1_name', 'testimonial1_source',
                'testimonial2_content', 'testimonial2_image', 'testimonial2_name', 'testimonial2_source',
                'testimonial3_content', 'testimonial3_image', 'testimonial3_name', 'testimonial3_source',
            )
        }),
    )

class GalleryImageInline(admin.TabularInline):
    model = GalleryImage
    extra = 1

@admin.register(GalleryPage)
class GalleryPageAdmin(admin.ModelAdmin):
    list_display = ('meta_title', 'gallery_section_title')
    fieldsets = (
        ('SEO', {
            'fields': ('meta_title', 'meta_description', 'meta_keywords')
        }),
        ('Hero Section', {
            'fields': ('hero_title', 'hero_paragraph', 'hero_image')
        }),
        ('Gallery Section', {
            'fields': ('gallery_section_title',)
        }),
    )
    inlines = [GalleryImageInline]
class BlogContentBlockInline(admin.StackedInline):
    model = BlogContentBlock
    extra = 1  
    fields = ('title', 'text_content', 'image_content', 'alt_text')  


class BlogAdmin(admin.ModelAdmin):
    list_display = ('blog_title', 'posted_date', 'view_count', 'author_name', 'category')
    search_fields = ('blog_title', 'meta_title', 'meta_description', 'author_name')
    prepopulated_fields = {"slug": ("blog_title",)}

    fieldsets = (
        (None, {
            'fields': ('meta_title', 'meta_description', 'meta_keywords', 'blog_title', 'posted_date', 'view_count', 'author_name', 'hero_image','small_image','slug', 'category')
        }),
        ('Related Content', {
            'fields': ('related_title', 'related_paragraph', 'button_text', 'button_link')
        }),
    )
    inlines = [BlogContentBlockInline]
admin.site.register(Blog, BlogAdmin)

@admin.register(BlogPage)
class BlogPageAdmin(admin.ModelAdmin):
    list_display = ('meta_title',)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('phone_number', 'email', 'location')


class FAQAdmin(admin.ModelAdmin):
    list_display = ('question', 'answer_title')
    search_fields = ('question', 'answer_title')
    list_per_page = 20

admin.site.register(FAQ, FAQAdmin)



class SiteMapEntryAdmin(admin.ModelAdmin):
    list_display = ('name',)  
    fields = ('name', 'content')  
    search_fields = ('name',) 

admin.site.register(SiteMapEntry, SiteMapEntryAdmin)
