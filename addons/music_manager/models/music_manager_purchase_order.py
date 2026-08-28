# -*- coding: utf-8 -*-
import logging

# noinspection PyProtectedMember
from odoo import _, api
from odoo.exceptions import ValidationError
from odoo.models import Model
from odoo.fields import Binary, Char, Date, Html, Integer, Many2one, Monetary, One2many, Selection

_logger = logging.getLogger(__name__)


class PurchaseOrder(Model):
    _name = 'music_manager.purchase_order'
    _description = 'Music Manager Purchase Order Model'
    _sql_constraints = [
        (
            'unique_store_order_reference',
            'UNIQUE(store_name, order_reference, custom_owner_id)',
            _("This Purchase Order already exists in that Store!")
         )
    ]

    # Model constants
    MAX_REF_LENGTH = 64

    # Basic fields
    amount = Monetary(string=_("Amount"), currency_field="currency_id", default=0)
    name = Char(string=_("Name"), compute='_compute_name')
    notes = Html(string=_("Notes"))
    order_reference = Char(string=_("Order Number"), size=MAX_REF_LENGTH, required=True)
    purchase_date = Date(string=_("Purchase Date"))
    receipt_file = Binary(string=_("Receipt (PDF)"), attachment=True)
    receipt_filename = Char(string=_("Filename"), default='')
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
    currency_id = Many2one(
        comodel_name='res.currency', string=_("Currency"), default=lambda self: self.env.company.currency_id
    )
    track_ids = One2many(
        comodel_name='music_manager.track', inverse_name='purchase_order_id', string=_("Track(s) Purchased")
    )

    # Computed fields
    display_title = Char(string=_("Display title"), compute='_compute_display_title_form', store=True)
    track_amount = Integer(string=_("Track amount"), compute='_compute_track_amount', default=0, store=False)

    # Techincal fields
    custom_owner_id = Many2one(
        comodel_name='res.users', string=_("Owner"), default=lambda self: self.env.user, required=True
    )

    @api.model_create_multi
    def create(self, vals_list):
        for purchase in vals_list:
            if purchase.get('order_reference'):
                purchase['order_reference'] = purchase['order_reference'].strip().upper()

        return super().create(vals_list)

    def write(self, vals):
        if vals.get('order_reference'):
            vals['order_reference'] = vals['order_reference'].strip().upper()

        return super().write(vals)

    @api.depends('order_reference')
    def _compute_display_title_form(self) -> None:
        for purchase in self:
            if not purchase.id:
                purchase.display_title = _("New purchase order")

            else:
                purchase.display_title = _("Editing '%s'", purchase.order_reference)

    @api.depends('store_name', 'order_reference')
    def _compute_name(self) -> None:
        for purchase in self:
            display_name = []

            if purchase.store_name:
                display_name.append(purchase.store_name.upper())

            if purchase.order_reference:
                display_name.append(purchase.order_reference.upper())

            new_name = " · ".join(display_name)
            purchase.name = new_name

    @api.depends('track_ids')
    def _compute_track_amount(self) -> None:
        for purchase in self:
            purchase.track_amount = len(purchase.track_ids)

    @api.constrains('order_reference')
    def _check_order_reference(self) -> None:
        for purchase in self:
            if purchase.order_reference and len(purchase.order_reference) > self.MAX_REF_LENGTH:
                raise ValidationError(
                    _("\nThe Order Reference '%(ref)s' exceeds the limit of '%(max)s' characters!",
                      ref=purchase.order_reference, max=self.MAX_REF_LENGTH)
                )

    @api.constrains('purchase_date')
    def _check_purchase_date(self) -> None:
        for purchase in self:
            if purchase.purchase_date and purchase.purchase_date > Date().today():
                raise ValidationError(_("\nThe purchase date cannot be later than today!"))

    def action_view_purchased_tracks(self):
        self.ensure_one()
        return {
            'name': _("Purchased Tracks"),
            'type': 'ir.actions.act_window',
            'res_model': 'music_manager.track',
            'view_mode': 'list,form',
            'domain': [('purchase_order_id', '=', self.id)],
            'context': {'default_purchase_order_id': self.id},
        }
