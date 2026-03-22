def subdomain_visits(cpdomains):
    """
    # Given a list of count-paired domains like "9001 mail.google.com",
    # return visit counts for each subdomain level.
    # e.g. "mail.google.com" visits also count toward "google.com" and "com".
    """
    # 1. Dictionary to track the total visits for each subdomain
    domain_count = {}
    
    # 2. Process each count-paired domain
    for cp in cpdomains:
        # Split the number from the domain string and convert count to integer once
        count_str, dom = cp.split(" ")
        count = int(count_str)
        
        # Split the domain by its dots to get individual parts
        vals = dom.split(".")
        
        # 3. Build the subdomains from right to left (e.g., "com" -> "google.com")
        for i in range(len(vals) - 1, -1, -1):
            if i == len(vals) - 1:
                val = vals[i] 
            else:
                val = vals[i] + "." + val
                
            # 4. Add the count to our dictionary
            if val not in domain_count:
                domain_count[val] = 0
            domain_count[val] += count

    # 5. Format the results back into a list of strings
    result = []
    for d, v in domain_count.items():
        result.append(str(v) + " " + d)

    return result

# --- Runnable Example ---
input1 = ["9001 mail.google.com"]
print(subdomain_visits(input1))
# Expected: ['9001 com', '9001 google.com', '9001 mail.google.com'] 
# Note: Dictionary order might vary, which is fine!

input2 = [
    "900 google.mail.com",
    "50 yahoo.com",
    "1 intel.mail.com",
    "5 wiki.org"
]

print(subdomain_visits(input2))
# Expected: 
# ['900 google.mail.com', '901 mail.com', '951 com', '50 yahoo.com', '1 intel.mail.com', '5 wiki.org', '5 org']

"""
    Complexity Analysis:
    
    * Time Complexity: O(N * D)
      - N is the number of entries in cpdomains.
      - D is the max depth of subdomains (number of dots + 1).
      - For each entry, we split and generate all subdomain levels.
    
    * Space Complexity: O(N * D)
      - The dictionary stores up to N * D unique subdomains.
"""