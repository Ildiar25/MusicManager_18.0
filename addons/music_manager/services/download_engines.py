from typing import Any, Dict, Final, List

from ..utils.custom_types import ArgsList, FfmpegSettingsDict, YtdlpSettingsDict, EngineSettingsDict


# -----------------------------------------------------------------------------
# QUALITY MAPPING
# -----------------------------------------------------------------------------

FFMPEG_CODEC_MAPPING: Final[Dict[str, str]] = {
    'flac': 'flac',
    'mp3': 'libmp3lame',
    'ogg': 'libvorbis',
}

FFMPEG_QUALITY_MAPPING: Final[Dict[str, Dict[str, List[str]]]] = {
    'flac': {
        'auto': ['-compression_level', '12'],
        'low': ['-compression_level', '5'],
        'medium': ['-compression_level', '8'],
        'high': ['-compression_level', '12'],
    },
    'mp3': {
        'auto': ['-q:a', '0'],
        'low': ['-b:a', '128k'],
        'medium': ['-b:a', '192k'],
        'high': ['-b:a', '320k'],
    },
    'ogg': {
        'auto': ['-q:a', '10'],
        'low': ['-q:a', '4'],
        'medium': ['-q:a', '6'],
        'high': ['-q:a', '9'],
    },
}


SPOTDL_QUALITY_MAPPING: Final[Dict[str, str]] = {
    'auto': 'auto',
    'low': '128k',
    'medium': '192k',
    'high': '320k',
}


YTDLP_QUALITY_MAPPING: Final[Dict[str, str]] = {
    'auto': '0',
    'low': '128',
    'medium': '192',
    'high': '320',
}



# -----------------------------------------------------------------------------
# ENGINE SETTINGS
# -----------------------------------------------------------------------------

def get_engine_settings(engine: str, fmt: str, preset: str) -> EngineSettingsDict:

    pytube_settings: FfmpegSettingsDict = {
        'codec': FFMPEG_CODEC_MAPPING.get(fmt, 'libmp3lame'),
        'args': FFMPEG_QUALITY_MAPPING.get(fmt, {}).get(preset, []),
        'output_format': fmt,
    }

    spotdl_args: ArgsList = [
        '--format', fmt,
        '--bitrate', SPOTDL_QUALITY_MAPPING.get(preset, 'auto'),
    ]

    ytdlp_settings: YtdlpSettingsDict = {
        'format': 'bestaudio/best',
        'quiet': False,
        'keepvideo': False,
        'noplaylist': True,
        'no_warnings': True,
        'prefer_ffmpeg': True,
        'postprocessors': [
            {
                'key': 'FFmpegExtractAudio',
                'preferredcodec': fmt,
                'preferredquality': YTDLP_QUALITY_MAPPING.get(preset, '0'),
            },
            {
                'key': 'FFmpegMetadata',
            }
        ],
    }

    settings: Dict[str, ArgsList | FfmpegSettingsDict | YtdlpSettingsDict] = {
        'pytube': pytube_settings,
        'spotdl': spotdl_args,
        'ytdlp': ytdlp_settings,
    }

    return {
        'engine': engine,
        'format': fmt,
        'preset': preset,
        'settings': settings.get(engine, {}),
    }