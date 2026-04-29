def find_critical_path_recursive(tasks, dependencies):
    # Komşuluk listesi oluştur (Hangi görevden hangisine gidiliyor)
    adj = {u: [] for u in tasks}
    for u, v in dependencies:
        adj[u].append(v)

    # Memoization (Daha önce hesaplanan yolları tutmak için)
    memo = {}
    path_map = {}

    def get_max_duration(u):
        # Eğer bu görev daha önce hesaplandıysa direkt döndür
        if u in memo:
            return memo[u]

        # Eğer görevin devamında başka görev yoksa (yaprak düğüm)
        if not adj[u]:
            memo[u] = tasks[u]
            path_map[u] = [u]
            return tasks[u]

        # Çocuklar (sonraki görevler) arasında en uzun yolu bul
        max_dist = 0
        best_sub_path = []

        for v in adj[u]:
            dist = get_max_duration(v)
            if dist > max_dist:
                max_dist = dist
                best_sub_path = path_map[v]

        # Mevcut görevin süresini ekle ve kaydet
        memo[u] = tasks[u] + max_dist
        path_map[u] = [u] + best_sub_path
        return memo[u]

    # Başlangıç noktalarını bul (hiçbir göreve bağımlı olmayanlar)
    starts = {u for u in tasks}
    for u, v in dependencies:
        if v in starts:
            starts.remove(v)

    # Tüm başlangıç noktalarından geçerek en uzun yolu belirle
    final_max_duration = 0
    final_path = []

    for start_node in starts:
        duration = get_max_duration(start_node)
        if duration > final_max_duration:
            final_max_duration = duration
            final_path = path_map[start_node]

    return final_max_duration, final_path


# --- Örnek Veri ---
tasks = {'A': 3, 'B': 4, 'C': 2, 'D': 5, 'E': 2}
dependencies = [('A', 'B'), ('A', 'C'), ('B', 'D'), ('C', 'D'), ('D', 'E')]

duration, path = find_critical_path_recursive(tasks, dependencies)

print(f"Toplam Süre: {duration} gün")
print(f"Kritik Yol: {' -> '.join(path)}")