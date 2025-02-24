from layers.application_layer import ApplicationLayer
from layers.presentation_layer import PresentationLayer
from layers.session_layer import SessionLayer
from layers.transport_layer import TransportLayer
from layers.network_layer import NetworkLayer
from layers.data_link_layer import DataLinkLayer
from layers.physical_layer import PhysicalLayer

def simulate_osi_model():
    message = "Hello, Network!"

    app = ApplicationLayer()
    pres = PresentationLayer()
    sess = SessionLayer()
    trans = TransportLayer()
    net = NetworkLayer()
    link = DataLinkLayer()
    phys = PhysicalLayer()

    # sending Data
    data = app.send(message)
    data = pres.send(data)
    data = sess.send(data)
    data = trans.send(data)
    data = net.send(data, "192.168.1.1")
    data = link.send(data, "00:1A:2B:3C:4D:5E")
    bits = phys.send(data)

    print("\n----- Data Transmission Complete -----\n")

    # receiving Data
    received_frame = phys.receive(bits)
    received_packet = link.receive(received_frame)
    received_segment = net.receive(received_packet)
    received_data = trans.receive(received_segment)
    received_data = sess.receive(received_data)
    received_data = pres.receive(received_data)
    response = app.receive(received_data)

simulate_osi_model()
