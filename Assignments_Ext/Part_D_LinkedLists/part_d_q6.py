# Part D - Question 6: Favorites List ADT


class FavoritesList:
    class _Item:
        def __init__(self, val):
            self.val = val
            self.count = 0

    def __init__(self):
        self.data = []

    def is_empty(self):
        return len(self.data) == 0

    def access(self, e):
        for item in self.data:
            if item.val == e:
                item.count += 1
                return
        new_item = self._Item(e)
        new_item.count = 1
        self.data.append(new_item)

    def remove(self, e):
        for i, item in enumerate(self.data):
            if item.val == e:
                self.data.pop(i)
                return True
        return False

    def top(self, k):
        sorted_items = sorted(self.data, key=lambda x: x.count, reverse=True)
        return [(item.val, item.count) for item in sorted_items[:k]]


if __name__ == "__main__":
    fav = FavoritesList()
    for page in ["google.com", "github.com", "google.com", "stackoverflow.com", "github.com", "google.com"]:
        fav.access(page)

    print("Top 2 favorites:")
    for url, count in fav.top(2):
        print(f"  {url} ({count} accesses)")

    fav.remove("github.com")
    print("\nAfter removing github.com:")
    for url, count in fav.top(2):
        print(f"  {url} ({count} accesses)")
