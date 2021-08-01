def collected_item(leg_item, key_mat):
    item = "".join([k for k, v in key_mat.items() if v >= 250])
    key_mat[item] -= 250
    return f"{leg_item[item]} obtained!"


legendary_items = {"shards": "Shadowmourne", "fragments": "Valanyr", "motes": "Dragonwrath"}
useful_items = {"shards": 0, "fragments": 0, "motes": 0}
junk_items = {}

data = input().lower().split()
while data:
    for i in range(0, len(data), 2):
        quantity = int(data[i])
        material = data[i + 1]
        if material not in useful_items:
            if material not in junk_items:
                junk_items[material] = quantity
            else:
                junk_items[material] += quantity
        else:
            useful_items[material] += quantity
        if useful_items["shards"] >= 250 or useful_items["fragments"] >= 250 or useful_items["motes"] >= 250:
            print(collected_item(legendary_items, useful_items))
            [print(f"{k}: {v}") for k, v in sorted(useful_items.items(), key=lambda x: (-x[1], x[0]))]
            [print(f"{k}: {v}") for k, v in sorted(junk_items.items(), key=lambda x: x)]
            exit()
    data = input().lower().split()