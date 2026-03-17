class Solution:
    # Questions:
    #  can one email appear more than 2 accounts?
    #  are the names unique?

    # Approach
    #  Brute Force: 
    #  [["John","johnsmith@mail.com","john_newyork@mail.com"],
    #   ["Smith","johnsmith@mail.com","john00@mail.com"],
    #   ["Mary","mary@mail.com"],
    #   ["John","johnnybravo@mail.com"]]
    #  Optimal :
    #    Union-Find on emails + email→name mapping

    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        parent = {}

        def find(x):
            if parent.setdefault(x,x) != x:
                parent[x] = find(parent[x]) # path compression Eg. 1<-2<-3  ->  2->1<-3
            return parent[x]

        def union(x,y):
            parent[find(x)]=find(y)   # merge 2 groups Eg. 1<-2  3<-4  ->  2->1->3<-4

        email_to_name = {}

        for account in accounts:
            name = account[0]
            for email in account[1:]:
                email_to_name[email] = name  # map email -> owner name
                union(email,account[1])  # union all email to first (first email will union with itself)
        # print("parent",parent)# print("email_to_name",email_to_name)

        
        # for account in accounts:
        #     name = account[0]
        #     pivot = account[1]
        #     email_to_name[pivot] = name        # only map first email → name
        #     for email in account[1:]:
        #         union(email, pivot)


        groups = defaultdict(list)  

        for email in email_to_name:
            groups[find(email)].append(email)   # Root of all common email will be same
                                                # m@m.com: [m@m.com,m1@m.com,m2@m.com]

        return [[email_to_name[root]]+sorted(emails) for root, emails in groups.items()]
