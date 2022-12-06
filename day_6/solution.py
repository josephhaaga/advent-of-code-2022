def index_of_first_packet(s: str, packet_length: int) -> int:
    for i in range(0, len(s) - (packet_length - 1)):
        j = i + (packet_length - 1)
        if len(set(s[i : j + 1])) == packet_length:
            return j + 1
    return 0


def main() -> int:
    with open("input.txt", "r") as f:
        x, *_ = f.readlines()
    # part 1
    print(index_of_first_packet(x, 4))
    # part 2
    print(index_of_first_packet(x, 14))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
