# -*- coding: utf-8 -*-
import logging

# noinspection PyProtectedMember
from odoo import _
from odoo.models import Model


class Track(Model):
    _name = 'music_manager.track'
    _description = 'Music Track'
