def variants(symbols, depth, current_depth=0):
    if not symbols or current_depth >= depth:
        yield ''
    for item in symbols:
        sym = symbols.copy()
        sym.remove(item)
        for tail in variants(sym, depth, current_depth + 1):
            yield item + tail


n = input("Enter N: ")
print(list(variants(list(n), 1)))

