def parse_trace_file(filename):
    sent_packets = {}
    received_packets = {}
    packet_delays = {}
    routing_packets = 0
    total_bytes_received = 0
    total_bytes_sent = 0
    dropped_packets = 0
    start_time = end_time = None

    with open(filename, 'r') as file:
        for line in file:
            fields = line.split()
            if len(fields) < 12:  # Ensure enough fields are present
                continue

            event_type = fields[0]
            time = float(fields[1])

            # Adjust these indices based on your trace file format
            src_dst_seq = fields[-2].strip('[]')
            packet_id = '_'.join(src_dst_seq.split()[:3])
            packet_size = int(fields[7])  # Corrected index for packet size

            if start_time is None or time < start_time:
                start_time = time
            if end_time is None or time > end_time:
                end_time = time

            if event_type == 's':
                sent_packets[packet_id] = time
                total_bytes_sent += packet_size
                if fields[3] == 'RTR':
                    routing_packets += 1
            elif event_type == 'r':
                received_packets[packet_id] = time
                if packet_id in sent_packets:
                    delay = time - sent_packets[packet_id]
                    packet_delays[packet_id] = delay
                total_bytes_received += packet_size
                if fields[3] == 'RTR':
                    routing_packets += 1
            elif event_type == 'd':
                dropped_packets += 1

    return sent_packets, received_packets, packet_delays, total_bytes_received, total_bytes_sent, dropped_packets, routing_packets, start_time, end_time

def calculate_metrics(sent_packets, received_packets, packet_delays, total_bytes_received, total_bytes_sent, dropped_packets, routing_packets, start_time, end_time):
    pdr = len(received_packets) / len(sent_packets) if sent_packets else 0
    average_delay = sum(packet_delays.values()) / len(packet_delays) if packet_delays else 0
    simulation_time = end_time - start_time if start_time and end_time else 0
    throughput = (total_bytes_received * 8) / simulation_time if simulation_time > 0 else 0  # in bits per second
    average_throughput = throughput / len(received_packets) if received_packets else 0
    packet_drop_rate = dropped_packets / len(sent_packets) if sent_packets else 0
    nrl = routing_packets / len(received_packets) if received_packets else 0

    return {
        'Packet Delivery Ratio': pdr,
        'Average End-to-End Delay': average_delay,
        'Throughput (bps)': throughput,
        'Average Throughput (bps per packet)': average_throughput,
        'Packet Drop Rate': packet_drop_rate,
        'Normalized Routing Load': nrl
    }

def main():
    trace_file = 'ghaziabad.tr'  # Replace with your trace file name
    metrics_data = parse_trace_file(trace_file)
    metrics = calculate_metrics(*metrics_data)

    for metric, value in metrics.items():
        print(f'{metric}: {value}')

if __name__ == "__main__":
    main()

