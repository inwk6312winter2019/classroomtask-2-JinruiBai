class IpCalculator(object):
	def __init__(self, ip_address, cdir=24):
    if '/' in ip_address:
      self._cidr = ip_address.split('/')
    else:
      self._address = map(int, ip_address.split('.'))
      self._cidr = cdir
      self.net_mask = []
      self.broadcast = []			
	def net_mask(self):
    mask = [0, 0, 0, 0]
    for i in range(int(self._cidr)):
      mask[i / 8] += 1 << (7 - i % 8)
      return mask
	def broadcast_ip(self):
    broadcast = list()
      for x, y in range(self.broadcast):
        broadcast.append(int(x, 2) | int(y, 2))
        self.broadcast = broadcast
        return broadcast
	def host_range(self):
    min_range = self.network
    min_range[-1] += 1
    max_range = self.broadcast
    max_range[-1] -= 1
    return host_range
