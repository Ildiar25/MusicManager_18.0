# -*- coding: utf-8 -*-
import logging

# noinspection PyProtectedMember
from odoo import _, api
from odoo.exceptions import ValidationError
from odoo.models import AbstractModel

from ...utils.exceptions import (
    InvalidFileFormatError,
    InvalidImageFormatError,
    ImagePersistenceError,
    MusicManagerError
)


_logger = logging.getLogger(__name__)


class ProcessImageMixin(AbstractModel):
    _name = 'music_manager.process_image_mixin'
    _description = 'Music Manager Process Image Mixin'

    # @api.onchange('picture')
    # def _validate_image_format(self):
    #     pass

    def _get_image_service_adapter(self):
        get_param = self.env['ir.config_parameter'].sudo().get_param

        img_format = get_param('music_manager.image_format') or 'png'
        img_size = get_param('music_manager.image_size') or '400'

    def _process_uploaded_image(self):
        pass
