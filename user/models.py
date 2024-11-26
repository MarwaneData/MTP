from django.db import models
from django.utils.text import slugify
from django.urls import reverse
import os
from django.conf import settings

class Tour(models.Model):
    meta_title = models.CharField(max_length=255, help_text="SEO title for the tour (between 50 to 60 characters)")
    meta_description = models.TextField(help_text="Meta description for SEO (between 150-160 characters)", blank=True, null=True)
    meta_keywords = models.CharField(max_length=255, help_text="Comma-separated keywords for SEO", blank=True, null=True)
    name = models.CharField(max_length=255, help_text="Marketing Tour Title")
    slug = models.SlugField(unique=True, blank=True, help_text="URL-friendly version of the tour title")
    description = models.TextField(help_text="Marketing Tour Description")
    departure_city = models.CharField(max_length=100, help_text="Departure city")
    end_city = models.CharField(max_length=100, help_text="End city")
    prices = models.TextField(help_text="Please each price on a new line.", blank=True, null=True)
    duration_days = models.IntegerField(help_text="Number of days of the tour")
    highlights = models.TextField(help_text="Please each highlight on a new line.")
    included = models.TextField(blank=True, null=True, help_text="Please each included item on a new line.")
    excluded = models.TextField(blank=True, null=True, help_text="Please each excluded item on a new line.")
    small_image = models.ImageField(upload_to='static/tours/', help_text="Small image for the tour(300w x 200H)")
    bigger_image = models.ImageField(upload_to='static/tours/', help_text="Bigger image for the tour(1300x680h)")
    gallery_images = models.ManyToManyField('TourImage', blank=True)
    briefly_points = models.TextField(blank=True, null=True, help_text="Briefly points for nights and locations, each on a new line.")
    is_active = models.BooleanField(default=True, help_text="Mark the tour as active or inactive")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name = "Tour"
        verbose_name_plural = "B- All Tours"
    def __str__(self):
        return self.name
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)  
        super(Tour, self).save(*args, **kwargs)
    def get_meta_keywords_list(self):
        return self.meta_keywords.split(',')
    def get_highlights_list(self):
        return self.highlights.splitlines()
    def get_included_list(self):
        return self.included.splitlines()
    def get_included_list2(self):
        return self.excluded.splitlines()
    def get_prices(self):
        return self.prices.splitlines()
    def get_briefly_points_list(self):
        return self.briefly_points.splitlines() 

class DayDetail(models.Model):
    tour = models.ForeignKey(Tour, related_name="days", on_delete=models.CASCADE)
    day_number = models.IntegerField(help_text="Day order Day(1, 2, 3, etc.)")
    title = models.CharField(max_length=255, help_text="Marketing Title day ")
    description = models.TextField(help_text="Detailed description of the day's activities")
    class Meta:
        verbose_name = "Tour Day"
        verbose_name_plural = "B- Days for Tour"
    def __str__(self):
        return f"Day {self.day_number}: {self.tour}"
    
class TourImage(models.Model):
    image = models.ImageField(upload_to='static/tours/galleries/', help_text="Gallery image")
    alt_text = models.CharField(max_length=255, blank=True, help_text="Alt text image description")
    class Meta:
        verbose_name = "Tour gallery image"
        verbose_name_plural = "B- Gallery for Tour"
    def __str__(self):
        return self.alt_text 
    

class Pop(models.Model):
    pop_title = models.CharField(max_length=255, help_text="Title of the pop")
    image = models.ImageField(upload_to='static/global/', help_text="Image for the pop")
    link = models.CharField(max_length=255, help_text="link")
    description = models.TextField(help_text="brief description")
    is_active = models.BooleanField(default=True, help_text="Mark the pop as active")
    class Meta:
        verbose_name = "POP"
        verbose_name_plural = "Marketing POP"
    def __str__(self):
        return f"Pop {self.pop_title}"

