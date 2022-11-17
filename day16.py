LITERAL_VALUE_PACKET = 4


def parse_input(input):
    binary = bin(int(input.strip(), 16))[2:]
    if padding_length := len(binary) % 4:
        binary = '0' * padding_length + binary
    return binary


def decode_packet(packet):
    packet = [c for c in packet]
    packets = []

    version = type_id = None

    while packet:
        if not version:
            version = int(''.join(packet[:3]), 2)
            del packet[:3]
        elif not type_id:
            type_id = int(''.join(packet[:3]), 2)
            del packet[:3]
        elif type_id == 4:
            continue_bit = '1'
            value = []
            while continue_bit == '1':
                chunk = packet[:5]
                del packet[:5]
                continue_bit = chunk[0]
                value += chunk[1:]

            packets.append({
                'version': version,
                'type_id': type_id,
                'value': int(''.join(value), 2)
            })

            if len(packet) < 4:
                packet = None

            version = type_id = None
        else:
            length_type_id = int(''.join(packet[0]), 2)
            print(length_type_id)
            packet = None



    return packets

    # version = int(packet[:3], 2)
    # type_id = int(packet[3:6], 2)

    # decoded = {
    #     'version': version,
    #     'type_id': type_id,
    # }

    # if type_id == LITERAL_VALUE_PACKET:
    #     value = []
    #     for i in range(6, len(packet), 5):
    #         control = packet[i]
    #         value.append(packet[i + 1:i + 5])
    #         if control == '0':
    #             break

    #     decoded['value'] = int(''.join(value), 2)
    # else:
    #     length_type_id = packet[6]
    #     if length_type_id == '0':
    #         sub_packet_length = int(packet[7:22], 2)
    #         print(sub_packet_length)

    #     decoded['sub_packets'] = []

    # return decoded
