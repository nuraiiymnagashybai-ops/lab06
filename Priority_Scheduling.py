pages = [1, 2, 3, 1, 4, 5, 1, 2, 3, 4, 5]
frames = []
frame_count = 4
page_faults = 0

print("Сұраныс | Жадтағы беттер | Page Fault")

for p in pages:
    if p not in frames:
        if len(frames) < frame_count:
            frames.append(p)
        else:
            frames.pop(0)
            frames.append(p)
        page_faults += 1
        fault = "Yes"
    else:
        fault = "No"
    print(f"   {p}     | {frames} | {fault}")

print(f"\nЖалпы бет қателері (page faults): {page_faults}")