class DayTrip(models.Model):
    meta_title = models.CharField(max_length=255, help_text="SEO title day trip (between 50 to 60 characters)")
    meta_description = models.TextField(help_text="Meta description for SEO (between 150-160 characters)", blank=True, null=True)
    meta_keywords = models.CharField(max_length=255, help_text="Comma-separated keywords for SEO", blank=True, null=True)
    name = models.CharField(max_length=255, help_text="Marketing day trip for user")
    slug = models.SlugField(unique=True, blank=True, help_text="URL-friendly version of the day trip title")
    description = models.TextField(help_text="Marketing day trip description")
    departure_city = models.CharField(max_length=100, help_text="Departure city")
    end_city = models.CharField(max_length=100, help_text="End city")
    prices = models.TextField(help_text="Please each price on a new line.", blank=True, null=True)
    duration_hours = models.IntegerField(help_text="Number of hours for the day trip")
    highlights = models.TextField(help_text="Each highlight on a new line.")
    included = models.TextField(blank=True, null=True, help_text="Each included item on a new line.")
    exluded = models.TextField(blank=True, null=True, help_text="Each included item on a new line.")
    briefly_points = models.TextField(blank=True, null=True, help_text="Briefly points for nights and locations, each on a new line.")
    actions = models.ManyToManyField('ActionDetail', related_name='daytrip_actions', blank=True)
    small_image = models.ImageField(upload_to='static/daytrips/', help_text="Small image for the day trip")
    bigger_image = models.ImageField(upload_to='static/daytrips/', help_text="Bigger image for the day trip")
    gallery_images = models.ManyToManyField('DayTripImage', blank=True)
    is_active = models.BooleanField(default=True, help_text="Mark the day trip as active or inactive")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_best = models.BooleanField(default=True, help_text="Mark the day trip as best")
    class Meta:
        verbose_name = "Day Trip"
        verbose_name_plural = "C- Day Trip"
    def __str__(self):
        return self.name
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(DayTrip, self).save(*args, **kwargs)
    def get_meta_keywords_list(self):
        return self.meta_keywords.split(',')
    def get_included_list(self):
        return self.included.splitlines()
    def get_included_list2(self):
        return self.exluded.splitlines()
    def get_prices(self):
        return self.prices.splitlines()
    def get_included_list(self):
        return self.included.splitlines()
    def get_briefly_points_list(self):
        return self.briefly_points.splitlines() 

class ActionDetail(models.Model):
    day_trip = models.ForeignKey(DayTrip, related_name="action_details", on_delete=models.CASCADE)
    action_number = models.IntegerField(help_text="Action number (1, 2, 3, etc.)")
    title = models.CharField(max_length=255, help_text="Marketing title action")
    description = models.TextField(help_text="Detailed description of the action's activities")
    class Meta:
        verbose_name = "Day trips Actions"
        verbose_name_plural = "C- Day Trip actions"
    def __str__(self):
        return f"Action {self.action_number}: {self.title}"
    
class DayTripImage(models.Model):
    image = models.ImageField(upload_to='static/daytrips/galleries/', help_text="Day trips images galleries")
    alt_text = models.CharField(max_length=255, blank=True, help_text="Alt image")
    class Meta:
        verbose_name = "Day trips gallery"
        verbose_name_plural = "C- Day Trip galleries"
    def __str__(self):
        return self.alt_text
    



