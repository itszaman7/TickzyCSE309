from django.urls import path
from ticket_buyer.views import userHome, sellTicket, ticketHistory, myAuctions

app_name = 'tickets'

urlpatterns = [
    # URL pattern for ticket listing
    path('', userHome.as_view(template_name='pages/user/Home.html'), name='ticket_listing'),
    path('ticketSell/', sellTicket.as_view(template_name='pages/user/SellTicket.html'), name='ticket_selling'),
    path('ticketHistory/', ticketHistory.as_view(template_name='pages/user/TicketHistory.html'), name='ticket_History'),
    path('myAuctions/', ticketHistory.as_view(template_name='pages/user/MyAuctions.html'), name='myAuction'),
    path('myInventory/', ticketHistory.as_view(template_name='pages/user/UserInventory.html'), name='UserInventory'),
    
    # Example of another URL pattern for a different page, you can modify or add more as needed
    path('error/', userHome.as_view(template_name='non-exist-file.html'), name='error_page'),
]
