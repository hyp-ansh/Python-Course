import wikipedia as wiki
query = input("What you want to search?\n-> ")
result = wiki.summary(query, sentences=2)
print(f"\n{query} :\n{result}\n")