class Camp(models.Model):
    meta_title = models.CharField(max_length=255, help_text="SEO Camp Title (between 50 to 60 characters)")
    meta_description = models.TextField(help_text="SEO Meta description (between 150-160 characters)", blank=True, null=True)
    meta_keywords = models.CharField(max_length=255, help_text="SEO Keywords", blank=True, null=True)
    name = models.CharField(max_length=255, help_text="Marketing Camp Title")
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField(help_text="Maeketing Camp description")
    hero_image = models.ImageField(upload_to='static/camps/', help_text="An image for header of the Camp")
    heroDescription = models.CharField(max_length=100, help_text="Location of the camp", default="Amazing desert Morocco Camp Experience")
    feature_1_icon = models.CharField(max_length=50, help_text="FontAwesome icon class for feature 1", default="fas fa-gem")
    feature_1_title = models.CharField(max_length=100, help_text="Title for feature 1")
    feature_1_description = models.TextField(help_text="Description for feature 1", blank=True)
    feature_2_icon = models.CharField(max_length=50, help_text="FontAwesome icon class for feature 2", default="fas fa-compass")
    feature_2_title = models.CharField(max_length=100, help_text="Title for feature 2")
    feature_2_description = models.TextField(help_text="Description for feature 2", blank=True)
    feature_3_icon = models.CharField(max_length=50, help_text="FontAwesome icon class for feature 3", default="fas fa-utensils")
    feature_3_title = models.CharField(max_length=100, help_text="Title for feature 3")
    feature_3_description = models.TextField(help_text="Description for feature 3", blank=True)
    feature_4_icon = models.CharField(max_length=50, help_text="FontAwesome icon class for feature 4", default="fas fa-spa")
    feature_4_title = models.CharField(max_length=100, help_text="Title for feature 4")
    feature_4_description = models.TextField(help_text="Description for feature 4", blank=True)

    suite_name = models.CharField(max_length=100, help_text="Marekting name Suite")
    suite_description = models.TextField(help_text=" Marekting Description Suite")
    suite_image = models.ImageField(upload_to='static/camps/', help_text="Image of the suite")
    suite_guest_capacity = models.CharField(max_length=50, help_text="Guest capacity description (e.g., 'Up to 2 guests')")
    suite_bed_type = models.CharField(max_length=50, help_text="Bed type (e.g., 'King-size bed')")
    suite_bathroom_type = models.CharField(max_length=100, help_text="Bathroom type (e.g., 'Ensuite bathroom with rain shower')")
    suite_additional_features = models.TextField(help_text="Comma-separated additional features (e.g., 'Private plunge pool')", blank=True)
    price = models.IntegerField(help_text="Price", blank=True, null=True)
    old_price = models.IntegerField(help_text="Old Price", blank=True, null=True)
    experience_1_title = models.CharField(max_length=100, help_text="Title for experience 1")
    experience_1_description = models.TextField(help_text="Description for experience 1")
    experience_1_image = models.ImageField(upload_to='static/camps/', help_text="Image for experience 1")
    experience_2_title = models.CharField(max_length=100, help_text="Title for experience 2")
    experience_2_description = models.TextField(help_text="Description for experience 2")
    experience_2_image = models.ImageField(upload_to='static/camps/', help_text="Image for experience 2")
    experience_3_title = models.CharField(max_length=100, help_text="Title for experience 3")
    experience_3_description = models.TextField(help_text="Description for experience 3")
    experience_3_image = models.ImageField(upload_to='static/camps/', help_text="Image for experience 3")
    dining_image = models.ImageField(upload_to='static/camps/', help_text="Background image for the dining section")
    dining_highlight_1 = models.CharField(max_length=100, help_text="First dining highlight")
    dining_highlight_2 = models.CharField(max_length=100, help_text="Second dining highlight")
    dining_highlight_3 = models.CharField(max_length=100, help_text="Third dining highlight")
    dining_highlight_4 = models.CharField(max_length=100, help_text="Fourth dining highlight")
    class Meta:
        verbose_name = "Camp"
        verbose_name_plural = "D- Camp"
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Camp, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
    

class HomePage(models.Model):
    meta_title = models.CharField(max_length=255, help_text="Title of the page (50 up to 60 characters)")
    meta_description = models.TextField(help_text="Description of the page (50 up to 60 characters)")
    meta_keywords = models.TextField(help_text="Keywords")
    hero_title = models.CharField(max_length=255, help_text="Marketing Title for users")
    hero_paragraph = models.TextField(help_text="Marketing small paragraphs for users")
    hero_image = models.ImageField(upload_to='static/pages_images/', help_text='An image for header of the page')
    mobile_hero_image = models.ImageField(upload_to='static/pages_images/', help_text='image For mobile')
    display_hero_button = models.BooleanField(default=True)
    hero_button_text = models.CharField(max_length=50, help_text="Content of your button")
    show_tours_section = models.BooleanField(default=True)
    tours_section_title = models.CharField(max_length=255, help_text="Title for Tour Section")
    show_excursions_section = models.BooleanField(default=True)
    excursions_section_title = models.CharField(max_length=255, help_text="Title for Day Trips Section")
    show_about_section = models.BooleanField(default=True)
    about_title = models.CharField(max_length=255, help_text="Title for about us section, be creative")
    about_paragraph = models.TextField(help_text="Description About us, for each paragraph in new line")
    about_image = models.ImageField(upload_to='static/pages_images/', default='default_about.jpg')
    satisfaction_rate = models.DecimalField(max_digits=5, decimal_places=0, default=100, help_text="Percentage satisfaction rate, e.g., 95.5")
    years_experience = models.PositiveIntegerField(default=0, help_text="Number of years of experience")
    destinations = models.PositiveIntegerField(default=0, help_text="Number of destinations offered")
    happy_travelers = models.PositiveIntegerField(default=0, help_text="Total number of happy travelers")
    show_comfort_section = models.BooleanField(default=True)
    comfort_title = models.CharField(max_length=255, help_text="Why client chouse you title?")
    comfort_paragraph = models.TextField(default="Answer to question using small paragraphs")
    comfort_image = models.ImageField(upload_to='static/pages_images/', default='default_comfort.jpg')
    class Meta:
        verbose_name = "Home page"
        verbose_name_plural = "A- Home Page"
    def __str__(self):
        return self.meta_title
    def get_about_list(self):
        return self.about_paragraph.splitlines()
    
    def get_about2_list(self):
        return self.comfort_paragraph.splitlines()


