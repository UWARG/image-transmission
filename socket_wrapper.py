"""
Wrapper for socket operations.
"""

import socket

class Socket:
    """
    Wrapper for Pyton's socket module.
    """
    __create_key = object()

    @classmethod
    def create(cls, host: str, port: int) -> "tuple[bool, Socket | None]":
        """
        Establishes connection to drone through provided host/port
        and stores the Socket object.

        Parameters
        ----------
        host: str
        port: int

        Returns
        -------
        tuple[bool, Socket | None]
            The first parameter represents if the socket creation is successful.
            - If it is not successful, the second parameter will be None.
            - If it is successful, the second parameter will be the created
              Socket object.
        """
        try:
            # TCP Connection, do we want UDP instead (socket.SOCK_DGRAM)?
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        except socket.error as e:
            print(f"Could not create socket: {e}.")
            return False, None

        try:
            s.connect(host, port)
        except socket.gaierror as e:
            print(f"Could not connect to socket, address related error: {e}. "
                  "Make sure host/port is a host host/port.")
            return False, None
        except socket.error as e:
            print(f"Could not connect to socket, connection error: {e}.")
            return False, None

        return True, Socket(cls.__create_key, s)

    def __init__(self, class_private_create_key, s: socket.socket):
        """
        Private constructor, use create() method.
        """
        assert class_private_create_key is Socket.__create_key, "Use create() method"

        self.s = s

    def send(self, data: bytes) -> bool:
        """
        Sends all data at once over the socket.

        Parameters
        ----------
        data: bytes

        Returns
        -------
        bool: If the data was sent successfully.
        """
        try:
            self.s.sendall(data)
        except socket.error as e:
            print(f"Could not send data: {e}.")
            return False

        return True
