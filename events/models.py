import uuid
from django.contrib.auth import get_user_model
from django.db import models


# 'event_cover_picture_upload_handler 
def event_cover_picture_upload_handler( instance, filename ):
    return '{0}/{1}/'.format( instance.event_name, filename )

# Event Model 
class Event( models.Model):
    event_name = models.CharField( max_length= 128, blank= False)
    event_tagline = models.CharField( max_length = 128, blank = True)
    event_id = models.UUIDField( default= uuid.uuid4, unique= True, primary_key= True)
    event_host = models.ForeignKey( get_user_model(), related_name = 'events_created', on_delete = models.SET_NULL, null = True)
    event_venue_address = models.CharField( max_length = 256, blank = False )
    event_notes = models.TextField( blank = True )
    event_date = models.DateField(blank = False)
    event_time = models.TimeField( blank = False)
    event_begins_at = models.DateTimeField( blank = False )
    event_cover_picture = models.ImageField( max_length = 255, blank = True,  null =True, upload_to = event_cover_picture_upload_handler)

    class Meta:
        verbose_name = 'Event'
        verbose_name_plural = 'Events'


    def __str__(self):
        return self.event_name

# Model for Event specifics, connects to main event model via a 1-1 relationship 
class EventSpecifics( models.Model):
    event = models.OneToOneField( Event, related_name = 'specifics',  on_delete = models.CASCADE )
    start_booking_date = models.DateTimeField( auto_now_add = True, blank = False)
    seats_start_at = models.PositiveIntegerField( default = 0, )
    allocate_seats = models.BooleanField( default = True)
    end_booking_date = models.DateTimeField( blank = False)
    no_of_reserved_space = models.PositiveIntegerField( default = 0,  )
    no_of_rows = models.PositiveIntegerField( default = 0, null = True)
    no_of_cols = models.PositiveIntegerField( default = 0, null = True)
    padding = models.PositiveIntegerField( default = 0,null = True)
    space_count = models.PositiveIntegerField( blank = False )
    use_email_authentication = models.BooleanField( default = True)
    info_collection_type = models.CharField( max_length = 48, default = 'basic',  choices = (
        ('basic', 'Basic Profile'),
        ('full','Full Profile'),
    ))
    allocation_mode = models.CharField( max_length = 48, default = 'fcfs', choices = (
        ( 'fcfs', 'First Come First Serve'),
        ( 'btf', 'Back To Front'),
        ('ra', 'Random Allocation'),
    ))
    identifier_type = models.CharField( max_length = 25, default = 'al', choices = (
        ('al', 'alphanumeric'),
        ( 'nu', 'numeric'),
    ))

    class Meta:
        verbose_name = "Event Info" 
        verbose_name_plural = "Event Info"

    def __str__(self):
        return 'Specifics For ' + self.event.event_name

    


