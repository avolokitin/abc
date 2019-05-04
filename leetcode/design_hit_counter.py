class HitCounter:

    def __init__(self, limit):
        """
        Initialize your data structure here.
        """
        self.limit_sec = limit
        self.counter = [None] * 300
        self.hits = [0] * 300
        

    def hit(self, timestamp: int) -> None:
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        index = timestamp % 300
        if self.counter[index] == timestamp:
          self.hits[index] += 1
        else:
          self.counter[index] = timestamp
          self.hits[index] = 1

          
    def getHits(self, timestamp: int) -> int:
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        print(self.counter)
        count = 0
        for i in range(300):
          t = self.counter[i]
          
          if t and timestamp - t < 300:
            count += self.hits[i]
        return count
            