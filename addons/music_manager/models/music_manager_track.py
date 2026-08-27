# -*- coding: utf-8 -*-
import logging

# noinspection PyProtectedMember
from odoo import _
from odoo.models import Model
from odoo.fields import Many2one

from .mixins.image_process_mixin import ProcessImageMixin


_logger = logging.getLogger(__name__)


class Track(Model, ProcessImageMixin):
    _name = 'music_manager.track'
    _description = 'Music Manager Track Model'

    # Relational fields
    purchase_order_id = Many2one(comodel_name='music_manager.purchase_order', string=_("Purchase Order"))

    # Techincal fields
    custom_owner_id = Many2one(
        comodel_name='res.users', string="Owner", default=lambda self: self.env.user, required=True
    )
