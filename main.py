from rapidfuzz import process, fuzz

names = [
    "Geetha", "Gita", "Geeta", "Gitu", "Geethanjali", "Githa", "Githu", "Gituu",
    "Seetha", "Sita", "Sitha", "Seeta", "Sethu", "Sheetal",
    "Rekha", "Rukmini", "Radha", "Radhika", "Raji", "Rajini",
    "Anita", "Anitha", "Sunita", "Sunitha", "Vinita", "Vinitha",
    "Latha", "Leela", "Lalitha", "Lavanya", "Lakshmi", "Laxmi"
]

def get_best_matches(query, names, limit=5):
    results = process.extract(query, names, limit=limit, scorer=fuzz.WRatio)
    best_match = results[0]
    return best_match, results

if __name__ == "__main__":
    while True:
        query_name = input("\nEnter a name to search (or type 'quit'/'exit' to stop): ").strip()
        
        if query_name.lower() in {"quit", "exit"}:
            print(" Exiting the name matcher. Goodbye!")
            break

        best_match, matches = get_best_matches(query_name, names, limit=10)

        print("\n Input Name:", query_name)
        print(" Best Match:", best_match)
        print("\n Ranked Matches:")
        for name, score, _ in matches:
            print(f"{name} → {score}")
