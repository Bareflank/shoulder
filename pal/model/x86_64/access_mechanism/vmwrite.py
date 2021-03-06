from pal.model.access_mechanism import AbstractAccessMechanism
from dataclasses import dataclass

@dataclass()
class VMWrite(AbstractAccessMechanism):
    """
    Access mechanism writing a value to a VMCS using the x86 vmwrite
    instruction
    """

    encoding: int = 0
    """ The encoding of the VMCS field to be written """

    name: str = "vmwrite"
    """ The name of this access mechanism  """

    def is_read(self):
        return False

    def is_write(self):
        return True

    def is_memory_mapped(self):
        return False

    def is_valid(self):
        # TODO Check source assembler mnemonic is valid
        return True

