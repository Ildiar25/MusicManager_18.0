# -*- coding: utf-8 -*-
import logging

# noinspection PyProtectedMember
from odoo import _, api
from odoo.models import Model
from odoo.fields import Binary, Char, Many2one, One2many, Selection

_logger = logging.getLogger(__name__)


class PurchaseOrder(Model):
    _name = 'music_manager.purchase_order'
    _description = 'Purchase Order'

    # Basic fields
    invoice_file = Binary(string=_("Invoice (PDF/JPEG"))
    name = Char(string=_("Description"), compute='_compute_name', store=True)
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

    # Relational fields
    track_ids = One2many(
        comodel_name='music_manager.track', inverse_name='purchase_order_id', string=_("Track(s) Purchased")
    )

    # Techincal fields
    custom_owner_id = Many2one(
        comodel_name='res.users', string=_("Owner"), default=lambda self: self.env.user, required=True
    )

    @api.onchange('store_name', 'order_reference')
    def _compute_name(self) -> None:
        for record in self:
            record.name = f"{record.store_name.upper() if record.store_name else ''} · {record.order_reference or ''}"
