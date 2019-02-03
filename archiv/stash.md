https://forum.omz-software.com/topic/2829/git-github-workflow-in-stash/12

Here is the section of an updated git tutorial (though i can't push it because I am in the midst of removing the gittle dependencies in stash git, so dont have a fully working git)

Setting up ssh keys

In some cases, you may need or want to use ssh instead of https. This is a somewhat more reliable way of pushing, though it can be a little slower. This might also work for private repos.

With guthub, the process is facilitated by the gh command in stash:

[git_tutorial]$ gh create_key stash 
creates a key, and adds it to your github account. Note this command uses the stored github password, so you will have to create a key in your keychain, or better yet just use git push on an existing repo.

If you are using a non-github ssh, bitbucket, etc, you can create an ssh key

$ ssh-keygen -trsa -b2048
pbcopy ~/.ssh/id_rsa.pub 
creates a key, and copies the public key to the clipboard. You can then paste this into whatever you use for setting up the keys on the server.

Next, we need to add a remote to an existing repo:

[git_tutorial]$ git remote originssh ssh://git@github.com/jsbain/stash_git_tutorial.git

Now you can fetch/push,etc from originssh

[git_tutorial] git push originssh