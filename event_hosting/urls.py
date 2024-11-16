from django.urls import path
from event_hosting.views import hostEvent, myEvents, EventEarnings
from ticket_buyer.views import userHome

app_name = 'event_hosting'

urlpatterns = [
    # URL pattern for creating an event
    path('createEvent/', hostEvent.as_view(template_name='pages/event_hoster/createEvent.html'), name='create_event'),
    
    # URL pattern for viewing hosted events
    path('myEvents/', myEvents.as_view(template_name='pages/event_hoster/myEvents.html'), name='my_events'),
    
    # URL pattern for viewing event earnings
    path('eventEarnings/', EventEarnings.as_view(template_name='pages/event_hoster/eventEarning.html'), name='event_earnings'),
    
    # Example of another URL pattern for a different page (error page)
    path('error/', userHome.as_view(template_name='non-exist-file.html'), name='error_page'),
]
