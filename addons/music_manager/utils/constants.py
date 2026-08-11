from typing import Dict, Final


# -----------------------------------------------------------------------------
# CONSTANTS
# -----------------------------------------------------------------------------

METADATA_TAG_MAPPING: Final[Dict[str, Dict[str, str]]] = {

    # ID & TRACK DATA
    # --------------------------------------
    'name': {
        'mp3': 'TIT2',
        'flac': 'TITLE',
        'ogg': 'TITLE',
    },
    'track_no': {
        'mp3': 'TRCK',  # 1/12 format
        'flac': 'TRACKNUMBER',
        'ogg': 'TRACKNUMBER',
    },
    'total_track': {
        'mp3': 'TRCK',  # 1/12 format
        'flac': 'TRACKTOTAL',
        'ogg': 'TRACKTOTAL',
    },
    'disk_no': {
        'mp3': 'TPOS',  # 1/2 format
        'flac': 'DISCNUMBER',
        'ogg': 'DISCNUMBER',
    },
    'total_disk': {
        'mp3': 'TPOS',  # 1/2 format
        'flac': 'DISCTOTAL',
        'ogg': 'DISCTOTAL',
    },
    'year': {
        'mp3': 'TDRC',
        'flac': 'DATE',
        'ogg': 'DATE',
    },
    'picture': {
        'mp3': 'APIC',
        'flac': 'METADATA_BLOCK_PICTURE',
        'ogg': 'METADATA_BLOCK_PICTURE',
    },

    # ALBUM & ARTISTS DATA
    # --------------------------------------
    'album_id': {
        'mp3': 'TALB',
        'flac': 'ALBUM',
        'ogg': 'ALBUM',
    },
    'track_artist_ids': {
        'mp3': 'TPE1',
        'flac': 'ARTIST',
        'ogg': 'ARTIST',
    },
    'album_artist_id': {
        'mp3': 'TPE2',
        'flac': 'ALBUMARTIST',
        'ogg': 'ALBUMARTIST',
    },
    'original_artist_id': {
        'mp3': 'TOPE',
        'flac': 'ORIGARTIST',
        'ogg': 'ORIGARTIST',
    },
    'genre_id': {
        'mp3': 'TCON',
        'flac': 'GENRE',
        'ogg': 'GENRE',
    },
    'compilation': {
        'mp3': 'TCMP',
        'flac': 'COMPILATION',
        'ogg': 'COMPILATION',
    },
    'track_language_ids': {
        'mp3': 'TLAN',
        'flac': 'LANGUAGE',
        'ogg': 'LANGUAGE',
    },

    # TECHNICAL DATA
    # --------------------------------------
    'bpm': {
        'mp3': 'TBPM',
        'flac': 'BPM',
        'ogg': 'BPM',
    },
    'isrc': {
        'mp3': 'TSRC',
        'flac': 'ISRC',
        'ogg': 'ISRC',
    },
    'lyrics': {
        'mp3': 'USLT',
        'flac': 'LYRICS',
        'ogg': 'LYRICS',
    },

    # INDUSTRY, LICENSE & OWNERSHIP
    # --------------------------------------
    'publisher': {
        'mp3': 'TPUB',
        'flac': 'PUBLISHER',
        'ogg': 'PUBLISHER',
    },
    'copyright': {
        'mp3': 'TCOP',
        'flac': 'COPYRIGHT',
        'ogg': 'COPYRIGHT',
    },
    'barcode': {
        'mp3': 'TXXX:BARCODE',
        'flac': 'BARCODE',
        'ogg': 'BARCODE',
    },
    'catalog_no': {
        'mp3': 'TXXX:CATALOGNUMBER',
        'flac': 'CATALOGNUMBER',
        'ogg': 'CATALOGNUMBER',
    },
    'custom_owner_id': {
        'mp3': 'TOWN',
        'flac': 'OWNER',
        'ogg': 'OWNER',
    },

    # PURCHASE DATA
    # --------------------------------------
    'store_vendor': {
        'mp3': 'TXXX:STORE',
        'flac': 'STORE',
        'ogg': 'STORE',
    },
    'order_id': {
        'mp3': 'TXXX:ORDER_ID',
        'flac': 'ORDER_ID',
        'ogg': 'ORDER_ID',
    },
    'purchase_date': {
        'mp3': 'TXXX:PURCHASE_DATE',
        'flac': 'PURCHASE_DATE',
        'ogg': 'PURCHASE_DATE',
    },
    'buyer_email': {
        'mp3': 'TXXX:BUYER',
        'flac': 'BUYER',
        'ogg': 'BUYER',
    },

    # MUSICBRAINZ IDS
    # --------------------------------------
    'mbrainz_track_id': {
        'mp3': 'TXXX:MUSICBRAINZ_TRACKID',
        'flac': 'MUSICBRAINZ_TRACKID',
        'ogg': 'MUSICBRAINZ_TRACKID',
    },
    'mbrainz_artist_id': {
        'mp3': 'TXXX:MUSICBRAINZ_ARTISTID',
        'flac': 'MUSICBRAINZ_ARTISTID',
        'ogg': 'MUSICBRAINZ_ARTISTID',
    },
    'mbrainz_album_id': {
        'mp3': 'TXXX:MUSICBRAINZ_ALBUMID',
        'flac': 'MUSICBRAINZ_ALBUMID',
        'ogg': 'MUSICBRAINZ_ALBUMID',
    },
    'mbrainz_albumartist_id': {
        'mp3': 'TXXX:MUSICBRAINZ_ALBUMARTISTID',
        'flac': 'MUSICBRAINZ_ALBUMARTISTID',
        'ogg': 'MUSICBRAINZ_ALBUMARTISTID',
    },
    'mbrainz_disc_id': {
        'mp3': 'TXXX:MUSICBRAINZ_DISCID',
        'flac': 'MUSICBRAINZ_DISCID',
        'ogg': 'MUSICBRAINZ_DISCID',
    },
}