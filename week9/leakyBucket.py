def leaky_bucket(bucket_capacity, output_rate, incoming_packets):
    stored = 0  # current number of packets in the bucket
    
    # Print Table Header
    print(f"{'Time (s)':<12}{'Incoming Packets':<18}{'Bucket State (Before Leak)':<24}{'Dropped Packets':<15}{'Transmitted Packets':<20}{'Packets Left in Bucket'}")
    print("="*90)
    
    for time, packets in enumerate(incoming_packets, start=1):
        # Handle overflow: if incoming packets cause bucket overflow
        if packets + stored > bucket_capacity:
            dropped = (packets + stored) - bucket_capacity
            stored = bucket_capacity
        else:
            dropped = 0
            stored += packets
        
        # Transmit packets at output rate
        transmitted = min(stored, output_rate)
        stored -= transmitted
        
        # Print row for the table
        print(f"{time:<12}{packets:<18}{stored + transmitted:<24}{dropped:<15}{transmitted:<20}{stored}")

    # Empty remaining packets in the bucket after incoming packets are done
    while stored > 0:
        time += 1
        transmitted = min(stored, output_rate)
        stored -= transmitted
        
        # Print row for remaining packets
        print(f"{time:<12}{'--':<18}{stored + transmitted:<24}{'--':<15}{transmitted:<20}{stored}")
    
    print("\nAll packets transmitted successfully.")

# ---- Main Program ----
if __name__ == "__main__":
    bucket_capacity = int(input("Enter bucket capacity (packets): "))
    output_rate = int(input("Enter output rate (packets/sec): "))

    n = int(input("Enter number of incoming packet sets: "))
    incoming_packets = []

    for i in range(n):
        packets = int(input(f"Packets arriving at time {i + 1}: "))
        incoming_packets.append(packets)

    leaky_bucket(bucket_capacity, output_rate, incoming_packets)