class StrengthItem(models.Model):
    title = models.CharField(max_length=255, default="Custom Tours")
    background_image = models.ImageField(upload_to='static/morocco_tours/strengths/', default='default_strength.jpg')
    def __str__(self):
        return self.title

class MoroccoToursPage(models.Model):
    meta_title = models.CharField(max_length=255, help_text="Title of the page (50 up to 60 characters)")
    meta_description = models.TextField(help_text="Description of the page (150 up to 160 characters)")
    meta_keywords = models.TextField(help_text="Keywords")
    hero_title = models.CharField(max_length=255, help_text="Marketing Title for users")
    hero_paragraph = models.TextField(help_text="Marketing small paragraphs for users")
    hero_image = models.ImageField(upload_to='static/pages_images/', help_text='An image for header of the page')
    display_hero_button = models.BooleanField(default=True)
    hero_button_text = models.CharField(max_length=50, help_text="Content of your button")
    show_tours_section = models.BooleanField(default=True)
    tours_section_title = models.CharField(max_length=255, default="Private Morocco Desert Tours")
    show_services_section = models.BooleanField(default=True)
    service_title1 = models.CharField(max_length=255, default="Licensed Guides")
    service_image1 = models.ImageField(upload_to='static/pages_images/', default='default_service1.jpg')
    service_title2 = models.CharField(max_length=255, default="Guided Walking Tour")
    service_image2 = models.ImageField(upload_to='static/pages_images/', default='default_service2.jpg')
    service_title3 = models.CharField(max_length=255, default="Flexible Rescheduling")
    service_image3 = models.ImageField(upload_to='static/pages_images/', default='default_service3.jpg')
    show_why_choose_section = models.BooleanField(default=True)
    why_choose_title = models.CharField(max_length=255, default="Why Choose Our Private Tours?")
    why_choose_paragraphs = models.TextField(default="At Discover Morocco Tours, we organize exceptional tours across Morocco.")
    why_choose_image = models.ImageField(upload_to='static/pages_images', default='default_hero.jpg')
    show_strengths_section = models.BooleanField(default=True)
    strengths_title = models.CharField(max_length=255, default="Our Strengths")
    strength_title1 = models.CharField(max_length=255, default="Custom Tours")
    strength_image1 = models.ImageField(upload_to='static/pages_images/', default='default_strength1.jpg')
    strength_title2 = models.CharField(max_length=255, default="Photography Tours")
    strength_image2 = models.ImageField(upload_to='static/pages_images/', default='default_strength2.jpg')
    strength_title3 = models.CharField(max_length=255, default="Licensed Guides")
    strength_image3 = models.ImageField(upload_to='static/pages_images/', default='default_strength3.jpg')
    strength_title4 = models.CharField(max_length=255, default="Satisfaction Guaranteed")
    strength_image4 = models.ImageField(upload_to='static/pages_images/', default='default_strength4.jpg')
    strength_title5 = models.CharField(max_length=255, default="Excellence")
    strength_image5 = models.ImageField(upload_to='static/pages_images/', default='default_strength5.jpg')
    strength_title6 = models.CharField(max_length=255, default="Trusted Experience")
    strength_image6 = models.ImageField(upload_to='static/pages_images/', default='default_strength6.jpg')
    steps_image = models.ImageField(upload_to='static/pages_images/', default='default_hero.jpg')
    show_steps_section = models.BooleanField(default=True)
    steps_title = models.CharField(max_length=255, default="3 Steps To Your Dream Vacation")
    step1_title = models.CharField(max_length=255, default="Step 1: Fill in the form")
    step1_description = models.TextField(default="Submit your details to start your journey with us.")
    step2_title = models.CharField(max_length=255, default="Step 2: Receive Your Customizable Itinerary")
    step2_description = models.TextField(default="We will send you a detailed itinerary.")
    step3_title = models.CharField(max_length=255, default="Step 3: Pack Your Bags")
    step3_description = models.TextField(default="Get ready to explore Morocco!")
    def __str__(self):
        return self.meta_title

    def get_why_choose_paragraphs(self):
        return self.why_choose_paragraphs.splitlines()
    class Meta:
        verbose_name = "Morocco Tours Page"
        verbose_name_plural = "A- Morocco Tours Page"
