from pathlib import Path
from typing import Union

from aiofile import AIOFile


async def write(filepath: Union[str, Path], content: Union[str, bytes]):
    """ Write binary content to file. """
    async with AIOFile(filepath, 'wb+') as afp:
        await afp.write(content)
