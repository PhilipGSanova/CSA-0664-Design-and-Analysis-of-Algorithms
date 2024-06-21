def split_message(message, limit):
    parts = []
    total_parts = (len(message) + limit - 1) // limit
    for i in range(total_parts):
        start = i * limit
        end = min(len(message), start + limit)
        part = message[start:end]
        parts.append(f"{part}<{i+1}/{total_parts}>")
    return parts
