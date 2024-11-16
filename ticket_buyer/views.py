from django.views.generic import TemplateView
from django.conf import settings
from _keenthemes.__init__ import KTLayout
from _keenthemes.libs.theme import KTTheme

class userHome(TemplateView):
    # The template for the ticket listing page
    template_name = 'pages/user/Home.html'

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

class sellTicket(TemplateView):
    # The template for the ticket listing page
    template_name = 'pages/user/SellTicket.html'

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
    
class ticketHistory(TemplateView):
    # The template for the ticket listing page
    template_name = 'pages/user/TicketHistory.html'

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
    

class myAuctions(TemplateView):
    # The template for the ticket listing page
    template_name = 'pages/user/MyAuctions.html'

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
    

class myInventory(TemplateView):
    # The template for the ticket listing page
    template_name = 'pages/user/UserInventory.html'

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