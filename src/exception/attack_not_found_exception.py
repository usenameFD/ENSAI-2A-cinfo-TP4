class AttackNotFoundException(Exception):
    def __init__(self, identifier):
        # Call the base class constructor with the parameters it needs
        super().__init__(f"The attack with the identifier {identifier} wasn't found")
