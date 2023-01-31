import logging
import coloredlogs
import socket
import re

def main():
    coloredlogs.install(level='DEBUG')

    addr = ("", 12345)
    if socket.has_dualstack_ipv6():
        s = socket.create_server(addr, family=socket.AF_INET6, dualstack_ipv6=True)
    else:
        logging.fatal("no dualstack support")
    logging.info("waiting for client to connect...")
    while True:
        client, client_addr = s.accept()
        logging.info(f"recv from {client_addr}")
        response = client_addr[0]
        # if client.recv(0x10) != b"LC~0#\x16\x03u\x8dB/~_fXF":
        #     logging.warning("detected untrusted client")
        #     client.close()
        #     continue
        m = re.match(r"::ffff:(\d+\.\d+\.\d+\.\d+)",response)
        # match ipv4
        if m:
            response = m.groups()[0]
        client.send(response.encode())
        client.close()

if __name__ == "__main__":
    main()