class DayTripsPage(models.Model):
    meta_title = models.CharField(max_length=255, help_text="Title of the page (50 up to 60 characters)")
    meta_description = models.TextField(help_text="Description of the page (150 up to 160 characters)")
    meta_keywords = models.TextField(help_text="Keywords")
    hero_title = models.CharField(max_length=255, help_text="Marketing Title for users")
    hero_paragraph = models.TextField(help_text="Marketing small paragraphs for users")
    hero_image = models.ImageField(upload_to='static/pages_images/', help_text='An image for header of the page')
    display_hero_button = models.BooleanField(default=True)
    hero_button_text = models.CharField(max_length=50, help_text="Content of your button")
    show_services_section = models.BooleanField(default=True)
    service_title1 = models.CharField(max_length=255, help_text="Licensed Guides")
    service_image1 = models.ImageField(upload_to='static/pages_images/', help_text='Icon')
    service_title2 = models.CharField(max_length=255, help_text="Guided Walking Tour")
    service_image2 = models.ImageField(upload_to='static/pages_images/', help_text='Icon')
    service_title3 = models.CharField(max_length=255, help_text="Flexible Rescheduling")
    service_image3 = models.ImageField(upload_to='static/pages_images/', help_text='Icon')
    show_best_day_trips_section = models.BooleanField(default=True)
    best_day_trips_title = models.CharField(max_length=255, help_text="Title for the best day trip section")
    show_all_day_trips_section = models.BooleanField(default=True)
    all_day_trips_title = models.CharField(max_length=255, help_text="Title All Private Excursions and Day Trips")
    show_blog_section = models.BooleanField(default=True)
    blog_title = models.CharField(max_length=255, help_text="Section Marekting title")
    blog_paragraph = models.TextField(default="Section Marekting title")
    blog_image = models.ImageField(upload_to='static/pages_images/', help_text='Imgae for your section')
    show_unique_experiences_section = models.BooleanField(default=True)
    unique_experiences_title = models.CharField(max_length=255, help_text="Second Section Marekting title")
    unique_experiences_paragraph = models.TextField(help_text="Marketing descriptions for your section")
    unique_experiences_image = models.ImageField(upload_to='static/pages_images/', help_text='image for your section')

    def __str__(self):
        return self.meta_title
    class Meta:
        verbose_name = "Day Trips page"
        verbose_name_plural = "A- Day Trips Page"
class PhotographerTourPage(models.Model):
    meta_title = models.CharField(max_length=255, help_text="Title of the page (50 up to 60 characters)")
    meta_description = models.TextField(help_text="Description of the page (150 up to 160 characters)")
    meta_keywords = models.TextField(help_text="Keywords")
    hero_title = models.CharField(max_length=255, help_text="Marketing Title for users")
    hero_paragraph = models.TextField(help_text="Marketing small paragraphs for users")
    hero_button_text = models.CharField(max_length=255, default="Explore more")
    hero_button_text = models.CharField(max_length=50, help_text="Content of your button")
    hero_image_large = models.ImageField(upload_to='static/pages_images/', help_text='Image for desktop')
    hero_image_medium = models.ImageField(upload_to='static/pages_images/', help_text='Image Medium')
    hero_image_small = models.ImageField(upload_to='static/pages_images/', help_text='Small image')
    package_section_title = models.CharField(max_length=255, help_text="Section Package Photography Title")
    section_title = models.CharField(max_length=255, help_text="Marketing title for section")
    paragraphs = models.TextField(help_text="Marketing Description fpr same section")
    image = models.ImageField(upload_to='static/pages_images/', help_text='image for this section')
    Second_section = models.CharField(null=True,blank=True, max_length=255, help_text="Title of second section")
    section_paragraphs = models.TextField(null=True,blank=True, help_text="Description markting for section")
    image_section = models.ImageField(null=True,blank=True, upload_to='static/pages_images/', help_text='image for this section')
    def __str__(self):
        return self.meta_title

    def get_destination_paragraphs(self):
        return self.paragraphs.splitlines()
    
    def get_destination_paragraphs2(self):
        return self.section_paragraphs.splitlines()
    class Meta:
        verbose_name = "Photography Page"
        verbose_name_plural = "A- Photography page"

