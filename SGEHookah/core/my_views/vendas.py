from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from core.funcoes import arruma_url_page
from core.models import *
from core.forms import *
