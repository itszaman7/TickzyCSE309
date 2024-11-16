from django.views.generic import TemplateView
from django.conf import settings
from _keenthemes.__init__ import KTLayout
from _keenthemes.libs.theme import KTTheme

class hostEvent(TemplateView):
    # The template for the ticket listing page
    template_name = 'pages/event_hoster/createEvent.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)

        # Initialize the global layout. This is defined in _keenthemes/__init__.py file
        context = KTLayout.init(context)

        # Include vendors and JavaScript files needed for the ticket listing page widgets
        KTTheme.addVendors(['amcharts', 'amcharts-maps', 'amcharts-stock'])

        # Example of adding some custom context data like a list of tickets
        # You can replace this with real data fetched from the database
        tickets = [
            {
                'title': 'Concert Ticket',
                'image_url': 'assets/media/stock/600x600/img-65.jpg',
                'price': 150,
                'date': 'Dec 20, 2024',
                'status': 'Available',
                'seller': 'Jane Doe',
                'description': 'VIP concert ticket with backstage pass.'
            },
            {
                'title': 'Football Match Ticket',
                'image_url': 'assets/media/stock/600x600/img-66.jpg',
                'price': 120,
                'date': 'Jan 15, 2025',
                'status': 'Sold Out',
                'seller': 'John Smith',
                'description': 'Ticket for the upcoming football match at the stadium.'
            }
        ]
        context['tickets'] = tickets

        # Optionally, you can also pass other context data like filters, categories, etc.
        context['filters'] = {
            'price_range': (50, 200),
            'categories': ['Music', 'Sports', 'Theater']
        }

        return context
    
class myEvents(TemplateView):
    # The template for displaying a list of events
    template_name = 'pages/event_hoster/myEvents.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)

        # Initialize the global layout
        context = KTLayout.init(context)

        # Include necessary JS and vendor files
        KTTheme.addVendors(['amcharts', 'amcharts-maps', 'amcharts-stock'])

        # Example event data, this should be replaced with actual database data
        events = [
            {
                'title': 'Christmas Charity Event',
                'image_url': 'assets/media/stock/600x600/img-55.jpg',
                'date': 'Dec 25, 2024',
                'location': 'City Center',
                'status': 'Upcoming',
                'ticket_count': 200,
                'earned': 12000,
                'host': 'John Doe'
            },
            {
                'title': 'Tech Conference 2025',
                'image_url': 'assets/media/stock/600x600/img-56.jpg',
                'date': 'Feb 10, 2025',
                'location': 'Convention Center',
                'status': 'Upcoming',
                'ticket_count': 500,
                'earned': 25000,
                'host': 'Jane Smith'
            }
        ]
        context['events'] = events

        # Optionally, you can pass other context data like filters or search terms
        context['filters'] = {
            'event_status': ['Upcoming', 'Completed'],
            'categories': ['Music', 'Technology', 'Charity']
        }

        return context


class EventEarnings(TemplateView):
    # The template for displaying event earnings
    template_name = 'pages/event_hoster/eventEarning.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)

        # Initialize the global layout
        context = KTLayout.init(context)

        # Include necessary JS and vendor files
        KTTheme.addVendors(['amcharts', 'amcharts-maps', 'amcharts-stock'])

        # Example earnings data, this should be replaced with actual database data
        event_earnings = [
            {
                'event': 'Christmas Charity Event',
                'tickets_sold': 150,
                'revenue': 12000,
                'date': 'Dec 25, 2024',
                'location': 'City Center',
                'status': 'Upcoming'
            },
            {
                'event': 'Tech Conference 2025',
                'tickets_sold': 450,
                'revenue': 22500,
                'date': 'Feb 10, 2025',
                'location': 'Convention Center',
                'status': 'Upcoming'
            }
        ]
        context['event_earnings'] = event_earnings

        # Optionally, you can pass other context data like filters or categories
        context['filters'] = {
            'status': ['Upcoming', 'Completed'],
            'date_range': ('2024-01-01', '2025-12-31')
        }

        return context
