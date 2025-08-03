class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        result = []
        n = len(s)

        # An IP address has between 4 and 12 digits.
        if not (4 <= n <= 12):
            return []

        def backtrack(start_index: int, parts: List[str]):
            # Base Case: We have found 4 parts and have consumed the entire string.
            if len(parts) == 4 and start_index == n:
                result.append(".".join(parts))
                return

            # Pruning: We have already found 4 parts but haven't consumed the
            # entire string, or we have consumed the string but don't have 4 parts.
            if len(parts) == 4 or start_index == n:
                return

            # Brnching: We can form a part of an address using 1, 2, or 3 digits.
            for part_length in range(1, 4):
                # Ensure the segment is within bounds
                if start_index + part_length > n:
                    break

                # Extract the potential segment.
                segment = s[start_index : start_index + part_length]

                # 1. Segment with more than one digit cannot start with '0'.
                if len(segment) > 1 and segment[0] == '0':
                    continue

                # 2. Segment must be between 0 and 255.
                if not (0 <= int(segment) <= 255):
                    continue

                # The segment is valid, add it to our current parts and
                # continue searching from the next index.
                parts.append(segment)
                backtrack(start_index + part_length, parts)
                
                # Backtrack
                parts.pop()

        # Startfrom the beginning of the string.
        backtrack(0, [])
        return result