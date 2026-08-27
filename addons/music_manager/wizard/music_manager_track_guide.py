# -*- coding: utf-8 -*-
import logging

# noinspection PyProtectedMember
from odoo import _
from odoo.fields import Binary, Boolean, Char, Date, Selection, Many2one
from odoo.models import TransientModel

from ..models.mixins.image_process_mixin import ProcessImageMixin
from ..utils.custom_types import WizardStates


_logger = logging.getLogger(__name__)


class TrackGuide(TransientModel, ProcessImageMixin):
    _name = 'music_manager.track_guide'
    _description = 'Track Guide Wizard'

    # Purchase Order fields
    order_reference = Char(string=_("Order Number"), required=True)
    store_name = Selection(
        selection=[
            ('bandcamp', _("Bandcamp")),
            ('beatport', _("Beatport")),
            ('amazon', _("Amazon Music")),
            ('itunes', _("iTunes Music")),
            ('other', _("Other")),
        ],
        string=_("Store"),
        required=True,
    )

    # Wizard fields
    file = Binary(string=_("File"))
    file_name = Char(string=_("Filename"), default='')
    url = Char(string=_("URL"))

    # Relational fields
    purchase_order_id = Many2one(
        comodel_name='music_manager.purchase_order', string=_("Purchase Order"), domain="[('custom_owner_id', '=', uid)]"
    )

    # Computed fields
    has_valid_path = Boolean(string=_("Valid path"), default=True)

    # Technical fields
    purchase_option = Selection(
        selection=[
            ('existing', _("Existing")),
            ('new', _("New")),
        ],
        string=_("Voucher"),
        default='existing',
        required=True,
    )
    state = Selection(
        selection=[
            ('start', _("Start")),
            ('uploaded', _("Uploaded")),
            ('metadata', _("Metadata Editing")),
            ('done', _("Done")),
        ],
        string=_("State"),
        default='start'
    )

    def action_back(self):
        self.ensure_one()

        states: WizardStates = ['start', 'uploaded', 'metadata', 'done']
        current_index = states.index(self.state)

        if current_index > 0:
            self.state = states[current_index - 1]

        return self._open_wizard()

    def action_next(self):
        self.ensure_one()

        match self.state:
            case 'start':
                self.state = 'uploaded'

            case 'uploaded':
                self.state = 'metadata'

            case 'metadata':
                self.state = 'done'

        return self._open_wizard()

    def action_save_file(self):
        self.ensure_one()


    def _open_wizard(self):
        return {
            'name': _("Track Wizard"),
            'type': 'ir.actions.act_window',
            'res_model': 'music_manager.track_guide',
            'view_mode': 'form',
            'target': 'new',
            'res_id': self.id,
            'context': self.env.context,
        }
