import math

sequence = open('input.txt', 'r').read().strip()


def decimal(seq):
    return int(seq, 2)


# de-frame a packet
def destructure(pkt):
    version = decimal(pkt[:3])
    type_id = decimal(pkt[3:6])
    payload = pkt[6:]
    consumed = 6
    if type_id == 4:  # literal value packet
        parts = []
        while True:
            sign = payload[0]
            num = payload[1:5]
            payload = payload[5:]
            consumed += 5
            parts.append(num)
            if sign == '0':
                break
        literal = int(''.join(parts), 2)
        return {'version': version, 'type_id': type_id, 'value': literal, 'consumed': consumed, 'rest': payload}
    else:  # operator packet
        length_type_id = payload[0]
        consumed += 1
        payload = payload[1:]
        subpackets = []
        if length_type_id == '0':
            # next 15 bits represent total length in bits of the sub-packets
            pkt_length = decimal(payload[:15])
            payload = payload[15:]
            consumed += 15

            subconsumed = 0
            while subconsumed < pkt_length:
                resp = destructure(payload)
                subpackets.append(resp)
                subconsumed += resp['consumed']
                payload = resp['rest']
            consumed += subconsumed

        elif length_type_id == '1':
            # next 11 bits represent number of sub-packets immediately contained
            num_subpackets = decimal(payload[:11])
            payload = payload[11:]
            consumed += 11

            while num_subpackets > 0:
                resp = destructure(payload)
                subpackets.append(resp)
                consumed += resp['consumed']
                payload = resp['rest']
                num_subpackets -= 1

        values = [pkt['value'] for pkt in subpackets]
        if type_id == 0:  # sum
            value = sum(values)
        elif type_id == 1:  # product
            value = math.prod(values)
        elif type_id == 2:  # min
            value = min(values)
        elif type_id == 3:  # max
            value = max(values)
        elif type_id == 5:  # greater than
            value = 1 if values[0] > values[1] else 0
        elif type_id == 6:  # less than
            value = 1 if values[0] < values[1] else 0
        elif type_id == 7:  # equal to
            value = 1 if values[0] == values[1] else 0

        return {
            'version': version,
            'type_id': type_id,
            'consumed': consumed,
            'rest': payload,
            'subpackets': subpackets,
            'value': value,
        }


def part1():
    pkt = bin(int('1' + sequence, 16))[3:]
    pkt = destructure(pkt)

    def count_field(pkt, field):
        ct = pkt[field]
        if 'subpackets' in pkt:
            for subpkt in pkt['subpackets']:
                ct += count_field(subpkt, field)
        return ct

    return count_field(pkt, 'version')


def part2():
    pkt = bin(int('1' + sequence, 16))[3:]
    pkt = destructure(pkt)
    return pkt['value']


print(part1())
print(part2())