class Package(models.Model):
    photographer_tour_page = models.ForeignKey(PhotographerTourPage, related_name='packages', on_delete=models.CASCADE, help_text="Choose photography page")
    title = models.CharField(max_length=100, help_text="Title of the Package")
    old_price = models.PositiveIntegerField(help_text="Old price of the Package") 
    current_price = models.PositiveIntegerField(help_text="Current price of the Package")  
    duration = models.CharField(max_length=50, help_text="Duration of the Package, like 2h")
    retouched_photos = models.PositiveIntegerField()
    color_corrected_photos = models.PositiveIntegerField()
    editing_time = models.CharField(max_length=50)
    def discount_percentage(self):
            return int(round(100 - (self.current_price / self.old_price) * 100, 2))
    def __str__(self):
        return self.title
class DesertCampPage(models.Model):
    meta_title = models.CharField(max_length=255, help_text="Title of the page (50 up to 60 characters)")
    meta_description = models.TextField(help_text="Description of the page (150 up to 160 characters)")
    meta_keywords = models.TextField(help_text="Keywords")
    hero_image = models.ImageField(upload_to='static/pages_images/', default='default_hero.jpg')
    hero_title = models.CharField(max_length=255, help_text="Marketing Title for users")
    hero_paragraph = models.TextField(help_text="Marketing small paragraphs for users")
    hero_button_text = models.CharField(max_length=255, default="Explore more")
    first_section_title = models.CharField(max_length=255, default="Luxury Desert camp")
    first_section_text = models.TextField(default="At Discover Morocco Tours, we specialize in organizing exceptional tours across Morocco.")
    first_section_image = models.ImageField(upload_to='static/pages_images/', default='default_image2.jpg')
    camps_section_title = models.CharField(max_length=255, default="OUR LODGES & TENTS")
    small_info_title = models.CharField(max_length=255, default="Luxury Desert Camp")
    small_info_text = models.TextField(default="At Discover Morocco Tours, we specialize in organizing exceptional tours across Morocco.")
    small_info_image = models.ImageField(upload_to='static/pages_images/', default='default_small_info.jpg')
    second_section_title = models.CharField(max_length=255, default="Luxury Desert camp")
    second_section_text = models.TextField(default="At Discover Morocco Tours, we specialize in organizing exceptional tours across Morocco.")
    second_section_image = models.ImageField(upload_to='static/pages_images/', default='default_image3.jpg')
    def __str__(self):
        return self.meta_title

    def get_first_section_paragraphs(self):
        return self.first_section_text.splitlines()

    def get_small_info_paragraphs(self):
        return self.small_info_text.splitlines()

    def get_second_section_paragraphs(self):
        return self.second_section_text.splitlines()
    class Meta:
        verbose_name = "Camps Page"
        verbose_name_plural = "A- Camps page"
