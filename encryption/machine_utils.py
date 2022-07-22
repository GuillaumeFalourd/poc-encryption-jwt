import platform
import re
import subprocess # nosec
from os import name, popen

class MetricsBuilder:

    def __init__(self):
        self.machine_id = self.__get_machine_id()

    def __get_machine_id(self) -> str:

        if platform.system() == "Darwin":
            return self.__get_machine_id_macos()

        if "nt" in name:
            return (
                subprocess.check_output("wmic csproduct get uuid", shell=False).strip().decode().split("\n")[1]  # nosec
            )
        else:
            return subprocess.check_output(["cat", "/etc/machine-id"], shell=False).strip().decode()  # nosec

    def __get_machine_id_macos(self) -> str:
        machine_uuid_str = ""

        p = popen("ioreg -rd1 -c IOPlatformExpertDevice | grep -E '(UUID)'", "r")  # nosec

        while 1:
            line = p.readline()
            if not line:
                break
            machine_uuid_str += line

        match_obj = re.compile("[A-Z,0-9]{8,8}-[A-Z,0-9]{4,4}-[A-Z,0-9]{4,4}-[A-Z,0-9]{4,4}-[A-Z,0-9]{12,12}")

        results = match_obj.findall(machine_uuid_str)

        if len(results):
            return results[0]