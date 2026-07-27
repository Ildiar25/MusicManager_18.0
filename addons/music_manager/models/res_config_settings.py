# -*- coding: utf-8 -*-
import logging

# noinspection PyProtectedMember
from odoo import _
from odoo.models import TransientModel
from odoo.fields import Boolean, Char, Selection

from ..services.download_engines import get_engine_settings
from ..utils.custom_types import DisplayNotification, NotificationType


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
            ('high', _("High")),
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
        self.execute()

        get_param = self.env['ir.config_parameter'].sudo().get_param

        root_dir = get_param('music_manager.root_directory')
        allow_deletes = get_param('music_manager.allow_deletes')
        engine = get_param('music_manager.download_engine')
        fmt = get_param('music_manager.file_format')
        preset = get_param('music_manager.audio_quality')

        settings = get_engine_settings(engine, fmt, preset)

        message = f"My engine: {settings}"


        return self._notify_user(message, 'info')

    @staticmethod
    def _notify_user(message: str, style: NotificationType, sticky: bool = False) -> DisplayNotification:
        return {
            'type': 'ir.actions.client',
            'tag': 'display_notification',
            'params': {
                'title': _("Music Manager says:"),
                'message': message,
                'type': style,
                'sticky': sticky,
            }
        }
