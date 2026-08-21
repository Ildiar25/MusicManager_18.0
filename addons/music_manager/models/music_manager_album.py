# -*- coding: utf-8 -*-
import logging

# noinspection PyProtectedMember
from odoo import _
from odoo.models import Model
from odoo.fields import Many2many

from .mixins.image_process_mixin import ProcessImageMixin


_logger = logging.getLogger(__name__)


class Album(Model, ProcessImageMixin):
    _name = 'music_manager.album'
    _description = 'Music Album'

    # Techincal fields
    custom_owner_ids = Many2many(
        comodel_name='res.users', string=_("Owners"), compute='_compute_album_owners', store=True
    )
