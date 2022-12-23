
import asyncio
import subprocess


def exec_sync(cmd: str, shell: bool = False) -> (str, str):
    """Execute a system command synchronously using Python and get the stdout and stderr as strings.

    Parameters:
        cmd: Command to execute.
        shell: Whether to run in shell mode.

    Returns:
        tuple of stdout and stderr as strings
    """
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=shell)
    stdout, stderr = proc.communicate()
    # None shouldn't be converted to "None" or b''
    if stdout:
        stdout = str(stdout.decode("utf-8"))
    else:
        stdout = ""
    if stderr:
        stderr = str(stderr.decode("utf-8"))
    else:
        stderr = ""
    return stdout, stderr


async def exec_async(cmd: str, shell: bool = False) -> (str, str):
    """Execute a system command asynchronously using Python and get the stdout and stderr as strings

    Parameters:
        cmd: Command to execute.
        shell: Whether to run in shell mode.

    Returns:
        tuple of stdout and stderr as strings
    """
    if shell:
        proc = await asyncio.create_subprocess_shell(cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.STDOUT, shell=True)
    else:
        proc = await asyncio.create_subprocess_shell(cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.STDOUT, shell=True)
    stdout, stderr = await proc.communicate()
    # None shouldn't be converted to "None" or b''
    if stdout:
        stdout = str(stdout.decode("utf-8"))
    else:
        stdout = ""
    if stderr:
        stderr = str(stderr.decode("utf-8"))
    else:
        stderr = ""
    return stdout, stderr
