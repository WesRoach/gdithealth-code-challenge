# Hiring Manager Instructions

Steps to setup this repository for each candidate.

## Step 1

Within the Github organization create a new, blank repository where the candidate will submit their Pull Request.

Example: `hiring-code-challenge-jane-doe`

## Step 2

Copy `hiring-code-challenge` to Step 1's repository:

1. Clone `https://github.com/WesRoach/hiring-code-challenge`
1. Point `hiring-code-challenge` clone remote to candidate's repository
1. Push

Example:

```bash
git clone https://github.com/WesRoach/hiring-code-challenge
cd hiring-code-challenge
git remote set-url origin https://github.com/WesRoach/hiring-code-challenge-jane-doe
git push
```

## Step 3

Within Github's UI - grant the candidate READ access ONLY to their private repository.

The candidate will need to fork the repository and submit a Pull Requst with their final solution(s).
