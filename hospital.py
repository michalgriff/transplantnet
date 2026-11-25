import rpyc

conn = rpyc.connect("localhost", 8000)

try:
    print(conn.root.ping())
finally:
    conn.close()