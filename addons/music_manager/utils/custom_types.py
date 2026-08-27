from typing import Dict, List, Literal, TypeAlias

# -----------------------------------------------------------------------------
# CLASS TYPES
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# CUSTOM ODOO TYPES
# -----------------------------------------------------------------------------

DisplayNotification: TypeAlias = Dict[str, str | Dict[str, str | bool]]
NotificationType: TypeAlias = Literal['success', 'info', 'warning', 'danger']
WizardStates: TypeAlias = List[Literal['start', 'uploaded', 'metadata', 'done']]

# -----------------------------------------------------------------------------
# TECHINCAL TYPES
# -----------------------------------------------------------------------------

ArgsList: TypeAlias = List[str]
FfmpegSettingsDict: TypeAlias = Dict[str, str | ArgsList]
YtdlpSettingsDict: TypeAlias = Dict[str, str | bool | List[Dict[str, str]]]

EngineSettingsDict: TypeAlias = Dict[str, str | ArgsList | FfmpegSettingsDict | YtdlpSettingsDict]
