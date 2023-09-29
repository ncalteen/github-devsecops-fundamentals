# Environment Management

As any software project evolves over time, it will become more complex. As the
level of complexity increases, there will likely be a need to maintain different
production-like environments for purposes such as testing, QA, UAT, and more.

GitHub Environments can be used to link different deployment targets to a
repository, as well as to control a number of different features. For example,
suppose you have separate environments, `development`, `staging`, and
`production`. Each environment corresponds to a different Azure subscription. In
order to deploy to each of these, you may require different credentials.
Repository environments can be used to scope secretes, enforce deployment rules,
and more.

In this section, you will configure required approvals to ensure that specific
users approve any future changes to your site.

## Step 1: Update the Environment

When GitHub Pages is enabled and first deployed for a repository, a separate
environment named `gh-pages` is automatically created. Any deployments to your
site will use this environment. In this scenario, suppose your organization
requires human review of changes to your public documentation. Here, you will
modify environment settings to require approvals before deployments can take
place.

1. Open your repository on GitHub.com
1. Click the **Settings** tab
1. Click **Environments**
1. Click the **`gh-pages`** environment
1. Select the **Required reviewers** checkbox
1. In the new input field, enter your GitHub handle

   Feel free to enter a different user's handle and have them review the
   deployment instead!

1. Click **Save protection rules**

Now that the environment protection rule is in place, try creating a new pull
request and merging it in. In this case, the required approver(s) will get a
notification that this deployment is awaiting their review.

## Step 2: Create a Branch

1. In your local repository or codespace, update your repository and create a
   new branch

   ```bash
   git checkout main
   git pull
   git checkout -b new-feature
   ```

1. Make some changes to the site
1. In `pyproject.toml`, update the **version** field (e.g. change it from
   `0.1.0` to `0.2.0`)
1. Stage and commit your changes

   ```bash
   git add .
   git commit -m 'Updating site contents v0.2.0'
   ```

1. Push your new branch to the remote on GitHub

   ```bash
   git push -u origin new-feature
   ```

## Step 3: Create a Pull Request

1. Navigate to your repository on GitHub.com
1. Click the **Pull requests** tab
1. In the **compare** drop-down menu, select your branch (e.g. `cd-workflow`)
1. Click **Create pull request**
1. Enter a title and description for your PR
1. Click **Create pull request**

As with the last PR, feel free to have another person review and approve your
changes. Otherwise, go ahead and merge them into `main`.

1. Click the cog icon next to the **Reviewers** section and add a reviewer
1. Click **assign yourself** to assign the PR to yourself
1. (Optional) Add any labels, projects, and milestones

## Step 4: Merge

Once you're ready, you can merge your PR into `main`.

1. Click **Merge pull request**
1. Click **Confirm merge**
1. Click **Delete branch**

Once the PR is merged, the required reviewer(s) will receive an email
notification that this deployment is awaiting their review.
