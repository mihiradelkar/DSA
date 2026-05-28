class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        # groups = defaultdict(list)
        groups = set()
        for email in emails:
            local, domain = email.split("@")
            # print(local,domain)
            if "+" in local:
                local, _ = local.split("+",1)
            local = local.replace(".","")
            # groups[domain].append(local+domain)
            groups.add(local+"@"+domain)

        # print(groups)
        return len(groups)
        