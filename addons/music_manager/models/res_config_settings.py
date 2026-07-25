# -*- coding: utf-8 -*-
import logging

# noinspection PyProtectedMember
from odoo import _
from odoo.models import TransientModel
from odoo.fields import Boolean, Char, Selection

_logger = logging.getLogger(__name__)

class ResConfigSettings(TransientModel):
    _inherit = 'res.config.settings'
    _description = 'Music Manager module settings'

    # Basic fields
    mm_allow_deletes = Boolean(
        string=_("Delete server files"), default=False, config_parameter='music_manager.allow_deletes', required=True
    )

    mm_audio_quality = Selection(
        selection=[
            ('auto', _("Auto")),
            ('low', _("Low")),
            ('medium', _("Medium")),
            ('High', _("High")),
        ],
        string=_("Download quality"),
        default='auto',
        config_parameter='music_manager.audio_quality',
        required=True,
    )

    mm_download_engine = Selection(
        selection=[
            ('pytube', _("PyTube")),
            ('ytdlp', _("YouTube DLP")),
            ('spotdl', _("SpotDL")),
        ],
        string=_("Available downloaders"),
        default='ytdlp',
        config_parameter='music_manager.download_engine',
        required=True,
    )

    mm_file_format = Selection(
        selection=[
            ('mp3', _("MP3")),
            ('ogg', _("Ogg")),
            ('flac', _("Lossless (FLAC)")),
        ],
        string=_("Download music format"),
        default='mp3',
        config_parameter='music_manager.file_format',
        required=True,
    )

    mm_image_format = Selection(
        selection=[
            ('png', _("PNG")),
            ('jpg', _("JPEG")),
        ],
        string=_("General image format"),
        default='png',
        config_parameter='music_manager.image_format',
        required=True,
    )

    mm_image_size = Selection(
        selection=[
            ('300', _("300x300 px")),
            ('400', _("400x400 px")),
            ('600', _("600x600 px")),
            ('1200', _("1200x1200 px")),
        ],
        string=_("Image size"),
        default='400',
        config_parameter='music_manager.image_size',
        required=True,
    )

    mm_root_directory = Char(
        string=_("Root directory"),
        default='/music',
        config_parameter='music_manager.root_directory',
        readonly=True,
        required=True,
    )

    def action_sync_music_library(self):
        return {
            'type': 'ir.actions.client',
            'tag': 'display_notification',
            'params': {
                'title': _("Music Manager says:"),
                'message': _("This is your first config!"),
                'type': 'success',
                'sticky': False,
            }
        }
