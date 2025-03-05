from typing import Iterable

from ..packet_builder import QuicSentPacket
from .base import (
    K_MINIMUM_WINDOW,
    QuicCongestionControl,
    QuicRttMonitor,
    register_congestion_control,
)

WINDOW_SIZE = 500_000_000

class FixedCongestionControl(QuicCongestionControl):
    """
    Fixed window length.
    """

    def __init__(self, *, max_datagram_size: int) -> None:
        super().__init__(max_datagram_size=max_datagram_size)
        self._max_datagram_size = max_datagram_size
        self.congestion_window = WINDOW_SIZE
        
    def on_packet_acked(self, *, now: float, packet: QuicSentPacket) -> None:
        pass

    def on_packet_sent(self, *, packet: QuicSentPacket) -> None:
        pass

    def on_packets_expired(self, *, packets: Iterable[QuicSentPacket]) -> None:
        pass

    def on_packets_lost(self, *, now: float, packets: Iterable[QuicSentPacket]) -> None:
        pass

    def on_rtt_measurement(self, *, now: float, rtt: float) -> None:
        pass


register_congestion_control("fixed", FixedCongestionControl)
