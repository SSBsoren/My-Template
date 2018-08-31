from django.views.generic import TemplateView


class MainPageView(TemplateView):
    template_name='index.html'
    # """docstring for MainPage View."""
    # def __init__(self, arg):
    #     super(MainPage View, self).__init__()
    #     self.arg = arg
class aboutPageView(TemplateView):
    template_name='about.html'
    # """docstring for aboutPageView."""
    # def __init__(self, arg):
    #     super(aboutPageView, self).__init__()
    #     self.arg = arg
    #
class ContactPageView(TemplateView):
    template_name='contact.html'
    # """docstring for ContactPageView."""
    # def __init__(self, arg):
    #     super(ContactPageView, self).__init__()
    #     self.arg = arg
