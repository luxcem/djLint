"""Format template tags with extra whitespace."""

import regex as re

from ..settings import Config


def clean_whitespace(html: str, config: Config) -> str:
    """Clean whitespace arround variables and template tags."""

    def _whitespace_variables(match: re.Match) -> str:
        """Remove whitespace around variables."""
        return "{{{{ {} }}}}".format(match.group(1))

    def _whitespace_blocks(match: re.Match) -> str:
        """Remove whitespace around blocks."""
        return "{{% {} %}}".format(match.group(1))

    regex_variables = "{{\s*(.*?\S)\s*}}"
    regex_template_tags = "{%\s*(.*?\S)\s*%}"

    html = re.sub(
        re.compile(
            regex_variables,
            flags=re.IGNORECASE | re.MULTILINE | re.VERBOSE,
        ),
        _whitespace_variables,
        html,
    )

    html = re.sub(
        re.compile(
            regex_template_tags,
            flags=re.IGNORECASE | re.MULTILINE | re.VERBOSE,
        ),
        _whitespace_blocks,
        html,
    )

    return html
