
class PacketDecoder:

    def decodeBITS(self, bits_message):
        packet_bits = self._hexToBin(bits_message)

        packet_data, rem_bits = self._parsePacket(packet_bits)
        return packet_data
    
    def getAllPacketVersions(self, packet_data):
        versions = []

        for packet in packet_data:
            versions.append(packet['version'])
            if 'subpackets' in packet:
                versions += self.getAllPacketVersions(packet['subpackets'])
        
        return versions
    
    def getPacketValue(self, packet_data):
        return packet_data['value']

    def _parsePacket(self, packet):
        packet_data = []
        this_packet = {}

        version, type_id, data = self._getPacketHeader(packet)

        this_packet['version'] = version
        this_packet['type_id'] = type_id
        
        if type_id == 4:
            value, data = self._parseLiteral(data)
            this_packet['value'] = value
        else:
            len_type_id = data[0]
            data = data[1:]

            this_packet['subpackets'] = []

            if len_type_id == '0':
                subpacket_len, subpackets, data = self._parseBitsOfSubPackets(data)
                while len(subpackets) > 0:
                    sub_packet_data, subpackets = self._parsePacket(subpackets)
                    this_packet['subpackets'] += sub_packet_data
                    test = subpackets.replace('0', '')
                    if len(test) == 0:
                        break
                
            elif len_type_id == '1':
                num_subpackets, data = self._parseNumSubPackets(data)

                for sub_packet_index in range(num_subpackets):
                    sub_packet_data, data = self._parsePacket(data)
                    this_packet['subpackets'] += sub_packet_data
            
            result = PacketDecoder.operations[type_id](self, this_packet['subpackets'])
            this_packet['value'] = result
        
        packet_data.append(this_packet)
        return packet_data, data

    def _hexToBin(self, input):
        num_digits = len(input)*4
        res = str(bin(int(input, 16)))[2:].zfill(num_digits)
        return res

    def _binToDec(self, bin_value):
        res = int(bin_value, 2)
        return res

    def _getPacketHeader(self, packet):
        version = self._binToDec(packet[0:3])
        type_id = self._binToDec(packet[3:6])
        data = packet[6:]
        return version, type_id, data

    def _parseLiteral(self, packet):
        value_binary = ''
        data = packet

        i = 0
        while True:
            byte = packet[i:i+5]
            data = packet[i+5:]
            value_binary += byte[1:]

            if byte[0] == '0':
                break

            i+=5
        
        value = self._binToDec(value_binary)

        return value, data

    def _parseBitsOfSubPackets(self, packet):
        
        subpacket_len_bin = packet[0:15]
        subpacket_len = self._binToDec(subpacket_len_bin)

        subpackets = packet[15:15+subpacket_len]
        data = packet[15+subpacket_len:]
        return subpacket_len, subpackets, data

    def _parseNumSubPackets(self, packet):
        num_subpackets = self._binToDec(packet[0:11])
        data = packet[11:]
        return num_subpackets, data

    def _getValuesFromPackets(self, packets):
        return [packet['value'] for packet in packets]

    def _sumPackets(self, packets):
        values = self._getValuesFromPackets(packets)
        if len(values) == 1:
            return values[0]
        result = sum(values)
        return result

    def _productPackets(self, packets):
        values = self._getValuesFromPackets(packets)
        if len(values) == 1:
            return values[0]

        # I originally used numpy.prod() here, but it overflowed on a large value
        result = 1
        for value in values:
            result *= value
        
        return result

    def _minimumPackets(self,packets):
        values = self._getValuesFromPackets(packets)
        result = min(values)
        return result

    def _maximumPackets(self, packets):
        values = self._getValuesFromPackets(packets)
        result = max(values)
        return result

    def _greaterThanPackets(self, packets):
        values = self._getValuesFromPackets(packets)
        if values[0] > values[1]:
            return 1
        return 0

    def _lessThanPackets(self, packets):
        values = self._getValuesFromPackets(packets)
        if values[0] < values[1]:
            return 1
        return 0

    def _equalToPackets(self, packets):
        values = self._getValuesFromPackets(packets)
        if values[0] == values[1]:
            return 1
        return 0

    operations = {0: _sumPackets, 
            1: _productPackets, 
            2: _minimumPackets,
            3: _maximumPackets,
            5: _greaterThanPackets,
            6: _lessThanPackets,
            7: _equalToPackets}
    
    def _sumVersions(self, bits_message):
        packet_data = self.decodeBITS(bits_message)
        versions = self.getAllPacketVersions(packet_data)
        return sum(versions)
    
    def _decodeToValue(self, bits_message):
        packet_data = self.decodeBITS(bits_message)
        return self.getPacketValue(packet_data[0])

    def testDecoder(self):
        print(self._sumVersions('D2FE28')==6)
        print(self._sumVersions('38006F45291200')==9)
        print(self._sumVersions('EE00D40C823060')==14)
        print(self._sumVersions('8A004A801A8002F478') == 16)
        print(self._sumVersions('620080001611562C8802118E34') == 12)
        print(self._sumVersions('C0015000016115A2E0802F182340') == 23)
        print(self._sumVersions('A0016C880162017C3686B18A3D4780') == 31)

        print(self._decodeToValue('C200B40A82') == 3)
        print(self._decodeToValue('04005AC33890') == 54)
        print(self._decodeToValue('880086C3E88112') == 7)
        print(self._decodeToValue('CE00C43D881120') == 9)
        print(self._decodeToValue('D8005AC2A8F0') == 1)
        print(self._decodeToValue('F600BC2D8F') == 0)
        print(self._decodeToValue('9C005AC2F8F0') == 0)
        print(self._decodeToValue('9C0141080250320F1802104A08') == 1)