class AboutPage(models.Model):
    meta_title = models.CharField(max_length=255, help_text="Title of the page (50 up to 60 characters)")
    meta_description = models.TextField(help_text="Description of the page (150 up to 160 characters)")
    meta_keywords = models.TextField(help_text="Keywords")
    hero_image = models.ImageField(upload_to='static/pages_images/', default='default_hero.jpg')
    hero_title = models.CharField(max_length=255, help_text="Marketing Title for users")
    hero_paragraph = models.TextField(help_text="Marketing small paragraphs for users")
    video_section_title = models.CharField(max_length=255, default="Explore Morocco Tours")
    video_section_description = models.TextField(default="Embark on a journey through the vibrant landscapes of Morocco...")
    video_url = models.URLField(default="https://www.youtube.com/embed/E2UrxR61CYM")
    first_section_title = models.CharField(max_length=255, default="Your Gateway to Morocco", help_text="Marketing title ")
    first_section_text = models.TextField(help_text="Marketing title")
    first_section_image = models.ImageField(upload_to='static/pages_images/', default='default_first_section.jpg')
    services_title = models.CharField(max_length=255, default="Services We Offer")
    service_title1 = models.CharField(max_length=255, default="Cultural Immersion")
    service_description1 = models.TextField(default="Our cultural tours take you deep into the heart of Morocco's history and traditions.")
    service_image1 = models.ImageField(upload_to='static/pages_images/', default='default_service1.jpg')
    service_title2 = models.CharField(max_length=255, default="Adventure Excursions")
    service_description2 = models.TextField(default="Experience thrilling adventures across Morocco's landscapes.")
    service_image2 = models.ImageField(upload_to='static/pages_images/', default='default_service2.jpg')
    service_title3 = models.CharField(max_length=255, default="Luxury Desert Camps")
    service_description3 = models.TextField(default="Stay in our luxurious desert camps for an unforgettable experience.")
    service_image3 = models.ImageField(upload_to='static/pages_images/', default='default_service3.jpg')
    client_care_title = models.CharField(max_length=255, default="How We Care for Our Clients")
    client_care_text = models.TextField(default="At Morocco Photographer Tours, our clients are at the heart of everything we do.")
    client_care_image = models.ImageField(upload_to='static/pages_images/', default='default_client_care.jpg')
    testimonials_title = models.CharField(max_length=255, default="Hear from Our Travelers")
    testimonial1_content = models.TextField(default="Sometimes I think the surest sign that intelligent life exists...")
    testimonial1_image = models.ImageField(upload_to='static/pages_images', default='default_testimonial1.jpg')
    testimonial1_name = models.CharField(max_length=255, default="Steve")
    testimonial1_source = models.CharField(max_length=255, default="TripAdvisor")
    testimonial2_content = models.TextField(default="Exploring Morocco with this tour was an unforgettable experience...")
    testimonial2_image = models.ImageField(upload_to='static/pages_images', default='default_testimonial2.jpg')
    testimonial2_name = models.CharField(max_length=255, default="Maxime")
    testimonial2_source = models.CharField(max_length=255, default="Instagram")
    testimonial3_content = models.TextField(default="The hospitality and depth of experience offered on this tour made Morocco come alive...")
    testimonial3_image = models.ImageField(upload_to='static/pages_images', default='default_testimonial3.jpg')
    testimonial3_name = models.CharField(max_length=255, default="Stephen")
    testimonial3_source = models.CharField(max_length=255, default="TripAdvisor")
    def __str__(self):
        return self.meta_title

    def get_first_section_text_lines(self):
        return self.first_section_text.splitlines()
    class Meta:
        verbose_name = "About Page"
        verbose_name_plural = "A- About us page"
class GalleryPage(models.Model):
    meta_title = models.CharField(max_length=255, help_text="Title of the page (50 up to 60 characters)")
    meta_description = models.TextField(help_text="Description of the page (150 up to 160 characters)")
    meta_keywords = models.TextField(help_text="Keywords")
    hero_image = models.ImageField(upload_to='static/pages_images/', default='default_hero.jpg')
    hero_title = models.CharField(max_length=255, help_text="Marketing Title for users")
    hero_paragraph = models.TextField(help_text="Marketing small paragraphs for users")
    gallery_section_title = models.CharField(max_length=255, default="Stunning Morocco Tours")
    def __str__(self):
        return self.meta_title
    class Meta:
        verbose_name = "Gallery Page"
        verbose_name_plural = "A- Gallery page"
class GalleryImage(models.Model):
    gallery_page = models.ForeignKey(GalleryPage, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='gallery_images/')
    alt_text = models.CharField(max_length=255, blank=True, null=True)
    def __str__(self):
        return f"Image for {self.gallery_page.meta_title}"

