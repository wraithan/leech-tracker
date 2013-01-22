from django.views.generic.list import ListView

from .models import Block


class BlockList(ListView):
    model = Block

    def get_queryset(self):
        return (Block.objects
                .filter(owner__id=self.request.user.id)
                .order_by('when'))
