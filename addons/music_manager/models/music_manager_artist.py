# -*- coding: utf-8 -*-
import logging

# noinspection PyProtectedMember
from odoo import _
from odoo.models import Model
from odoo.fields import Many2one

from .mixins.image_process_mixin import ProcessImageMixin


_logger = logging.getLogger(__name__)


class Artist(Model, ProcessImageMixin):
    _name = 'music_manager.artist'
    _description = 'Music Manager Artist Model'

    # Techincal fields
    custom_owner_id = Many2one(
        comodel_name='res.users', string="Owner", default=lambda self: self.env.user, required=True
    )
