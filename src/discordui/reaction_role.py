from __future__ import annotations

from discord import ButtonStyle
from discord.ui import Button, Container, DesignerView, TextDisplay, Thumbnail
from schemas.reaction_role import OPTION_CLICK, ReactionRoleOption, ReactionRolePanel
from schemas.routing import build_custom_id

from discordui.colors import FroggeColor
from discordui.components import add_button_rows, text_container

__all__ = ["render_panel_post"]


def render_panel_post(panel: ReactionRolePanel, options: list[ReactionRoleOption]) -> Container[DesignerView]:
    header_lines = [f"## {panel.title or 'Untitled Panel'}"]
    if panel.description:
        header_lines.append(panel.description)

    container = text_container(color=FroggeColor(panel.color) if panel.color is not None else None)
    if panel.thumbnail_url:
        container.add_section(*(TextDisplay(line) for line in header_lines), accessory=Thumbnail(panel.thumbnail_url))
    else:
        for line in header_lines:
            container.add_text(line)

    buttons = [
        Button[DesignerView](
            label=option.label or f"Option {index}",
            emoji=option.emoji or None,
            custom_id=build_custom_id(OPTION_CLICK, panel.id, option.id),
            style=ButtonStyle.secondary,
        )
        for index, option in enumerate(options, start=1)
    ]
    add_button_rows(container, buttons, per_row=5)

    return container
