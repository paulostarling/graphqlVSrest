query_graphql = ["""
{
  user(login: "paulostarling") {
    company,
    createdAt,
    followers {
       totalCount  
    },
    following {
       totalCount  
    },
    bio,
    twitterUsername,
    updatedAt,
    url,
    repositories {
        totalCount
    }
    avatarUrl,
  }
}
""",
"""
{
  search(query: "is:public stars:>100 sort:stars-desc", type: REPOSITORY, first: 100) {
    edges {
      node {
        ... on Repository {
          name
          url
          createdAt
          releases {
            totalCount
          }
          stargazers {
             totalCount
           }
        }
      }
    }
  }
}
"""
]

query_rest = [
    """https://api.github.com/users/paulostarling""",
    """https://api.github.com/search/repositories?q=stars:%3E1&sort=stars&per_page=100""",
]