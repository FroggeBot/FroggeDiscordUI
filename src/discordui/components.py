from __future__ import annotations

from collections.abc import Sequence

from discord.ui import Button, Container, DesignerView

from discordui.colors import FroggeColor

__all__ = [
    "add_button_rows",
    "menu_view",
    "text_container",
]


def menu_view(*containers: Container[DesignerView], timeout: float | None = 180.0) -> DesignerView:
    return DesignerView(*containers, timeout=timeout)


def text_container(
    *lines: str, color: FroggeColor | None = None, color_override: bool = False
) -> Container[DesignerView]:
    container: Container[DesignerView] = Container(
        color=color or (
            FroggeColor.random_all()
            if not color_override
            else FroggeColor(0x2B2D31)  # Dark Mode Background Color
        )
    )
    for line in lines:
        container.add_text(line)
    return container


def add_button_rows(
    container: Container[DesignerView], buttons: Sequence[Button[DesignerView]], *, per_row: int = 3
) -> None:
    """Chunk a flat list of buttons into rows of at most `per_row` (Discord allows up to 5) -
    keeps pure navigation-menu screens from cramming everything into one wide row."""
    for i in range(0, len(buttons), per_row):
        container.add_row(*buttons[i : i + per_row])