class Blog(models.Model):
    meta_title = models.CharField(max_length=255, help_text="Title of the page (50 up to 60 characters)")
    meta_description = models.TextField(help_text="Description of the page (150 up to 160 characters)")
    meta_keywords = models.TextField(help_text="Keywords")
    blog_title = models.CharField(max_length=255, default="Blog title Marketing")
    blog_description = models.TextField(default="Description of the blog")
    posted_date = models.DateField()
    view_count = models.PositiveIntegerField(default=300)
    author_name = models.CharField(max_length=255, default="By Mohammed")
    hero_image = models.ImageField(upload_to='static/blogs/', default='default_hero.jpg')
    slug = models.SlugField(unique=True, blank=True)
    category = models.CharField(max_length=255, default="Write a category of your blog")
    related_title = models.CharField(max_length=255, default="Related Tour Title marketing")
    related_paragraph = models.TextField(default="Desciption for you related tour marketing")
    button_text = models.CharField(max_length=255, default="Read More")
    button_link = models.URLField(max_length=255, default="Link here like: https://example.com/tour")
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.blog_title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.blog_title

    def get_absolute_url(self):
        return reverse('blog_detail', kwargs={'slug': self.slug})

    @staticmethod
    def get_related_blogs():
        return Blog.objects.order_by('?')[:4]
    
    class Meta:
        verbose_name = "Blog"
        verbose_name_plural = "E- Blog"


class BlogContentBlock(models.Model):
    blog = models.ForeignKey(Blog, related_name='content_blocks', on_delete=models.CASCADE)
    title = models.CharField(max_length=255, blank=True, null=True, help_text="Title of the blog")
    text_content = models.TextField(blank=True, null=True)
    image_content = models.ImageField(upload_to='static/blogs/', blank=True, null=True)
    alt_text = models.CharField(max_length=255, blank=True, null=True)
    def __str__(self):
        return f"{self.blog.blog_title} - Section"
    def formatted_text(self):
        # Splits text by new lines and wraps each line in <p> tags for HTML rendering
        paragraphs = self.text_content.split('\n')
        return ''.join(f'<p>{line}</p>' for line in paragraphs if line.strip())

class BlogPage(models.Model):
    meta_title = models.CharField(max_length=255, help_text="Title of the page (50 up to 60 characters)")
    meta_description = models.TextField(help_text="Description of the page (150 up to 160 characters)")
    meta_keywords = models.TextField(help_text="Keywords")
    hero_image = models.ImageField(upload_to='static/pages_images/', default='default_hero.jpg')
    hero_title = models.CharField(max_length=255, help_text="Marketing Title for users")
    hero_paragraph = models.TextField(blank=True, null=True, help_text="Marketing small paragraphs for users")
    class Meta:
        verbose_name = "Blog page"
        verbose_name_plural = "A- Blogs Page"

    def __str__(self):
        return self.meta_title
    

class Contact(models.Model):
    phone_number = models.CharField(max_length=20, help_text="Enter contact phone number")
    email = models.EmailField(help_text="Enter contact email address")
    location = models.CharField(max_length=255, help_text="Enter physical location or address")
    facebook_url = models.URLField(blank=True, null=True)
    facebook_active = models.BooleanField(default=False)
    instagram_url = models.URLField(blank=True, null=True)
    instagram_active = models.BooleanField(default=False)
    twitter_url = models.URLField(blank=True, null=True)
    twitter_active = models.BooleanField(default=False)
    youtube_url = models.URLField(blank=True, null=True)
    youtube_active = models.BooleanField(default=False)
    whatssap_url = models.URLField(blank=True, null=True)
    whatssap_active = models.BooleanField(default=False)
    wechat_url = models.URLField(blank=True, null=True)
    wechat_url_active = models.BooleanField(default=False)
    def __str__(self):
        return f"Contact info for {self.location or 'Company'}"
    class Meta:
        verbose_name = "Contact info"
        verbose_name_plural = "Z- Contact info"

class FAQ(models.Model):
    question = models.CharField(max_length=255, help_text="The FAQ question.")
    answer_title = models.CharField(max_length=255, help_text="Title of the answer.")
    answer_items = models.TextField(help_text="List items of the answer. Use new lines to separate items.")
    def get_answer_items(self):
        return self.answer_items.strip().split('\n')

    def __str__(self):
        return self.question
class SiteMapEntry(models.Model):
    name = models.CharField(max_length=200, unique=True, default="my Site map")
    content = models.TextField(help_text="Put your site map here:")
    def __str__(self):
        return self.name
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)        
        sitemap_file_path = os.path.join(settings.BASE_DIR, 'templates', 'sitemap.xml')        
        with open(sitemap_file_path, 'w', encoding='utf-8') as sitemap_file:
            sitemap_file.write(self.content)