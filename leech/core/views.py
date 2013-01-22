import logging

from django import http
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView

from .models import Block


logger = logging.getLogger('core')

class BlockList(ListView):
    model = Block

    def get_queryset(self):
        return (Block.objects
                .filter(owner__id=self.request.user.id)
                .order_by('when'))


class BlockUrl(TemplateView):
    template_name = 'core/block-url.html'

    def render_to_response(self, context, **response_kwargs):
        if self.request.GET.get('url'):
            context['next'] = self.request.get_full_path()
            context['url'] = self.request.GET.get('url')
            if self.request.user.is_authenticated():
                Block.objects.create(url=self.request.GET.get('url'),
                                     owner=self.request.user)
        return super(BlockUrl, self).render_to_response(context,
                                                        **response_kwargs)
