# -*- coding: utf-8 -*-
import logging

# noinspection PyProtectedMember
from odoo import _
from odoo.models import TransientModel

from .mixins.image_process_mixin import ProcessImageMixin


_logger = logging.getLogger(__name__)


class TrackGuide(TransientModel, ProcessImageMixin):
    _name = 'music_manager.track_guide'
    _description = 'Track Guide Wizard'
