import pydivert

def modify_packet_ttl(packet, new_ttl):
    """
    Modifies the TTL (Time to Live) value of the IP packet.

    Args:
        packet: The network packet to be modified.
        new_ttl: The new TTL value to assign to the packet.
    """
    packet.ipv4.ttl = new_ttl

def intercept_and_modify_ttl(filter_rule, target_ttl):
    """
    Intercepts inbound network packets matching a filter rule, modifies their TTL, and reinjects them.

    Args:
        filter_rule: The WinDivert filter string used to capture specific network packets.
        target_ttl: The TTL value to assign to the intercepted packets.
    """
    with pydivert.WinDivert(filter_rule) as w:
        for packet in w:
            # Modify the packet's TTL value
            modify_packet_ttl(packet, target_ttl)
            
            # Reinject the modified packet into the network
            w.send(packet)

if __name__ == "__main__":
    FILTER_RULE = "inbound && ip.TTL == 1"  # Define the filter for capturing packets with TTL = 1
    TARGET_TTL = 32  # Define the new TTL value to assign to the packets
    
    print("Intercepting and modifying packets...")

    intercept_and_modify_ttl(FILTER_RULE, TARGET_TTL)
    
    print("Packet interception and modification complete.")
