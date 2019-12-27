#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 19:10:16 2019

@author: sambhav
"""

from django.conf.urls import url
from rest.app.profile.views import UserProfileView


urlpatterns = [
    url(r'^profile', UserProfileView.as_view()),
    ]
