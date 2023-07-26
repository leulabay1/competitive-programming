class Solution:
	def minSpeedOnTime(self, dist: List[int], hour: float) -> int:        
		def helper(speed):
			time = 0
			for i in range(len(dist) - 1):
				if dist[i] % speed == 0:
					time += dist[i] // speed
				else:
					time += dist[i] // speed + 1
			time += dist[-1] / speed
			return time
		l = 1
		r = 10 ** 7
		if helper(r) > hour:
			return -1
		while l < r:
			m = l + (r - l) // 2
			if helper(m) > hour:
				l = m + 1
			else:
				r = m
		return l