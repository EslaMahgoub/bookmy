from .models import Settings


def site_footer(request):
  site_footer = Settings.objects.last()
  return {"site_footer": site_footer}