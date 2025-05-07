Last login: Wed Apr 30 17:48:55 on ttys001
achintaggarwal@My-air ~ % 
achintaggarwal@My-air ~ % 
achintaggarwal@My-air ~ % 
achintaggarwal@My-air ~ % 
achintaggarwal@My-air ~ % cd Documents/GenAI/genAI_experiments 
achintaggarwal@My-air genAI_experiments % 
achintaggarwal@My-air genAI_experiments % 
achintaggarwal@My-air genAI_experiments % cd LI
cd: no such file or directory: LI
achintaggarwal@My-air genAI_experiments % mkdir LICA
achintaggarwal@My-air genAI_experiments % 
achintaggarwal@My-air genAI_experiments % 
achintaggarwal@My-air genAI_experiments % 
achintaggarwal@My-air genAI_experiments % cp ../LICA/Sarvam/pipeline.py ./LICA 
achintaggarwal@My-air genAI_experiments % 
achintaggarwal@My-air genAI_experiments % 
achintaggarwal@My-air genAI_experiments % 
achintaggarwal@My-air genAI_experiments % touch ./LICA/README.md
achintaggarwal@My-air genAI_experiments % 
achintaggarwal@My-air genAI_experiments % 
achintaggarwal@My-air genAI_experiments % 
achintaggarwal@My-air genAI_experiments % 
achintaggarwal@My-air genAI_experiments % 
achintaggarwal@My-air genAI_experiments % rm -rf LICA 
achintaggarwal@My-air genAI_experiments % 
achintaggarwal@My-air genAI_experiments % 
achintaggarwal@My-air genAI_experiments % 
achintaggarwal@My-air genAI_experiments % 
achintaggarwal@My-air genAI_experiments % 
achintaggarwal@My-air genAI_experiments % 
achintaggarwal@My-air genAI_experiments % git clone https://github.com/aashish-1990/lica-teacher-assist.git LICA              
Cloning into 'LICA'...
remote: Enumerating objects: 6273, done.
remote: Counting objects: 100% (6273/6273), done.
remote: Compressing objects: 100% (4750/4750), done.
Receiving objects:   7% (493/6273), 9.68 MiB | 298.00 KiB/s 
remote: Total 6273 (delta 1448), reused 6248 (delta 1435), pack-reused 0 (from 0)
Receiving objects: 100% (6273/6273), 33.35 MiB | 279.00 KiB/s, done.
Resolving deltas: 100% (1448/1448), done.
achintaggarwal@My-air genAI_experiments % 
achintaggarwal@My-air genAI_experiments % 
achintaggarwal@My-air genAI_experiments % 
achintaggarwal@My-air genAI_experiments % cd LICA 
achintaggarwal@My-air LICA % ls
app.py			root@164.52.193.175	venv
requirements.txt	templates
achintaggarwal@My-air LICA % git remote remove origin
achintaggarwal@My-air LICA % git remote add origin git@github.com:rsachint/LICA.git
achintaggarwal@My-air LICA % 
achintaggarwal@My-air LICA % 
achintaggarwal@My-air LICA % git push -u origin main
git@github.com: Permission denied (publickey).
fatal: Could not read from remote repository.

Please make sure you have the correct access rights
and the repository exists.
achintaggarwal@My-air LICA % 
achintaggarwal@My-air LICA % 
achintaggarwal@My-air LICA % 
achintaggarwal@My-air LICA % 
achintaggarwal@My-air LICA % 
achintaggarwal@My-air LICA % ls ~/.ssh/id_*.pub

zsh: no matches found: /Users/achintaggarwal/.ssh/id_*.pub
achintaggarwal@My-air LICA % 
achintaggarwal@My-air LICA % 
achintaggarwal@My-air LICA % ssh-keygen -t ed25519 -C "your_email@example.com"

Generating public/private ed25519 key pair.
Enter file in which to save the key (/Users/achintaggarwal/.ssh/id_ed25519): 
Enter passphrase (empty for no passphrase): 
Enter same passphrase again: 
Passphrases do not match.  Try again.
Enter passphrase (empty for no passphrase): 
Enter same passphrase again: 
Your identification has been saved in /Users/achintaggarwal/.ssh/id_ed25519
Your public key has been saved in /Users/achintaggarwal/.ssh/id_ed25519.pub
The key fingerprint is:
SHA256:Z0cHK22h04XSnH1JJxTrNMiA2YHHB6td3kcO2H9LDTo your_email@example.com
The key's randomart image is:
+--[ED25519 256]--+
|         *+=o=*oo|
|        + =B*O.+o|
|         .=o@ O..|
|         o B * B.|
|        S + E o.*|
|         o . ...o|
|               . |
|                 |
|                 |
+----[SHA256]-----+
achintaggarwal@My-air LICA % 
achintaggarwal@My-air LICA % 
achintaggarwal@My-air LICA % 
achintaggarwal@My-air LICA % eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519

Agent pid 63661
Enter passphrase for /Users/achintaggarwal/.ssh/id_ed25519: 
achintaggarwal@My-air LICA % 
achintaggarwal@My-air LICA % pbcopy < ~/.ssh/id_ed25519.pub

achintaggarwal@My-air LICA % 
achintaggarwal@My-air LICA % 
achintaggarwal@My-air LICA % 
achintaggarwal@My-air LICA % ssh -T git@github.com

Enter passphrase for key '/Users/achintaggarwal/.ssh/id_ed25519': 
Hi rsachint! You've successfully authenticated, but GitHub does not provide shell access.
achintaggarwal@My-air LICA % 
achintaggarwal@My-air LICA % 
achintaggarwal@My-air LICA % git push -u origin main
Enter passphrase for key '/Users/achintaggarwal/.ssh/id_ed25519': 
branch 'main' set up to track 'origin/main'.
Everything up-to-date
achintaggarwal@My-air LICA % 
achintaggarwal@My-air LICA % 
achintaggarwal@My-air LICA % 
achintaggarwal@My-air LICA % 
achintaggarwal@My-air LICA % 
achintaggarwal@My-air LICA %                        
achintaggarwal@My-air LICA % 
achintaggarwal@My-air LICA % cd ../
achintaggarwal@My-air genAI_experiments % 
achintaggarwal@My-air genAI_experiments % 
achintaggarwal@My-air genAI_experiments % git add lica-teacher-assist
fatal: pathspec 'lica-teacher-assist' did not match any files
achintaggarwal@My-air genAI_experiments % git add LICA               
warning: adding embedded git repository: LICA
hint: You've added another git repository inside your current repository.
hint: Clones of the outer repository will not contain the contents of
hint: the embedded repository and will not know how to obtain it.
hint: If you meant to add a submodule, use:
hint: 
hint: 	git submodule add <url> LICA
hint: 
hint: If you added this path by mistake, you can remove it from the
hint: index with:
hint: 
hint: 	git rm --cached LICA
hint: 
hint: See "git help submodule" for more information.
achintaggarwal@My-air genAI_experiments % git commit -m "Import LICA code"               
[main 87cde66] Import LICA code
 Committer: Achint Aggarwal <achintaggarwal@My-air.local>
Your name and email address were configured automatically based
on your username and hostname. Please check that they are accurate.
You can suppress this message by setting them explicitly:

    git config --global user.name "Your Name"
    git config --global user.email you@example.com

After doing this, you may fix the identity used for this commit with:

    git commit --amend --reset-author

 1 file changed, 1 insertion(+)
 create mode 160000 LICA
achintaggarwal@My-air genAI_experiments % 
achintaggarwal@My-air genAI_experiments % 
achintaggarwal@My-air genAI_experiments % git push
To https://github.com/rsachint/genAI_experiments.git
 ! [rejected]        main -> main (fetch first)
error: failed to push some refs to 'https://github.com/rsachint/genAI_experiments.git'
hint: Updates were rejected because the remote contains work that you do
hint: not have locally. This is usually caused by another repository pushing
hint: to the same ref. You may want to first integrate the remote changes
hint: (e.g., 'git pull ...') before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details.
achintaggarwal@My-air genAI_experiments % 
achintaggarwal@My-air genAI_experiments % 
achintaggarwal@My-air genAI_experiments % 
achintaggarwal@My-air genAI_experiments % git rm --cached LICA
git commit -m "Remove erroneous LICA folder entry"

rm 'LICA'
[main a491cad] Remove erroneous LICA folder entry
 Committer: Achint Aggarwal <achintaggarwal@My-air.local>
Your name and email address were configured automatically based
on your username and hostname. Please check that they are accurate.
You can suppress this message by setting them explicitly:

    git config --global user.name "Your Name"
    git config --global user.email you@example.com

After doing this, you may fix the identity used for this commit with:

    git commit --amend --reset-author

 1 file changed, 1 deletion(-)
 delete mode 160000 LICA
achintaggarwal@My-air genAI_experiments % git rm --cached LICA
git commit -m "Remove erroneous LICAc folder entry"

achintaggarwal@My-air genAI_experiments % git submodule add https://github.com/rsachint/LICA.git LICA
Adding existing repo at 'LICA' to the index
achintaggarwal@My-air genAI_experiments % 
achintaggarwal@My-air genAI_experiments % 
achintaggarwal@My-air genAI_experiments % 
achintaggarwal@My-air genAI_experiments % git commit -m "Add LICA as a submodule"
[main cf3f484] Add LICA as a submodule
 Committer: Achint Aggarwal <achintaggarwal@My-air.local>
Your name and email address were configured automatically based
on your username and hostname. Please check that they are accurate.
You can suppress this message by setting them explicitly:

    git config --global user.name "Your Name"
    git config --global user.email you@example.com

After doing this, you may fix the identity used for this commit with:

    git commit --amend --reset-author

 2 files changed, 4 insertions(+)
 create mode 100644 .gitmodules
 create mode 160000 LICA
achintaggarwal@My-air genAI_experiments % git fetch origin
git rebase origin/main

remote: Enumerating objects: 7, done.
remote: Counting objects: 100% (7/7), done.
remote: Compressing objects: 100% (4/4), done.
remote: Total 4 (delta 2), reused 0 (delta 0), pack-reused 0 (from 0)
Unpacking objects: 100% (4/4), 1.22 KiB | 208.00 KiB/s, done.
From https://github.com/rsachint/genAI_experiments
   0d2b5fd..3203aed  main       -> origin/main
error: cannot rebase: You have unstaged changes.
error: Please commit or stash them.
achintaggarwal@My-air genAI_experiments % 
achintaggarwal@My-air genAI_experiments % git commit -m "Add LICA as a submodule"
On branch main
Your branch and 'origin/main' have diverged,
and have 3 and 4 different commits each, respectively.
  (use "git pull" to merge the remote branch into yours)

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
	modified:   cv-job-matcher/matchCVToJobs.py

Untracked files:
  (use "git add <file>..." to include in what will be committed)
	.DS_Store
	cv-job-matcher/.DS_Store
	cv-job-matcher/.idea/
	stock_quarterly_guidance/

no changes added to commit (use "git add" and/or "git commit -a")
achintaggarwal@My-air genAI_experiments % 
achintaggarwal@My-air genAI_experiments %                     
achintaggarwal@My-air genAI_experiments % 
achintaggarwal@My-air genAI_experiments % 
achintaggarwal@My-air genAI_experiments % git rm --cached LICA
rm -rf LICA/.git           # delete its internal Git folder

rm 'LICA'
achintaggarwal@My-air genAI_experiments % 
achintaggarwal@My-air genAI_experiments % 
achintaggarwal@My-air genAI_experiments % 
achintaggarwal@My-air genAI_experiments % cd LIq
cd: no such file or directory: LIq
achintaggarwal@My-air genAI_experiments % cd LICA 
achintaggarwal@My-air LICA % ls
app.py			root@164.52.193.175	venv
requirements.txt	templates
achintaggarwal@My-air LICA % ls plrt
ls: plrt: No such file or directory
achintaggarwal@My-air LICA % ls -lrt
total 16
-rw-r--r--  1 achintaggarwal  staff  2377 May  7 13:30 app.py
-rw-r--r--  1 achintaggarwal  staff    68 May  7 13:30 requirements.txt
drwxr-xr-x  7 achintaggarwal  staff   224 May  7 13:30 root@164.52.193.175
drwxr-xr-x  3 achintaggarwal  staff    96 May  7 13:30 templates
drwxr-xr-x  7 achintaggarwal  staff   224 May  7 13:30 venv
achintaggarwal@My-air LICA % 
achintaggarwal@My-air LICA % 
achintaggarwal@My-air LICA % cd ../
achintaggarwal@My-air genAI_experiments % 
achintaggarwal@My-air genAI_experiments % 
achintaggarwal@My-air genAI_experiments % 
achintaggarwal@My-air genAI_experiments % git add LICA/*
git commit -m "Import LICA files as normal folder"

The following paths are ignored by one of your .gitignore files:
LICA/requirements.txt
hint: Use -f if you really want to add them.
hint: Turn this message off by running
hint: "git config advice.addIgnoredFile false"
[main c61ba51] Import LICA files as normal folder
 Committer: Achint Aggarwal <achintaggarwal@My-air.local>
Your name and email address were configured automatically based
on your username and hostname. Please check that they are accurate.
You can suppress this message by setting them explicitly:

    git config --global user.name "Your Name"
    git config --global user.email you@example.com

After doing this, you may fix the identity used for this commit with:

    git commit --amend --reset-author

 6199 files changed, 1154374 insertions(+), 1 deletion(-)
 delete mode 160000 LICA
 create mode 100644 LICA/app.py
 create mode 100644 LICA/root@164.52.193.175/.DS_Store
 create mode 100644 LICA/root@164.52.193.175/app.py
 create mode 100644 LICA/root@164.52.193.175/templates/index.html
 create mode 100644 LICA/root@164.52.193.175/venv/bin/Activate.ps1
 create mode 100644 LICA/root@164.52.193.175/venv/bin/activate
 create mode 100644 LICA/root@164.52.193.175/venv/bin/activate.csh
 create mode 100644 LICA/root@164.52.193.175/venv/bin/activate.fish
 create mode 100755 LICA/root@164.52.193.175/venv/bin/dotenv
 create mode 100755 LICA/root@164.52.193.175/venv/bin/f2py
 create mode 100755 LICA/root@164.52.193.175/venv/bin/flask
 create mode 100755 LICA/root@164.52.193.175/venv/bin/normalizer
 create mode 100755 LICA/root@164.52.193.175/venv/bin/numpy-config
 create mode 100755 LICA/root@164.52.193.175/venv/bin/pip
 create mode 100755 LICA/root@164.52.193.175/venv/bin/pip3
 create mode 100755 LICA/root@164.52.193.175/venv/bin/pip3.11
 create mode 100755 LICA/root@164.52.193.175/venv/bin/python
 create mode 100755 LICA/root@164.52.193.175/venv/bin/python3
 create mode 100755 LICA/root@164.52.193.175/venv/bin/python3.11
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/MarkupSafe-3.0.2.dist-info/INSTALLER
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/MarkupSafe-3.0.2.dist-info/METADATA
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/MarkupSafe-3.0.2.dist-info/RECORD
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/MarkupSafe-3.0.2.dist-info/WHEEL
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/__pycache__/_sounddevice.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/__pycache__/_soundfile.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/__pycache__/sounddevice.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/__pycache__/soundfile.cpython-311.pyc
 create mode 100755 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/_cffi_backend.cpython-311-darwin.so
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/_distutils_hack/__init__.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/_distutils_hack/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/_distutils_hack/__pycache__/override.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/_distutils_hack/override.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/_sounddevice.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/_sounddevice_data/__init__.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/_sounddevice_data/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/_sounddevice_data/portaudio-binaries/README.md
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/_sounddevice_data/portaudio-binaries/libportaudio.dylib
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/_soundfile.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/_soundfile_data/COPYING
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/_soundfile_data/__init__.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/_soundfile_data/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/_soundfile_data/libsndfile_arm64.dylib
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/blinker-1.9.0.dist-info/INSTALLER
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/blinker-1.9.0.dist-info/METADATA
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/blinker-1.9.0.dist-info/RECORD
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/blinker-1.9.0.dist-info/WHEEL
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/blinker/__init__.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/blinker/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/blinker/__pycache__/_utilities.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/blinker/__pycache__/base.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/blinker/_utilities.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/blinker/base.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/blinker/py.typed
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/certifi-2025.4.26.dist-info/INSTALLER
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/certifi-2025.4.26.dist-info/METADATA
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/certifi-2025.4.26.dist-info/RECORD
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/certifi-2025.4.26.dist-info/WHEEL
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/certifi-2025.4.26.dist-info/licenses/LICENSE
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/certifi/__init__.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/certifi/__main__.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/certifi/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/certifi/__pycache__/__main__.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/certifi/__pycache__/core.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/certifi/cacert.pem
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/certifi/core.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/certifi/py.typed
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/cffi-1.17.1.dist-info/INSTALLER
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/cffi-1.17.1.dist-info/LICENSE
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/cffi-1.17.1.dist-info/METADATA
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/cffi-1.17.1.dist-info/RECORD
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/cffi-1.17.1.dist-info/WHEEL
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/cffi/__init__.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/cffi/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/cffi/__pycache__/_imp_emulation.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/cffi/__pycache__/_shimmed_dist_utils.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/cffi/__pycache__/api.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/cffi/__pycache__/backend_ctypes.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/cffi/__pycache__/cffi_opcode.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/cffi/__pycache__/commontypes.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/cffi/__pycache__/cparser.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/cffi/__pycache__/error.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/cffi/__pycache__/ffiplatform.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/cffi/__pycache__/lock.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/cffi/__pycache__/model.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/cffi/__pycache__/pkgconfig.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/cffi/__pycache__/recompiler.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/cffi/__pycache__/setuptools_ext.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/cffi/__pycache__/vengine_cpy.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/cffi/__pycache__/vengine_gen.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/cffi/__pycache__/verifier.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/cffi/_cffi_errors.h
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/cffi/_cffi_include.h
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/cffi/_embedding.h
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/cffi/_imp_emulation.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/cffi/_shimmed_dist_utils.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/cffi/api.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/cffi/backend_ctypes.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/cffi/cffi_opcode.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/cffi/commontypes.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/cffi/cparser.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/cffi/error.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/cffi/ffiplatform.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/cffi/lock.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/cffi/model.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/cffi/parse_c_type.h
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/cffi/pkgconfig.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/cffi/recompiler.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/cffi/setuptools_ext.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/cffi/vengine_cpy.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/cffi/vengine_gen.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/cffi/verifier.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/charset_normalizer-3.4.2.dist-info/INSTALLER
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/charset_normalizer-3.4.2.dist-info/METADATA
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/charset_normalizer-3.4.2.dist-info/RECORD
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/charset_normalizer-3.4.2.dist-info/WHEEL
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/charset_normalizer-3.4.2.dist-info/licenses/LICENSE
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/charset_normalizer/__init__.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/charset_normalizer/__main__.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/charset_normalizer/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/charset_normalizer/__pycache__/__main__.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/charset_normalizer/__pycache__/api.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/charset_normalizer/__pycache__/cd.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/charset_normalizer/__pycache__/constant.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/charset_normalizer/__pycache__/legacy.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/charset_normalizer/__pycache__/md.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/charset_normalizer/__pycache__/models.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/charset_normalizer/__pycache__/utils.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/charset_normalizer/__pycache__/version.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/charset_normalizer/api.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/charset_normalizer/cd.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/charset_normalizer/cli/__init__.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/charset_normalizer/cli/__main__.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/charset_normalizer/cli/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/charset_normalizer/cli/__pycache__/__main__.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/charset_normalizer/constant.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/charset_normalizer/legacy.py
 create mode 100755 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/charset_normalizer/md.cpython-311-darwin.so
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/charset_normalizer/md.py
 create mode 100755 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/charset_normalizer/md__mypyc.cpython-311-darwin.so
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/charset_normalizer/models.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/charset_normalizer/py.typed
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/charset_normalizer/utils.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/charset_normalizer/version.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/click-8.1.8.dist-info/INSTALLER
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/click-8.1.8.dist-info/METADATA
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/click-8.1.8.dist-info/RECORD
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/click-8.1.8.dist-info/WHEEL
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/click/__init__.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/click/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/click/__pycache__/_compat.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/click/__pycache__/_termui_impl.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/click/__pycache__/_textwrap.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/click/__pycache__/_winconsole.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/click/__pycache__/core.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/click/__pycache__/decorators.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/click/__pycache__/exceptions.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/click/__pycache__/formatting.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/click/__pycache__/globals.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/click/__pycache__/parser.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/click/__pycache__/shell_completion.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/click/__pycache__/termui.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/click/__pycache__/testing.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/click/__pycache__/types.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/click/__pycache__/utils.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/click/_compat.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/click/_termui_impl.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/click/_textwrap.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/click/_winconsole.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/click/core.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/click/decorators.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/click/exceptions.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/click/formatting.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/click/globals.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/click/parser.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/click/py.typed
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/click/shell_completion.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/click/termui.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/click/testing.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/click/types.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/click/utils.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/distutils-precedence.pth
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/dotenv/__init__.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/dotenv/__main__.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/dotenv/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/dotenv/__pycache__/__main__.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/dotenv/__pycache__/cli.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/dotenv/__pycache__/ipython.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/dotenv/__pycache__/main.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/dotenv/__pycache__/parser.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/dotenv/__pycache__/variables.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/dotenv/__pycache__/version.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/dotenv/cli.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/dotenv/ipython.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/dotenv/main.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/dotenv/parser.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/dotenv/py.typed
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/dotenv/variables.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/dotenv/version.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/flask-3.1.0.dist-info/INSTALLER
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/flask-3.1.0.dist-info/METADATA
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/flask-3.1.0.dist-info/RECORD
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/flask-3.1.0.dist-info/REQUESTED
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/flask-3.1.0.dist-info/WHEEL
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/flask/__init__.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/flask/__main__.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/flask/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/flask/__pycache__/__main__.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/flask/__pycache__/app.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/flask/__pycache__/blueprints.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/flask/__pycache__/cli.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/flask/__pycache__/config.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/flask/__pycache__/ctx.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/flask/__pycache__/debughelpers.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/flask/__pycache__/globals.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/flask/__pycache__/helpers.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/flask/__pycache__/logging.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/flask/__pycache__/sessions.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/flask/__pycache__/signals.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/flask/__pycache__/templating.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/flask/__pycache__/testing.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/flask/__pycache__/typing.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/flask/__pycache__/views.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/flask/__pycache__/wrappers.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/flask/app.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/flask/blueprints.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/flask/cli.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/flask/config.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/flask/ctx.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/flask/debughelpers.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/flask/globals.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/flask/helpers.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/flask/json/__init__.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/flask/json/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/flask/json/__pycache__/provider.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/flask/json/__pycache__/tag.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/flask/json/provider.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/flask/json/tag.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/flask/logging.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/flask/py.typed
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/flask/sansio/README.md
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/flask/sansio/__pycache__/app.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/flask/sansio/__pycache__/blueprints.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/flask/sansio/__pycache__/scaffold.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/flask/sansio/app.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/flask/sansio/blueprints.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/flask/sansio/scaffold.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/flask/sessions.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/flask/signals.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/flask/templating.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/flask/testing.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/flask/typing.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/flask/views.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/flask/wrappers.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/idna-3.10.dist-info/INSTALLER
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/idna-3.10.dist-info/LICENSE.md
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/idna-3.10.dist-info/METADATA
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/idna-3.10.dist-info/RECORD
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/idna-3.10.dist-info/WHEEL
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/idna/__init__.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/idna/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/idna/__pycache__/codec.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/idna/__pycache__/compat.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/idna/__pycache__/core.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/idna/__pycache__/idnadata.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/idna/__pycache__/intranges.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/idna/__pycache__/package_data.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/idna/__pycache__/uts46data.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/idna/codec.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/idna/compat.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/idna/core.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/idna/idnadata.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/idna/intranges.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/idna/package_data.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/idna/py.typed
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/idna/uts46data.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/itsdangerous-2.2.0.dist-info/INSTALLER
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/itsdangerous-2.2.0.dist-info/METADATA
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/itsdangerous-2.2.0.dist-info/RECORD
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/itsdangerous-2.2.0.dist-info/WHEEL
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/itsdangerous/__init__.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/itsdangerous/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/itsdangerous/__pycache__/_json.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/itsdangerous/__pycache__/encoding.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/itsdangerous/__pycache__/exc.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/itsdangerous/__pycache__/serializer.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/itsdangerous/__pycache__/signer.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/itsdangerous/__pycache__/timed.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/itsdangerous/__pycache__/url_safe.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/itsdangerous/_json.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/itsdangerous/encoding.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/itsdangerous/exc.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/itsdangerous/py.typed
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/itsdangerous/serializer.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/itsdangerous/signer.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/itsdangerous/timed.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/itsdangerous/url_safe.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/jinja2-3.1.6.dist-info/INSTALLER
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/jinja2-3.1.6.dist-info/METADATA
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/jinja2-3.1.6.dist-info/RECORD
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/jinja2-3.1.6.dist-info/WHEEL
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/jinja2/__init__.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/jinja2/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/jinja2/__pycache__/_identifier.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/jinja2/__pycache__/async_utils.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/jinja2/__pycache__/bccache.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/jinja2/__pycache__/compiler.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/jinja2/__pycache__/constants.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/jinja2/__pycache__/debug.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/jinja2/__pycache__/defaults.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/jinja2/__pycache__/environment.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/jinja2/__pycache__/exceptions.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/jinja2/__pycache__/ext.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/jinja2/__pycache__/filters.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/jinja2/__pycache__/idtracking.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/jinja2/__pycache__/lexer.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/jinja2/__pycache__/loaders.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/jinja2/__pycache__/meta.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/jinja2/__pycache__/nativetypes.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/jinja2/__pycache__/nodes.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/jinja2/__pycache__/optimizer.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/jinja2/__pycache__/parser.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/jinja2/__pycache__/runtime.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/jinja2/__pycache__/sandbox.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/jinja2/__pycache__/tests.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/jinja2/__pycache__/utils.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/jinja2/__pycache__/visitor.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/jinja2/_identifier.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/jinja2/async_utils.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/jinja2/bccache.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/jinja2/compiler.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/jinja2/constants.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/jinja2/debug.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/jinja2/defaults.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/jinja2/environment.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/jinja2/exceptions.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/jinja2/ext.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/jinja2/filters.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/jinja2/idtracking.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/jinja2/lexer.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/jinja2/loaders.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/jinja2/meta.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/jinja2/nativetypes.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/jinja2/nodes.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/jinja2/optimizer.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/jinja2/parser.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/jinja2/py.typed
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/jinja2/runtime.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/jinja2/sandbox.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/jinja2/tests.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/jinja2/utils.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/jinja2/visitor.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/markupsafe/__init__.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/markupsafe/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/markupsafe/__pycache__/_native.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/markupsafe/_native.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/markupsafe/_speedups.c
 create mode 100755 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/markupsafe/_speedups.cpython-311-darwin.so
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/markupsafe/_speedups.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/markupsafe/py.typed
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy-2.2.5.dist-info/INSTALLER
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy-2.2.5.dist-info/METADATA
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy-2.2.5.dist-info/RECORD
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy-2.2.5.dist-info/WHEEL
 create mode 100755 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/.dylibs/libgcc_s.1.1.dylib
 create mode 100755 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/.dylibs/libgfortran.5.dylib
 create mode 100755 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/.dylibs/libquadmath.0.dylib
 create mode 100755 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/.dylibs/libscipy_openblas64_.dylib
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/__config__.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/__config__.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/__init__.cython-30.pxd
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/__init__.pxd
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/__init__.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/__init__.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/__pycache__/__config__.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/__pycache__/_array_api_info.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/__pycache__/_configtool.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/__pycache__/_distributor_init.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/__pycache__/_expired_attrs_2_0.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/__pycache__/_globals.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/__pycache__/_pytesttester.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/__pycache__/conftest.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/__pycache__/ctypeslib.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/__pycache__/dtypes.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/__pycache__/exceptions.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/__pycache__/matlib.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/__pycache__/version.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_array_api_info.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_array_api_info.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_configtool.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_configtool.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/__init__.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/__init__.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/__pycache__/_add_newdocs.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/__pycache__/_add_newdocs_scalars.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/__pycache__/_asarray.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/__pycache__/_dtype.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/__pycache__/_dtype_ctypes.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/__pycache__/_exceptions.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/__pycache__/_internal.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/__pycache__/_machar.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/__pycache__/_methods.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/__pycache__/_string_helpers.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/__pycache__/_type_aliases.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/__pycache__/_ufunc_config.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/__pycache__/arrayprint.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/__pycache__/cversions.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/__pycache__/defchararray.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/__pycache__/einsumfunc.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/__pycache__/fromnumeric.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/__pycache__/function_base.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/__pycache__/getlimits.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/__pycache__/memmap.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/__pycache__/multiarray.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/__pycache__/numeric.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/__pycache__/numerictypes.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/__pycache__/overrides.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/__pycache__/printoptions.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/__pycache__/records.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/__pycache__/shape_base.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/__pycache__/strings.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/__pycache__/umath.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/_add_newdocs.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/_add_newdocs.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/_add_newdocs_scalars.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/_add_newdocs_scalars.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/_asarray.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/_asarray.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/_dtype.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/_dtype.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/_dtype_ctypes.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/_dtype_ctypes.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/_exceptions.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/_exceptions.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/_internal.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/_internal.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/_machar.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/_machar.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/_methods.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/_methods.pyi
 create mode 100755 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/_multiarray_tests.cpython-311-darwin.so
 create mode 100755 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/_multiarray_umath.cpython-311-darwin.so
 create mode 100755 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/_operand_flag_tests.cpython-311-darwin.so
 create mode 100755 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/_rational_tests.cpython-311-darwin.so
 create mode 100755 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/_simd.cpython-311-darwin.so
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/_simd.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/_string_helpers.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/_string_helpers.pyi
 create mode 100755 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/_struct_ufunc_tests.cpython-311-darwin.so
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/_type_aliases.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/_type_aliases.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/_ufunc_config.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/_ufunc_config.pyi
 create mode 100755 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/_umath_tests.cpython-311-darwin.so
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/arrayprint.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/arrayprint.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/cversions.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/defchararray.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/defchararray.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/einsumfunc.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/einsumfunc.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/fromnumeric.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/fromnumeric.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/function_base.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/function_base.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/getlimits.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/getlimits.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/include/numpy/__multiarray_api.c
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/include/numpy/__multiarray_api.h
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/include/numpy/__ufunc_api.c
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/include/numpy/__ufunc_api.h
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/include/numpy/_neighborhood_iterator_imp.h
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/include/numpy/_numpyconfig.h
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/include/numpy/_public_dtype_api_table.h
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/include/numpy/arrayobject.h
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/include/numpy/arrayscalars.h
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/include/numpy/dtype_api.h
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/include/numpy/halffloat.h
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/include/numpy/ndarrayobject.h
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/include/numpy/ndarraytypes.h
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/include/numpy/npy_1_7_deprecated_api.h
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/include/numpy/npy_2_compat.h
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/include/numpy/npy_2_complexcompat.h
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/include/numpy/npy_3kcompat.h
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/include/numpy/npy_common.h
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/include/numpy/npy_cpu.h
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/include/numpy/npy_endian.h
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/include/numpy/npy_math.h
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/include/numpy/npy_no_deprecated_api.h
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/include/numpy/npy_os.h
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/include/numpy/numpyconfig.h
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/include/numpy/random/bitgen.h
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/include/numpy/random/distributions.h
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/include/numpy/random/libdivide.h
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/include/numpy/ufuncobject.h
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/include/numpy/utils.h
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/lib/libnpymath.a
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/lib/npy-pkg-config/mlib.ini
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/lib/npy-pkg-config/npymath.ini
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/lib/pkgconfig/numpy.pc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/memmap.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/memmap.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/multiarray.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/multiarray.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/numeric.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/numeric.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/numerictypes.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/numerictypes.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/overrides.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/overrides.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/printoptions.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/printoptions.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/records.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/records.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/shape_base.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/shape_base.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/strings.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/strings.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/tests/__pycache__/_locales.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/tests/__pycache__/_natype.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/tests/__pycache__/test__exceptions.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/tests/__pycache__/test_abc.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/tests/__pycache__/test_api.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/tests/__pycache__/test_argparse.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/tests/__pycache__/test_array_api_info.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/tests/__pycache__/test_array_coercion.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/tests/__pycache__/test_array_interface.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/tests/__pycache__/test_arraymethod.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/tests/__pycache__/test_arrayobject.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/tests/__pycache__/test_arrayprint.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/tests/__pycache__/test_casting_floatingpoint_errors.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/tests/__pycache__/test_casting_unittests.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/tests/__pycache__/test_conversion_utils.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/tests/__pycache__/test_cpu_dispatcher.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/tests/__pycache__/test_cpu_features.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/tests/__pycache__/test_custom_dtypes.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/tests/__pycache__/test_cython.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/tests/__pycache__/test_datetime.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/tests/__pycache__/test_defchararray.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/tests/__pycache__/test_deprecations.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/tests/__pycache__/test_dlpack.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/tests/__pycache__/test_dtype.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/tests/__pycache__/test_einsum.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/tests/__pycache__/test_errstate.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/tests/__pycache__/test_extint128.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/tests/__pycache__/test_function_base.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/tests/__pycache__/test_getlimits.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/tests/__pycache__/test_half.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/tests/__pycache__/test_hashtable.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/tests/__pycache__/test_indexerrors.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/tests/__pycache__/test_indexing.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/tests/__pycache__/test_item_selection.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/tests/__pycache__/test_limited_api.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/tests/__pycache__/test_longdouble.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/tests/__pycache__/test_machar.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/tests/__pycache__/test_mem_overlap.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/tests/__pycache__/test_mem_policy.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/tests/__pycache__/test_memmap.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/tests/__pycache__/test_multiarray.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/tests/__pycache__/test_multithreading.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/tests/__pycache__/test_nditer.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/tests/__pycache__/test_nep50_promotions.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/tests/__pycache__/test_numeric.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/tests/__pycache__/test_numerictypes.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/tests/__pycache__/test_overrides.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/tests/__pycache__/test_print.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/tests/__pycache__/test_protocols.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/tests/__pycache__/test_records.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/tests/__pycache__/test_regression.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/tests/__pycache__/test_scalar_ctors.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/tests/__pycache__/test_scalar_methods.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/tests/__pycache__/test_scalarbuffer.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/tests/__pycache__/test_scalarinherit.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/tests/__pycache__/test_scalarmath.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/tests/__pycache__/test_scalarprint.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/tests/__pycache__/test_shape_base.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/tests/__pycache__/test_simd.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/tests/__pycache__/test_simd_module.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/tests/__pycache__/test_stringdtype.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/tests/__pycache__/test_strings.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/tests/__pycache__/test_ufunc.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/tests/__pycache__/test_umath.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/tests/__pycache__/test_umath_accuracy.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/tests/__pycache__/test_umath_complex.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/tests/__pycache__/test_unicode.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/tests/_locales.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/tests/_natype.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/tests/data/astype_copy.pkl
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/tests/data/generate_umath_validation_data.cpp
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/tests/data/recarray_from_file.fits
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/tests/data/umath-validation-set-arccos.csv
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/tests/data/umath-validation-set-arccosh.csv
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/tests/data/umath-validation-set-arcsin.csv
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/tests/data/umath-validation-set-arcsinh.csv
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/tests/data/umath-validation-set-arctan.csv
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/tests/data/umath-validation-set-arctanh.csv
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/tests/data/umath-validation-set-cbrt.csv
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/tests/data/umath-validation-set-cos.csv
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/tests/data/umath-validation-set-cosh.csv
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/tests/data/umath-validation-set-exp.csv
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/tests/data/umath-validation-set-exp2.csv
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/tests/data/umath-validation-set-expm1.csv
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/tests/data/umath-validation-set-log.csv
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/tests/data/umath-validation-set-log10.csv
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/tests/data/umath-validation-set-log1p.csv
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/tests/data/umath-validation-set-log2.csv
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/tests/data/umath-validation-set-sin.csv
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/tests/data/umath-validation-set-sinh.csv
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/tests/data/umath-validation-set-tan.csv
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/tests/data/umath-validation-set-tanh.csv
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/tests/examples/cython/__pycache__/setup.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/tests/examples/cython/checks.pyx
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/tests/examples/cython/meson.build
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/tests/examples/cython/setup.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/tests/examples/limited_api/__pycache__/setup.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/tests/examples/limited_api/limited_api1.c
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/tests/examples/limited_api/limited_api2.pyx
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/tests/examples/limited_api/limited_api_latest.c
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/tests/examples/limited_api/meson.build
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/tests/examples/limited_api/setup.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/tests/test__exceptions.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/tests/test_abc.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/tests/test_api.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/tests/test_argparse.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/tests/test_array_api_info.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/tests/test_array_coercion.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/tests/test_array_interface.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/tests/test_arraymethod.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/tests/test_arrayobject.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/tests/test_arrayprint.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/tests/test_casting_floatingpoint_errors.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/tests/test_casting_unittests.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/tests/test_conversion_utils.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/tests/test_cpu_dispatcher.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/tests/test_cpu_features.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/tests/test_custom_dtypes.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/tests/test_cython.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/tests/test_datetime.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/tests/test_defchararray.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/tests/test_deprecations.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/tests/test_dlpack.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/tests/test_dtype.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/tests/test_einsum.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/tests/test_errstate.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/tests/test_extint128.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/tests/test_function_base.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/tests/test_getlimits.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/tests/test_half.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/tests/test_hashtable.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/tests/test_indexerrors.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/tests/test_indexing.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/tests/test_item_selection.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/tests/test_limited_api.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/tests/test_longdouble.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/tests/test_machar.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/tests/test_mem_overlap.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/tests/test_mem_policy.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/tests/test_memmap.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/tests/test_multiarray.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/tests/test_multithreading.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/tests/test_nditer.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/tests/test_nep50_promotions.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/tests/test_numeric.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/tests/test_numerictypes.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/tests/test_overrides.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/tests/test_print.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/tests/test_protocols.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/tests/test_records.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/tests/test_regression.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/tests/test_scalar_ctors.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/tests/test_scalar_methods.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/tests/test_scalarbuffer.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/tests/test_scalarinherit.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/tests/test_scalarmath.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/tests/test_scalarprint.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/tests/test_shape_base.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/tests/test_simd.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/tests/test_simd_module.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/tests/test_stringdtype.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/tests/test_strings.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/tests/test_ufunc.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/tests/test_umath.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/tests/test_umath_accuracy.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/tests/test_umath_complex.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/tests/test_unicode.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/umath.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_core/umath.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_distributor_init.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_distributor_init.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_expired_attrs_2_0.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_expired_attrs_2_0.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_globals.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_globals.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_pyinstaller/__init__.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_pyinstaller/__init__.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_pyinstaller/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_pyinstaller/__pycache__/hook-numpy.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_pyinstaller/hook-numpy.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_pyinstaller/hook-numpy.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_pyinstaller/tests/__init__.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_pyinstaller/tests/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_pyinstaller/tests/__pycache__/pyinstaller-smoke.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_pyinstaller/tests/__pycache__/test_pyinstaller.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_pyinstaller/tests/pyinstaller-smoke.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_pyinstaller/tests/test_pyinstaller.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_pytesttester.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_pytesttester.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_typing/__init__.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_typing/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_typing/__pycache__/_add_docstring.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_typing/__pycache__/_array_like.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_typing/__pycache__/_char_codes.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_typing/__pycache__/_dtype_like.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_typing/__pycache__/_extended_precision.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_typing/__pycache__/_nbit.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_typing/__pycache__/_nbit_base.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_typing/__pycache__/_nested_sequence.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_typing/__pycache__/_scalars.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_typing/__pycache__/_shape.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_typing/__pycache__/_ufunc.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_typing/_add_docstring.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_typing/_array_like.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_typing/_callable.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_typing/_char_codes.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_typing/_dtype_like.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_typing/_extended_precision.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_typing/_nbit.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_typing/_nbit_base.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_typing/_nested_sequence.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_typing/_scalars.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_typing/_shape.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_typing/_ufunc.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_typing/_ufunc.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_utils/__init__.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_utils/__init__.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_utils/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_utils/__pycache__/_convertions.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_utils/__pycache__/_inspect.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_utils/__pycache__/_pep440.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_utils/_convertions.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_utils/_convertions.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_utils/_inspect.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_utils/_inspect.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_utils/_pep440.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/_utils/_pep440.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/char/__init__.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/char/__init__.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/char/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/compat/__init__.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/compat/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/compat/__pycache__/py3k.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/compat/py3k.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/compat/tests/__init__.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/compat/tests/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/conftest.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/core/__init__.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/core/__init__.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/core/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/core/__pycache__/_dtype.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/core/__pycache__/_dtype_ctypes.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/core/__pycache__/_internal.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/core/__pycache__/_multiarray_umath.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/core/__pycache__/_utils.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/core/__pycache__/arrayprint.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/core/__pycache__/defchararray.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/core/__pycache__/einsumfunc.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/core/__pycache__/fromnumeric.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/core/__pycache__/function_base.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/core/__pycache__/getlimits.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/core/__pycache__/multiarray.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/core/__pycache__/numeric.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/core/__pycache__/numerictypes.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/core/__pycache__/overrides.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/core/__pycache__/records.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/core/__pycache__/shape_base.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/core/__pycache__/umath.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/core/_dtype.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/core/_dtype.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/core/_dtype_ctypes.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/core/_dtype_ctypes.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/core/_internal.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/core/_multiarray_umath.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/core/_utils.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/core/arrayprint.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/core/defchararray.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/core/einsumfunc.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/core/fromnumeric.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/core/function_base.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/core/getlimits.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/core/multiarray.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/core/numeric.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/core/numerictypes.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/core/overrides.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/core/overrides.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/core/records.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/core/shape_base.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/core/umath.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/ctypeslib.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/ctypeslib.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/distutils/__init__.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/distutils/__init__.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/distutils/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/distutils/__pycache__/_shell_utils.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/distutils/__pycache__/armccompiler.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/distutils/__pycache__/ccompiler.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/distutils/__pycache__/ccompiler_opt.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/distutils/__pycache__/conv_template.cpython-310.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/distutils/__pycache__/conv_template.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/distutils/__pycache__/core.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/distutils/__pycache__/cpuinfo.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/distutils/__pycache__/exec_command.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/distutils/__pycache__/extension.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/distutils/__pycache__/from_template.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/distutils/__pycache__/fujitsuccompiler.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/distutils/__pycache__/intelccompiler.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/distutils/__pycache__/lib2def.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/distutils/__pycache__/line_endings.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/distutils/__pycache__/log.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/distutils/__pycache__/mingw32ccompiler.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/distutils/__pycache__/misc_util.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/distutils/__pycache__/msvc9compiler.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/distutils/__pycache__/msvccompiler.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/distutils/__pycache__/npy_pkg_config.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/distutils/__pycache__/numpy_distribution.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/distutils/__pycache__/pathccompiler.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/distutils/__pycache__/system_info.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/distutils/__pycache__/unixccompiler.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/distutils/_shell_utils.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/distutils/armccompiler.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/distutils/ccompiler.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/distutils/ccompiler_opt.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/distutils/checks/cpu_asimd.c
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/distutils/checks/cpu_asimddp.c
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/distutils/checks/cpu_asimdfhm.c
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/distutils/checks/cpu_asimdhp.c
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/distutils/checks/cpu_avx.c
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/distutils/checks/cpu_avx2.c
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/distutils/checks/cpu_avx512_clx.c
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/distutils/checks/cpu_avx512_cnl.c
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/distutils/checks/cpu_avx512_icl.c
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/distutils/checks/cpu_avx512_knl.c
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/distutils/checks/cpu_avx512_knm.c
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/distutils/checks/cpu_avx512_skx.c
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/distutils/checks/cpu_avx512_spr.c
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/distutils/checks/cpu_avx512cd.c
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/distutils/checks/cpu_avx512f.c
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/distutils/checks/cpu_f16c.c
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/distutils/checks/cpu_fma3.c
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/distutils/checks/cpu_fma4.c
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/distutils/checks/cpu_neon.c
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/distutils/checks/cpu_neon_fp16.c
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/distutils/checks/cpu_neon_vfpv4.c
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/distutils/checks/cpu_popcnt.c
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/distutils/checks/cpu_rvv.c
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/distutils/checks/cpu_sse.c
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/distutils/checks/cpu_sse2.c
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/distutils/checks/cpu_sse3.c
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/distutils/checks/cpu_sse41.c
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/distutils/checks/cpu_sse42.c
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/distutils/checks/cpu_ssse3.c
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/distutils/checks/cpu_sve.c
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/distutils/checks/cpu_vsx.c
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/distutils/checks/cpu_vsx2.c
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/distutils/checks/cpu_vsx3.c
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/distutils/checks/cpu_vsx4.c
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/distutils/checks/cpu_vx.c
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/distutils/checks/cpu_vxe.c
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/distutils/checks/cpu_vxe2.c
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/distutils/checks/cpu_xop.c
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/distutils/checks/extra_avx512bw_mask.c
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/distutils/checks/extra_avx512dq_mask.c
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/distutils/checks/extra_avx512f_reduce.c
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/distutils/checks/extra_vsx3_half_double.c
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/distutils/checks/extra_vsx4_mma.c
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/distutils/checks/extra_vsx_asm.c
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/distutils/checks/test_flags.c
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/distutils/command/__init__.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/distutils/command/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/distutils/command/__pycache__/autodist.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/distutils/command/__pycache__/bdist_rpm.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/distutils/command/__pycache__/build.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/distutils/command/__pycache__/build_clib.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/distutils/command/__pycache__/build_ext.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/distutils/command/__pycache__/build_py.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/distutils/command/__pycache__/build_scripts.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/distutils/command/__pycache__/build_src.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/distutils/command/__pycache__/config.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/distutils/command/__pycache__/config_compiler.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/distutils/command/__pycache__/develop.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/distutils/command/__pycache__/egg_info.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/distutils/command/__pycache__/install.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/distutils/command/__pycache__/install_clib.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/distutils/command/__pycache__/install_data.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/distutils/command/__pycache__/install_headers.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/distutils/command/__pycache__/sdist.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/distutils/command/autodist.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/distutils/command/bdist_rpm.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/distutils/command/build.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/distutils/command/build_clib.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/distutils/command/build_ext.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/distutils/command/build_py.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/distutils/command/build_scripts.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/distutils/command/build_src.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/distutils/command/config.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/distutils/command/config_compiler.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/distutils/command/develop.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/distutils/command/egg_info.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/distutils/command/install.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/distutils/command/install_clib.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/distutils/command/install_data.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/distutils/command/install_headers.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/distutils/command/sdist.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/distutils/conv_template.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/distutils/core.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/distutils/cpuinfo.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/distutils/exec_command.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/distutils/extension.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/distutils/fcompiler/__init__.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/distutils/fcompiler/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/distutils/fcompiler/__pycache__/absoft.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/distutils/fcompiler/__pycache__/arm.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/distutils/fcompiler/__pycache__/compaq.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/distutils/fcompiler/__pycache__/environment.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/distutils/fcompiler/__pycache__/fujitsu.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/distutils/fcompiler/__pycache__/g95.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/distutils/fcompiler/__pycache__/gnu.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/distutils/fcompiler/__pycache__/hpux.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/distutils/fcompiler/__pycache__/ibm.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/distutils/fcompiler/__pycache__/intel.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/distutils/fcompiler/__pycache__/lahey.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/distutils/fcompiler/__pycache__/mips.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/distutils/fcompiler/__pycache__/nag.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/distutils/fcompiler/__pycache__/none.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/distutils/fcompiler/__pycache__/nv.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/distutils/fcompiler/__pycache__/pathf95.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/distutils/fcompiler/__pycache__/pg.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/distutils/fcompiler/__pycache__/sun.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/distutils/fcompiler/__pycache__/vast.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/distutils/fcompiler/absoft.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/distutils/fcompiler/arm.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/distutils/fcompiler/compaq.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/distutils/fcompiler/environment.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/distutils/fcompiler/fujitsu.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/distutils/fcompiler/g95.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/distutils/fcompiler/gnu.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/distutils/fcompiler/hpux.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/distutils/fcompiler/ibm.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/distutils/fcompiler/intel.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/distutils/fcompiler/lahey.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/distutils/fcompiler/mips.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/distutils/fcompiler/nag.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/distutils/fcompiler/none.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/distutils/fcompiler/nv.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/distutils/fcompiler/pathf95.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/distutils/fcompiler/pg.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/distutils/fcompiler/sun.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/distutils/fcompiler/vast.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/distutils/from_template.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/distutils/fujitsuccompiler.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/distutils/intelccompiler.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/distutils/lib2def.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/distutils/line_endings.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/distutils/log.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/distutils/mingw/gfortran_vs2003_hack.c
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/distutils/mingw32ccompiler.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/distutils/misc_util.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/distutils/msvc9compiler.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/distutils/msvccompiler.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/distutils/npy_pkg_config.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/distutils/numpy_distribution.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/distutils/pathccompiler.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/distutils/system_info.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/distutils/tests/__init__.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/distutils/tests/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/distutils/tests/__pycache__/test_build_ext.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/distutils/tests/__pycache__/test_ccompiler_opt.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/distutils/tests/__pycache__/test_ccompiler_opt_conf.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/distutils/tests/__pycache__/test_exec_command.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/distutils/tests/__pycache__/test_fcompiler.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/distutils/tests/__pycache__/test_fcompiler_gnu.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/distutils/tests/__pycache__/test_fcompiler_intel.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/distutils/tests/__pycache__/test_fcompiler_nagfor.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/distutils/tests/__pycache__/test_from_template.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/distutils/tests/__pycache__/test_log.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/distutils/tests/__pycache__/test_mingw32ccompiler.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/distutils/tests/__pycache__/test_misc_util.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/distutils/tests/__pycache__/test_npy_pkg_config.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/distutils/tests/__pycache__/test_shell_utils.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/distutils/tests/__pycache__/test_system_info.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/distutils/tests/__pycache__/utilities.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/distutils/tests/test_build_ext.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/distutils/tests/test_ccompiler_opt.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/distutils/tests/test_ccompiler_opt_conf.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/distutils/tests/test_exec_command.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/distutils/tests/test_fcompiler.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/distutils/tests/test_fcompiler_gnu.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/distutils/tests/test_fcompiler_intel.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/distutils/tests/test_fcompiler_nagfor.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/distutils/tests/test_from_template.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/distutils/tests/test_log.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/distutils/tests/test_mingw32ccompiler.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/distutils/tests/test_misc_util.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/distutils/tests/test_npy_pkg_config.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/distutils/tests/test_shell_utils.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/distutils/tests/test_system_info.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/distutils/tests/utilities.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/distutils/unixccompiler.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/doc/__pycache__/ufuncs.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/doc/ufuncs.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/dtypes.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/dtypes.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/exceptions.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/exceptions.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/f2py/__init__.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/f2py/__init__.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/f2py/__main__.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/f2py/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/f2py/__pycache__/__main__.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/f2py/__pycache__/__version__.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/f2py/__pycache__/_isocbind.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/f2py/__pycache__/_src_pyf.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/f2py/__pycache__/auxfuncs.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/f2py/__pycache__/capi_maps.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/f2py/__pycache__/cb_rules.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/f2py/__pycache__/cfuncs.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/f2py/__pycache__/common_rules.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/f2py/__pycache__/crackfortran.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/f2py/__pycache__/diagnose.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/f2py/__pycache__/f2py2e.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/f2py/__pycache__/f90mod_rules.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/f2py/__pycache__/func2subr.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/f2py/__pycache__/rules.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/f2py/__pycache__/symbolic.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/f2py/__pycache__/use_rules.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/f2py/__version__.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/f2py/_backends/__init__.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/f2py/_backends/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/f2py/_backends/__pycache__/_backend.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/f2py/_backends/__pycache__/_distutils.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/f2py/_backends/__pycache__/_meson.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/f2py/_backends/_backend.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/f2py/_backends/_distutils.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/f2py/_backends/_meson.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/f2py/_backends/meson.build.template
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/f2py/_isocbind.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/f2py/_src_pyf.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/f2py/auxfuncs.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/f2py/capi_maps.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/f2py/cb_rules.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/f2py/cfuncs.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/f2py/common_rules.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/f2py/crackfortran.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/f2py/diagnose.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/f2py/f2py2e.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/f2py/f90mod_rules.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/f2py/func2subr.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/f2py/rules.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/f2py/setup.cfg
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/f2py/src/fortranobject.c
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/f2py/src/fortranobject.h
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/f2py/symbolic.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/f2py/tests/__init__.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/f2py/tests/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/f2py/tests/__pycache__/test_abstract_interface.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/f2py/tests/__pycache__/test_array_from_pyobj.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/f2py/tests/__pycache__/test_assumed_shape.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/f2py/tests/__pycache__/test_block_docstring.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/f2py/tests/__pycache__/test_callback.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/f2py/tests/__pycache__/test_character.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/f2py/tests/__pycache__/test_common.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/f2py/tests/__pycache__/test_crackfortran.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/f2py/tests/__pycache__/test_data.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/f2py/tests/__pycache__/test_docs.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/f2py/tests/__pycache__/test_f2cmap.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/f2py/tests/__pycache__/test_f2py2e.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/f2py/tests/__pycache__/test_isoc.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/f2py/tests/__pycache__/test_kind.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/f2py/tests/__pycache__/test_mixed.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/f2py/tests/__pycache__/test_modules.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/f2py/tests/__pycache__/test_parameter.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/f2py/tests/__pycache__/test_pyf_src.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/f2py/tests/__pycache__/test_quoted_character.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/f2py/tests/__pycache__/test_regression.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/f2py/tests/__pycache__/test_return_character.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/f2py/tests/__pycache__/test_return_complex.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/f2py/tests/__pycache__/test_return_integer.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/f2py/tests/__pycache__/test_return_logical.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/f2py/tests/__pycache__/test_return_real.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/f2py/tests/__pycache__/test_routines.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/f2py/tests/__pycache__/test_semicolon_split.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/f2py/tests/__pycache__/test_size.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/f2py/tests/__pycache__/test_string.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/f2py/tests/__pycache__/test_symbolic.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/f2py/tests/__pycache__/test_value_attrspec.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/f2py/tests/__pycache__/util.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/f2py/tests/src/abstract_interface/foo.f90
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/f2py/tests/src/abstract_interface/gh18403_mod.f90
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/f2py/tests/src/array_from_pyobj/wrapmodule.c
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/f2py/tests/src/assumed_shape/.f2py_f2cmap
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/f2py/tests/src/assumed_shape/foo_free.f90
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/f2py/tests/src/assumed_shape/foo_mod.f90
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/f2py/tests/src/assumed_shape/foo_use.f90
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/f2py/tests/src/assumed_shape/precision.f90
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/f2py/tests/src/block_docstring/foo.f
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/f2py/tests/src/callback/foo.f
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/f2py/tests/src/callback/gh17797.f90
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/f2py/tests/src/callback/gh18335.f90
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/f2py/tests/src/callback/gh25211.f
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/f2py/tests/src/callback/gh25211.pyf
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/f2py/tests/src/callback/gh26681.f90
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/f2py/tests/src/cli/gh_22819.pyf
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/f2py/tests/src/cli/hi77.f
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/f2py/tests/src/cli/hiworld.f90
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/f2py/tests/src/common/block.f
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/f2py/tests/src/common/gh19161.f90
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/f2py/tests/src/crackfortran/accesstype.f90
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/f2py/tests/src/crackfortran/common_with_division.f
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/f2py/tests/src/crackfortran/data_common.f
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/f2py/tests/src/crackfortran/data_multiplier.f
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/f2py/tests/src/crackfortran/data_stmts.f90
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/f2py/tests/src/crackfortran/data_with_comments.f
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/f2py/tests/src/crackfortran/foo_deps.f90
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/f2py/tests/src/crackfortran/gh15035.f
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/f2py/tests/src/crackfortran/gh17859.f
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/f2py/tests/src/crackfortran/gh22648.pyf
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/f2py/tests/src/crackfortran/gh23533.f
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/f2py/tests/src/crackfortran/gh23598.f90
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/f2py/tests/src/crackfortran/gh23598Warn.f90
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/f2py/tests/src/crackfortran/gh23879.f90
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/f2py/tests/src/crackfortran/gh27697.f90
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/f2py/tests/src/crackfortran/gh2848.f90
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/f2py/tests/src/crackfortran/operators.f90
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/f2py/tests/src/crackfortran/privatemod.f90
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/f2py/tests/src/crackfortran/publicmod.f90
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/f2py/tests/src/crackfortran/pubprivmod.f90
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/f2py/tests/src/crackfortran/unicode_comment.f90
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/f2py/tests/src/f2cmap/.f2py_f2cmap
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/f2py/tests/src/f2cmap/isoFortranEnvMap.f90
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/f2py/tests/src/isocintrin/isoCtests.f90
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/f2py/tests/src/kind/foo.f90
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/f2py/tests/src/mixed/foo.f
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/f2py/tests/src/mixed/foo_fixed.f90
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/f2py/tests/src/mixed/foo_free.f90
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/f2py/tests/src/modules/gh25337/data.f90
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/f2py/tests/src/modules/gh25337/use_data.f90
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/f2py/tests/src/modules/gh26920/two_mods_with_no_public_entities.f90
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/f2py/tests/src/modules/gh26920/two_mods_with_one_public_routine.f90
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/f2py/tests/src/modules/module_data_docstring.f90
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/f2py/tests/src/modules/use_modules.f90
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/f2py/tests/src/negative_bounds/issue_20853.f90
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/f2py/tests/src/parameter/constant_array.f90
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/f2py/tests/src/parameter/constant_both.f90
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/f2py/tests/src/parameter/constant_compound.f90
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/f2py/tests/src/parameter/constant_integer.f90
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/f2py/tests/src/parameter/constant_non_compound.f90
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/f2py/tests/src/parameter/constant_real.f90
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/f2py/tests/src/quoted_character/foo.f
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/f2py/tests/src/regression/AB.inc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/f2py/tests/src/regression/assignOnlyModule.f90
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/f2py/tests/src/regression/datonly.f90
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/f2py/tests/src/regression/f77comments.f
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/f2py/tests/src/regression/f77fixedform.f95
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/f2py/tests/src/regression/f90continuation.f90
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/f2py/tests/src/regression/incfile.f90
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/f2py/tests/src/regression/inout.f90
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/f2py/tests/src/regression/lower_f2py_fortran.f90
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/f2py/tests/src/return_character/foo77.f
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/f2py/tests/src/return_character/foo90.f90
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/f2py/tests/src/return_complex/foo77.f
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/f2py/tests/src/return_complex/foo90.f90
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/f2py/tests/src/return_integer/foo77.f
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/f2py/tests/src/return_integer/foo90.f90
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/f2py/tests/src/return_logical/foo77.f
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/f2py/tests/src/return_logical/foo90.f90
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/f2py/tests/src/return_real/foo77.f
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/f2py/tests/src/return_real/foo90.f90
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/f2py/tests/src/routines/funcfortranname.f
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/f2py/tests/src/routines/funcfortranname.pyf
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/f2py/tests/src/routines/subrout.f
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/f2py/tests/src/routines/subrout.pyf
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/f2py/tests/src/size/foo.f90
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/f2py/tests/src/string/char.f90
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/f2py/tests/src/string/fixed_string.f90
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/f2py/tests/src/string/gh24008.f
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/f2py/tests/src/string/gh24662.f90
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/f2py/tests/src/string/gh25286.f90
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/f2py/tests/src/string/gh25286.pyf
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/f2py/tests/src/string/gh25286_bc.pyf
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/f2py/tests/src/string/scalar_string.f90
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/f2py/tests/src/string/string.f
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/f2py/tests/src/value_attrspec/gh21665.f90
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/f2py/tests/test_abstract_interface.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/f2py/tests/test_array_from_pyobj.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/f2py/tests/test_assumed_shape.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/f2py/tests/test_block_docstring.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/f2py/tests/test_callback.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/f2py/tests/test_character.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/f2py/tests/test_common.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/f2py/tests/test_crackfortran.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/f2py/tests/test_data.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/f2py/tests/test_docs.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/f2py/tests/test_f2cmap.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/f2py/tests/test_f2py2e.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/f2py/tests/test_isoc.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/f2py/tests/test_kind.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/f2py/tests/test_mixed.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/f2py/tests/test_modules.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/f2py/tests/test_parameter.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/f2py/tests/test_pyf_src.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/f2py/tests/test_quoted_character.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/f2py/tests/test_regression.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/f2py/tests/test_return_character.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/f2py/tests/test_return_complex.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/f2py/tests/test_return_integer.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/f2py/tests/test_return_logical.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/f2py/tests/test_return_real.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/f2py/tests/test_routines.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/f2py/tests/test_semicolon_split.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/f2py/tests/test_size.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/f2py/tests/test_string.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/f2py/tests/test_symbolic.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/f2py/tests/test_value_attrspec.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/f2py/tests/util.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/f2py/use_rules.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/fft/__init__.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/fft/__init__.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/fft/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/fft/__pycache__/_helper.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/fft/__pycache__/_pocketfft.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/fft/__pycache__/helper.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/fft/_helper.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/fft/_helper.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/fft/_pocketfft.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/fft/_pocketfft.pyi
 create mode 100755 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/fft/_pocketfft_umath.cpython-311-darwin.so
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/fft/helper.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/fft/helper.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/fft/tests/__init__.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/fft/tests/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/fft/tests/__pycache__/test_helper.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/fft/tests/__pycache__/test_pocketfft.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/fft/tests/test_helper.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/fft/tests/test_pocketfft.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/lib/__init__.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/lib/__init__.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/lib/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/lib/__pycache__/_array_utils_impl.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/lib/__pycache__/_arraypad_impl.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/lib/__pycache__/_arraysetops_impl.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/lib/__pycache__/_arrayterator_impl.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/lib/__pycache__/_datasource.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/lib/__pycache__/_function_base_impl.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/lib/__pycache__/_histograms_impl.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/lib/__pycache__/_index_tricks_impl.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/lib/__pycache__/_iotools.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/lib/__pycache__/_nanfunctions_impl.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/lib/__pycache__/_npyio_impl.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/lib/__pycache__/_polynomial_impl.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/lib/__pycache__/_scimath_impl.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/lib/__pycache__/_shape_base_impl.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/lib/__pycache__/_stride_tricks_impl.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/lib/__pycache__/_twodim_base_impl.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/lib/__pycache__/_type_check_impl.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/lib/__pycache__/_ufunclike_impl.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/lib/__pycache__/_user_array_impl.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/lib/__pycache__/_utils_impl.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/lib/__pycache__/_version.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/lib/__pycache__/array_utils.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/lib/__pycache__/format.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/lib/__pycache__/introspect.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/lib/__pycache__/mixins.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/lib/__pycache__/npyio.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/lib/__pycache__/recfunctions.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/lib/__pycache__/scimath.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/lib/__pycache__/stride_tricks.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/lib/__pycache__/user_array.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/lib/_array_utils_impl.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/lib/_array_utils_impl.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/lib/_arraypad_impl.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/lib/_arraypad_impl.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/lib/_arraysetops_impl.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/lib/_arraysetops_impl.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/lib/_arrayterator_impl.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/lib/_arrayterator_impl.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/lib/_datasource.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/lib/_datasource.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/lib/_function_base_impl.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/lib/_function_base_impl.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/lib/_histograms_impl.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/lib/_histograms_impl.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/lib/_index_tricks_impl.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/lib/_index_tricks_impl.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/lib/_iotools.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/lib/_iotools.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/lib/_nanfunctions_impl.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/lib/_nanfunctions_impl.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/lib/_npyio_impl.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/lib/_npyio_impl.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/lib/_polynomial_impl.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/lib/_polynomial_impl.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/lib/_scimath_impl.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/lib/_scimath_impl.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/lib/_shape_base_impl.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/lib/_shape_base_impl.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/lib/_stride_tricks_impl.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/lib/_stride_tricks_impl.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/lib/_twodim_base_impl.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/lib/_twodim_base_impl.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/lib/_type_check_impl.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/lib/_type_check_impl.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/lib/_ufunclike_impl.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/lib/_ufunclike_impl.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/lib/_user_array_impl.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/lib/_user_array_impl.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/lib/_utils_impl.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/lib/_utils_impl.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/lib/_version.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/lib/_version.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/lib/array_utils.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/lib/array_utils.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/lib/format.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/lib/format.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/lib/introspect.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/lib/introspect.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/lib/mixins.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/lib/mixins.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/lib/npyio.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/lib/npyio.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/lib/recfunctions.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/lib/recfunctions.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/lib/scimath.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/lib/scimath.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/lib/stride_tricks.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/lib/stride_tricks.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/lib/tests/__init__.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/lib/tests/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/lib/tests/__pycache__/test__datasource.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/lib/tests/__pycache__/test__iotools.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/lib/tests/__pycache__/test__version.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/lib/tests/__pycache__/test_array_utils.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/lib/tests/__pycache__/test_arraypad.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/lib/tests/__pycache__/test_arraysetops.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/lib/tests/__pycache__/test_arrayterator.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/lib/tests/__pycache__/test_format.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/lib/tests/__pycache__/test_function_base.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/lib/tests/__pycache__/test_histograms.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/lib/tests/__pycache__/test_index_tricks.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/lib/tests/__pycache__/test_io.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/lib/tests/__pycache__/test_loadtxt.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/lib/tests/__pycache__/test_mixins.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/lib/tests/__pycache__/test_nanfunctions.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/lib/tests/__pycache__/test_packbits.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/lib/tests/__pycache__/test_polynomial.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/lib/tests/__pycache__/test_recfunctions.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/lib/tests/__pycache__/test_regression.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/lib/tests/__pycache__/test_shape_base.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/lib/tests/__pycache__/test_stride_tricks.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/lib/tests/__pycache__/test_twodim_base.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/lib/tests/__pycache__/test_type_check.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/lib/tests/__pycache__/test_ufunclike.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/lib/tests/__pycache__/test_utils.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/lib/tests/data/py2-np0-objarr.npy
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/lib/tests/data/py2-objarr.npy
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/lib/tests/data/py2-objarr.npz
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/lib/tests/data/py3-objarr.npy
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/lib/tests/data/py3-objarr.npz
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/lib/tests/data/python3.npy
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/lib/tests/data/win64python2.npy
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/lib/tests/test__datasource.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/lib/tests/test__iotools.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/lib/tests/test__version.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/lib/tests/test_array_utils.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/lib/tests/test_arraypad.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/lib/tests/test_arraysetops.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/lib/tests/test_arrayterator.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/lib/tests/test_format.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/lib/tests/test_function_base.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/lib/tests/test_histograms.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/lib/tests/test_index_tricks.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/lib/tests/test_io.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/lib/tests/test_loadtxt.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/lib/tests/test_mixins.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/lib/tests/test_nanfunctions.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/lib/tests/test_packbits.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/lib/tests/test_polynomial.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/lib/tests/test_recfunctions.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/lib/tests/test_regression.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/lib/tests/test_shape_base.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/lib/tests/test_stride_tricks.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/lib/tests/test_twodim_base.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/lib/tests/test_type_check.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/lib/tests/test_ufunclike.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/lib/tests/test_utils.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/lib/user_array.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/lib/user_array.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/linalg/__init__.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/linalg/__init__.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/linalg/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/linalg/__pycache__/_linalg.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/linalg/__pycache__/linalg.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/linalg/_linalg.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/linalg/_linalg.pyi
 create mode 100755 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/linalg/_umath_linalg.cpython-311-darwin.so
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/linalg/_umath_linalg.pyi
 create mode 100755 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/linalg/lapack_lite.cpython-311-darwin.so
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/linalg/lapack_lite.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/linalg/linalg.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/linalg/linalg.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/linalg/tests/__init__.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/linalg/tests/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/linalg/tests/__pycache__/test_deprecations.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/linalg/tests/__pycache__/test_linalg.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/linalg/tests/__pycache__/test_regression.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/linalg/tests/test_deprecations.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/linalg/tests/test_linalg.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/linalg/tests/test_regression.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/ma/LICENSE
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/ma/README.rst
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/ma/__init__.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/ma/__init__.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/ma/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/ma/__pycache__/core.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/ma/__pycache__/extras.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/ma/__pycache__/mrecords.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/ma/__pycache__/testutils.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/ma/__pycache__/timer_comparison.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/ma/core.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/ma/core.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/ma/extras.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/ma/extras.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/ma/mrecords.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/ma/mrecords.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/ma/tests/__init__.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/ma/tests/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/ma/tests/__pycache__/test_arrayobject.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/ma/tests/__pycache__/test_core.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/ma/tests/__pycache__/test_deprecations.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/ma/tests/__pycache__/test_extras.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/ma/tests/__pycache__/test_mrecords.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/ma/tests/__pycache__/test_old_ma.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/ma/tests/__pycache__/test_regression.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/ma/tests/__pycache__/test_subclassing.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/ma/tests/test_arrayobject.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/ma/tests/test_core.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/ma/tests/test_deprecations.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/ma/tests/test_extras.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/ma/tests/test_mrecords.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/ma/tests/test_old_ma.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/ma/tests/test_regression.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/ma/tests/test_subclassing.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/ma/testutils.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/ma/timer_comparison.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/matlib.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/matlib.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/matrixlib/__init__.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/matrixlib/__init__.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/matrixlib/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/matrixlib/__pycache__/defmatrix.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/matrixlib/defmatrix.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/matrixlib/defmatrix.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/matrixlib/tests/__init__.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/matrixlib/tests/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/matrixlib/tests/__pycache__/test_defmatrix.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/matrixlib/tests/__pycache__/test_interaction.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/matrixlib/tests/__pycache__/test_masked_matrix.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/matrixlib/tests/__pycache__/test_matrix_linalg.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/matrixlib/tests/__pycache__/test_multiarray.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/matrixlib/tests/__pycache__/test_numeric.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/matrixlib/tests/__pycache__/test_regression.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/matrixlib/tests/test_defmatrix.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/matrixlib/tests/test_interaction.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/matrixlib/tests/test_masked_matrix.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/matrixlib/tests/test_matrix_linalg.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/matrixlib/tests/test_multiarray.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/matrixlib/tests/test_numeric.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/matrixlib/tests/test_regression.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/polynomial/__init__.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/polynomial/__init__.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/polynomial/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/polynomial/__pycache__/_polybase.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/polynomial/__pycache__/chebyshev.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/polynomial/__pycache__/hermite.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/polynomial/__pycache__/hermite_e.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/polynomial/__pycache__/laguerre.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/polynomial/__pycache__/legendre.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/polynomial/__pycache__/polynomial.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/polynomial/__pycache__/polyutils.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/polynomial/_polybase.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/polynomial/_polybase.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/polynomial/_polytypes.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/polynomial/chebyshev.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/polynomial/chebyshev.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/polynomial/hermite.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/polynomial/hermite.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/polynomial/hermite_e.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/polynomial/hermite_e.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/polynomial/laguerre.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/polynomial/laguerre.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/polynomial/legendre.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/polynomial/legendre.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/polynomial/polynomial.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/polynomial/polynomial.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/polynomial/polyutils.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/polynomial/polyutils.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/polynomial/tests/__init__.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/polynomial/tests/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/polynomial/tests/__pycache__/test_chebyshev.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/polynomial/tests/__pycache__/test_classes.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/polynomial/tests/__pycache__/test_hermite.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/polynomial/tests/__pycache__/test_hermite_e.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/polynomial/tests/__pycache__/test_laguerre.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/polynomial/tests/__pycache__/test_legendre.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/polynomial/tests/__pycache__/test_polynomial.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/polynomial/tests/__pycache__/test_polyutils.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/polynomial/tests/__pycache__/test_printing.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/polynomial/tests/__pycache__/test_symbol.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/polynomial/tests/test_chebyshev.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/polynomial/tests/test_classes.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/polynomial/tests/test_hermite.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/polynomial/tests/test_hermite_e.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/polynomial/tests/test_laguerre.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/polynomial/tests/test_legendre.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/polynomial/tests/test_polynomial.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/polynomial/tests/test_polyutils.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/polynomial/tests/test_printing.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/polynomial/tests/test_symbol.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/py.typed
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/random/LICENSE.md
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/random/__init__.pxd
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/random/__init__.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/random/__init__.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/random/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/random/__pycache__/_pickle.cpython-311.pyc
 create mode 100755 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/random/_bounded_integers.cpython-311-darwin.so
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/random/_bounded_integers.pxd
 create mode 100755 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/random/_common.cpython-311-darwin.so
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/random/_common.pxd
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/random/_examples/cffi/__pycache__/extending.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/random/_examples/cffi/__pycache__/parse.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/random/_examples/cffi/extending.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/random/_examples/cffi/parse.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/random/_examples/cython/extending.pyx
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/random/_examples/cython/extending_distributions.pyx
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/random/_examples/cython/meson.build
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/random/_examples/numba/__pycache__/extending.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/random/_examples/numba/__pycache__/extending_distributions.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/random/_examples/numba/extending.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/random/_examples/numba/extending_distributions.py
 create mode 100755 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/random/_generator.cpython-311-darwin.so
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/random/_generator.pyi
 create mode 100755 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/random/_mt19937.cpython-311-darwin.so
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/random/_mt19937.pyi
 create mode 100755 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/random/_pcg64.cpython-311-darwin.so
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/random/_pcg64.pyi
 create mode 100755 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/random/_philox.cpython-311-darwin.so
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/random/_philox.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/random/_pickle.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/random/_pickle.pyi
 create mode 100755 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/random/_sfc64.cpython-311-darwin.so
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/random/_sfc64.pyi
 create mode 100755 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/random/bit_generator.cpython-311-darwin.so
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/random/bit_generator.pxd
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/random/bit_generator.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/random/c_distributions.pxd
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/random/lib/libnpyrandom.a
 create mode 100755 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/random/mtrand.cpython-311-darwin.so
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/random/mtrand.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/random/tests/__init__.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/random/tests/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/random/tests/__pycache__/test_direct.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/random/tests/__pycache__/test_extending.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/random/tests/__pycache__/test_generator_mt19937.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/random/tests/__pycache__/test_generator_mt19937_regressions.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/random/tests/__pycache__/test_random.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/random/tests/__pycache__/test_randomstate.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/random/tests/__pycache__/test_randomstate_regression.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/random/tests/__pycache__/test_regression.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/random/tests/__pycache__/test_seed_sequence.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/random/tests/__pycache__/test_smoke.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/random/tests/data/__init__.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/random/tests/data/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/random/tests/data/generator_pcg64_np121.pkl.gz
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/random/tests/data/generator_pcg64_np126.pkl.gz
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/random/tests/data/mt19937-testset-1.csv
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/random/tests/data/mt19937-testset-2.csv
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/random/tests/data/pcg64-testset-1.csv
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/random/tests/data/pcg64-testset-2.csv
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/random/tests/data/pcg64dxsm-testset-1.csv
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/random/tests/data/pcg64dxsm-testset-2.csv
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/random/tests/data/philox-testset-1.csv
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/random/tests/data/philox-testset-2.csv
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/random/tests/data/sfc64-testset-1.csv
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/random/tests/data/sfc64-testset-2.csv
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/random/tests/data/sfc64_np126.pkl.gz
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/random/tests/test_direct.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/random/tests/test_extending.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/random/tests/test_generator_mt19937.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/random/tests/test_generator_mt19937_regressions.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/random/tests/test_random.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/random/tests/test_randomstate.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/random/tests/test_randomstate_regression.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/random/tests/test_regression.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/random/tests/test_seed_sequence.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/random/tests/test_smoke.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/rec/__init__.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/rec/__init__.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/rec/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/strings/__init__.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/strings/__init__.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/strings/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/testing/__init__.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/testing/__init__.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/testing/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/testing/__pycache__/overrides.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/testing/__pycache__/print_coercion_tables.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/testing/_private/__init__.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/testing/_private/__init__.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/testing/_private/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/testing/_private/__pycache__/extbuild.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/testing/_private/__pycache__/utils.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/testing/_private/extbuild.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/testing/_private/extbuild.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/testing/_private/utils.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/testing/_private/utils.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/testing/overrides.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/testing/overrides.pyi
 create mode 100755 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/testing/print_coercion_tables.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/testing/print_coercion_tables.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/testing/tests/__init__.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/testing/tests/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/testing/tests/__pycache__/test_utils.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/testing/tests/test_utils.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/tests/__init__.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/tests/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/tests/__pycache__/test__all__.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/tests/__pycache__/test_configtool.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/tests/__pycache__/test_ctypeslib.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/tests/__pycache__/test_lazyloading.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/tests/__pycache__/test_matlib.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/tests/__pycache__/test_numpy_config.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/tests/__pycache__/test_numpy_version.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/tests/__pycache__/test_public_api.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/tests/__pycache__/test_reloading.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/tests/__pycache__/test_scripts.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/tests/__pycache__/test_warnings.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/tests/test__all__.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/tests/test_configtool.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/tests/test_ctypeslib.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/tests/test_lazyloading.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/tests/test_matlib.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/tests/test_numpy_config.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/tests/test_numpy_version.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/tests/test_public_api.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/tests/test_reloading.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/tests/test_scripts.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/tests/test_warnings.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/typing/__init__.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/typing/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/typing/__pycache__/mypy_plugin.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/typing/mypy_plugin.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/typing/tests/__init__.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/typing/tests/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/typing/tests/__pycache__/test_isfile.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/typing/tests/__pycache__/test_runtime.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/typing/tests/__pycache__/test_typing.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/typing/tests/data/fail/arithmetic.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/typing/tests/data/fail/array_constructors.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/typing/tests/data/fail/array_like.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/typing/tests/data/fail/array_pad.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/typing/tests/data/fail/arrayprint.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/typing/tests/data/fail/arrayterator.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/typing/tests/data/fail/bitwise_ops.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/typing/tests/data/fail/char.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/typing/tests/data/fail/chararray.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/typing/tests/data/fail/comparisons.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/typing/tests/data/fail/constants.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/typing/tests/data/fail/datasource.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/typing/tests/data/fail/dtype.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/typing/tests/data/fail/einsumfunc.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/typing/tests/data/fail/flatiter.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/typing/tests/data/fail/fromnumeric.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/typing/tests/data/fail/histograms.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/typing/tests/data/fail/index_tricks.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/typing/tests/data/fail/lib_function_base.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/typing/tests/data/fail/lib_polynomial.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/typing/tests/data/fail/lib_utils.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/typing/tests/data/fail/lib_version.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/typing/tests/data/fail/linalg.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/typing/tests/data/fail/memmap.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/typing/tests/data/fail/modules.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/typing/tests/data/fail/multiarray.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/typing/tests/data/fail/ndarray.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/typing/tests/data/fail/ndarray_misc.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/typing/tests/data/fail/nditer.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/typing/tests/data/fail/nested_sequence.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/typing/tests/data/fail/npyio.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/typing/tests/data/fail/numerictypes.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/typing/tests/data/fail/random.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/typing/tests/data/fail/rec.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/typing/tests/data/fail/scalars.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/typing/tests/data/fail/shape.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/typing/tests/data/fail/shape_base.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/typing/tests/data/fail/stride_tricks.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/typing/tests/data/fail/strings.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/typing/tests/data/fail/testing.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/typing/tests/data/fail/twodim_base.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/typing/tests/data/fail/type_check.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/typing/tests/data/fail/ufunc_config.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/typing/tests/data/fail/ufunclike.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/typing/tests/data/fail/ufuncs.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/typing/tests/data/fail/warnings_and_errors.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/typing/tests/data/misc/extended_precision.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/typing/tests/data/mypy.ini
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/typing/tests/data/pass/__pycache__/arithmetic.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/typing/tests/data/pass/__pycache__/array_constructors.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/typing/tests/data/pass/__pycache__/array_like.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/typing/tests/data/pass/__pycache__/arrayprint.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/typing/tests/data/pass/__pycache__/arrayterator.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/typing/tests/data/pass/__pycache__/bitwise_ops.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/typing/tests/data/pass/__pycache__/comparisons.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/typing/tests/data/pass/__pycache__/dtype.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/typing/tests/data/pass/__pycache__/einsumfunc.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/typing/tests/data/pass/__pycache__/flatiter.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/typing/tests/data/pass/__pycache__/fromnumeric.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/typing/tests/data/pass/__pycache__/index_tricks.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/typing/tests/data/pass/__pycache__/lib_user_array.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/typing/tests/data/pass/__pycache__/lib_utils.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/typing/tests/data/pass/__pycache__/lib_version.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/typing/tests/data/pass/__pycache__/literal.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/typing/tests/data/pass/__pycache__/ma.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/typing/tests/data/pass/__pycache__/mod.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/typing/tests/data/pass/__pycache__/modules.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/typing/tests/data/pass/__pycache__/multiarray.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/typing/tests/data/pass/__pycache__/ndarray_conversion.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/typing/tests/data/pass/__pycache__/ndarray_misc.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/typing/tests/data/pass/__pycache__/ndarray_shape_manipulation.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/typing/tests/data/pass/__pycache__/nditer.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/typing/tests/data/pass/__pycache__/numeric.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/typing/tests/data/pass/__pycache__/numerictypes.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/typing/tests/data/pass/__pycache__/random.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/typing/tests/data/pass/__pycache__/recfunctions.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/typing/tests/data/pass/__pycache__/scalars.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/typing/tests/data/pass/__pycache__/shape.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/typing/tests/data/pass/__pycache__/simple.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/typing/tests/data/pass/__pycache__/simple_py3.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/typing/tests/data/pass/__pycache__/ufunc_config.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/typing/tests/data/pass/__pycache__/ufunclike.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/typing/tests/data/pass/__pycache__/ufuncs.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/typing/tests/data/pass/__pycache__/warnings_and_errors.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/typing/tests/data/pass/arithmetic.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/typing/tests/data/pass/array_constructors.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/typing/tests/data/pass/array_like.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/typing/tests/data/pass/arrayprint.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/typing/tests/data/pass/arrayterator.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/typing/tests/data/pass/bitwise_ops.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/typing/tests/data/pass/comparisons.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/typing/tests/data/pass/dtype.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/typing/tests/data/pass/einsumfunc.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/typing/tests/data/pass/flatiter.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/typing/tests/data/pass/fromnumeric.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/typing/tests/data/pass/index_tricks.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/typing/tests/data/pass/lib_user_array.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/typing/tests/data/pass/lib_utils.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/typing/tests/data/pass/lib_version.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/typing/tests/data/pass/literal.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/typing/tests/data/pass/ma.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/typing/tests/data/pass/mod.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/typing/tests/data/pass/modules.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/typing/tests/data/pass/multiarray.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/typing/tests/data/pass/ndarray_conversion.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/typing/tests/data/pass/ndarray_misc.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/typing/tests/data/pass/ndarray_shape_manipulation.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/typing/tests/data/pass/nditer.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/typing/tests/data/pass/numeric.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/typing/tests/data/pass/numerictypes.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/typing/tests/data/pass/random.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/typing/tests/data/pass/recfunctions.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/typing/tests/data/pass/scalars.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/typing/tests/data/pass/shape.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/typing/tests/data/pass/simple.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/typing/tests/data/pass/simple_py3.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/typing/tests/data/pass/ufunc_config.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/typing/tests/data/pass/ufunclike.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/typing/tests/data/pass/ufuncs.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/typing/tests/data/pass/warnings_and_errors.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/typing/tests/data/reveal/arithmetic.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/typing/tests/data/reveal/array_api_info.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/typing/tests/data/reveal/array_constructors.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/typing/tests/data/reveal/arraypad.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/typing/tests/data/reveal/arrayprint.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/typing/tests/data/reveal/arraysetops.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/typing/tests/data/reveal/arrayterator.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/typing/tests/data/reveal/bitwise_ops.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/typing/tests/data/reveal/char.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/typing/tests/data/reveal/chararray.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/typing/tests/data/reveal/comparisons.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/typing/tests/data/reveal/constants.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/typing/tests/data/reveal/ctypeslib.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/typing/tests/data/reveal/datasource.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/typing/tests/data/reveal/dtype.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/typing/tests/data/reveal/einsumfunc.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/typing/tests/data/reveal/emath.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/typing/tests/data/reveal/fft.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/typing/tests/data/reveal/flatiter.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/typing/tests/data/reveal/fromnumeric.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/typing/tests/data/reveal/getlimits.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/typing/tests/data/reveal/histograms.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/typing/tests/data/reveal/index_tricks.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/typing/tests/data/reveal/lib_function_base.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/typing/tests/data/reveal/lib_polynomial.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/typing/tests/data/reveal/lib_utils.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/typing/tests/data/reveal/lib_version.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/typing/tests/data/reveal/linalg.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/typing/tests/data/reveal/matrix.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/typing/tests/data/reveal/memmap.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/typing/tests/data/reveal/mod.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/typing/tests/data/reveal/modules.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/typing/tests/data/reveal/multiarray.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/typing/tests/data/reveal/nbit_base_example.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/typing/tests/data/reveal/ndarray_assignability.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/typing/tests/data/reveal/ndarray_conversion.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/typing/tests/data/reveal/ndarray_misc.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/typing/tests/data/reveal/ndarray_shape_manipulation.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/typing/tests/data/reveal/nditer.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/typing/tests/data/reveal/nested_sequence.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/typing/tests/data/reveal/npyio.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/typing/tests/data/reveal/numeric.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/typing/tests/data/reveal/numerictypes.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/typing/tests/data/reveal/polynomial_polybase.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/typing/tests/data/reveal/polynomial_polyutils.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/typing/tests/data/reveal/polynomial_series.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/typing/tests/data/reveal/random.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/typing/tests/data/reveal/rec.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/typing/tests/data/reveal/scalars.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/typing/tests/data/reveal/shape.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/typing/tests/data/reveal/shape_base.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/typing/tests/data/reveal/stride_tricks.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/typing/tests/data/reveal/strings.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/typing/tests/data/reveal/testing.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/typing/tests/data/reveal/twodim_base.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/typing/tests/data/reveal/type_check.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/typing/tests/data/reveal/ufunc_config.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/typing/tests/data/reveal/ufunclike.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/typing/tests/data/reveal/ufuncs.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/typing/tests/data/reveal/warnings_and_errors.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/typing/tests/test_isfile.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/typing/tests/test_runtime.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/typing/tests/test_typing.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/version.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/numpy/version.pyi
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip-24.0.dist-info/INSTALLER
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip-24.0.dist-info/METADATA
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip-24.0.dist-info/RECORD
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip-24.0.dist-info/REQUESTED
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip-24.0.dist-info/WHEEL
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/__init__.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/__main__.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/__pip-runner__.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/__pycache__/__main__.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/__pycache__/__pip-runner__.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/__init__.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/__pycache__/build_env.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/__pycache__/cache.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/__pycache__/configuration.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/__pycache__/exceptions.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/__pycache__/main.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/__pycache__/pyproject.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/__pycache__/self_outdated_check.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/__pycache__/wheel_builder.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/build_env.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/cache.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/cli/__init__.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/cli/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/cli/__pycache__/autocompletion.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/cli/__pycache__/base_command.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/cli/__pycache__/cmdoptions.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/cli/__pycache__/command_context.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/cli/__pycache__/main.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/cli/__pycache__/main_parser.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/cli/__pycache__/parser.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/cli/__pycache__/progress_bars.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/cli/__pycache__/req_command.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/cli/__pycache__/spinners.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/cli/__pycache__/status_codes.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/cli/autocompletion.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/cli/base_command.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/cli/cmdoptions.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/cli/command_context.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/cli/main.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/cli/main_parser.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/cli/parser.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/cli/progress_bars.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/cli/req_command.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/cli/spinners.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/cli/status_codes.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/commands/__init__.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/commands/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/commands/__pycache__/cache.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/commands/__pycache__/check.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/commands/__pycache__/completion.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/commands/__pycache__/configuration.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/commands/__pycache__/debug.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/commands/__pycache__/download.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/commands/__pycache__/freeze.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/commands/__pycache__/hash.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/commands/__pycache__/help.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/commands/__pycache__/index.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/commands/__pycache__/inspect.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/commands/__pycache__/install.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/commands/__pycache__/list.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/commands/__pycache__/search.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/commands/__pycache__/show.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/commands/__pycache__/uninstall.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/commands/__pycache__/wheel.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/commands/cache.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/commands/check.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/commands/completion.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/commands/configuration.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/commands/debug.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/commands/download.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/commands/freeze.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/commands/hash.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/commands/help.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/commands/index.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/commands/inspect.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/commands/install.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/commands/list.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/commands/search.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/commands/show.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/commands/uninstall.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/commands/wheel.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/configuration.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/distributions/__init__.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/distributions/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/distributions/__pycache__/base.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/distributions/__pycache__/installed.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/distributions/__pycache__/sdist.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/distributions/__pycache__/wheel.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/distributions/base.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/distributions/installed.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/distributions/sdist.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/distributions/wheel.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/exceptions.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/index/__init__.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/index/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/index/__pycache__/collector.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/index/__pycache__/package_finder.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/index/__pycache__/sources.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/index/collector.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/index/package_finder.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/index/sources.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/locations/__init__.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/locations/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/locations/__pycache__/_distutils.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/locations/__pycache__/_sysconfig.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/locations/__pycache__/base.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/locations/_distutils.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/locations/_sysconfig.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/locations/base.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/main.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/metadata/__init__.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/metadata/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/metadata/__pycache__/_json.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/metadata/__pycache__/base.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/metadata/__pycache__/pkg_resources.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/metadata/_json.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/metadata/base.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/metadata/importlib/__init__.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/metadata/importlib/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/metadata/importlib/__pycache__/_compat.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/metadata/importlib/__pycache__/_dists.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/metadata/importlib/__pycache__/_envs.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/metadata/importlib/_compat.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/metadata/importlib/_dists.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/metadata/importlib/_envs.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/metadata/pkg_resources.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/models/__init__.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/models/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/models/__pycache__/candidate.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/models/__pycache__/direct_url.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/models/__pycache__/format_control.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/models/__pycache__/index.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/models/__pycache__/installation_report.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/models/__pycache__/link.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/models/__pycache__/scheme.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/models/__pycache__/search_scope.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/models/__pycache__/selection_prefs.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/models/__pycache__/target_python.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/models/__pycache__/wheel.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/models/candidate.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/models/direct_url.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/models/format_control.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/models/index.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/models/installation_report.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/models/link.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/models/scheme.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/models/search_scope.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/models/selection_prefs.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/models/target_python.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/models/wheel.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/network/__init__.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/network/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/network/__pycache__/auth.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/network/__pycache__/cache.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/network/__pycache__/download.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/network/__pycache__/lazy_wheel.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/network/__pycache__/session.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/network/__pycache__/utils.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/network/__pycache__/xmlrpc.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/network/auth.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/network/cache.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/network/download.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/network/lazy_wheel.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/network/session.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/network/utils.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/network/xmlrpc.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/operations/__init__.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/operations/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/operations/__pycache__/check.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/operations/__pycache__/freeze.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/operations/__pycache__/prepare.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/operations/build/__init__.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/operations/build/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/operations/build/__pycache__/build_tracker.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/operations/build/__pycache__/metadata.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/operations/build/__pycache__/metadata_editable.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/operations/build/__pycache__/metadata_legacy.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/operations/build/__pycache__/wheel.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/operations/build/__pycache__/wheel_editable.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/operations/build/__pycache__/wheel_legacy.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/operations/build/build_tracker.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/operations/build/metadata.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/operations/build/metadata_editable.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/operations/build/metadata_legacy.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/operations/build/wheel.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/operations/build/wheel_editable.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/operations/build/wheel_legacy.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/operations/check.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/operations/freeze.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/operations/install/__init__.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/operations/install/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/operations/install/__pycache__/editable_legacy.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/operations/install/__pycache__/wheel.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/operations/install/editable_legacy.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/operations/install/wheel.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/operations/prepare.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/pyproject.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/req/__init__.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/req/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/req/__pycache__/constructors.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/req/__pycache__/req_file.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/req/__pycache__/req_install.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/req/__pycache__/req_set.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/req/__pycache__/req_uninstall.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/req/constructors.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/req/req_file.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/req/req_install.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/req/req_set.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/req/req_uninstall.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/resolution/__init__.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/resolution/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/resolution/__pycache__/base.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/resolution/base.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/resolution/legacy/__init__.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/resolution/legacy/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/resolution/legacy/__pycache__/resolver.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/resolution/legacy/resolver.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/resolution/resolvelib/__init__.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/resolution/resolvelib/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/resolution/resolvelib/__pycache__/base.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/resolution/resolvelib/__pycache__/candidates.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/resolution/resolvelib/__pycache__/factory.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/resolution/resolvelib/__pycache__/found_candidates.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/resolution/resolvelib/__pycache__/provider.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/resolution/resolvelib/__pycache__/reporter.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/resolution/resolvelib/__pycache__/requirements.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/resolution/resolvelib/__pycache__/resolver.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/resolution/resolvelib/base.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/resolution/resolvelib/candidates.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/resolution/resolvelib/factory.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/resolution/resolvelib/found_candidates.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/resolution/resolvelib/provider.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/resolution/resolvelib/reporter.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/resolution/resolvelib/requirements.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/resolution/resolvelib/resolver.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/self_outdated_check.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/utils/__init__.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/utils/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/utils/__pycache__/_jaraco_text.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/utils/__pycache__/_log.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/utils/__pycache__/appdirs.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/utils/__pycache__/compat.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/utils/__pycache__/compatibility_tags.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/utils/__pycache__/datetime.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/utils/__pycache__/deprecation.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/utils/__pycache__/direct_url_helpers.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/utils/__pycache__/egg_link.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/utils/__pycache__/encoding.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/utils/__pycache__/entrypoints.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/utils/__pycache__/filesystem.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/utils/__pycache__/filetypes.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/utils/__pycache__/glibc.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/utils/__pycache__/hashes.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/utils/__pycache__/logging.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/utils/__pycache__/misc.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/utils/__pycache__/models.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/utils/__pycache__/packaging.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/utils/__pycache__/setuptools_build.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/utils/__pycache__/subprocess.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/utils/__pycache__/temp_dir.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/utils/__pycache__/unpacking.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/utils/__pycache__/urls.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/utils/__pycache__/virtualenv.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/utils/__pycache__/wheel.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/utils/_jaraco_text.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/utils/_log.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/utils/appdirs.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/utils/compat.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/utils/compatibility_tags.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/utils/datetime.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/utils/deprecation.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/utils/direct_url_helpers.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/utils/egg_link.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/utils/encoding.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/utils/entrypoints.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/utils/filesystem.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/utils/filetypes.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/utils/glibc.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/utils/hashes.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/utils/logging.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/utils/misc.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/utils/models.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/utils/packaging.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/utils/setuptools_build.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/utils/subprocess.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/utils/temp_dir.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/utils/unpacking.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/utils/urls.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/utils/virtualenv.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/utils/wheel.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/vcs/__init__.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/vcs/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/vcs/__pycache__/bazaar.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/vcs/__pycache__/git.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/vcs/__pycache__/mercurial.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/vcs/__pycache__/subversion.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/vcs/__pycache__/versioncontrol.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/vcs/bazaar.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/vcs/git.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/vcs/mercurial.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/vcs/subversion.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/vcs/versioncontrol.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_internal/wheel_builder.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/__init__.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/__pycache__/six.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/__pycache__/typing_extensions.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/cachecontrol/__init__.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/cachecontrol/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/cachecontrol/__pycache__/_cmd.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/cachecontrol/__pycache__/adapter.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/cachecontrol/__pycache__/cache.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/cachecontrol/__pycache__/controller.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/cachecontrol/__pycache__/filewrapper.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/cachecontrol/__pycache__/heuristics.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/cachecontrol/__pycache__/serialize.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/cachecontrol/__pycache__/wrapper.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/cachecontrol/_cmd.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/cachecontrol/adapter.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/cachecontrol/cache.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/cachecontrol/caches/__init__.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/cachecontrol/caches/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/cachecontrol/caches/__pycache__/file_cache.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/cachecontrol/caches/__pycache__/redis_cache.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/cachecontrol/caches/file_cache.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/cachecontrol/caches/redis_cache.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/cachecontrol/controller.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/cachecontrol/filewrapper.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/cachecontrol/heuristics.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/cachecontrol/py.typed
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/cachecontrol/serialize.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/cachecontrol/wrapper.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/certifi/__init__.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/certifi/__main__.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/certifi/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/certifi/__pycache__/__main__.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/certifi/__pycache__/core.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/certifi/cacert.pem
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/certifi/core.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/certifi/py.typed
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/chardet/__init__.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/chardet/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/chardet/__pycache__/big5freq.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/chardet/__pycache__/big5prober.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/chardet/__pycache__/chardistribution.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/chardet/__pycache__/charsetgroupprober.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/chardet/__pycache__/charsetprober.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/chardet/__pycache__/codingstatemachine.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/chardet/__pycache__/codingstatemachinedict.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/chardet/__pycache__/cp949prober.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/chardet/__pycache__/enums.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/chardet/__pycache__/escprober.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/chardet/__pycache__/escsm.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/chardet/__pycache__/eucjpprober.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/chardet/__pycache__/euckrfreq.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/chardet/__pycache__/euckrprober.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/chardet/__pycache__/euctwfreq.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/chardet/__pycache__/euctwprober.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/chardet/__pycache__/gb2312freq.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/chardet/__pycache__/gb2312prober.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/chardet/__pycache__/hebrewprober.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/chardet/__pycache__/jisfreq.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/chardet/__pycache__/johabfreq.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/chardet/__pycache__/johabprober.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/chardet/__pycache__/jpcntx.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/chardet/__pycache__/langbulgarianmodel.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/chardet/__pycache__/langgreekmodel.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/chardet/__pycache__/langhebrewmodel.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/chardet/__pycache__/langhungarianmodel.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/chardet/__pycache__/langrussianmodel.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/chardet/__pycache__/langthaimodel.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/chardet/__pycache__/langturkishmodel.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/chardet/__pycache__/latin1prober.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/chardet/__pycache__/macromanprober.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/chardet/__pycache__/mbcharsetprober.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/chardet/__pycache__/mbcsgroupprober.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/chardet/__pycache__/mbcssm.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/chardet/__pycache__/resultdict.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/chardet/__pycache__/sbcharsetprober.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/chardet/__pycache__/sbcsgroupprober.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/chardet/__pycache__/sjisprober.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/chardet/__pycache__/universaldetector.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/chardet/__pycache__/utf1632prober.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/chardet/__pycache__/utf8prober.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/chardet/__pycache__/version.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/chardet/big5freq.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/chardet/big5prober.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/chardet/chardistribution.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/chardet/charsetgroupprober.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/chardet/charsetprober.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/chardet/cli/__init__.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/chardet/cli/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/chardet/cli/__pycache__/chardetect.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/chardet/cli/chardetect.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/chardet/codingstatemachine.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/chardet/codingstatemachinedict.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/chardet/cp949prober.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/chardet/enums.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/chardet/escprober.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/chardet/escsm.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/chardet/eucjpprober.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/chardet/euckrfreq.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/chardet/euckrprober.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/chardet/euctwfreq.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/chardet/euctwprober.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/chardet/gb2312freq.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/chardet/gb2312prober.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/chardet/hebrewprober.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/chardet/jisfreq.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/chardet/johabfreq.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/chardet/johabprober.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/chardet/jpcntx.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/chardet/langbulgarianmodel.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/chardet/langgreekmodel.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/chardet/langhebrewmodel.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/chardet/langhungarianmodel.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/chardet/langrussianmodel.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/chardet/langthaimodel.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/chardet/langturkishmodel.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/chardet/latin1prober.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/chardet/macromanprober.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/chardet/mbcharsetprober.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/chardet/mbcsgroupprober.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/chardet/mbcssm.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/chardet/metadata/__init__.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/chardet/metadata/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/chardet/metadata/__pycache__/languages.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/chardet/metadata/languages.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/chardet/py.typed
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/chardet/resultdict.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/chardet/sbcharsetprober.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/chardet/sbcsgroupprober.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/chardet/sjisprober.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/chardet/universaldetector.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/chardet/utf1632prober.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/chardet/utf8prober.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/chardet/version.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/colorama/__init__.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/colorama/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/colorama/__pycache__/ansi.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/colorama/__pycache__/ansitowin32.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/colorama/__pycache__/initialise.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/colorama/__pycache__/win32.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/colorama/__pycache__/winterm.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/colorama/ansi.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/colorama/ansitowin32.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/colorama/initialise.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/colorama/tests/__init__.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/colorama/tests/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/colorama/tests/__pycache__/ansi_test.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/colorama/tests/__pycache__/ansitowin32_test.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/colorama/tests/__pycache__/initialise_test.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/colorama/tests/__pycache__/isatty_test.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/colorama/tests/__pycache__/utils.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/colorama/tests/__pycache__/winterm_test.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/colorama/tests/ansi_test.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/colorama/tests/ansitowin32_test.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/colorama/tests/initialise_test.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/colorama/tests/isatty_test.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/colorama/tests/utils.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/colorama/tests/winterm_test.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/colorama/win32.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/colorama/winterm.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/distlib/__init__.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/distlib/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/distlib/__pycache__/compat.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/distlib/__pycache__/database.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/distlib/__pycache__/index.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/distlib/__pycache__/locators.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/distlib/__pycache__/manifest.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/distlib/__pycache__/markers.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/distlib/__pycache__/metadata.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/distlib/__pycache__/resources.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/distlib/__pycache__/scripts.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/distlib/__pycache__/util.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/distlib/__pycache__/version.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/distlib/__pycache__/wheel.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/distlib/compat.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/distlib/database.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/distlib/index.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/distlib/locators.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/distlib/manifest.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/distlib/markers.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/distlib/metadata.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/distlib/resources.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/distlib/scripts.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/distlib/t32.exe
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/distlib/t64-arm.exe
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/distlib/t64.exe
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/distlib/util.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/distlib/version.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/distlib/w32.exe
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/distlib/w64-arm.exe
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/distlib/w64.exe
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/distlib/wheel.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/distro/__init__.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/distro/__main__.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/distro/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/distro/__pycache__/__main__.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/distro/__pycache__/distro.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/distro/distro.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/distro/py.typed
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/idna/__init__.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/idna/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/idna/__pycache__/codec.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/idna/__pycache__/compat.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/idna/__pycache__/core.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/idna/__pycache__/idnadata.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/idna/__pycache__/intranges.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/idna/__pycache__/package_data.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/idna/__pycache__/uts46data.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/idna/codec.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/idna/compat.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/idna/core.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/idna/idnadata.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/idna/intranges.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/idna/package_data.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/idna/py.typed
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/idna/uts46data.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/msgpack/__init__.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/msgpack/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/msgpack/__pycache__/exceptions.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/msgpack/__pycache__/ext.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/msgpack/__pycache__/fallback.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/msgpack/exceptions.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/msgpack/ext.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/msgpack/fallback.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/packaging/__about__.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/packaging/__init__.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/packaging/__pycache__/__about__.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/packaging/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/packaging/__pycache__/_manylinux.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/packaging/__pycache__/_musllinux.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/packaging/__pycache__/_structures.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/packaging/__pycache__/markers.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/packaging/__pycache__/requirements.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/packaging/__pycache__/specifiers.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/packaging/__pycache__/tags.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/packaging/__pycache__/utils.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/packaging/__pycache__/version.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/packaging/_manylinux.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/packaging/_musllinux.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/packaging/_structures.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/packaging/markers.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/packaging/py.typed
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/packaging/requirements.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/packaging/specifiers.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/packaging/tags.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/packaging/utils.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/packaging/version.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/pkg_resources/__init__.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/pkg_resources/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/platformdirs/__init__.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/platformdirs/__main__.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/platformdirs/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/platformdirs/__pycache__/__main__.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/platformdirs/__pycache__/android.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/platformdirs/__pycache__/api.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/platformdirs/__pycache__/macos.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/platformdirs/__pycache__/unix.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/platformdirs/__pycache__/version.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/platformdirs/__pycache__/windows.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/platformdirs/android.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/platformdirs/api.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/platformdirs/macos.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/platformdirs/py.typed
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/platformdirs/unix.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/platformdirs/version.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/platformdirs/windows.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/pygments/__init__.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/pygments/__main__.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/pygments/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/pygments/__pycache__/__main__.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/pygments/__pycache__/cmdline.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/pygments/__pycache__/console.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/pygments/__pycache__/filter.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/pygments/__pycache__/formatter.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/pygments/__pycache__/lexer.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/pygments/__pycache__/modeline.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/pygments/__pycache__/plugin.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/pygments/__pycache__/regexopt.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/pygments/__pycache__/scanner.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/pygments/__pycache__/sphinxext.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/pygments/__pycache__/style.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/pygments/__pycache__/token.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/pygments/__pycache__/unistring.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/pygments/__pycache__/util.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/pygments/cmdline.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/pygments/console.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/pygments/filter.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/pygments/filters/__init__.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/pygments/filters/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/pygments/formatter.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/pygments/formatters/__init__.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/pygments/formatters/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/pygments/formatters/__pycache__/_mapping.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/pygments/formatters/__pycache__/bbcode.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/pygments/formatters/__pycache__/groff.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/pygments/formatters/__pycache__/html.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/pygments/formatters/__pycache__/img.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/pygments/formatters/__pycache__/irc.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/pygments/formatters/__pycache__/latex.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/pygments/formatters/__pycache__/other.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/pygments/formatters/__pycache__/pangomarkup.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/pygments/formatters/__pycache__/rtf.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/pygments/formatters/__pycache__/svg.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/pygments/formatters/__pycache__/terminal.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/pygments/formatters/__pycache__/terminal256.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/pygments/formatters/_mapping.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/pygments/formatters/bbcode.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/pygments/formatters/groff.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/pygments/formatters/html.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/pygments/formatters/img.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/pygments/formatters/irc.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/pygments/formatters/latex.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/pygments/formatters/other.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/pygments/formatters/pangomarkup.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/pygments/formatters/rtf.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/pygments/formatters/svg.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/pygments/formatters/terminal.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/pygments/formatters/terminal256.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/pygments/lexer.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/pygments/lexers/__init__.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/pygments/lexers/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/pygments/lexers/__pycache__/_mapping.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/pygments/lexers/__pycache__/python.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/pygments/lexers/_mapping.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/pygments/lexers/python.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/pygments/modeline.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/pygments/plugin.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/pygments/regexopt.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/pygments/scanner.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/pygments/sphinxext.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/pygments/style.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/pygments/styles/__init__.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/pygments/styles/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/pygments/token.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/pygments/unistring.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/pygments/util.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/pyparsing/__init__.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/pyparsing/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/pyparsing/__pycache__/actions.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/pyparsing/__pycache__/common.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/pyparsing/__pycache__/core.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/pyparsing/__pycache__/exceptions.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/pyparsing/__pycache__/helpers.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/pyparsing/__pycache__/results.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/pyparsing/__pycache__/testing.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/pyparsing/__pycache__/unicode.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/pyparsing/__pycache__/util.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/pyparsing/actions.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/pyparsing/common.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/pyparsing/core.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/pyparsing/diagram/__init__.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/pyparsing/diagram/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/pyparsing/exceptions.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/pyparsing/helpers.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/pyparsing/py.typed
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/pyparsing/results.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/pyparsing/testing.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/pyparsing/unicode.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/pyparsing/util.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/pyproject_hooks/__init__.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/pyproject_hooks/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/pyproject_hooks/__pycache__/_compat.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/pyproject_hooks/__pycache__/_impl.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/pyproject_hooks/_compat.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/pyproject_hooks/_impl.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/pyproject_hooks/_in_process/__init__.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/pyproject_hooks/_in_process/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/pyproject_hooks/_in_process/__pycache__/_in_process.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/pyproject_hooks/_in_process/_in_process.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/requests/__init__.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/requests/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/requests/__pycache__/__version__.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/requests/__pycache__/_internal_utils.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/requests/__pycache__/adapters.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/requests/__pycache__/api.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/requests/__pycache__/auth.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/requests/__pycache__/certs.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/requests/__pycache__/compat.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/requests/__pycache__/cookies.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/requests/__pycache__/exceptions.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/requests/__pycache__/help.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/requests/__pycache__/hooks.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/requests/__pycache__/models.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/requests/__pycache__/packages.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/requests/__pycache__/sessions.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/requests/__pycache__/status_codes.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/requests/__pycache__/structures.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/requests/__pycache__/utils.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/requests/__version__.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/requests/_internal_utils.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/requests/adapters.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/requests/api.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/requests/auth.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/requests/certs.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/requests/compat.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/requests/cookies.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/requests/exceptions.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/requests/help.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/requests/hooks.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/requests/models.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/requests/packages.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/requests/sessions.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/requests/status_codes.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/requests/structures.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/requests/utils.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/resolvelib/__init__.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/resolvelib/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/resolvelib/__pycache__/providers.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/resolvelib/__pycache__/reporters.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/resolvelib/__pycache__/resolvers.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/resolvelib/__pycache__/structs.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/resolvelib/compat/__init__.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/resolvelib/compat/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/resolvelib/compat/__pycache__/collections_abc.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/resolvelib/compat/collections_abc.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/resolvelib/providers.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/resolvelib/py.typed
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/resolvelib/reporters.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/resolvelib/resolvers.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/resolvelib/structs.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/rich/__init__.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/rich/__main__.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/rich/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/rich/__pycache__/__main__.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/rich/__pycache__/_cell_widths.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/rich/__pycache__/_emoji_codes.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/rich/__pycache__/_emoji_replace.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/rich/__pycache__/_export_format.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/rich/__pycache__/_extension.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/rich/__pycache__/_fileno.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/rich/__pycache__/_inspect.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/rich/__pycache__/_log_render.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/rich/__pycache__/_loop.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/rich/__pycache__/_null_file.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/rich/__pycache__/_palettes.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/rich/__pycache__/_pick.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/rich/__pycache__/_ratio.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/rich/__pycache__/_spinners.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/rich/__pycache__/_stack.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/rich/__pycache__/_timer.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/rich/__pycache__/_win32_console.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/rich/__pycache__/_windows.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/rich/__pycache__/_windows_renderer.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/rich/__pycache__/_wrap.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/rich/__pycache__/abc.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/rich/__pycache__/align.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/rich/__pycache__/ansi.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/rich/__pycache__/bar.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/rich/__pycache__/box.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/rich/__pycache__/cells.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/rich/__pycache__/color.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/rich/__pycache__/color_triplet.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/rich/__pycache__/columns.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/rich/__pycache__/console.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/rich/__pycache__/constrain.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/rich/__pycache__/containers.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/rich/__pycache__/control.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/rich/__pycache__/default_styles.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/rich/__pycache__/diagnose.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/rich/__pycache__/emoji.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/rich/__pycache__/errors.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/rich/__pycache__/file_proxy.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/rich/__pycache__/filesize.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/rich/__pycache__/highlighter.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/rich/__pycache__/json.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/rich/__pycache__/jupyter.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/rich/__pycache__/layout.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/rich/__pycache__/live.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/rich/__pycache__/live_render.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/rich/__pycache__/logging.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/rich/__pycache__/markup.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/rich/__pycache__/measure.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/rich/__pycache__/padding.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/rich/__pycache__/pager.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/rich/__pycache__/palette.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/rich/__pycache__/panel.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/rich/__pycache__/pretty.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/rich/__pycache__/progress.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/rich/__pycache__/progress_bar.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/rich/__pycache__/prompt.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/rich/__pycache__/protocol.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/rich/__pycache__/region.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/rich/__pycache__/repr.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/rich/__pycache__/rule.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/rich/__pycache__/scope.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/rich/__pycache__/screen.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/rich/__pycache__/segment.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/rich/__pycache__/spinner.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/rich/__pycache__/status.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/rich/__pycache__/style.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/rich/__pycache__/styled.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/rich/__pycache__/syntax.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/rich/__pycache__/table.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/rich/__pycache__/terminal_theme.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/rich/__pycache__/text.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/rich/__pycache__/theme.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/rich/__pycache__/themes.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/rich/__pycache__/traceback.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/rich/__pycache__/tree.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/rich/_cell_widths.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/rich/_emoji_codes.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/rich/_emoji_replace.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/rich/_export_format.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/rich/_extension.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/rich/_fileno.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/rich/_inspect.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/rich/_log_render.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/rich/_loop.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/rich/_null_file.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/rich/_palettes.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/rich/_pick.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/rich/_ratio.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/rich/_spinners.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/rich/_stack.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/rich/_timer.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/rich/_win32_console.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/rich/_windows.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/rich/_windows_renderer.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/rich/_wrap.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/rich/abc.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/rich/align.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/rich/ansi.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/rich/bar.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/rich/box.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/rich/cells.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/rich/color.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/rich/color_triplet.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/rich/columns.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/rich/console.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/rich/constrain.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/rich/containers.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/rich/control.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/rich/default_styles.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/rich/diagnose.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/rich/emoji.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/rich/errors.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/rich/file_proxy.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/rich/filesize.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/rich/highlighter.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/rich/json.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/rich/jupyter.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/rich/layout.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/rich/live.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/rich/live_render.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/rich/logging.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/rich/markup.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/rich/measure.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/rich/padding.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/rich/pager.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/rich/palette.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/rich/panel.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/rich/pretty.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/rich/progress.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/rich/progress_bar.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/rich/prompt.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/rich/protocol.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/rich/py.typed
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/rich/region.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/rich/repr.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/rich/rule.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/rich/scope.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/rich/screen.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/rich/segment.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/rich/spinner.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/rich/status.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/rich/style.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/rich/styled.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/rich/syntax.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/rich/table.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/rich/terminal_theme.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/rich/text.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/rich/theme.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/rich/themes.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/rich/traceback.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/rich/tree.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/six.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/tenacity/__init__.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/tenacity/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/tenacity/__pycache__/_asyncio.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/tenacity/__pycache__/_utils.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/tenacity/__pycache__/after.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/tenacity/__pycache__/before.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/tenacity/__pycache__/before_sleep.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/tenacity/__pycache__/nap.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/tenacity/__pycache__/retry.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/tenacity/__pycache__/stop.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/tenacity/__pycache__/tornadoweb.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/tenacity/__pycache__/wait.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/tenacity/_asyncio.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/tenacity/_utils.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/tenacity/after.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/tenacity/before.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/tenacity/before_sleep.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/tenacity/nap.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/tenacity/py.typed
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/tenacity/retry.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/tenacity/stop.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/tenacity/tornadoweb.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/tenacity/wait.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/tomli/__init__.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/tomli/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/tomli/__pycache__/_parser.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/tomli/__pycache__/_re.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/tomli/__pycache__/_types.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/tomli/_parser.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/tomli/_re.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/tomli/_types.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/tomli/py.typed
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/truststore/__init__.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/truststore/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/truststore/__pycache__/_api.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/truststore/__pycache__/_macos.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/truststore/__pycache__/_openssl.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/truststore/__pycache__/_ssl_constants.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/truststore/__pycache__/_windows.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/truststore/_api.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/truststore/_macos.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/truststore/_openssl.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/truststore/_ssl_constants.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/truststore/_windows.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/truststore/py.typed
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/typing_extensions.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/urllib3/__init__.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/urllib3/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/urllib3/__pycache__/_collections.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/urllib3/__pycache__/_version.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/urllib3/__pycache__/connection.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/urllib3/__pycache__/connectionpool.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/urllib3/__pycache__/exceptions.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/urllib3/__pycache__/fields.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/urllib3/__pycache__/filepost.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/urllib3/__pycache__/poolmanager.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/urllib3/__pycache__/request.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/urllib3/__pycache__/response.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/urllib3/_collections.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/urllib3/_version.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/urllib3/connection.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/urllib3/connectionpool.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/urllib3/contrib/__init__.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/urllib3/contrib/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/urllib3/contrib/__pycache__/_appengine_environ.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/urllib3/contrib/__pycache__/appengine.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/urllib3/contrib/__pycache__/ntlmpool.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/urllib3/contrib/__pycache__/pyopenssl.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/urllib3/contrib/__pycache__/securetransport.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/urllib3/contrib/__pycache__/socks.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/urllib3/contrib/_appengine_environ.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/urllib3/contrib/_securetransport/__init__.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/urllib3/contrib/_securetransport/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/urllib3/contrib/_securetransport/__pycache__/bindings.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/urllib3/contrib/_securetransport/__pycache__/low_level.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/urllib3/contrib/_securetransport/bindings.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/urllib3/contrib/_securetransport/low_level.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/urllib3/contrib/appengine.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/urllib3/contrib/ntlmpool.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/urllib3/contrib/pyopenssl.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/urllib3/contrib/securetransport.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/urllib3/contrib/socks.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/urllib3/exceptions.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/urllib3/fields.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/urllib3/filepost.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/urllib3/packages/__init__.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/urllib3/packages/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/urllib3/packages/__pycache__/six.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/urllib3/packages/backports/__init__.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/urllib3/packages/backports/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/urllib3/packages/backports/__pycache__/makefile.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/urllib3/packages/backports/__pycache__/weakref_finalize.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/urllib3/packages/backports/makefile.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/urllib3/packages/backports/weakref_finalize.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/urllib3/packages/six.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/urllib3/poolmanager.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/urllib3/request.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/urllib3/response.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/urllib3/util/__init__.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/urllib3/util/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/urllib3/util/__pycache__/connection.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/urllib3/util/__pycache__/proxy.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/urllib3/util/__pycache__/queue.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/urllib3/util/__pycache__/request.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/urllib3/util/__pycache__/response.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/urllib3/util/__pycache__/retry.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/urllib3/util/__pycache__/ssl_.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/urllib3/util/__pycache__/ssl_match_hostname.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/urllib3/util/__pycache__/ssltransport.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/urllib3/util/__pycache__/timeout.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/urllib3/util/__pycache__/url.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/urllib3/util/__pycache__/wait.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/urllib3/util/connection.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/urllib3/util/proxy.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/urllib3/util/queue.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/urllib3/util/request.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/urllib3/util/response.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/urllib3/util/retry.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/urllib3/util/ssl_.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/urllib3/util/ssl_match_hostname.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/urllib3/util/ssltransport.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/urllib3/util/timeout.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/urllib3/util/url.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/urllib3/util/wait.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/webencodings/__init__.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/webencodings/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/webencodings/__pycache__/labels.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/webencodings/__pycache__/mklabels.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/webencodings/__pycache__/tests.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/webencodings/__pycache__/x_user_defined.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/webencodings/labels.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/webencodings/mklabels.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/webencodings/tests.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/_vendor/webencodings/x_user_defined.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pip/py.typed
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pkg_resources/__init__.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pkg_resources/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pkg_resources/_vendor/__init__.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pkg_resources/_vendor/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pkg_resources/_vendor/__pycache__/appdirs.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pkg_resources/_vendor/__pycache__/zipp.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pkg_resources/_vendor/appdirs.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pkg_resources/_vendor/importlib_resources/__init__.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pkg_resources/_vendor/importlib_resources/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pkg_resources/_vendor/importlib_resources/__pycache__/_adapters.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pkg_resources/_vendor/importlib_resources/__pycache__/_common.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pkg_resources/_vendor/importlib_resources/__pycache__/_compat.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pkg_resources/_vendor/importlib_resources/__pycache__/_itertools.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pkg_resources/_vendor/importlib_resources/__pycache__/_legacy.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pkg_resources/_vendor/importlib_resources/__pycache__/abc.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pkg_resources/_vendor/importlib_resources/__pycache__/readers.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pkg_resources/_vendor/importlib_resources/__pycache__/simple.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pkg_resources/_vendor/importlib_resources/_adapters.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pkg_resources/_vendor/importlib_resources/_common.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pkg_resources/_vendor/importlib_resources/_compat.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pkg_resources/_vendor/importlib_resources/_itertools.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pkg_resources/_vendor/importlib_resources/_legacy.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pkg_resources/_vendor/importlib_resources/abc.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pkg_resources/_vendor/importlib_resources/readers.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pkg_resources/_vendor/importlib_resources/simple.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pkg_resources/_vendor/jaraco/__init__.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pkg_resources/_vendor/jaraco/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pkg_resources/_vendor/jaraco/__pycache__/context.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pkg_resources/_vendor/jaraco/__pycache__/functools.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pkg_resources/_vendor/jaraco/context.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pkg_resources/_vendor/jaraco/functools.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pkg_resources/_vendor/jaraco/text/__init__.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pkg_resources/_vendor/jaraco/text/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pkg_resources/_vendor/more_itertools/__init__.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pkg_resources/_vendor/more_itertools/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pkg_resources/_vendor/more_itertools/__pycache__/more.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pkg_resources/_vendor/more_itertools/__pycache__/recipes.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pkg_resources/_vendor/more_itertools/more.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pkg_resources/_vendor/more_itertools/recipes.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pkg_resources/_vendor/packaging/__about__.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pkg_resources/_vendor/packaging/__init__.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pkg_resources/_vendor/packaging/__pycache__/__about__.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pkg_resources/_vendor/packaging/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pkg_resources/_vendor/packaging/__pycache__/_manylinux.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pkg_resources/_vendor/packaging/__pycache__/_musllinux.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pkg_resources/_vendor/packaging/__pycache__/_structures.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pkg_resources/_vendor/packaging/__pycache__/markers.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pkg_resources/_vendor/packaging/__pycache__/requirements.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pkg_resources/_vendor/packaging/__pycache__/specifiers.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pkg_resources/_vendor/packaging/__pycache__/tags.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pkg_resources/_vendor/packaging/__pycache__/utils.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pkg_resources/_vendor/packaging/__pycache__/version.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pkg_resources/_vendor/packaging/_manylinux.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pkg_resources/_vendor/packaging/_musllinux.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pkg_resources/_vendor/packaging/_structures.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pkg_resources/_vendor/packaging/markers.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pkg_resources/_vendor/packaging/requirements.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pkg_resources/_vendor/packaging/specifiers.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pkg_resources/_vendor/packaging/tags.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pkg_resources/_vendor/packaging/utils.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pkg_resources/_vendor/packaging/version.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pkg_resources/_vendor/pyparsing/__init__.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pkg_resources/_vendor/pyparsing/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pkg_resources/_vendor/pyparsing/__pycache__/actions.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pkg_resources/_vendor/pyparsing/__pycache__/common.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pkg_resources/_vendor/pyparsing/__pycache__/core.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pkg_resources/_vendor/pyparsing/__pycache__/exceptions.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pkg_resources/_vendor/pyparsing/__pycache__/helpers.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pkg_resources/_vendor/pyparsing/__pycache__/results.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pkg_resources/_vendor/pyparsing/__pycache__/testing.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pkg_resources/_vendor/pyparsing/__pycache__/unicode.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pkg_resources/_vendor/pyparsing/__pycache__/util.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pkg_resources/_vendor/pyparsing/actions.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pkg_resources/_vendor/pyparsing/common.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pkg_resources/_vendor/pyparsing/core.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pkg_resources/_vendor/pyparsing/diagram/__init__.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pkg_resources/_vendor/pyparsing/diagram/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pkg_resources/_vendor/pyparsing/exceptions.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pkg_resources/_vendor/pyparsing/helpers.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pkg_resources/_vendor/pyparsing/results.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pkg_resources/_vendor/pyparsing/testing.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pkg_resources/_vendor/pyparsing/unicode.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pkg_resources/_vendor/pyparsing/util.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pkg_resources/_vendor/zipp.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pkg_resources/extern/__init__.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pkg_resources/extern/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pycparser-2.22.dist-info/INSTALLER
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pycparser-2.22.dist-info/LICENSE
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pycparser-2.22.dist-info/METADATA
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pycparser-2.22.dist-info/RECORD
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pycparser-2.22.dist-info/WHEEL
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pycparser/__init__.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pycparser/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pycparser/__pycache__/_ast_gen.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pycparser/__pycache__/_build_tables.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pycparser/__pycache__/ast_transforms.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pycparser/__pycache__/c_ast.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pycparser/__pycache__/c_generator.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pycparser/__pycache__/c_lexer.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pycparser/__pycache__/c_parser.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pycparser/__pycache__/lextab.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pycparser/__pycache__/plyparser.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pycparser/__pycache__/yacctab.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pycparser/_ast_gen.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pycparser/_build_tables.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pycparser/_c_ast.cfg
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pycparser/ast_transforms.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pycparser/c_ast.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pycparser/c_generator.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pycparser/c_lexer.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pycparser/c_parser.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pycparser/lextab.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pycparser/ply/__init__.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pycparser/ply/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pycparser/ply/__pycache__/cpp.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pycparser/ply/__pycache__/ctokens.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pycparser/ply/__pycache__/lex.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pycparser/ply/__pycache__/yacc.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pycparser/ply/__pycache__/ygen.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pycparser/ply/cpp.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pycparser/ply/ctokens.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pycparser/ply/lex.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pycparser/ply/yacc.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pycparser/ply/ygen.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pycparser/plyparser.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pycparser/yacctab.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pydub-0.25.1.dist-info/AUTHORS
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pydub-0.25.1.dist-info/INSTALLER
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pydub-0.25.1.dist-info/LICENSE
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pydub-0.25.1.dist-info/METADATA
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pydub-0.25.1.dist-info/RECORD
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pydub-0.25.1.dist-info/REQUESTED
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pydub-0.25.1.dist-info/WHEEL
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pydub/__init__.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pydub/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pydub/__pycache__/audio_segment.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pydub/__pycache__/effects.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pydub/__pycache__/exceptions.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pydub/__pycache__/generators.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pydub/__pycache__/logging_utils.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pydub/__pycache__/playback.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pydub/__pycache__/pyaudioop.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pydub/__pycache__/scipy_effects.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pydub/__pycache__/silence.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pydub/__pycache__/utils.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pydub/audio_segment.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pydub/effects.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pydub/exceptions.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pydub/generators.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pydub/logging_utils.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pydub/playback.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pydub/pyaudioop.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pydub/scipy_effects.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pydub/silence.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/pydub/utils.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/python_dotenv-1.1.0.dist-info/INSTALLER
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/python_dotenv-1.1.0.dist-info/METADATA
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/python_dotenv-1.1.0.dist-info/RECORD
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/python_dotenv-1.1.0.dist-info/REQUESTED
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/python_dotenv-1.1.0.dist-info/WHEEL
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/python_dotenv-1.1.0.dist-info/licenses/LICENSE
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/requests-2.32.3.dist-info/INSTALLER
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/requests-2.32.3.dist-info/LICENSE
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/requests-2.32.3.dist-info/METADATA
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/requests-2.32.3.dist-info/RECORD
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/requests-2.32.3.dist-info/REQUESTED
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/requests-2.32.3.dist-info/WHEEL
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/requests/__init__.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/requests/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/requests/__pycache__/__version__.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/requests/__pycache__/_internal_utils.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/requests/__pycache__/adapters.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/requests/__pycache__/api.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/requests/__pycache__/auth.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/requests/__pycache__/certs.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/requests/__pycache__/compat.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/requests/__pycache__/cookies.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/requests/__pycache__/exceptions.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/requests/__pycache__/help.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/requests/__pycache__/hooks.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/requests/__pycache__/models.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/requests/__pycache__/packages.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/requests/__pycache__/sessions.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/requests/__pycache__/status_codes.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/requests/__pycache__/structures.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/requests/__pycache__/utils.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/requests/__version__.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/requests/_internal_utils.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/requests/adapters.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/requests/api.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/requests/auth.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/requests/certs.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/requests/compat.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/requests/cookies.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/requests/exceptions.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/requests/help.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/requests/hooks.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/requests/models.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/requests/packages.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/requests/sessions.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/requests/status_codes.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/requests/structures.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/requests/utils.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools-65.5.0.dist-info/INSTALLER
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools-65.5.0.dist-info/LICENSE
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools-65.5.0.dist-info/METADATA
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools-65.5.0.dist-info/RECORD
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools-65.5.0.dist-info/REQUESTED
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools-65.5.0.dist-info/WHEEL
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/__init__.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/__pycache__/_deprecation_warning.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/__pycache__/_entry_points.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/__pycache__/_imp.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/__pycache__/_importlib.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/__pycache__/_itertools.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/__pycache__/_path.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/__pycache__/_reqs.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/__pycache__/archive_util.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/__pycache__/build_meta.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/__pycache__/dep_util.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/__pycache__/depends.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/__pycache__/discovery.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/__pycache__/dist.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/__pycache__/errors.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/__pycache__/extension.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/__pycache__/glob.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/__pycache__/installer.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/__pycache__/launch.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/__pycache__/logging.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/__pycache__/monkey.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/__pycache__/msvc.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/__pycache__/namespaces.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/__pycache__/package_index.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/__pycache__/py34compat.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/__pycache__/sandbox.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/__pycache__/unicode_utils.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/__pycache__/version.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/__pycache__/wheel.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/__pycache__/windows_support.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_deprecation_warning.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_distutils/__init__.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_distutils/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_distutils/__pycache__/_collections.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_distutils/__pycache__/_functools.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_distutils/__pycache__/_macos_compat.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_distutils/__pycache__/_msvccompiler.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_distutils/__pycache__/archive_util.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_distutils/__pycache__/bcppcompiler.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_distutils/__pycache__/ccompiler.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_distutils/__pycache__/cmd.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_distutils/__pycache__/config.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_distutils/__pycache__/core.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_distutils/__pycache__/cygwinccompiler.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_distutils/__pycache__/debug.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_distutils/__pycache__/dep_util.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_distutils/__pycache__/dir_util.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_distutils/__pycache__/dist.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_distutils/__pycache__/errors.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_distutils/__pycache__/extension.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_distutils/__pycache__/fancy_getopt.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_distutils/__pycache__/file_util.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_distutils/__pycache__/filelist.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_distutils/__pycache__/log.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_distutils/__pycache__/msvc9compiler.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_distutils/__pycache__/msvccompiler.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_distutils/__pycache__/py38compat.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_distutils/__pycache__/py39compat.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_distutils/__pycache__/spawn.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_distutils/__pycache__/sysconfig.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_distutils/__pycache__/text_file.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_distutils/__pycache__/unixccompiler.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_distutils/__pycache__/util.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_distutils/__pycache__/version.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_distutils/__pycache__/versionpredicate.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_distutils/_collections.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_distutils/_functools.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_distutils/_macos_compat.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_distutils/_msvccompiler.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_distutils/archive_util.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_distutils/bcppcompiler.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_distutils/ccompiler.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_distutils/cmd.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_distutils/command/__init__.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_distutils/command/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_distutils/command/__pycache__/_framework_compat.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_distutils/command/__pycache__/bdist.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_distutils/command/__pycache__/bdist_dumb.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_distutils/command/__pycache__/bdist_rpm.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_distutils/command/__pycache__/build.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_distutils/command/__pycache__/build_clib.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_distutils/command/__pycache__/build_ext.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_distutils/command/__pycache__/build_py.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_distutils/command/__pycache__/build_scripts.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_distutils/command/__pycache__/check.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_distutils/command/__pycache__/clean.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_distutils/command/__pycache__/config.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_distutils/command/__pycache__/install.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_distutils/command/__pycache__/install_data.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_distutils/command/__pycache__/install_egg_info.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_distutils/command/__pycache__/install_headers.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_distutils/command/__pycache__/install_lib.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_distutils/command/__pycache__/install_scripts.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_distutils/command/__pycache__/py37compat.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_distutils/command/__pycache__/register.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_distutils/command/__pycache__/sdist.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_distutils/command/__pycache__/upload.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_distutils/command/_framework_compat.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_distutils/command/bdist.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_distutils/command/bdist_dumb.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_distutils/command/bdist_rpm.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_distutils/command/build.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_distutils/command/build_clib.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_distutils/command/build_ext.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_distutils/command/build_py.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_distutils/command/build_scripts.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_distutils/command/check.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_distutils/command/clean.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_distutils/command/config.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_distutils/command/install.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_distutils/command/install_data.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_distutils/command/install_egg_info.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_distutils/command/install_headers.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_distutils/command/install_lib.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_distutils/command/install_scripts.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_distutils/command/py37compat.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_distutils/command/register.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_distutils/command/sdist.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_distutils/command/upload.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_distutils/config.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_distutils/core.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_distutils/cygwinccompiler.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_distutils/debug.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_distutils/dep_util.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_distutils/dir_util.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_distutils/dist.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_distutils/errors.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_distutils/extension.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_distutils/fancy_getopt.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_distutils/file_util.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_distutils/filelist.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_distutils/log.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_distutils/msvc9compiler.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_distutils/msvccompiler.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_distutils/py38compat.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_distutils/py39compat.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_distutils/spawn.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_distutils/sysconfig.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_distutils/text_file.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_distutils/unixccompiler.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_distutils/util.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_distutils/version.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_distutils/versionpredicate.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_entry_points.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_imp.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_importlib.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_itertools.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_path.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_reqs.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_vendor/__init__.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_vendor/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_vendor/__pycache__/ordered_set.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_vendor/__pycache__/typing_extensions.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_vendor/__pycache__/zipp.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_vendor/importlib_metadata/__init__.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_vendor/importlib_metadata/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_vendor/importlib_metadata/__pycache__/_adapters.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_vendor/importlib_metadata/__pycache__/_collections.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_vendor/importlib_metadata/__pycache__/_compat.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_vendor/importlib_metadata/__pycache__/_functools.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_vendor/importlib_metadata/__pycache__/_itertools.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_vendor/importlib_metadata/__pycache__/_meta.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_vendor/importlib_metadata/__pycache__/_text.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_vendor/importlib_metadata/_adapters.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_vendor/importlib_metadata/_collections.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_vendor/importlib_metadata/_compat.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_vendor/importlib_metadata/_functools.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_vendor/importlib_metadata/_itertools.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_vendor/importlib_metadata/_meta.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_vendor/importlib_metadata/_text.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_vendor/importlib_resources/__init__.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_vendor/importlib_resources/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_vendor/importlib_resources/__pycache__/_adapters.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_vendor/importlib_resources/__pycache__/_common.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_vendor/importlib_resources/__pycache__/_compat.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_vendor/importlib_resources/__pycache__/_itertools.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_vendor/importlib_resources/__pycache__/_legacy.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_vendor/importlib_resources/__pycache__/abc.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_vendor/importlib_resources/__pycache__/readers.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_vendor/importlib_resources/__pycache__/simple.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_vendor/importlib_resources/_adapters.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_vendor/importlib_resources/_common.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_vendor/importlib_resources/_compat.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_vendor/importlib_resources/_itertools.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_vendor/importlib_resources/_legacy.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_vendor/importlib_resources/abc.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_vendor/importlib_resources/readers.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_vendor/importlib_resources/simple.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_vendor/jaraco/__init__.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_vendor/jaraco/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_vendor/jaraco/__pycache__/context.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_vendor/jaraco/__pycache__/functools.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_vendor/jaraco/context.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_vendor/jaraco/functools.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_vendor/jaraco/text/__init__.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_vendor/jaraco/text/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_vendor/more_itertools/__init__.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_vendor/more_itertools/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_vendor/more_itertools/__pycache__/more.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_vendor/more_itertools/__pycache__/recipes.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_vendor/more_itertools/more.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_vendor/more_itertools/recipes.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_vendor/ordered_set.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_vendor/packaging/__about__.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_vendor/packaging/__init__.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_vendor/packaging/__pycache__/__about__.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_vendor/packaging/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_vendor/packaging/__pycache__/_manylinux.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_vendor/packaging/__pycache__/_musllinux.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_vendor/packaging/__pycache__/_structures.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_vendor/packaging/__pycache__/markers.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_vendor/packaging/__pycache__/requirements.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_vendor/packaging/__pycache__/specifiers.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_vendor/packaging/__pycache__/tags.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_vendor/packaging/__pycache__/utils.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_vendor/packaging/__pycache__/version.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_vendor/packaging/_manylinux.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_vendor/packaging/_musllinux.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_vendor/packaging/_structures.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_vendor/packaging/markers.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_vendor/packaging/requirements.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_vendor/packaging/specifiers.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_vendor/packaging/tags.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_vendor/packaging/utils.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_vendor/packaging/version.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_vendor/pyparsing/__init__.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_vendor/pyparsing/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_vendor/pyparsing/__pycache__/actions.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_vendor/pyparsing/__pycache__/common.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_vendor/pyparsing/__pycache__/core.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_vendor/pyparsing/__pycache__/exceptions.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_vendor/pyparsing/__pycache__/helpers.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_vendor/pyparsing/__pycache__/results.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_vendor/pyparsing/__pycache__/testing.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_vendor/pyparsing/__pycache__/unicode.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_vendor/pyparsing/__pycache__/util.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_vendor/pyparsing/actions.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_vendor/pyparsing/common.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_vendor/pyparsing/core.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_vendor/pyparsing/diagram/__init__.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_vendor/pyparsing/diagram/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_vendor/pyparsing/exceptions.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_vendor/pyparsing/helpers.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_vendor/pyparsing/results.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_vendor/pyparsing/testing.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_vendor/pyparsing/unicode.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_vendor/pyparsing/util.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_vendor/tomli/__init__.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_vendor/tomli/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_vendor/tomli/__pycache__/_parser.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_vendor/tomli/__pycache__/_re.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_vendor/tomli/__pycache__/_types.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_vendor/tomli/_parser.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_vendor/tomli/_re.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_vendor/tomli/_types.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_vendor/typing_extensions.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/_vendor/zipp.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/archive_util.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/build_meta.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/cli-32.exe
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/cli-64.exe
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/cli-arm64.exe
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/cli.exe
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/command/__init__.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/command/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/command/__pycache__/alias.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/command/__pycache__/bdist_egg.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/command/__pycache__/bdist_rpm.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/command/__pycache__/build.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/command/__pycache__/build_clib.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/command/__pycache__/build_ext.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/command/__pycache__/build_py.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/command/__pycache__/develop.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/command/__pycache__/dist_info.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/command/__pycache__/easy_install.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/command/__pycache__/editable_wheel.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/command/__pycache__/egg_info.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/command/__pycache__/install.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/command/__pycache__/install_egg_info.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/command/__pycache__/install_lib.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/command/__pycache__/install_scripts.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/command/__pycache__/py36compat.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/command/__pycache__/register.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/command/__pycache__/rotate.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/command/__pycache__/saveopts.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/command/__pycache__/sdist.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/command/__pycache__/setopt.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/command/__pycache__/test.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/command/__pycache__/upload.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/command/__pycache__/upload_docs.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/command/alias.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/command/bdist_egg.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/command/bdist_rpm.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/command/build.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/command/build_clib.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/command/build_ext.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/command/build_py.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/command/develop.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/command/dist_info.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/command/easy_install.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/command/editable_wheel.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/command/egg_info.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/command/install.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/command/install_egg_info.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/command/install_lib.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/command/install_scripts.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/command/launcher manifest.xml
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/command/py36compat.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/command/register.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/command/rotate.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/command/saveopts.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/command/sdist.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/command/setopt.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/command/test.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/command/upload.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/command/upload_docs.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/config/__init__.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/config/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/config/__pycache__/_apply_pyprojecttoml.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/config/__pycache__/expand.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/config/__pycache__/pyprojecttoml.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/config/__pycache__/setupcfg.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/config/_apply_pyprojecttoml.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/config/_validate_pyproject/__init__.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/config/_validate_pyproject/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/config/_validate_pyproject/__pycache__/error_reporting.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/config/_validate_pyproject/__pycache__/extra_validations.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/config/_validate_pyproject/__pycache__/fastjsonschema_exceptions.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/config/_validate_pyproject/__pycache__/fastjsonschema_validations.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/config/_validate_pyproject/__pycache__/formats.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/config/_validate_pyproject/error_reporting.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/config/_validate_pyproject/extra_validations.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/config/_validate_pyproject/fastjsonschema_exceptions.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/config/_validate_pyproject/fastjsonschema_validations.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/config/_validate_pyproject/formats.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/config/expand.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/config/pyprojecttoml.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/config/setupcfg.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/dep_util.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/depends.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/discovery.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/dist.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/errors.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/extension.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/extern/__init__.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/extern/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/glob.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/gui-32.exe
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/gui-64.exe
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/gui-arm64.exe
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/gui.exe
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/installer.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/launch.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/logging.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/monkey.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/msvc.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/namespaces.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/package_index.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/py34compat.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/sandbox.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/script (dev).tmpl
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/script.tmpl
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/unicode_utils.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/version.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/wheel.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/setuptools/windows_support.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/sounddevice-0.5.1.dist-info/INSTALLER
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/sounddevice-0.5.1.dist-info/LICENSE
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/sounddevice-0.5.1.dist-info/METADATA
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/sounddevice-0.5.1.dist-info/RECORD
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/sounddevice-0.5.1.dist-info/REQUESTED
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/sounddevice-0.5.1.dist-info/WHEEL
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/sounddevice.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/soundfile-0.13.1.dist-info/INSTALLER
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/soundfile-0.13.1.dist-info/LICENSE
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/soundfile-0.13.1.dist-info/METADATA
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/soundfile-0.13.1.dist-info/RECORD
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/soundfile-0.13.1.dist-info/REQUESTED
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/soundfile-0.13.1.dist-info/WHEEL
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/soundfile.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/urllib3-2.4.0.dist-info/INSTALLER
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/urllib3-2.4.0.dist-info/METADATA
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/urllib3-2.4.0.dist-info/RECORD
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/urllib3-2.4.0.dist-info/WHEEL
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/urllib3/__init__.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/urllib3/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/urllib3/__pycache__/_base_connection.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/urllib3/__pycache__/_collections.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/urllib3/__pycache__/_request_methods.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/urllib3/__pycache__/_version.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/urllib3/__pycache__/connection.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/urllib3/__pycache__/connectionpool.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/urllib3/__pycache__/exceptions.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/urllib3/__pycache__/fields.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/urllib3/__pycache__/filepost.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/urllib3/__pycache__/poolmanager.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/urllib3/__pycache__/response.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/urllib3/_base_connection.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/urllib3/_collections.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/urllib3/_request_methods.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/urllib3/_version.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/urllib3/connection.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/urllib3/connectionpool.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/urllib3/contrib/__init__.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/urllib3/contrib/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/urllib3/contrib/__pycache__/pyopenssl.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/urllib3/contrib/__pycache__/socks.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/urllib3/contrib/emscripten/__init__.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/urllib3/contrib/emscripten/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/urllib3/contrib/emscripten/__pycache__/connection.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/urllib3/contrib/emscripten/__pycache__/fetch.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/urllib3/contrib/emscripten/__pycache__/request.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/urllib3/contrib/emscripten/__pycache__/response.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/urllib3/contrib/emscripten/connection.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/urllib3/contrib/emscripten/emscripten_fetch_worker.js
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/urllib3/contrib/emscripten/fetch.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/urllib3/contrib/emscripten/request.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/urllib3/contrib/emscripten/response.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/urllib3/contrib/pyopenssl.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/urllib3/contrib/socks.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/urllib3/exceptions.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/urllib3/fields.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/urllib3/filepost.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/urllib3/http2/__init__.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/urllib3/http2/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/urllib3/http2/__pycache__/connection.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/urllib3/http2/__pycache__/probe.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/urllib3/http2/connection.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/urllib3/http2/probe.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/urllib3/poolmanager.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/urllib3/py.typed
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/urllib3/response.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/urllib3/util/__init__.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/urllib3/util/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/urllib3/util/__pycache__/connection.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/urllib3/util/__pycache__/proxy.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/urllib3/util/__pycache__/request.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/urllib3/util/__pycache__/response.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/urllib3/util/__pycache__/retry.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/urllib3/util/__pycache__/ssl_.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/urllib3/util/__pycache__/ssl_match_hostname.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/urllib3/util/__pycache__/ssltransport.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/urllib3/util/__pycache__/timeout.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/urllib3/util/__pycache__/url.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/urllib3/util/__pycache__/util.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/urllib3/util/__pycache__/wait.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/urllib3/util/connection.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/urllib3/util/proxy.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/urllib3/util/request.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/urllib3/util/response.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/urllib3/util/retry.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/urllib3/util/ssl_.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/urllib3/util/ssl_match_hostname.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/urllib3/util/ssltransport.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/urllib3/util/timeout.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/urllib3/util/url.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/urllib3/util/util.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/urllib3/util/wait.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/werkzeug-3.1.3.dist-info/INSTALLER
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/werkzeug-3.1.3.dist-info/METADATA
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/werkzeug-3.1.3.dist-info/RECORD
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/werkzeug-3.1.3.dist-info/WHEEL
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/werkzeug/__init__.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/werkzeug/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/werkzeug/__pycache__/_internal.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/werkzeug/__pycache__/_reloader.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/werkzeug/__pycache__/exceptions.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/werkzeug/__pycache__/formparser.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/werkzeug/__pycache__/http.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/werkzeug/__pycache__/local.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/werkzeug/__pycache__/security.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/werkzeug/__pycache__/serving.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/werkzeug/__pycache__/test.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/werkzeug/__pycache__/testapp.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/werkzeug/__pycache__/urls.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/werkzeug/__pycache__/user_agent.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/werkzeug/__pycache__/utils.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/werkzeug/__pycache__/wsgi.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/werkzeug/_internal.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/werkzeug/_reloader.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/werkzeug/datastructures/__init__.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/werkzeug/datastructures/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/werkzeug/datastructures/__pycache__/accept.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/werkzeug/datastructures/__pycache__/auth.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/werkzeug/datastructures/__pycache__/cache_control.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/werkzeug/datastructures/__pycache__/csp.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/werkzeug/datastructures/__pycache__/etag.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/werkzeug/datastructures/__pycache__/file_storage.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/werkzeug/datastructures/__pycache__/headers.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/werkzeug/datastructures/__pycache__/mixins.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/werkzeug/datastructures/__pycache__/range.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/werkzeug/datastructures/__pycache__/structures.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/werkzeug/datastructures/accept.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/werkzeug/datastructures/auth.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/werkzeug/datastructures/cache_control.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/werkzeug/datastructures/csp.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/werkzeug/datastructures/etag.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/werkzeug/datastructures/file_storage.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/werkzeug/datastructures/headers.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/werkzeug/datastructures/mixins.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/werkzeug/datastructures/range.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/werkzeug/datastructures/structures.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/werkzeug/debug/__init__.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/werkzeug/debug/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/werkzeug/debug/__pycache__/console.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/werkzeug/debug/__pycache__/repr.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/werkzeug/debug/__pycache__/tbtools.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/werkzeug/debug/console.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/werkzeug/debug/repr.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/werkzeug/debug/shared/ICON_LICENSE.md
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/werkzeug/debug/shared/console.png
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/werkzeug/debug/shared/debugger.js
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/werkzeug/debug/shared/less.png
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/werkzeug/debug/shared/more.png
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/werkzeug/debug/shared/style.css
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/werkzeug/debug/tbtools.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/werkzeug/exceptions.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/werkzeug/formparser.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/werkzeug/http.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/werkzeug/local.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/werkzeug/middleware/__init__.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/werkzeug/middleware/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/werkzeug/middleware/__pycache__/dispatcher.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/werkzeug/middleware/__pycache__/http_proxy.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/werkzeug/middleware/__pycache__/lint.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/werkzeug/middleware/__pycache__/profiler.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/werkzeug/middleware/__pycache__/proxy_fix.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/werkzeug/middleware/__pycache__/shared_data.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/werkzeug/middleware/dispatcher.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/werkzeug/middleware/http_proxy.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/werkzeug/middleware/lint.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/werkzeug/middleware/profiler.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/werkzeug/middleware/proxy_fix.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/werkzeug/middleware/shared_data.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/werkzeug/py.typed
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/werkzeug/routing/__init__.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/werkzeug/routing/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/werkzeug/routing/__pycache__/converters.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/werkzeug/routing/__pycache__/exceptions.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/werkzeug/routing/__pycache__/map.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/werkzeug/routing/__pycache__/matcher.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/werkzeug/routing/__pycache__/rules.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/werkzeug/routing/converters.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/werkzeug/routing/exceptions.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/werkzeug/routing/map.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/werkzeug/routing/matcher.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/werkzeug/routing/rules.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/werkzeug/sansio/__init__.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/werkzeug/sansio/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/werkzeug/sansio/__pycache__/http.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/werkzeug/sansio/__pycache__/multipart.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/werkzeug/sansio/__pycache__/request.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/werkzeug/sansio/__pycache__/response.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/werkzeug/sansio/__pycache__/utils.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/werkzeug/sansio/http.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/werkzeug/sansio/multipart.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/werkzeug/sansio/request.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/werkzeug/sansio/response.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/werkzeug/sansio/utils.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/werkzeug/security.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/werkzeug/serving.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/werkzeug/test.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/werkzeug/testapp.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/werkzeug/urls.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/werkzeug/user_agent.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/werkzeug/utils.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/werkzeug/wrappers/__init__.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/werkzeug/wrappers/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/werkzeug/wrappers/__pycache__/request.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/werkzeug/wrappers/__pycache__/response.cpython-311.pyc
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/werkzeug/wrappers/request.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/werkzeug/wrappers/response.py
 create mode 100644 LICA/root@164.52.193.175/venv/lib/python3.11/site-packages/werkzeug/wsgi.py
 create mode 100644 LICA/root@164.52.193.175/venv/pyvenv.cfg
 create mode 100644 LICA/templates/index.html
 create mode 100644 LICA/venv/bin/Activate.ps1
 create mode 100644 LICA/venv/bin/activate
 create mode 100644 LICA/venv/bin/activate.csh
 create mode 100644 LICA/venv/bin/activate.fish
 create mode 100755 LICA/venv/bin/dotenv
 create mode 100755 LICA/venv/bin/flask
 create mode 100755 LICA/venv/bin/normalizer
 create mode 100755 LICA/venv/bin/pip
 create mode 100755 LICA/venv/bin/pip3
 create mode 100755 LICA/venv/bin/pip3.11
 create mode 120000 LICA/venv/bin/python
 create mode 120000 LICA/venv/bin/python3
 create mode 120000 LICA/venv/bin/python3.11
 create mode 100644 LICA/venv/include/site/python3.11/greenlet/greenlet.h
 create mode 100644 LICA/venv/lib/python3.11/site-packages/Flask_SocketIO-5.5.1.dist-info/INSTALLER
 create mode 100644 LICA/venv/lib/python3.11/site-packages/Flask_SocketIO-5.5.1.dist-info/LICENSE
 create mode 100644 LICA/venv/lib/python3.11/site-packages/Flask_SocketIO-5.5.1.dist-info/METADATA
 create mode 100644 LICA/venv/lib/python3.11/site-packages/Flask_SocketIO-5.5.1.dist-info/RECORD
 create mode 100644 LICA/venv/lib/python3.11/site-packages/Flask_SocketIO-5.5.1.dist-info/REQUESTED
 create mode 100644 LICA/venv/lib/python3.11/site-packages/Flask_SocketIO-5.5.1.dist-info/WHEEL
 create mode 100644 LICA/venv/lib/python3.11/site-packages/MarkupSafe-3.0.2.dist-info/INSTALLER
 create mode 100644 LICA/venv/lib/python3.11/site-packages/MarkupSafe-3.0.2.dist-info/METADATA
 create mode 100644 LICA/venv/lib/python3.11/site-packages/MarkupSafe-3.0.2.dist-info/RECORD
 create mode 100644 LICA/venv/lib/python3.11/site-packages/MarkupSafe-3.0.2.dist-info/WHEEL
 create mode 100644 LICA/venv/lib/python3.11/site-packages/_distutils_hack/__init__.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/_distutils_hack/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/_distutils_hack/__pycache__/override.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/_distutils_hack/override.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/bidict-0.23.1.dist-info/INSTALLER
 create mode 100644 LICA/venv/lib/python3.11/site-packages/bidict-0.23.1.dist-info/LICENSE
 create mode 100644 LICA/venv/lib/python3.11/site-packages/bidict-0.23.1.dist-info/METADATA
 create mode 100644 LICA/venv/lib/python3.11/site-packages/bidict-0.23.1.dist-info/RECORD
 create mode 100644 LICA/venv/lib/python3.11/site-packages/bidict-0.23.1.dist-info/WHEEL
 create mode 100644 LICA/venv/lib/python3.11/site-packages/bidict/__init__.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/bidict/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/bidict/__pycache__/_abc.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/bidict/__pycache__/_base.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/bidict/__pycache__/_bidict.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/bidict/__pycache__/_dup.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/bidict/__pycache__/_exc.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/bidict/__pycache__/_frozen.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/bidict/__pycache__/_iter.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/bidict/__pycache__/_orderedbase.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/bidict/__pycache__/_orderedbidict.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/bidict/__pycache__/_typing.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/bidict/__pycache__/metadata.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/bidict/_abc.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/bidict/_base.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/bidict/_bidict.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/bidict/_dup.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/bidict/_exc.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/bidict/_frozen.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/bidict/_iter.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/bidict/_orderedbase.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/bidict/_orderedbidict.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/bidict/_typing.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/bidict/metadata.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/bidict/py.typed
 create mode 100644 LICA/venv/lib/python3.11/site-packages/blinker-1.9.0.dist-info/INSTALLER
 create mode 100644 LICA/venv/lib/python3.11/site-packages/blinker-1.9.0.dist-info/METADATA
 create mode 100644 LICA/venv/lib/python3.11/site-packages/blinker-1.9.0.dist-info/RECORD
 create mode 100644 LICA/venv/lib/python3.11/site-packages/blinker-1.9.0.dist-info/WHEEL
 create mode 100644 LICA/venv/lib/python3.11/site-packages/blinker/__init__.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/blinker/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/blinker/__pycache__/_utilities.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/blinker/__pycache__/base.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/blinker/_utilities.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/blinker/base.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/blinker/py.typed
 create mode 100644 LICA/venv/lib/python3.11/site-packages/certifi-2025.4.26.dist-info/INSTALLER
 create mode 100644 LICA/venv/lib/python3.11/site-packages/certifi-2025.4.26.dist-info/METADATA
 create mode 100644 LICA/venv/lib/python3.11/site-packages/certifi-2025.4.26.dist-info/RECORD
 create mode 100644 LICA/venv/lib/python3.11/site-packages/certifi-2025.4.26.dist-info/WHEEL
 create mode 100644 LICA/venv/lib/python3.11/site-packages/certifi-2025.4.26.dist-info/licenses/LICENSE
 create mode 100644 LICA/venv/lib/python3.11/site-packages/certifi/__init__.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/certifi/__main__.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/certifi/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/certifi/__pycache__/__main__.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/certifi/__pycache__/core.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/certifi/cacert.pem
 create mode 100644 LICA/venv/lib/python3.11/site-packages/certifi/core.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/certifi/py.typed
 create mode 100644 LICA/venv/lib/python3.11/site-packages/charset_normalizer-3.4.2.dist-info/INSTALLER
 create mode 100644 LICA/venv/lib/python3.11/site-packages/charset_normalizer-3.4.2.dist-info/METADATA
 create mode 100644 LICA/venv/lib/python3.11/site-packages/charset_normalizer-3.4.2.dist-info/RECORD
 create mode 100644 LICA/venv/lib/python3.11/site-packages/charset_normalizer-3.4.2.dist-info/WHEEL
 create mode 100644 LICA/venv/lib/python3.11/site-packages/charset_normalizer-3.4.2.dist-info/licenses/LICENSE
 create mode 100644 LICA/venv/lib/python3.11/site-packages/charset_normalizer/__init__.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/charset_normalizer/__main__.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/charset_normalizer/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/charset_normalizer/__pycache__/__main__.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/charset_normalizer/__pycache__/api.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/charset_normalizer/__pycache__/cd.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/charset_normalizer/__pycache__/constant.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/charset_normalizer/__pycache__/legacy.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/charset_normalizer/__pycache__/md.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/charset_normalizer/__pycache__/models.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/charset_normalizer/__pycache__/utils.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/charset_normalizer/__pycache__/version.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/charset_normalizer/api.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/charset_normalizer/cd.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/charset_normalizer/cli/__init__.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/charset_normalizer/cli/__main__.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/charset_normalizer/cli/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/charset_normalizer/cli/__pycache__/__main__.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/charset_normalizer/constant.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/charset_normalizer/legacy.py
 create mode 100755 LICA/venv/lib/python3.11/site-packages/charset_normalizer/md.cpython-311-x86_64-linux-gnu.so
 create mode 100644 LICA/venv/lib/python3.11/site-packages/charset_normalizer/md.py
 create mode 100755 LICA/venv/lib/python3.11/site-packages/charset_normalizer/md__mypyc.cpython-311-x86_64-linux-gnu.so
 create mode 100644 LICA/venv/lib/python3.11/site-packages/charset_normalizer/models.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/charset_normalizer/py.typed
 create mode 100644 LICA/venv/lib/python3.11/site-packages/charset_normalizer/utils.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/charset_normalizer/version.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/click-8.1.8.dist-info/INSTALLER
 create mode 100644 LICA/venv/lib/python3.11/site-packages/click-8.1.8.dist-info/METADATA
 create mode 100644 LICA/venv/lib/python3.11/site-packages/click-8.1.8.dist-info/RECORD
 create mode 100644 LICA/venv/lib/python3.11/site-packages/click-8.1.8.dist-info/WHEEL
 create mode 100644 LICA/venv/lib/python3.11/site-packages/click/__init__.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/click/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/click/__pycache__/_compat.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/click/__pycache__/_termui_impl.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/click/__pycache__/_textwrap.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/click/__pycache__/_winconsole.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/click/__pycache__/core.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/click/__pycache__/decorators.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/click/__pycache__/exceptions.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/click/__pycache__/formatting.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/click/__pycache__/globals.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/click/__pycache__/parser.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/click/__pycache__/shell_completion.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/click/__pycache__/termui.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/click/__pycache__/testing.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/click/__pycache__/types.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/click/__pycache__/utils.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/click/_compat.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/click/_termui_impl.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/click/_textwrap.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/click/_winconsole.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/click/core.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/click/decorators.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/click/exceptions.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/click/formatting.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/click/globals.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/click/parser.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/click/py.typed
 create mode 100644 LICA/venv/lib/python3.11/site-packages/click/shell_completion.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/click/termui.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/click/testing.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/click/types.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/click/utils.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/distutils-precedence.pth
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/__init__.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/__pycache__/_asyncbackend.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/__pycache__/_asyncio_backend.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/__pycache__/_ddr.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/__pycache__/_features.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/__pycache__/_immutable_ctx.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/__pycache__/_trio_backend.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/__pycache__/asyncbackend.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/__pycache__/asyncquery.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/__pycache__/asyncresolver.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/__pycache__/dnssec.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/__pycache__/dnssectypes.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/__pycache__/e164.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/__pycache__/edns.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/__pycache__/entropy.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/__pycache__/enum.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/__pycache__/exception.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/__pycache__/flags.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/__pycache__/grange.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/__pycache__/immutable.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/__pycache__/inet.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/__pycache__/ipv4.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/__pycache__/ipv6.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/__pycache__/message.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/__pycache__/name.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/__pycache__/namedict.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/__pycache__/nameserver.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/__pycache__/node.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/__pycache__/opcode.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/__pycache__/query.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/__pycache__/rcode.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/__pycache__/rdata.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/__pycache__/rdataclass.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/__pycache__/rdataset.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/__pycache__/rdatatype.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/__pycache__/renderer.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/__pycache__/resolver.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/__pycache__/reversename.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/__pycache__/rrset.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/__pycache__/serial.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/__pycache__/set.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/__pycache__/tokenizer.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/__pycache__/transaction.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/__pycache__/tsig.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/__pycache__/tsigkeyring.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/__pycache__/ttl.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/__pycache__/update.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/__pycache__/version.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/__pycache__/versioned.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/__pycache__/win32util.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/__pycache__/wire.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/__pycache__/xfr.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/__pycache__/zone.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/__pycache__/zonefile.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/__pycache__/zonetypes.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/_asyncbackend.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/_asyncio_backend.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/_ddr.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/_features.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/_immutable_ctx.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/_trio_backend.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/asyncbackend.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/asyncquery.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/asyncresolver.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/dnssec.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/dnssecalgs/__init__.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/dnssecalgs/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/dnssecalgs/__pycache__/base.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/dnssecalgs/__pycache__/cryptography.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/dnssecalgs/__pycache__/dsa.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/dnssecalgs/__pycache__/ecdsa.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/dnssecalgs/__pycache__/eddsa.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/dnssecalgs/__pycache__/rsa.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/dnssecalgs/base.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/dnssecalgs/cryptography.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/dnssecalgs/dsa.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/dnssecalgs/ecdsa.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/dnssecalgs/eddsa.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/dnssecalgs/rsa.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/dnssectypes.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/e164.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/edns.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/entropy.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/enum.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/exception.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/flags.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/grange.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/immutable.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/inet.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/ipv4.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/ipv6.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/message.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/name.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/namedict.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/nameserver.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/node.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/opcode.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/py.typed
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/query.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/quic/__init__.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/quic/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/quic/__pycache__/_asyncio.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/quic/__pycache__/_common.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/quic/__pycache__/_sync.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/quic/__pycache__/_trio.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/quic/_asyncio.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/quic/_common.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/quic/_sync.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/quic/_trio.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/rcode.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/rdata.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/rdataclass.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/rdataset.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/rdatatype.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/rdtypes/ANY/AFSDB.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/rdtypes/ANY/AMTRELAY.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/rdtypes/ANY/AVC.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/rdtypes/ANY/CAA.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/rdtypes/ANY/CDNSKEY.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/rdtypes/ANY/CDS.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/rdtypes/ANY/CERT.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/rdtypes/ANY/CNAME.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/rdtypes/ANY/CSYNC.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/rdtypes/ANY/DLV.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/rdtypes/ANY/DNAME.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/rdtypes/ANY/DNSKEY.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/rdtypes/ANY/DS.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/rdtypes/ANY/EUI48.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/rdtypes/ANY/EUI64.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/rdtypes/ANY/GPOS.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/rdtypes/ANY/HINFO.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/rdtypes/ANY/HIP.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/rdtypes/ANY/ISDN.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/rdtypes/ANY/L32.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/rdtypes/ANY/L64.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/rdtypes/ANY/LOC.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/rdtypes/ANY/LP.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/rdtypes/ANY/MX.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/rdtypes/ANY/NID.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/rdtypes/ANY/NINFO.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/rdtypes/ANY/NS.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/rdtypes/ANY/NSEC.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/rdtypes/ANY/NSEC3.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/rdtypes/ANY/NSEC3PARAM.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/rdtypes/ANY/OPENPGPKEY.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/rdtypes/ANY/OPT.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/rdtypes/ANY/PTR.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/rdtypes/ANY/RESINFO.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/rdtypes/ANY/RP.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/rdtypes/ANY/RRSIG.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/rdtypes/ANY/RT.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/rdtypes/ANY/SMIMEA.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/rdtypes/ANY/SOA.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/rdtypes/ANY/SPF.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/rdtypes/ANY/SSHFP.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/rdtypes/ANY/TKEY.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/rdtypes/ANY/TLSA.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/rdtypes/ANY/TSIG.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/rdtypes/ANY/TXT.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/rdtypes/ANY/URI.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/rdtypes/ANY/WALLET.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/rdtypes/ANY/X25.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/rdtypes/ANY/ZONEMD.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/rdtypes/ANY/__init__.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/rdtypes/ANY/__pycache__/AFSDB.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/rdtypes/ANY/__pycache__/AMTRELAY.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/rdtypes/ANY/__pycache__/AVC.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/rdtypes/ANY/__pycache__/CAA.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/rdtypes/ANY/__pycache__/CDNSKEY.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/rdtypes/ANY/__pycache__/CDS.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/rdtypes/ANY/__pycache__/CERT.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/rdtypes/ANY/__pycache__/CNAME.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/rdtypes/ANY/__pycache__/CSYNC.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/rdtypes/ANY/__pycache__/DLV.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/rdtypes/ANY/__pycache__/DNAME.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/rdtypes/ANY/__pycache__/DNSKEY.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/rdtypes/ANY/__pycache__/DS.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/rdtypes/ANY/__pycache__/EUI48.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/rdtypes/ANY/__pycache__/EUI64.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/rdtypes/ANY/__pycache__/GPOS.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/rdtypes/ANY/__pycache__/HINFO.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/rdtypes/ANY/__pycache__/HIP.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/rdtypes/ANY/__pycache__/ISDN.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/rdtypes/ANY/__pycache__/L32.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/rdtypes/ANY/__pycache__/L64.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/rdtypes/ANY/__pycache__/LOC.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/rdtypes/ANY/__pycache__/LP.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/rdtypes/ANY/__pycache__/MX.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/rdtypes/ANY/__pycache__/NID.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/rdtypes/ANY/__pycache__/NINFO.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/rdtypes/ANY/__pycache__/NS.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/rdtypes/ANY/__pycache__/NSEC.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/rdtypes/ANY/__pycache__/NSEC3.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/rdtypes/ANY/__pycache__/NSEC3PARAM.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/rdtypes/ANY/__pycache__/OPENPGPKEY.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/rdtypes/ANY/__pycache__/OPT.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/rdtypes/ANY/__pycache__/PTR.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/rdtypes/ANY/__pycache__/RESINFO.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/rdtypes/ANY/__pycache__/RP.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/rdtypes/ANY/__pycache__/RRSIG.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/rdtypes/ANY/__pycache__/RT.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/rdtypes/ANY/__pycache__/SMIMEA.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/rdtypes/ANY/__pycache__/SOA.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/rdtypes/ANY/__pycache__/SPF.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/rdtypes/ANY/__pycache__/SSHFP.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/rdtypes/ANY/__pycache__/TKEY.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/rdtypes/ANY/__pycache__/TLSA.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/rdtypes/ANY/__pycache__/TSIG.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/rdtypes/ANY/__pycache__/TXT.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/rdtypes/ANY/__pycache__/URI.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/rdtypes/ANY/__pycache__/WALLET.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/rdtypes/ANY/__pycache__/X25.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/rdtypes/ANY/__pycache__/ZONEMD.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/rdtypes/ANY/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/rdtypes/CH/A.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/rdtypes/CH/__init__.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/rdtypes/CH/__pycache__/A.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/rdtypes/CH/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/rdtypes/IN/A.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/rdtypes/IN/AAAA.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/rdtypes/IN/APL.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/rdtypes/IN/DHCID.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/rdtypes/IN/HTTPS.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/rdtypes/IN/IPSECKEY.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/rdtypes/IN/KX.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/rdtypes/IN/NAPTR.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/rdtypes/IN/NSAP.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/rdtypes/IN/NSAP_PTR.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/rdtypes/IN/PX.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/rdtypes/IN/SRV.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/rdtypes/IN/SVCB.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/rdtypes/IN/WKS.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/rdtypes/IN/__init__.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/rdtypes/IN/__pycache__/A.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/rdtypes/IN/__pycache__/AAAA.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/rdtypes/IN/__pycache__/APL.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/rdtypes/IN/__pycache__/DHCID.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/rdtypes/IN/__pycache__/HTTPS.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/rdtypes/IN/__pycache__/IPSECKEY.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/rdtypes/IN/__pycache__/KX.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/rdtypes/IN/__pycache__/NAPTR.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/rdtypes/IN/__pycache__/NSAP.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/rdtypes/IN/__pycache__/NSAP_PTR.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/rdtypes/IN/__pycache__/PX.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/rdtypes/IN/__pycache__/SRV.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/rdtypes/IN/__pycache__/SVCB.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/rdtypes/IN/__pycache__/WKS.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/rdtypes/IN/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/rdtypes/__init__.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/rdtypes/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/rdtypes/__pycache__/dnskeybase.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/rdtypes/__pycache__/dsbase.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/rdtypes/__pycache__/euibase.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/rdtypes/__pycache__/mxbase.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/rdtypes/__pycache__/nsbase.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/rdtypes/__pycache__/svcbbase.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/rdtypes/__pycache__/tlsabase.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/rdtypes/__pycache__/txtbase.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/rdtypes/__pycache__/util.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/rdtypes/dnskeybase.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/rdtypes/dsbase.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/rdtypes/euibase.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/rdtypes/mxbase.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/rdtypes/nsbase.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/rdtypes/svcbbase.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/rdtypes/tlsabase.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/rdtypes/txtbase.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/rdtypes/util.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/renderer.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/resolver.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/reversename.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/rrset.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/serial.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/set.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/tokenizer.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/transaction.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/tsig.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/tsigkeyring.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/ttl.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/update.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/version.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/versioned.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/win32util.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/wire.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/xfr.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/zone.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/zonefile.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dns/zonetypes.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dnspython-2.7.0.dist-info/INSTALLER
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dnspython-2.7.0.dist-info/METADATA
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dnspython-2.7.0.dist-info/RECORD
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dnspython-2.7.0.dist-info/WHEEL
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dnspython-2.7.0.dist-info/licenses/LICENSE
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dotenv/__init__.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dotenv/__main__.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dotenv/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dotenv/__pycache__/__main__.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dotenv/__pycache__/cli.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dotenv/__pycache__/ipython.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dotenv/__pycache__/main.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dotenv/__pycache__/parser.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dotenv/__pycache__/variables.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dotenv/__pycache__/version.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dotenv/cli.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dotenv/ipython.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dotenv/main.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dotenv/parser.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dotenv/py.typed
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dotenv/variables.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/dotenv/version.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/engineio/__init__.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/engineio/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/engineio/__pycache__/async_client.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/engineio/__pycache__/async_server.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/engineio/__pycache__/async_socket.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/engineio/__pycache__/base_client.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/engineio/__pycache__/base_server.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/engineio/__pycache__/base_socket.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/engineio/__pycache__/client.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/engineio/__pycache__/exceptions.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/engineio/__pycache__/json.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/engineio/__pycache__/middleware.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/engineio/__pycache__/packet.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/engineio/__pycache__/payload.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/engineio/__pycache__/server.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/engineio/__pycache__/socket.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/engineio/__pycache__/static_files.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/engineio/async_client.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/engineio/async_drivers/__init__.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/engineio/async_drivers/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/engineio/async_drivers/__pycache__/_websocket_wsgi.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/engineio/async_drivers/__pycache__/aiohttp.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/engineio/async_drivers/__pycache__/asgi.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/engineio/async_drivers/__pycache__/eventlet.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/engineio/async_drivers/__pycache__/gevent.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/engineio/async_drivers/__pycache__/gevent_uwsgi.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/engineio/async_drivers/__pycache__/sanic.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/engineio/async_drivers/__pycache__/threading.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/engineio/async_drivers/__pycache__/tornado.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/engineio/async_drivers/_websocket_wsgi.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/engineio/async_drivers/aiohttp.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/engineio/async_drivers/asgi.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/engineio/async_drivers/eventlet.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/engineio/async_drivers/gevent.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/engineio/async_drivers/gevent_uwsgi.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/engineio/async_drivers/sanic.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/engineio/async_drivers/threading.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/engineio/async_drivers/tornado.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/engineio/async_server.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/engineio/async_socket.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/engineio/base_client.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/engineio/base_server.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/engineio/base_socket.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/engineio/client.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/engineio/exceptions.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/engineio/json.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/engineio/middleware.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/engineio/packet.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/engineio/payload.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/engineio/server.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/engineio/socket.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/engineio/static_files.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/eventlet-0.39.1.dist-info/INSTALLER
 create mode 100644 LICA/venv/lib/python3.11/site-packages/eventlet-0.39.1.dist-info/METADATA
 create mode 100644 LICA/venv/lib/python3.11/site-packages/eventlet-0.39.1.dist-info/RECORD
 create mode 100644 LICA/venv/lib/python3.11/site-packages/eventlet-0.39.1.dist-info/REQUESTED
 create mode 100644 LICA/venv/lib/python3.11/site-packages/eventlet-0.39.1.dist-info/WHEEL
 create mode 100644 LICA/venv/lib/python3.11/site-packages/eventlet-0.39.1.dist-info/licenses/AUTHORS
 create mode 100644 LICA/venv/lib/python3.11/site-packages/eventlet-0.39.1.dist-info/licenses/LICENSE
 create mode 100644 LICA/venv/lib/python3.11/site-packages/eventlet/__init__.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/eventlet/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/eventlet/__pycache__/_version.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/eventlet/__pycache__/asyncio.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/eventlet/__pycache__/backdoor.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/eventlet/__pycache__/convenience.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/eventlet/__pycache__/corolocal.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/eventlet/__pycache__/coros.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/eventlet/__pycache__/dagpool.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/eventlet/__pycache__/db_pool.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/eventlet/__pycache__/debug.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/eventlet/__pycache__/event.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/eventlet/__pycache__/greenpool.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/eventlet/__pycache__/greenthread.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/eventlet/__pycache__/lock.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/eventlet/__pycache__/patcher.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/eventlet/__pycache__/pools.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/eventlet/__pycache__/queue.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/eventlet/__pycache__/semaphore.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/eventlet/__pycache__/timeout.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/eventlet/__pycache__/tpool.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/eventlet/__pycache__/websocket.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/eventlet/__pycache__/wsgi.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/eventlet/_version.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/eventlet/asyncio.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/eventlet/backdoor.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/eventlet/convenience.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/eventlet/corolocal.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/eventlet/coros.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/eventlet/dagpool.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/eventlet/db_pool.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/eventlet/debug.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/eventlet/event.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/eventlet/green/BaseHTTPServer.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/eventlet/green/CGIHTTPServer.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/eventlet/green/MySQLdb.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/eventlet/green/OpenSSL/SSL.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/eventlet/green/OpenSSL/__init__.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/eventlet/green/OpenSSL/__pycache__/SSL.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/eventlet/green/OpenSSL/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/eventlet/green/OpenSSL/__pycache__/crypto.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/eventlet/green/OpenSSL/__pycache__/tsafe.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/eventlet/green/OpenSSL/__pycache__/version.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/eventlet/green/OpenSSL/crypto.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/eventlet/green/OpenSSL/tsafe.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/eventlet/green/OpenSSL/version.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/eventlet/green/Queue.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/eventlet/green/SimpleHTTPServer.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/eventlet/green/SocketServer.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/eventlet/green/__init__.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/eventlet/green/__pycache__/BaseHTTPServer.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/eventlet/green/__pycache__/CGIHTTPServer.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/eventlet/green/__pycache__/MySQLdb.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/eventlet/green/__pycache__/Queue.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/eventlet/green/__pycache__/SimpleHTTPServer.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/eventlet/green/__pycache__/SocketServer.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/eventlet/green/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/eventlet/green/__pycache__/_socket_nodns.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/eventlet/green/__pycache__/asynchat.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/eventlet/green/__pycache__/asyncore.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/eventlet/green/__pycache__/builtin.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/eventlet/green/__pycache__/ftplib.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/eventlet/green/__pycache__/httplib.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/eventlet/green/__pycache__/os.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/eventlet/green/__pycache__/profile.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/eventlet/green/__pycache__/select.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/eventlet/green/__pycache__/selectors.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/eventlet/green/__pycache__/socket.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/eventlet/green/__pycache__/ssl.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/eventlet/green/__pycache__/subprocess.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/eventlet/green/__pycache__/thread.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/eventlet/green/__pycache__/threading.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/eventlet/green/__pycache__/time.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/eventlet/green/__pycache__/urllib2.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/eventlet/green/__pycache__/zmq.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/eventlet/green/_socket_nodns.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/eventlet/green/asynchat.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/eventlet/green/asyncore.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/eventlet/green/builtin.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/eventlet/green/ftplib.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/eventlet/green/http/__init__.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/eventlet/green/http/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/eventlet/green/http/__pycache__/client.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/eventlet/green/http/__pycache__/cookiejar.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/eventlet/green/http/__pycache__/cookies.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/eventlet/green/http/__pycache__/server.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/eventlet/green/http/client.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/eventlet/green/http/cookiejar.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/eventlet/green/http/cookies.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/eventlet/green/http/server.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/eventlet/green/httplib.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/eventlet/green/os.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/eventlet/green/profile.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/eventlet/green/select.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/eventlet/green/selectors.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/eventlet/green/socket.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/eventlet/green/ssl.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/eventlet/green/subprocess.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/eventlet/green/thread.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/eventlet/green/threading.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/eventlet/green/time.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/eventlet/green/urllib/__init__.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/eventlet/green/urllib/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/eventlet/green/urllib/__pycache__/error.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/eventlet/green/urllib/__pycache__/parse.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/eventlet/green/urllib/__pycache__/request.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/eventlet/green/urllib/__pycache__/response.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/eventlet/green/urllib/error.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/eventlet/green/urllib/parse.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/eventlet/green/urllib/request.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/eventlet/green/urllib/response.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/eventlet/green/urllib2.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/eventlet/green/zmq.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/eventlet/greenio/__init__.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/eventlet/greenio/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/eventlet/greenio/__pycache__/base.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/eventlet/greenio/__pycache__/py3.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/eventlet/greenio/base.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/eventlet/greenio/py3.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/eventlet/greenpool.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/eventlet/greenthread.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/eventlet/hubs/__init__.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/eventlet/hubs/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/eventlet/hubs/__pycache__/asyncio.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/eventlet/hubs/__pycache__/epolls.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/eventlet/hubs/__pycache__/hub.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/eventlet/hubs/__pycache__/kqueue.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/eventlet/hubs/__pycache__/poll.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/eventlet/hubs/__pycache__/pyevent.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/eventlet/hubs/__pycache__/selects.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/eventlet/hubs/__pycache__/timer.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/eventlet/hubs/asyncio.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/eventlet/hubs/epolls.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/eventlet/hubs/hub.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/eventlet/hubs/kqueue.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/eventlet/hubs/poll.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/eventlet/hubs/pyevent.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/eventlet/hubs/selects.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/eventlet/hubs/timer.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/eventlet/lock.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/eventlet/patcher.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/eventlet/pools.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/eventlet/queue.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/eventlet/semaphore.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/eventlet/support/__init__.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/eventlet/support/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/eventlet/support/__pycache__/greendns.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/eventlet/support/__pycache__/greenlets.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/eventlet/support/__pycache__/psycopg2_patcher.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/eventlet/support/__pycache__/pylib.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/eventlet/support/__pycache__/stacklesspypys.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/eventlet/support/__pycache__/stacklesss.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/eventlet/support/greendns.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/eventlet/support/greenlets.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/eventlet/support/psycopg2_patcher.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/eventlet/support/pylib.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/eventlet/support/stacklesspypys.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/eventlet/support/stacklesss.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/eventlet/timeout.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/eventlet/tpool.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/eventlet/websocket.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/eventlet/wsgi.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/eventlet/zipkin/README.rst
 create mode 100644 LICA/venv/lib/python3.11/site-packages/eventlet/zipkin/__init__.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/eventlet/zipkin/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/eventlet/zipkin/__pycache__/api.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/eventlet/zipkin/__pycache__/client.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/eventlet/zipkin/__pycache__/greenthread.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/eventlet/zipkin/__pycache__/http.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/eventlet/zipkin/__pycache__/log.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/eventlet/zipkin/__pycache__/patcher.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/eventlet/zipkin/__pycache__/wsgi.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/eventlet/zipkin/_thrift/README.rst
 create mode 100644 LICA/venv/lib/python3.11/site-packages/eventlet/zipkin/_thrift/__init__.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/eventlet/zipkin/_thrift/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/eventlet/zipkin/_thrift/zipkinCore.thrift
 create mode 100644 LICA/venv/lib/python3.11/site-packages/eventlet/zipkin/_thrift/zipkinCore/__init__.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/eventlet/zipkin/_thrift/zipkinCore/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/eventlet/zipkin/_thrift/zipkinCore/__pycache__/constants.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/eventlet/zipkin/_thrift/zipkinCore/__pycache__/ttypes.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/eventlet/zipkin/_thrift/zipkinCore/constants.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/eventlet/zipkin/_thrift/zipkinCore/ttypes.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/eventlet/zipkin/api.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/eventlet/zipkin/client.py
 create mode 100755 LICA/venv/lib/python3.11/site-packages/eventlet/zipkin/example/ex1.png
 create mode 100755 LICA/venv/lib/python3.11/site-packages/eventlet/zipkin/example/ex2.png
 create mode 100755 LICA/venv/lib/python3.11/site-packages/eventlet/zipkin/example/ex3.png
 create mode 100644 LICA/venv/lib/python3.11/site-packages/eventlet/zipkin/greenthread.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/eventlet/zipkin/http.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/eventlet/zipkin/log.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/eventlet/zipkin/patcher.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/eventlet/zipkin/wsgi.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/flask-3.1.0.dist-info/INSTALLER
 create mode 100644 LICA/venv/lib/python3.11/site-packages/flask-3.1.0.dist-info/METADATA
 create mode 100644 LICA/venv/lib/python3.11/site-packages/flask-3.1.0.dist-info/RECORD
 create mode 100644 LICA/venv/lib/python3.11/site-packages/flask-3.1.0.dist-info/REQUESTED
 create mode 100644 LICA/venv/lib/python3.11/site-packages/flask-3.1.0.dist-info/WHEEL
 create mode 100644 LICA/venv/lib/python3.11/site-packages/flask/__init__.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/flask/__main__.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/flask/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/flask/__pycache__/__main__.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/flask/__pycache__/app.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/flask/__pycache__/blueprints.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/flask/__pycache__/cli.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/flask/__pycache__/config.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/flask/__pycache__/ctx.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/flask/__pycache__/debughelpers.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/flask/__pycache__/globals.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/flask/__pycache__/helpers.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/flask/__pycache__/logging.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/flask/__pycache__/sessions.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/flask/__pycache__/signals.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/flask/__pycache__/templating.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/flask/__pycache__/testing.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/flask/__pycache__/typing.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/flask/__pycache__/views.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/flask/__pycache__/wrappers.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/flask/app.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/flask/blueprints.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/flask/cli.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/flask/config.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/flask/ctx.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/flask/debughelpers.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/flask/globals.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/flask/helpers.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/flask/json/__init__.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/flask/json/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/flask/json/__pycache__/provider.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/flask/json/__pycache__/tag.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/flask/json/provider.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/flask/json/tag.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/flask/logging.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/flask/py.typed
 create mode 100644 LICA/venv/lib/python3.11/site-packages/flask/sansio/README.md
 create mode 100644 LICA/venv/lib/python3.11/site-packages/flask/sansio/__pycache__/app.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/flask/sansio/__pycache__/blueprints.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/flask/sansio/__pycache__/scaffold.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/flask/sansio/app.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/flask/sansio/blueprints.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/flask/sansio/scaffold.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/flask/sessions.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/flask/signals.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/flask/templating.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/flask/testing.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/flask/typing.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/flask/views.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/flask/wrappers.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/flask_socketio/__init__.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/flask_socketio/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/flask_socketio/__pycache__/namespace.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/flask_socketio/__pycache__/test_client.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/flask_socketio/namespace.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/flask_socketio/test_client.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/greenlet-3.2.1.dist-info/INSTALLER
 create mode 100644 LICA/venv/lib/python3.11/site-packages/greenlet-3.2.1.dist-info/METADATA
 create mode 100644 LICA/venv/lib/python3.11/site-packages/greenlet-3.2.1.dist-info/RECORD
 create mode 100644 LICA/venv/lib/python3.11/site-packages/greenlet-3.2.1.dist-info/WHEEL
 create mode 100644 LICA/venv/lib/python3.11/site-packages/greenlet-3.2.1.dist-info/licenses/LICENSE
 create mode 100644 LICA/venv/lib/python3.11/site-packages/greenlet-3.2.1.dist-info/licenses/LICENSE.PSF
 create mode 100644 LICA/venv/lib/python3.11/site-packages/greenlet/CObjects.cpp
 create mode 100644 LICA/venv/lib/python3.11/site-packages/greenlet/PyGreenlet.cpp
 create mode 100644 LICA/venv/lib/python3.11/site-packages/greenlet/PyGreenlet.hpp
 create mode 100644 LICA/venv/lib/python3.11/site-packages/greenlet/PyGreenletUnswitchable.cpp
 create mode 100644 LICA/venv/lib/python3.11/site-packages/greenlet/PyModule.cpp
 create mode 100644 LICA/venv/lib/python3.11/site-packages/greenlet/TBrokenGreenlet.cpp
 create mode 100644 LICA/venv/lib/python3.11/site-packages/greenlet/TExceptionState.cpp
 create mode 100644 LICA/venv/lib/python3.11/site-packages/greenlet/TGreenlet.cpp
 create mode 100644 LICA/venv/lib/python3.11/site-packages/greenlet/TGreenlet.hpp
 create mode 100644 LICA/venv/lib/python3.11/site-packages/greenlet/TGreenletGlobals.cpp
 create mode 100644 LICA/venv/lib/python3.11/site-packages/greenlet/TMainGreenlet.cpp
 create mode 100644 LICA/venv/lib/python3.11/site-packages/greenlet/TPythonState.cpp
 create mode 100644 LICA/venv/lib/python3.11/site-packages/greenlet/TStackState.cpp
 create mode 100644 LICA/venv/lib/python3.11/site-packages/greenlet/TThreadState.hpp
 create mode 100644 LICA/venv/lib/python3.11/site-packages/greenlet/TThreadStateCreator.hpp
 create mode 100644 LICA/venv/lib/python3.11/site-packages/greenlet/TThreadStateDestroy.cpp
 create mode 100644 LICA/venv/lib/python3.11/site-packages/greenlet/TUserGreenlet.cpp
 create mode 100644 LICA/venv/lib/python3.11/site-packages/greenlet/__init__.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/greenlet/__pycache__/__init__.cpython-311.pyc
 create mode 100755 LICA/venv/lib/python3.11/site-packages/greenlet/_greenlet.cpython-311-x86_64-linux-gnu.so
 create mode 100644 LICA/venv/lib/python3.11/site-packages/greenlet/greenlet.cpp
 create mode 100644 LICA/venv/lib/python3.11/site-packages/greenlet/greenlet.h
 create mode 100644 LICA/venv/lib/python3.11/site-packages/greenlet/greenlet_allocator.hpp
 create mode 100644 LICA/venv/lib/python3.11/site-packages/greenlet/greenlet_compiler_compat.hpp
 create mode 100644 LICA/venv/lib/python3.11/site-packages/greenlet/greenlet_cpython_compat.hpp
 create mode 100644 LICA/venv/lib/python3.11/site-packages/greenlet/greenlet_exceptions.hpp
 create mode 100644 LICA/venv/lib/python3.11/site-packages/greenlet/greenlet_internal.hpp
 create mode 100644 LICA/venv/lib/python3.11/site-packages/greenlet/greenlet_refs.hpp
 create mode 100644 LICA/venv/lib/python3.11/site-packages/greenlet/greenlet_slp_switch.hpp
 create mode 100644 LICA/venv/lib/python3.11/site-packages/greenlet/greenlet_thread_support.hpp
 create mode 100644 LICA/venv/lib/python3.11/site-packages/greenlet/platform/__init__.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/greenlet/platform/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/greenlet/platform/setup_switch_x64_masm.cmd
 create mode 100644 LICA/venv/lib/python3.11/site-packages/greenlet/platform/switch_aarch64_gcc.h
 create mode 100644 LICA/venv/lib/python3.11/site-packages/greenlet/platform/switch_alpha_unix.h
 create mode 100644 LICA/venv/lib/python3.11/site-packages/greenlet/platform/switch_amd64_unix.h
 create mode 100644 LICA/venv/lib/python3.11/site-packages/greenlet/platform/switch_arm32_gcc.h
 create mode 100644 LICA/venv/lib/python3.11/site-packages/greenlet/platform/switch_arm32_ios.h
 create mode 100644 LICA/venv/lib/python3.11/site-packages/greenlet/platform/switch_arm64_masm.asm
 create mode 100644 LICA/venv/lib/python3.11/site-packages/greenlet/platform/switch_arm64_masm.obj
 create mode 100644 LICA/venv/lib/python3.11/site-packages/greenlet/platform/switch_arm64_msvc.h
 create mode 100644 LICA/venv/lib/python3.11/site-packages/greenlet/platform/switch_csky_gcc.h
 create mode 100644 LICA/venv/lib/python3.11/site-packages/greenlet/platform/switch_loongarch64_linux.h
 create mode 100644 LICA/venv/lib/python3.11/site-packages/greenlet/platform/switch_m68k_gcc.h
 create mode 100644 LICA/venv/lib/python3.11/site-packages/greenlet/platform/switch_mips_unix.h
 create mode 100644 LICA/venv/lib/python3.11/site-packages/greenlet/platform/switch_ppc64_aix.h
 create mode 100644 LICA/venv/lib/python3.11/site-packages/greenlet/platform/switch_ppc64_linux.h
 create mode 100644 LICA/venv/lib/python3.11/site-packages/greenlet/platform/switch_ppc_aix.h
 create mode 100644 LICA/venv/lib/python3.11/site-packages/greenlet/platform/switch_ppc_linux.h
 create mode 100644 LICA/venv/lib/python3.11/site-packages/greenlet/platform/switch_ppc_macosx.h
 create mode 100644 LICA/venv/lib/python3.11/site-packages/greenlet/platform/switch_ppc_unix.h
 create mode 100644 LICA/venv/lib/python3.11/site-packages/greenlet/platform/switch_riscv_unix.h
 create mode 100644 LICA/venv/lib/python3.11/site-packages/greenlet/platform/switch_s390_unix.h
 create mode 100644 LICA/venv/lib/python3.11/site-packages/greenlet/platform/switch_sh_gcc.h
 create mode 100644 LICA/venv/lib/python3.11/site-packages/greenlet/platform/switch_sparc_sun_gcc.h
 create mode 100644 LICA/venv/lib/python3.11/site-packages/greenlet/platform/switch_x32_unix.h
 create mode 100644 LICA/venv/lib/python3.11/site-packages/greenlet/platform/switch_x64_masm.asm
 create mode 100644 LICA/venv/lib/python3.11/site-packages/greenlet/platform/switch_x64_masm.obj
 create mode 100644 LICA/venv/lib/python3.11/site-packages/greenlet/platform/switch_x64_msvc.h
 create mode 100644 LICA/venv/lib/python3.11/site-packages/greenlet/platform/switch_x86_msvc.h
 create mode 100644 LICA/venv/lib/python3.11/site-packages/greenlet/platform/switch_x86_unix.h
 create mode 100644 LICA/venv/lib/python3.11/site-packages/greenlet/slp_platformselect.h
 create mode 100644 LICA/venv/lib/python3.11/site-packages/greenlet/tests/__init__.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/greenlet/tests/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/greenlet/tests/__pycache__/fail_clearing_run_switches.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/greenlet/tests/__pycache__/fail_cpp_exception.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/greenlet/tests/__pycache__/fail_initialstub_already_started.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/greenlet/tests/__pycache__/fail_slp_switch.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/greenlet/tests/__pycache__/fail_switch_three_greenlets.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/greenlet/tests/__pycache__/fail_switch_three_greenlets2.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/greenlet/tests/__pycache__/fail_switch_two_greenlets.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/greenlet/tests/__pycache__/leakcheck.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/greenlet/tests/__pycache__/test_contextvars.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/greenlet/tests/__pycache__/test_cpp.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/greenlet/tests/__pycache__/test_extension_interface.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/greenlet/tests/__pycache__/test_gc.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/greenlet/tests/__pycache__/test_generator.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/greenlet/tests/__pycache__/test_generator_nested.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/greenlet/tests/__pycache__/test_greenlet.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/greenlet/tests/__pycache__/test_greenlet_trash.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/greenlet/tests/__pycache__/test_leaks.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/greenlet/tests/__pycache__/test_stack_saved.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/greenlet/tests/__pycache__/test_throw.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/greenlet/tests/__pycache__/test_tracing.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/greenlet/tests/__pycache__/test_version.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/greenlet/tests/__pycache__/test_weakref.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/greenlet/tests/_test_extension.c
 create mode 100755 LICA/venv/lib/python3.11/site-packages/greenlet/tests/_test_extension.cpython-311-x86_64-linux-gnu.so
 create mode 100644 LICA/venv/lib/python3.11/site-packages/greenlet/tests/_test_extension_cpp.cpp
 create mode 100755 LICA/venv/lib/python3.11/site-packages/greenlet/tests/_test_extension_cpp.cpython-311-x86_64-linux-gnu.so
 create mode 100644 LICA/venv/lib/python3.11/site-packages/greenlet/tests/fail_clearing_run_switches.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/greenlet/tests/fail_cpp_exception.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/greenlet/tests/fail_initialstub_already_started.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/greenlet/tests/fail_slp_switch.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/greenlet/tests/fail_switch_three_greenlets.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/greenlet/tests/fail_switch_three_greenlets2.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/greenlet/tests/fail_switch_two_greenlets.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/greenlet/tests/leakcheck.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/greenlet/tests/test_contextvars.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/greenlet/tests/test_cpp.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/greenlet/tests/test_extension_interface.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/greenlet/tests/test_gc.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/greenlet/tests/test_generator.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/greenlet/tests/test_generator_nested.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/greenlet/tests/test_greenlet.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/greenlet/tests/test_greenlet_trash.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/greenlet/tests/test_leaks.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/greenlet/tests/test_stack_saved.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/greenlet/tests/test_throw.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/greenlet/tests/test_tracing.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/greenlet/tests/test_version.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/greenlet/tests/test_weakref.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/h11-0.16.0.dist-info/INSTALLER
 create mode 100644 LICA/venv/lib/python3.11/site-packages/h11-0.16.0.dist-info/METADATA
 create mode 100644 LICA/venv/lib/python3.11/site-packages/h11-0.16.0.dist-info/RECORD
 create mode 100644 LICA/venv/lib/python3.11/site-packages/h11-0.16.0.dist-info/WHEEL
 create mode 100644 LICA/venv/lib/python3.11/site-packages/h11/__init__.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/h11/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/h11/__pycache__/_abnf.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/h11/__pycache__/_connection.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/h11/__pycache__/_events.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/h11/__pycache__/_headers.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/h11/__pycache__/_readers.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/h11/__pycache__/_receivebuffer.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/h11/__pycache__/_state.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/h11/__pycache__/_util.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/h11/__pycache__/_version.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/h11/__pycache__/_writers.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/h11/_abnf.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/h11/_connection.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/h11/_events.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/h11/_headers.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/h11/_readers.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/h11/_receivebuffer.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/h11/_state.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/h11/_util.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/h11/_version.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/h11/_writers.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/h11/py.typed
 create mode 100644 LICA/venv/lib/python3.11/site-packages/idna-3.10.dist-info/INSTALLER
 create mode 100644 LICA/venv/lib/python3.11/site-packages/idna-3.10.dist-info/LICENSE.md
 create mode 100644 LICA/venv/lib/python3.11/site-packages/idna-3.10.dist-info/METADATA
 create mode 100644 LICA/venv/lib/python3.11/site-packages/idna-3.10.dist-info/RECORD
 create mode 100644 LICA/venv/lib/python3.11/site-packages/idna-3.10.dist-info/WHEEL
 create mode 100644 LICA/venv/lib/python3.11/site-packages/idna/__init__.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/idna/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/idna/__pycache__/codec.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/idna/__pycache__/compat.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/idna/__pycache__/core.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/idna/__pycache__/idnadata.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/idna/__pycache__/intranges.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/idna/__pycache__/package_data.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/idna/__pycache__/uts46data.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/idna/codec.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/idna/compat.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/idna/core.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/idna/idnadata.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/idna/intranges.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/idna/package_data.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/idna/py.typed
 create mode 100644 LICA/venv/lib/python3.11/site-packages/idna/uts46data.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/itsdangerous-2.2.0.dist-info/INSTALLER
 create mode 100644 LICA/venv/lib/python3.11/site-packages/itsdangerous-2.2.0.dist-info/METADATA
 create mode 100644 LICA/venv/lib/python3.11/site-packages/itsdangerous-2.2.0.dist-info/RECORD
 create mode 100644 LICA/venv/lib/python3.11/site-packages/itsdangerous-2.2.0.dist-info/WHEEL
 create mode 100644 LICA/venv/lib/python3.11/site-packages/itsdangerous/__init__.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/itsdangerous/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/itsdangerous/__pycache__/_json.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/itsdangerous/__pycache__/encoding.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/itsdangerous/__pycache__/exc.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/itsdangerous/__pycache__/serializer.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/itsdangerous/__pycache__/signer.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/itsdangerous/__pycache__/timed.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/itsdangerous/__pycache__/url_safe.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/itsdangerous/_json.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/itsdangerous/encoding.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/itsdangerous/exc.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/itsdangerous/py.typed
 create mode 100644 LICA/venv/lib/python3.11/site-packages/itsdangerous/serializer.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/itsdangerous/signer.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/itsdangerous/timed.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/itsdangerous/url_safe.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/jinja2-3.1.6.dist-info/INSTALLER
 create mode 100644 LICA/venv/lib/python3.11/site-packages/jinja2-3.1.6.dist-info/METADATA
 create mode 100644 LICA/venv/lib/python3.11/site-packages/jinja2-3.1.6.dist-info/RECORD
 create mode 100644 LICA/venv/lib/python3.11/site-packages/jinja2-3.1.6.dist-info/WHEEL
 create mode 100644 LICA/venv/lib/python3.11/site-packages/jinja2/__init__.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/jinja2/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/jinja2/__pycache__/_identifier.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/jinja2/__pycache__/async_utils.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/jinja2/__pycache__/bccache.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/jinja2/__pycache__/compiler.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/jinja2/__pycache__/constants.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/jinja2/__pycache__/debug.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/jinja2/__pycache__/defaults.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/jinja2/__pycache__/environment.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/jinja2/__pycache__/exceptions.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/jinja2/__pycache__/ext.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/jinja2/__pycache__/filters.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/jinja2/__pycache__/idtracking.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/jinja2/__pycache__/lexer.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/jinja2/__pycache__/loaders.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/jinja2/__pycache__/meta.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/jinja2/__pycache__/nativetypes.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/jinja2/__pycache__/nodes.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/jinja2/__pycache__/optimizer.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/jinja2/__pycache__/parser.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/jinja2/__pycache__/runtime.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/jinja2/__pycache__/sandbox.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/jinja2/__pycache__/tests.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/jinja2/__pycache__/utils.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/jinja2/__pycache__/visitor.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/jinja2/_identifier.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/jinja2/async_utils.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/jinja2/bccache.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/jinja2/compiler.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/jinja2/constants.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/jinja2/debug.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/jinja2/defaults.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/jinja2/environment.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/jinja2/exceptions.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/jinja2/ext.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/jinja2/filters.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/jinja2/idtracking.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/jinja2/lexer.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/jinja2/loaders.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/jinja2/meta.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/jinja2/nativetypes.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/jinja2/nodes.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/jinja2/optimizer.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/jinja2/parser.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/jinja2/py.typed
 create mode 100644 LICA/venv/lib/python3.11/site-packages/jinja2/runtime.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/jinja2/sandbox.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/jinja2/tests.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/jinja2/utils.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/jinja2/visitor.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/markupsafe/__init__.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/markupsafe/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/markupsafe/__pycache__/_native.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/markupsafe/_native.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/markupsafe/_speedups.c
 create mode 100755 LICA/venv/lib/python3.11/site-packages/markupsafe/_speedups.cpython-311-x86_64-linux-gnu.so
 create mode 100644 LICA/venv/lib/python3.11/site-packages/markupsafe/_speedups.pyi
 create mode 100644 LICA/venv/lib/python3.11/site-packages/markupsafe/py.typed
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip-25.1.1.dist-info/INSTALLER
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip-25.1.1.dist-info/METADATA
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip-25.1.1.dist-info/RECORD
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip-25.1.1.dist-info/REQUESTED
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip-25.1.1.dist-info/WHEEL
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/__init__.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/__main__.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/__pip-runner__.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/__pycache__/__main__.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/__pycache__/__pip-runner__.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/__init__.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/__pycache__/build_env.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/__pycache__/cache.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/__pycache__/configuration.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/__pycache__/exceptions.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/__pycache__/main.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/__pycache__/pyproject.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/__pycache__/self_outdated_check.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/__pycache__/wheel_builder.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/build_env.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/cache.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/cli/__init__.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/cli/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/cli/__pycache__/autocompletion.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/cli/__pycache__/base_command.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/cli/__pycache__/cmdoptions.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/cli/__pycache__/command_context.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/cli/__pycache__/index_command.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/cli/__pycache__/main.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/cli/__pycache__/main_parser.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/cli/__pycache__/parser.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/cli/__pycache__/progress_bars.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/cli/__pycache__/req_command.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/cli/__pycache__/spinners.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/cli/__pycache__/status_codes.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/cli/autocompletion.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/cli/base_command.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/cli/cmdoptions.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/cli/command_context.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/cli/index_command.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/cli/main.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/cli/main_parser.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/cli/parser.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/cli/progress_bars.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/cli/req_command.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/cli/spinners.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/cli/status_codes.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/commands/__init__.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/commands/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/commands/__pycache__/cache.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/commands/__pycache__/check.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/commands/__pycache__/completion.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/commands/__pycache__/configuration.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/commands/__pycache__/debug.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/commands/__pycache__/download.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/commands/__pycache__/freeze.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/commands/__pycache__/hash.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/commands/__pycache__/help.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/commands/__pycache__/index.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/commands/__pycache__/inspect.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/commands/__pycache__/install.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/commands/__pycache__/list.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/commands/__pycache__/lock.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/commands/__pycache__/search.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/commands/__pycache__/show.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/commands/__pycache__/uninstall.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/commands/__pycache__/wheel.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/commands/cache.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/commands/check.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/commands/completion.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/commands/configuration.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/commands/debug.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/commands/download.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/commands/freeze.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/commands/hash.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/commands/help.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/commands/index.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/commands/inspect.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/commands/install.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/commands/list.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/commands/lock.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/commands/search.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/commands/show.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/commands/uninstall.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/commands/wheel.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/configuration.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/distributions/__init__.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/distributions/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/distributions/__pycache__/base.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/distributions/__pycache__/installed.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/distributions/__pycache__/sdist.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/distributions/__pycache__/wheel.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/distributions/base.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/distributions/installed.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/distributions/sdist.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/distributions/wheel.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/exceptions.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/index/__init__.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/index/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/index/__pycache__/collector.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/index/__pycache__/package_finder.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/index/__pycache__/sources.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/index/collector.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/index/package_finder.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/index/sources.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/locations/__init__.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/locations/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/locations/__pycache__/_distutils.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/locations/__pycache__/_sysconfig.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/locations/__pycache__/base.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/locations/_distutils.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/locations/_sysconfig.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/locations/base.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/main.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/metadata/__init__.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/metadata/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/metadata/__pycache__/_json.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/metadata/__pycache__/base.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/metadata/__pycache__/pkg_resources.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/metadata/_json.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/metadata/base.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/metadata/importlib/__init__.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/metadata/importlib/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/metadata/importlib/__pycache__/_compat.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/metadata/importlib/__pycache__/_dists.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/metadata/importlib/__pycache__/_envs.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/metadata/importlib/_compat.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/metadata/importlib/_dists.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/metadata/importlib/_envs.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/metadata/pkg_resources.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/models/__init__.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/models/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/models/__pycache__/candidate.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/models/__pycache__/direct_url.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/models/__pycache__/format_control.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/models/__pycache__/index.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/models/__pycache__/installation_report.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/models/__pycache__/link.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/models/__pycache__/pylock.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/models/__pycache__/scheme.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/models/__pycache__/search_scope.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/models/__pycache__/selection_prefs.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/models/__pycache__/target_python.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/models/__pycache__/wheel.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/models/candidate.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/models/direct_url.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/models/format_control.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/models/index.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/models/installation_report.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/models/link.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/models/pylock.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/models/scheme.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/models/search_scope.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/models/selection_prefs.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/models/target_python.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/models/wheel.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/network/__init__.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/network/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/network/__pycache__/auth.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/network/__pycache__/cache.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/network/__pycache__/download.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/network/__pycache__/lazy_wheel.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/network/__pycache__/session.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/network/__pycache__/utils.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/network/__pycache__/xmlrpc.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/network/auth.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/network/cache.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/network/download.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/network/lazy_wheel.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/network/session.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/network/utils.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/network/xmlrpc.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/operations/__init__.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/operations/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/operations/__pycache__/check.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/operations/__pycache__/freeze.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/operations/__pycache__/prepare.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/operations/build/__init__.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/operations/build/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/operations/build/__pycache__/build_tracker.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/operations/build/__pycache__/metadata.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/operations/build/__pycache__/metadata_editable.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/operations/build/__pycache__/metadata_legacy.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/operations/build/__pycache__/wheel.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/operations/build/__pycache__/wheel_editable.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/operations/build/__pycache__/wheel_legacy.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/operations/build/build_tracker.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/operations/build/metadata.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/operations/build/metadata_editable.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/operations/build/metadata_legacy.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/operations/build/wheel.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/operations/build/wheel_editable.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/operations/build/wheel_legacy.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/operations/check.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/operations/freeze.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/operations/install/__init__.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/operations/install/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/operations/install/__pycache__/editable_legacy.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/operations/install/__pycache__/wheel.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/operations/install/editable_legacy.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/operations/install/wheel.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/operations/prepare.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/pyproject.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/req/__init__.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/req/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/req/__pycache__/constructors.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/req/__pycache__/req_dependency_group.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/req/__pycache__/req_file.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/req/__pycache__/req_install.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/req/__pycache__/req_set.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/req/__pycache__/req_uninstall.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/req/constructors.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/req/req_dependency_group.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/req/req_file.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/req/req_install.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/req/req_set.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/req/req_uninstall.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/resolution/__init__.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/resolution/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/resolution/__pycache__/base.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/resolution/base.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/resolution/legacy/__init__.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/resolution/legacy/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/resolution/legacy/__pycache__/resolver.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/resolution/legacy/resolver.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/resolution/resolvelib/__init__.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/resolution/resolvelib/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/resolution/resolvelib/__pycache__/base.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/resolution/resolvelib/__pycache__/candidates.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/resolution/resolvelib/__pycache__/factory.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/resolution/resolvelib/__pycache__/found_candidates.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/resolution/resolvelib/__pycache__/provider.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/resolution/resolvelib/__pycache__/reporter.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/resolution/resolvelib/__pycache__/requirements.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/resolution/resolvelib/__pycache__/resolver.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/resolution/resolvelib/base.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/resolution/resolvelib/candidates.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/resolution/resolvelib/factory.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/resolution/resolvelib/found_candidates.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/resolution/resolvelib/provider.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/resolution/resolvelib/reporter.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/resolution/resolvelib/requirements.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/resolution/resolvelib/resolver.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/self_outdated_check.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/utils/__init__.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/utils/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/utils/__pycache__/_jaraco_text.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/utils/__pycache__/_log.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/utils/__pycache__/appdirs.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/utils/__pycache__/compat.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/utils/__pycache__/compatibility_tags.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/utils/__pycache__/datetime.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/utils/__pycache__/deprecation.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/utils/__pycache__/direct_url_helpers.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/utils/__pycache__/egg_link.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/utils/__pycache__/entrypoints.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/utils/__pycache__/filesystem.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/utils/__pycache__/filetypes.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/utils/__pycache__/glibc.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/utils/__pycache__/hashes.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/utils/__pycache__/logging.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/utils/__pycache__/misc.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/utils/__pycache__/packaging.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/utils/__pycache__/retry.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/utils/__pycache__/setuptools_build.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/utils/__pycache__/subprocess.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/utils/__pycache__/temp_dir.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/utils/__pycache__/unpacking.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/utils/__pycache__/urls.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/utils/__pycache__/virtualenv.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/utils/__pycache__/wheel.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/utils/_jaraco_text.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/utils/_log.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/utils/appdirs.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/utils/compat.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/utils/compatibility_tags.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/utils/datetime.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/utils/deprecation.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/utils/direct_url_helpers.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/utils/egg_link.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/utils/entrypoints.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/utils/filesystem.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/utils/filetypes.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/utils/glibc.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/utils/hashes.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/utils/logging.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/utils/misc.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/utils/packaging.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/utils/retry.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/utils/setuptools_build.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/utils/subprocess.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/utils/temp_dir.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/utils/unpacking.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/utils/urls.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/utils/virtualenv.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/utils/wheel.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/vcs/__init__.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/vcs/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/vcs/__pycache__/bazaar.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/vcs/__pycache__/git.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/vcs/__pycache__/mercurial.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/vcs/__pycache__/subversion.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/vcs/__pycache__/versioncontrol.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/vcs/bazaar.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/vcs/git.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/vcs/mercurial.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/vcs/subversion.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/vcs/versioncontrol.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_internal/wheel_builder.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/__init__.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/__pycache__/typing_extensions.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/cachecontrol/__init__.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/cachecontrol/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/cachecontrol/__pycache__/_cmd.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/cachecontrol/__pycache__/adapter.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/cachecontrol/__pycache__/cache.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/cachecontrol/__pycache__/controller.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/cachecontrol/__pycache__/filewrapper.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/cachecontrol/__pycache__/heuristics.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/cachecontrol/__pycache__/serialize.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/cachecontrol/__pycache__/wrapper.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/cachecontrol/_cmd.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/cachecontrol/adapter.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/cachecontrol/cache.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/cachecontrol/caches/__init__.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/cachecontrol/caches/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/cachecontrol/caches/__pycache__/file_cache.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/cachecontrol/caches/__pycache__/redis_cache.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/cachecontrol/caches/file_cache.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/cachecontrol/caches/redis_cache.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/cachecontrol/controller.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/cachecontrol/filewrapper.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/cachecontrol/heuristics.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/cachecontrol/py.typed
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/cachecontrol/serialize.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/cachecontrol/wrapper.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/certifi/__init__.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/certifi/__main__.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/certifi/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/certifi/__pycache__/__main__.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/certifi/__pycache__/core.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/certifi/cacert.pem
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/certifi/core.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/certifi/py.typed
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/dependency_groups/__init__.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/dependency_groups/__main__.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/dependency_groups/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/dependency_groups/__pycache__/__main__.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/dependency_groups/__pycache__/_implementation.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/dependency_groups/__pycache__/_lint_dependency_groups.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/dependency_groups/__pycache__/_pip_wrapper.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/dependency_groups/__pycache__/_toml_compat.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/dependency_groups/_implementation.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/dependency_groups/_lint_dependency_groups.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/dependency_groups/_pip_wrapper.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/dependency_groups/_toml_compat.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/dependency_groups/py.typed
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/distlib/__init__.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/distlib/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/distlib/__pycache__/compat.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/distlib/__pycache__/database.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/distlib/__pycache__/index.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/distlib/__pycache__/locators.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/distlib/__pycache__/manifest.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/distlib/__pycache__/markers.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/distlib/__pycache__/metadata.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/distlib/__pycache__/resources.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/distlib/__pycache__/scripts.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/distlib/__pycache__/util.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/distlib/__pycache__/version.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/distlib/__pycache__/wheel.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/distlib/compat.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/distlib/database.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/distlib/index.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/distlib/locators.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/distlib/manifest.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/distlib/markers.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/distlib/metadata.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/distlib/resources.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/distlib/scripts.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/distlib/t32.exe
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/distlib/t64-arm.exe
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/distlib/t64.exe
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/distlib/util.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/distlib/version.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/distlib/w32.exe
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/distlib/w64-arm.exe
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/distlib/w64.exe
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/distlib/wheel.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/distro/__init__.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/distro/__main__.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/distro/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/distro/__pycache__/__main__.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/distro/__pycache__/distro.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/distro/distro.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/distro/py.typed
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/idna/__init__.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/idna/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/idna/__pycache__/codec.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/idna/__pycache__/compat.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/idna/__pycache__/core.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/idna/__pycache__/idnadata.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/idna/__pycache__/intranges.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/idna/__pycache__/package_data.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/idna/__pycache__/uts46data.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/idna/codec.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/idna/compat.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/idna/core.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/idna/idnadata.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/idna/intranges.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/idna/package_data.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/idna/py.typed
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/idna/uts46data.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/msgpack/__init__.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/msgpack/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/msgpack/__pycache__/exceptions.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/msgpack/__pycache__/ext.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/msgpack/__pycache__/fallback.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/msgpack/exceptions.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/msgpack/ext.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/msgpack/fallback.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/packaging/__init__.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/packaging/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/packaging/__pycache__/_elffile.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/packaging/__pycache__/_manylinux.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/packaging/__pycache__/_musllinux.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/packaging/__pycache__/_parser.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/packaging/__pycache__/_structures.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/packaging/__pycache__/_tokenizer.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/packaging/__pycache__/markers.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/packaging/__pycache__/metadata.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/packaging/__pycache__/requirements.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/packaging/__pycache__/specifiers.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/packaging/__pycache__/tags.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/packaging/__pycache__/utils.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/packaging/__pycache__/version.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/packaging/_elffile.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/packaging/_manylinux.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/packaging/_musllinux.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/packaging/_parser.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/packaging/_structures.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/packaging/_tokenizer.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/packaging/licenses/__init__.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/packaging/licenses/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/packaging/licenses/__pycache__/_spdx.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/packaging/licenses/_spdx.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/packaging/markers.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/packaging/metadata.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/packaging/py.typed
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/packaging/requirements.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/packaging/specifiers.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/packaging/tags.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/packaging/utils.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/packaging/version.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/pkg_resources/__init__.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/pkg_resources/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/platformdirs/__init__.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/platformdirs/__main__.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/platformdirs/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/platformdirs/__pycache__/__main__.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/platformdirs/__pycache__/android.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/platformdirs/__pycache__/api.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/platformdirs/__pycache__/macos.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/platformdirs/__pycache__/unix.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/platformdirs/__pycache__/version.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/platformdirs/__pycache__/windows.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/platformdirs/android.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/platformdirs/api.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/platformdirs/macos.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/platformdirs/py.typed
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/platformdirs/unix.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/platformdirs/version.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/platformdirs/windows.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/pygments/__init__.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/pygments/__main__.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/pygments/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/pygments/__pycache__/__main__.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/pygments/__pycache__/console.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/pygments/__pycache__/filter.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/pygments/__pycache__/formatter.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/pygments/__pycache__/lexer.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/pygments/__pycache__/modeline.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/pygments/__pycache__/plugin.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/pygments/__pycache__/regexopt.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/pygments/__pycache__/scanner.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/pygments/__pycache__/sphinxext.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/pygments/__pycache__/style.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/pygments/__pycache__/token.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/pygments/__pycache__/unistring.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/pygments/__pycache__/util.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/pygments/console.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/pygments/filter.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/pygments/filters/__init__.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/pygments/filters/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/pygments/formatter.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/pygments/formatters/__init__.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/pygments/formatters/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/pygments/formatters/__pycache__/_mapping.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/pygments/formatters/_mapping.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/pygments/lexer.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/pygments/lexers/__init__.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/pygments/lexers/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/pygments/lexers/__pycache__/_mapping.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/pygments/lexers/__pycache__/python.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/pygments/lexers/_mapping.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/pygments/lexers/python.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/pygments/modeline.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/pygments/plugin.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/pygments/regexopt.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/pygments/scanner.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/pygments/sphinxext.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/pygments/style.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/pygments/styles/__init__.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/pygments/styles/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/pygments/styles/__pycache__/_mapping.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/pygments/styles/_mapping.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/pygments/token.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/pygments/unistring.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/pygments/util.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/pyproject_hooks/__init__.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/pyproject_hooks/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/pyproject_hooks/__pycache__/_impl.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/pyproject_hooks/_impl.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/pyproject_hooks/_in_process/__init__.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/pyproject_hooks/_in_process/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/pyproject_hooks/_in_process/__pycache__/_in_process.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/pyproject_hooks/_in_process/_in_process.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/pyproject_hooks/py.typed
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/requests/__init__.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/requests/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/requests/__pycache__/__version__.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/requests/__pycache__/_internal_utils.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/requests/__pycache__/adapters.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/requests/__pycache__/api.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/requests/__pycache__/auth.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/requests/__pycache__/certs.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/requests/__pycache__/compat.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/requests/__pycache__/cookies.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/requests/__pycache__/exceptions.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/requests/__pycache__/help.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/requests/__pycache__/hooks.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/requests/__pycache__/models.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/requests/__pycache__/packages.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/requests/__pycache__/sessions.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/requests/__pycache__/status_codes.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/requests/__pycache__/structures.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/requests/__pycache__/utils.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/requests/__version__.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/requests/_internal_utils.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/requests/adapters.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/requests/api.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/requests/auth.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/requests/certs.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/requests/compat.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/requests/cookies.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/requests/exceptions.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/requests/help.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/requests/hooks.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/requests/models.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/requests/packages.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/requests/sessions.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/requests/status_codes.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/requests/structures.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/requests/utils.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/resolvelib/__init__.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/resolvelib/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/resolvelib/__pycache__/providers.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/resolvelib/__pycache__/reporters.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/resolvelib/__pycache__/structs.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/resolvelib/providers.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/resolvelib/py.typed
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/resolvelib/reporters.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/resolvelib/resolvers/__init__.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/resolvelib/resolvers/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/resolvelib/resolvers/__pycache__/abstract.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/resolvelib/resolvers/__pycache__/criterion.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/resolvelib/resolvers/__pycache__/exceptions.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/resolvelib/resolvers/__pycache__/resolution.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/resolvelib/resolvers/abstract.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/resolvelib/resolvers/criterion.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/resolvelib/resolvers/exceptions.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/resolvelib/resolvers/resolution.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/resolvelib/structs.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/rich/__init__.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/rich/__main__.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/rich/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/rich/__pycache__/__main__.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/rich/__pycache__/_cell_widths.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/rich/__pycache__/_emoji_codes.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/rich/__pycache__/_emoji_replace.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/rich/__pycache__/_export_format.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/rich/__pycache__/_extension.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/rich/__pycache__/_fileno.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/rich/__pycache__/_inspect.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/rich/__pycache__/_log_render.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/rich/__pycache__/_loop.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/rich/__pycache__/_null_file.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/rich/__pycache__/_palettes.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/rich/__pycache__/_pick.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/rich/__pycache__/_ratio.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/rich/__pycache__/_spinners.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/rich/__pycache__/_stack.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/rich/__pycache__/_timer.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/rich/__pycache__/_win32_console.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/rich/__pycache__/_windows.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/rich/__pycache__/_windows_renderer.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/rich/__pycache__/_wrap.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/rich/__pycache__/abc.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/rich/__pycache__/align.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/rich/__pycache__/ansi.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/rich/__pycache__/bar.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/rich/__pycache__/box.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/rich/__pycache__/cells.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/rich/__pycache__/color.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/rich/__pycache__/color_triplet.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/rich/__pycache__/columns.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/rich/__pycache__/console.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/rich/__pycache__/constrain.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/rich/__pycache__/containers.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/rich/__pycache__/control.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/rich/__pycache__/default_styles.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/rich/__pycache__/diagnose.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/rich/__pycache__/emoji.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/rich/__pycache__/errors.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/rich/__pycache__/file_proxy.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/rich/__pycache__/filesize.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/rich/__pycache__/highlighter.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/rich/__pycache__/json.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/rich/__pycache__/jupyter.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/rich/__pycache__/layout.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/rich/__pycache__/live.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/rich/__pycache__/live_render.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/rich/__pycache__/logging.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/rich/__pycache__/markup.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/rich/__pycache__/measure.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/rich/__pycache__/padding.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/rich/__pycache__/pager.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/rich/__pycache__/palette.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/rich/__pycache__/panel.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/rich/__pycache__/pretty.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/rich/__pycache__/progress.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/rich/__pycache__/progress_bar.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/rich/__pycache__/prompt.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/rich/__pycache__/protocol.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/rich/__pycache__/region.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/rich/__pycache__/repr.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/rich/__pycache__/rule.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/rich/__pycache__/scope.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/rich/__pycache__/screen.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/rich/__pycache__/segment.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/rich/__pycache__/spinner.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/rich/__pycache__/status.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/rich/__pycache__/style.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/rich/__pycache__/styled.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/rich/__pycache__/syntax.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/rich/__pycache__/table.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/rich/__pycache__/terminal_theme.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/rich/__pycache__/text.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/rich/__pycache__/theme.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/rich/__pycache__/themes.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/rich/__pycache__/traceback.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/rich/__pycache__/tree.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/rich/_cell_widths.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/rich/_emoji_codes.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/rich/_emoji_replace.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/rich/_export_format.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/rich/_extension.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/rich/_fileno.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/rich/_inspect.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/rich/_log_render.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/rich/_loop.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/rich/_null_file.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/rich/_palettes.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/rich/_pick.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/rich/_ratio.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/rich/_spinners.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/rich/_stack.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/rich/_timer.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/rich/_win32_console.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/rich/_windows.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/rich/_windows_renderer.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/rich/_wrap.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/rich/abc.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/rich/align.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/rich/ansi.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/rich/bar.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/rich/box.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/rich/cells.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/rich/color.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/rich/color_triplet.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/rich/columns.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/rich/console.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/rich/constrain.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/rich/containers.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/rich/control.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/rich/default_styles.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/rich/diagnose.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/rich/emoji.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/rich/errors.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/rich/file_proxy.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/rich/filesize.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/rich/highlighter.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/rich/json.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/rich/jupyter.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/rich/layout.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/rich/live.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/rich/live_render.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/rich/logging.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/rich/markup.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/rich/measure.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/rich/padding.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/rich/pager.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/rich/palette.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/rich/panel.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/rich/pretty.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/rich/progress.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/rich/progress_bar.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/rich/prompt.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/rich/protocol.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/rich/py.typed
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/rich/region.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/rich/repr.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/rich/rule.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/rich/scope.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/rich/screen.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/rich/segment.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/rich/spinner.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/rich/status.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/rich/style.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/rich/styled.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/rich/syntax.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/rich/table.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/rich/terminal_theme.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/rich/text.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/rich/theme.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/rich/themes.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/rich/traceback.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/rich/tree.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/tomli/__init__.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/tomli/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/tomli/__pycache__/_parser.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/tomli/__pycache__/_re.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/tomli/__pycache__/_types.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/tomli/_parser.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/tomli/_re.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/tomli/_types.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/tomli/py.typed
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/tomli_w/__init__.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/tomli_w/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/tomli_w/__pycache__/_writer.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/tomli_w/_writer.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/tomli_w/py.typed
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/truststore/__init__.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/truststore/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/truststore/__pycache__/_api.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/truststore/__pycache__/_macos.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/truststore/__pycache__/_openssl.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/truststore/__pycache__/_ssl_constants.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/truststore/__pycache__/_windows.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/truststore/_api.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/truststore/_macos.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/truststore/_openssl.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/truststore/_ssl_constants.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/truststore/_windows.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/truststore/py.typed
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/typing_extensions.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/urllib3/__init__.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/urllib3/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/urllib3/__pycache__/_collections.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/urllib3/__pycache__/_version.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/urllib3/__pycache__/connection.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/urllib3/__pycache__/connectionpool.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/urllib3/__pycache__/exceptions.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/urllib3/__pycache__/fields.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/urllib3/__pycache__/filepost.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/urllib3/__pycache__/poolmanager.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/urllib3/__pycache__/request.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/urllib3/__pycache__/response.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/urllib3/_collections.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/urllib3/_version.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/urllib3/connection.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/urllib3/connectionpool.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/urllib3/contrib/__init__.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/urllib3/contrib/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/urllib3/contrib/__pycache__/_appengine_environ.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/urllib3/contrib/__pycache__/appengine.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/urllib3/contrib/__pycache__/ntlmpool.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/urllib3/contrib/__pycache__/pyopenssl.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/urllib3/contrib/__pycache__/securetransport.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/urllib3/contrib/__pycache__/socks.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/urllib3/contrib/_appengine_environ.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/urllib3/contrib/_securetransport/__init__.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/urllib3/contrib/_securetransport/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/urllib3/contrib/_securetransport/__pycache__/bindings.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/urllib3/contrib/_securetransport/__pycache__/low_level.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/urllib3/contrib/_securetransport/bindings.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/urllib3/contrib/_securetransport/low_level.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/urllib3/contrib/appengine.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/urllib3/contrib/ntlmpool.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/urllib3/contrib/pyopenssl.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/urllib3/contrib/securetransport.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/urllib3/contrib/socks.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/urllib3/exceptions.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/urllib3/fields.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/urllib3/filepost.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/urllib3/packages/__init__.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/urllib3/packages/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/urllib3/packages/__pycache__/six.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/urllib3/packages/backports/__init__.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/urllib3/packages/backports/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/urllib3/packages/backports/__pycache__/makefile.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/urllib3/packages/backports/__pycache__/weakref_finalize.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/urllib3/packages/backports/makefile.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/urllib3/packages/backports/weakref_finalize.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/urllib3/packages/six.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/urllib3/poolmanager.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/urllib3/request.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/urllib3/response.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/urllib3/util/__init__.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/urllib3/util/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/urllib3/util/__pycache__/connection.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/urllib3/util/__pycache__/proxy.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/urllib3/util/__pycache__/queue.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/urllib3/util/__pycache__/request.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/urllib3/util/__pycache__/response.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/urllib3/util/__pycache__/retry.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/urllib3/util/__pycache__/ssl_.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/urllib3/util/__pycache__/ssl_match_hostname.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/urllib3/util/__pycache__/ssltransport.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/urllib3/util/__pycache__/timeout.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/urllib3/util/__pycache__/url.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/urllib3/util/__pycache__/wait.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/urllib3/util/connection.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/urllib3/util/proxy.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/urllib3/util/queue.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/urllib3/util/request.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/urllib3/util/response.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/urllib3/util/retry.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/urllib3/util/ssl_.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/urllib3/util/ssl_match_hostname.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/urllib3/util/ssltransport.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/urllib3/util/timeout.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/urllib3/util/url.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/_vendor/urllib3/util/wait.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pip/py.typed
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pkg_resources/__init__.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pkg_resources/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pkg_resources/_vendor/__init__.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pkg_resources/_vendor/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pkg_resources/_vendor/__pycache__/appdirs.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pkg_resources/_vendor/__pycache__/pyparsing.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pkg_resources/_vendor/appdirs.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pkg_resources/_vendor/packaging/__about__.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pkg_resources/_vendor/packaging/__init__.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pkg_resources/_vendor/packaging/__pycache__/__about__.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pkg_resources/_vendor/packaging/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pkg_resources/_vendor/packaging/__pycache__/_manylinux.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pkg_resources/_vendor/packaging/__pycache__/_musllinux.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pkg_resources/_vendor/packaging/__pycache__/_structures.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pkg_resources/_vendor/packaging/__pycache__/markers.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pkg_resources/_vendor/packaging/__pycache__/requirements.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pkg_resources/_vendor/packaging/__pycache__/specifiers.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pkg_resources/_vendor/packaging/__pycache__/tags.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pkg_resources/_vendor/packaging/__pycache__/utils.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pkg_resources/_vendor/packaging/__pycache__/version.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pkg_resources/_vendor/packaging/_manylinux.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pkg_resources/_vendor/packaging/_musllinux.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pkg_resources/_vendor/packaging/_structures.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pkg_resources/_vendor/packaging/markers.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pkg_resources/_vendor/packaging/requirements.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pkg_resources/_vendor/packaging/specifiers.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pkg_resources/_vendor/packaging/tags.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pkg_resources/_vendor/packaging/utils.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pkg_resources/_vendor/packaging/version.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pkg_resources/_vendor/pyparsing.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pkg_resources/extern/__init__.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pkg_resources/extern/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pkg_resources/tests/data/my-test-package-source/__pycache__/setup.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pkg_resources/tests/data/my-test-package-source/setup.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pydub-0.25.1.dist-info/AUTHORS
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pydub-0.25.1.dist-info/INSTALLER
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pydub-0.25.1.dist-info/LICENSE
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pydub-0.25.1.dist-info/METADATA
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pydub-0.25.1.dist-info/RECORD
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pydub-0.25.1.dist-info/REQUESTED
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pydub-0.25.1.dist-info/WHEEL
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pydub/__init__.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pydub/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pydub/__pycache__/audio_segment.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pydub/__pycache__/effects.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pydub/__pycache__/exceptions.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pydub/__pycache__/generators.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pydub/__pycache__/logging_utils.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pydub/__pycache__/playback.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pydub/__pycache__/pyaudioop.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pydub/__pycache__/scipy_effects.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pydub/__pycache__/silence.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pydub/__pycache__/utils.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pydub/audio_segment.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pydub/effects.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pydub/exceptions.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pydub/generators.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pydub/logging_utils.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pydub/playback.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pydub/pyaudioop.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pydub/scipy_effects.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pydub/silence.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/pydub/utils.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/python_dotenv-1.1.0.dist-info/INSTALLER
 create mode 100644 LICA/venv/lib/python3.11/site-packages/python_dotenv-1.1.0.dist-info/METADATA
 create mode 100644 LICA/venv/lib/python3.11/site-packages/python_dotenv-1.1.0.dist-info/RECORD
 create mode 100644 LICA/venv/lib/python3.11/site-packages/python_dotenv-1.1.0.dist-info/REQUESTED
 create mode 100644 LICA/venv/lib/python3.11/site-packages/python_dotenv-1.1.0.dist-info/WHEEL
 create mode 100644 LICA/venv/lib/python3.11/site-packages/python_dotenv-1.1.0.dist-info/licenses/LICENSE
 create mode 100644 LICA/venv/lib/python3.11/site-packages/python_engineio-4.12.0.dist-info/INSTALLER
 create mode 100644 LICA/venv/lib/python3.11/site-packages/python_engineio-4.12.0.dist-info/METADATA
 create mode 100644 LICA/venv/lib/python3.11/site-packages/python_engineio-4.12.0.dist-info/RECORD
 create mode 100644 LICA/venv/lib/python3.11/site-packages/python_engineio-4.12.0.dist-info/WHEEL
 create mode 100644 LICA/venv/lib/python3.11/site-packages/python_engineio-4.12.0.dist-info/licenses/LICENSE
 create mode 100644 LICA/venv/lib/python3.11/site-packages/python_socketio-5.13.0.dist-info/INSTALLER
 create mode 100644 LICA/venv/lib/python3.11/site-packages/python_socketio-5.13.0.dist-info/METADATA
 create mode 100644 LICA/venv/lib/python3.11/site-packages/python_socketio-5.13.0.dist-info/RECORD
 create mode 100644 LICA/venv/lib/python3.11/site-packages/python_socketio-5.13.0.dist-info/WHEEL
 create mode 100644 LICA/venv/lib/python3.11/site-packages/python_socketio-5.13.0.dist-info/licenses/LICENSE
 create mode 100644 LICA/venv/lib/python3.11/site-packages/requests-2.32.3.dist-info/INSTALLER
 create mode 100644 LICA/venv/lib/python3.11/site-packages/requests-2.32.3.dist-info/LICENSE
 create mode 100644 LICA/venv/lib/python3.11/site-packages/requests-2.32.3.dist-info/METADATA
 create mode 100644 LICA/venv/lib/python3.11/site-packages/requests-2.32.3.dist-info/RECORD
 create mode 100644 LICA/venv/lib/python3.11/site-packages/requests-2.32.3.dist-info/REQUESTED
 create mode 100644 LICA/venv/lib/python3.11/site-packages/requests-2.32.3.dist-info/WHEEL
 create mode 100644 LICA/venv/lib/python3.11/site-packages/requests/__init__.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/requests/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/requests/__pycache__/__version__.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/requests/__pycache__/_internal_utils.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/requests/__pycache__/adapters.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/requests/__pycache__/api.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/requests/__pycache__/auth.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/requests/__pycache__/certs.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/requests/__pycache__/compat.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/requests/__pycache__/cookies.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/requests/__pycache__/exceptions.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/requests/__pycache__/help.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/requests/__pycache__/hooks.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/requests/__pycache__/models.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/requests/__pycache__/packages.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/requests/__pycache__/sessions.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/requests/__pycache__/status_codes.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/requests/__pycache__/structures.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/requests/__pycache__/utils.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/requests/__version__.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/requests/_internal_utils.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/requests/adapters.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/requests/api.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/requests/auth.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/requests/certs.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/requests/compat.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/requests/cookies.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/requests/exceptions.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/requests/help.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/requests/hooks.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/requests/models.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/requests/packages.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/requests/sessions.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/requests/status_codes.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/requests/structures.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/requests/utils.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools-59.6.0.dist-info/INSTALLER
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools-59.6.0.dist-info/LICENSE
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools-59.6.0.dist-info/METADATA
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools-59.6.0.dist-info/RECORD
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools-59.6.0.dist-info/REQUESTED
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools-59.6.0.dist-info/WHEEL
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/__init__.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/__pycache__/_deprecation_warning.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/__pycache__/_imp.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/__pycache__/archive_util.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/__pycache__/build_meta.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/__pycache__/config.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/__pycache__/dep_util.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/__pycache__/depends.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/__pycache__/dist.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/__pycache__/errors.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/__pycache__/extension.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/__pycache__/glob.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/__pycache__/installer.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/__pycache__/launch.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/__pycache__/monkey.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/__pycache__/msvc.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/__pycache__/namespaces.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/__pycache__/package_index.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/__pycache__/py34compat.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/__pycache__/sandbox.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/__pycache__/unicode_utils.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/__pycache__/version.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/__pycache__/wheel.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/__pycache__/windows_support.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/_deprecation_warning.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/_distutils/__init__.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/_distutils/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/_distutils/__pycache__/_msvccompiler.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/_distutils/__pycache__/archive_util.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/_distutils/__pycache__/bcppcompiler.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/_distutils/__pycache__/ccompiler.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/_distutils/__pycache__/cmd.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/_distutils/__pycache__/config.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/_distutils/__pycache__/core.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/_distutils/__pycache__/cygwinccompiler.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/_distutils/__pycache__/debug.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/_distutils/__pycache__/dep_util.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/_distutils/__pycache__/dir_util.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/_distutils/__pycache__/dist.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/_distutils/__pycache__/errors.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/_distutils/__pycache__/extension.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/_distutils/__pycache__/fancy_getopt.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/_distutils/__pycache__/file_util.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/_distutils/__pycache__/filelist.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/_distutils/__pycache__/log.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/_distutils/__pycache__/msvc9compiler.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/_distutils/__pycache__/msvccompiler.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/_distutils/__pycache__/py35compat.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/_distutils/__pycache__/py38compat.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/_distutils/__pycache__/spawn.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/_distutils/__pycache__/sysconfig.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/_distutils/__pycache__/text_file.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/_distutils/__pycache__/unixccompiler.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/_distutils/__pycache__/util.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/_distutils/__pycache__/version.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/_distutils/__pycache__/versionpredicate.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/_distutils/_msvccompiler.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/_distutils/archive_util.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/_distutils/bcppcompiler.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/_distutils/ccompiler.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/_distutils/cmd.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/_distutils/command/__init__.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/_distutils/command/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/_distutils/command/__pycache__/bdist.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/_distutils/command/__pycache__/bdist_dumb.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/_distutils/command/__pycache__/bdist_msi.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/_distutils/command/__pycache__/bdist_rpm.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/_distutils/command/__pycache__/bdist_wininst.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/_distutils/command/__pycache__/build.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/_distutils/command/__pycache__/build_clib.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/_distutils/command/__pycache__/build_ext.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/_distutils/command/__pycache__/build_py.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/_distutils/command/__pycache__/build_scripts.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/_distutils/command/__pycache__/check.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/_distutils/command/__pycache__/clean.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/_distutils/command/__pycache__/config.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/_distutils/command/__pycache__/install.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/_distutils/command/__pycache__/install_data.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/_distutils/command/__pycache__/install_egg_info.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/_distutils/command/__pycache__/install_headers.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/_distutils/command/__pycache__/install_lib.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/_distutils/command/__pycache__/install_scripts.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/_distutils/command/__pycache__/py37compat.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/_distutils/command/__pycache__/register.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/_distutils/command/__pycache__/sdist.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/_distutils/command/__pycache__/upload.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/_distutils/command/bdist.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/_distutils/command/bdist_dumb.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/_distutils/command/bdist_msi.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/_distutils/command/bdist_rpm.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/_distutils/command/bdist_wininst.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/_distutils/command/build.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/_distutils/command/build_clib.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/_distutils/command/build_ext.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/_distutils/command/build_py.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/_distutils/command/build_scripts.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/_distutils/command/check.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/_distutils/command/clean.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/_distutils/command/config.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/_distutils/command/install.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/_distutils/command/install_data.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/_distutils/command/install_egg_info.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/_distutils/command/install_headers.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/_distutils/command/install_lib.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/_distutils/command/install_scripts.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/_distutils/command/py37compat.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/_distutils/command/register.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/_distutils/command/sdist.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/_distutils/command/upload.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/_distutils/config.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/_distutils/core.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/_distutils/cygwinccompiler.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/_distutils/debug.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/_distutils/dep_util.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/_distutils/dir_util.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/_distutils/dist.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/_distutils/errors.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/_distutils/extension.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/_distutils/fancy_getopt.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/_distutils/file_util.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/_distutils/filelist.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/_distutils/log.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/_distutils/msvc9compiler.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/_distutils/msvccompiler.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/_distutils/py35compat.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/_distutils/py38compat.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/_distutils/spawn.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/_distutils/sysconfig.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/_distutils/text_file.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/_distutils/unixccompiler.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/_distutils/util.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/_distutils/version.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/_distutils/versionpredicate.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/_imp.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/_vendor/__init__.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/_vendor/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/_vendor/__pycache__/ordered_set.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/_vendor/__pycache__/pyparsing.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/_vendor/more_itertools/__init__.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/_vendor/more_itertools/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/_vendor/more_itertools/__pycache__/more.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/_vendor/more_itertools/__pycache__/recipes.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/_vendor/more_itertools/more.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/_vendor/more_itertools/recipes.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/_vendor/ordered_set.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/_vendor/packaging/__about__.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/_vendor/packaging/__init__.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/_vendor/packaging/__pycache__/__about__.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/_vendor/packaging/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/_vendor/packaging/__pycache__/_manylinux.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/_vendor/packaging/__pycache__/_musllinux.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/_vendor/packaging/__pycache__/_structures.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/_vendor/packaging/__pycache__/markers.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/_vendor/packaging/__pycache__/requirements.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/_vendor/packaging/__pycache__/specifiers.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/_vendor/packaging/__pycache__/tags.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/_vendor/packaging/__pycache__/utils.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/_vendor/packaging/__pycache__/version.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/_vendor/packaging/_manylinux.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/_vendor/packaging/_musllinux.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/_vendor/packaging/_structures.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/_vendor/packaging/markers.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/_vendor/packaging/requirements.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/_vendor/packaging/specifiers.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/_vendor/packaging/tags.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/_vendor/packaging/utils.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/_vendor/packaging/version.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/_vendor/pyparsing.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/archive_util.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/build_meta.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/cli-32.exe
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/cli-64.exe
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/cli-arm64.exe
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/cli.exe
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/command/__init__.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/command/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/command/__pycache__/alias.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/command/__pycache__/bdist_egg.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/command/__pycache__/bdist_rpm.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/command/__pycache__/build_clib.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/command/__pycache__/build_ext.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/command/__pycache__/build_py.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/command/__pycache__/develop.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/command/__pycache__/dist_info.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/command/__pycache__/easy_install.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/command/__pycache__/egg_info.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/command/__pycache__/install.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/command/__pycache__/install_egg_info.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/command/__pycache__/install_lib.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/command/__pycache__/install_scripts.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/command/__pycache__/py36compat.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/command/__pycache__/register.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/command/__pycache__/rotate.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/command/__pycache__/saveopts.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/command/__pycache__/sdist.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/command/__pycache__/setopt.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/command/__pycache__/test.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/command/__pycache__/upload.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/command/__pycache__/upload_docs.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/command/alias.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/command/bdist_egg.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/command/bdist_rpm.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/command/build_clib.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/command/build_ext.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/command/build_py.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/command/develop.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/command/dist_info.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/command/easy_install.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/command/egg_info.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/command/install.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/command/install_egg_info.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/command/install_lib.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/command/install_scripts.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/command/launcher manifest.xml
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/command/py36compat.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/command/register.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/command/rotate.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/command/saveopts.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/command/sdist.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/command/setopt.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/command/test.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/command/upload.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/command/upload_docs.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/config.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/dep_util.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/depends.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/dist.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/errors.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/extension.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/extern/__init__.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/extern/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/glob.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/gui-32.exe
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/gui-64.exe
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/gui-arm64.exe
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/gui.exe
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/installer.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/launch.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/monkey.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/msvc.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/namespaces.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/package_index.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/py34compat.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/sandbox.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/script (dev).tmpl
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/script.tmpl
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/unicode_utils.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/version.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/wheel.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/setuptools/windows_support.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/simple_websocket-1.1.0.dist-info/INSTALLER
 create mode 100644 LICA/venv/lib/python3.11/site-packages/simple_websocket-1.1.0.dist-info/LICENSE
 create mode 100644 LICA/venv/lib/python3.11/site-packages/simple_websocket-1.1.0.dist-info/METADATA
 create mode 100644 LICA/venv/lib/python3.11/site-packages/simple_websocket-1.1.0.dist-info/RECORD
 create mode 100644 LICA/venv/lib/python3.11/site-packages/simple_websocket-1.1.0.dist-info/WHEEL
 create mode 100644 LICA/venv/lib/python3.11/site-packages/simple_websocket/__init__.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/simple_websocket/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/simple_websocket/__pycache__/aiows.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/simple_websocket/__pycache__/asgi.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/simple_websocket/__pycache__/errors.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/simple_websocket/__pycache__/ws.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/simple_websocket/aiows.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/simple_websocket/asgi.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/simple_websocket/errors.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/simple_websocket/ws.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/socketio/__init__.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/socketio/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/socketio/__pycache__/admin.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/socketio/__pycache__/asgi.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/socketio/__pycache__/async_admin.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/socketio/__pycache__/async_aiopika_manager.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/socketio/__pycache__/async_client.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/socketio/__pycache__/async_manager.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/socketio/__pycache__/async_namespace.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/socketio/__pycache__/async_pubsub_manager.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/socketio/__pycache__/async_redis_manager.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/socketio/__pycache__/async_server.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/socketio/__pycache__/async_simple_client.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/socketio/__pycache__/base_client.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/socketio/__pycache__/base_manager.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/socketio/__pycache__/base_namespace.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/socketio/__pycache__/base_server.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/socketio/__pycache__/client.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/socketio/__pycache__/exceptions.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/socketio/__pycache__/kafka_manager.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/socketio/__pycache__/kombu_manager.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/socketio/__pycache__/manager.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/socketio/__pycache__/middleware.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/socketio/__pycache__/msgpack_packet.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/socketio/__pycache__/namespace.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/socketio/__pycache__/packet.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/socketio/__pycache__/pubsub_manager.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/socketio/__pycache__/redis_manager.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/socketio/__pycache__/server.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/socketio/__pycache__/simple_client.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/socketio/__pycache__/tornado.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/socketio/__pycache__/zmq_manager.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/socketio/admin.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/socketio/asgi.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/socketio/async_admin.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/socketio/async_aiopika_manager.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/socketio/async_client.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/socketio/async_manager.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/socketio/async_namespace.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/socketio/async_pubsub_manager.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/socketio/async_redis_manager.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/socketio/async_server.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/socketio/async_simple_client.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/socketio/base_client.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/socketio/base_manager.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/socketio/base_namespace.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/socketio/base_server.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/socketio/client.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/socketio/exceptions.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/socketio/kafka_manager.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/socketio/kombu_manager.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/socketio/manager.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/socketio/middleware.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/socketio/msgpack_packet.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/socketio/namespace.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/socketio/packet.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/socketio/pubsub_manager.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/socketio/redis_manager.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/socketio/server.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/socketio/simple_client.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/socketio/tornado.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/socketio/zmq_manager.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/urllib3-2.4.0.dist-info/INSTALLER
 create mode 100644 LICA/venv/lib/python3.11/site-packages/urllib3-2.4.0.dist-info/METADATA
 create mode 100644 LICA/venv/lib/python3.11/site-packages/urllib3-2.4.0.dist-info/RECORD
 create mode 100644 LICA/venv/lib/python3.11/site-packages/urllib3-2.4.0.dist-info/WHEEL
 create mode 100644 LICA/venv/lib/python3.11/site-packages/urllib3/__init__.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/urllib3/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/urllib3/__pycache__/_base_connection.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/urllib3/__pycache__/_collections.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/urllib3/__pycache__/_request_methods.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/urllib3/__pycache__/_version.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/urllib3/__pycache__/connection.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/urllib3/__pycache__/connectionpool.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/urllib3/__pycache__/exceptions.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/urllib3/__pycache__/fields.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/urllib3/__pycache__/filepost.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/urllib3/__pycache__/poolmanager.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/urllib3/__pycache__/response.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/urllib3/_base_connection.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/urllib3/_collections.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/urllib3/_request_methods.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/urllib3/_version.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/urllib3/connection.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/urllib3/connectionpool.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/urllib3/contrib/__init__.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/urllib3/contrib/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/urllib3/contrib/__pycache__/pyopenssl.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/urllib3/contrib/__pycache__/socks.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/urllib3/contrib/emscripten/__init__.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/urllib3/contrib/emscripten/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/urllib3/contrib/emscripten/__pycache__/connection.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/urllib3/contrib/emscripten/__pycache__/fetch.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/urllib3/contrib/emscripten/__pycache__/request.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/urllib3/contrib/emscripten/__pycache__/response.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/urllib3/contrib/emscripten/connection.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/urllib3/contrib/emscripten/emscripten_fetch_worker.js
 create mode 100644 LICA/venv/lib/python3.11/site-packages/urllib3/contrib/emscripten/fetch.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/urllib3/contrib/emscripten/request.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/urllib3/contrib/emscripten/response.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/urllib3/contrib/pyopenssl.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/urllib3/contrib/socks.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/urllib3/exceptions.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/urllib3/fields.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/urllib3/filepost.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/urllib3/http2/__init__.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/urllib3/http2/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/urllib3/http2/__pycache__/connection.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/urllib3/http2/__pycache__/probe.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/urllib3/http2/connection.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/urllib3/http2/probe.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/urllib3/poolmanager.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/urllib3/py.typed
 create mode 100644 LICA/venv/lib/python3.11/site-packages/urllib3/response.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/urllib3/util/__init__.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/urllib3/util/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/urllib3/util/__pycache__/connection.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/urllib3/util/__pycache__/proxy.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/urllib3/util/__pycache__/request.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/urllib3/util/__pycache__/response.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/urllib3/util/__pycache__/retry.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/urllib3/util/__pycache__/ssl_.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/urllib3/util/__pycache__/ssl_match_hostname.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/urllib3/util/__pycache__/ssltransport.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/urllib3/util/__pycache__/timeout.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/urllib3/util/__pycache__/url.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/urllib3/util/__pycache__/util.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/urllib3/util/__pycache__/wait.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/urllib3/util/connection.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/urllib3/util/proxy.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/urllib3/util/request.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/urllib3/util/response.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/urllib3/util/retry.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/urllib3/util/ssl_.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/urllib3/util/ssl_match_hostname.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/urllib3/util/ssltransport.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/urllib3/util/timeout.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/urllib3/util/url.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/urllib3/util/util.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/urllib3/util/wait.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/werkzeug-3.1.3.dist-info/INSTALLER
 create mode 100644 LICA/venv/lib/python3.11/site-packages/werkzeug-3.1.3.dist-info/METADATA
 create mode 100644 LICA/venv/lib/python3.11/site-packages/werkzeug-3.1.3.dist-info/RECORD
 create mode 100644 LICA/venv/lib/python3.11/site-packages/werkzeug-3.1.3.dist-info/WHEEL
 create mode 100644 LICA/venv/lib/python3.11/site-packages/werkzeug/__init__.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/werkzeug/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/werkzeug/__pycache__/_internal.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/werkzeug/__pycache__/_reloader.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/werkzeug/__pycache__/exceptions.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/werkzeug/__pycache__/formparser.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/werkzeug/__pycache__/http.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/werkzeug/__pycache__/local.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/werkzeug/__pycache__/security.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/werkzeug/__pycache__/serving.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/werkzeug/__pycache__/test.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/werkzeug/__pycache__/testapp.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/werkzeug/__pycache__/urls.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/werkzeug/__pycache__/user_agent.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/werkzeug/__pycache__/utils.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/werkzeug/__pycache__/wsgi.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/werkzeug/_internal.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/werkzeug/_reloader.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/werkzeug/datastructures/__init__.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/werkzeug/datastructures/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/werkzeug/datastructures/__pycache__/accept.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/werkzeug/datastructures/__pycache__/auth.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/werkzeug/datastructures/__pycache__/cache_control.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/werkzeug/datastructures/__pycache__/csp.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/werkzeug/datastructures/__pycache__/etag.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/werkzeug/datastructures/__pycache__/file_storage.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/werkzeug/datastructures/__pycache__/headers.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/werkzeug/datastructures/__pycache__/mixins.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/werkzeug/datastructures/__pycache__/range.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/werkzeug/datastructures/__pycache__/structures.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/werkzeug/datastructures/accept.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/werkzeug/datastructures/auth.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/werkzeug/datastructures/cache_control.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/werkzeug/datastructures/csp.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/werkzeug/datastructures/etag.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/werkzeug/datastructures/file_storage.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/werkzeug/datastructures/headers.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/werkzeug/datastructures/mixins.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/werkzeug/datastructures/range.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/werkzeug/datastructures/structures.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/werkzeug/debug/__init__.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/werkzeug/debug/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/werkzeug/debug/__pycache__/console.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/werkzeug/debug/__pycache__/repr.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/werkzeug/debug/__pycache__/tbtools.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/werkzeug/debug/console.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/werkzeug/debug/repr.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/werkzeug/debug/shared/ICON_LICENSE.md
 create mode 100644 LICA/venv/lib/python3.11/site-packages/werkzeug/debug/shared/console.png
 create mode 100644 LICA/venv/lib/python3.11/site-packages/werkzeug/debug/shared/debugger.js
 create mode 100644 LICA/venv/lib/python3.11/site-packages/werkzeug/debug/shared/less.png
 create mode 100644 LICA/venv/lib/python3.11/site-packages/werkzeug/debug/shared/more.png
 create mode 100644 LICA/venv/lib/python3.11/site-packages/werkzeug/debug/shared/style.css
 create mode 100644 LICA/venv/lib/python3.11/site-packages/werkzeug/debug/tbtools.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/werkzeug/exceptions.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/werkzeug/formparser.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/werkzeug/http.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/werkzeug/local.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/werkzeug/middleware/__init__.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/werkzeug/middleware/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/werkzeug/middleware/__pycache__/dispatcher.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/werkzeug/middleware/__pycache__/http_proxy.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/werkzeug/middleware/__pycache__/lint.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/werkzeug/middleware/__pycache__/profiler.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/werkzeug/middleware/__pycache__/proxy_fix.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/werkzeug/middleware/__pycache__/shared_data.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/werkzeug/middleware/dispatcher.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/werkzeug/middleware/http_proxy.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/werkzeug/middleware/lint.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/werkzeug/middleware/profiler.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/werkzeug/middleware/proxy_fix.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/werkzeug/middleware/shared_data.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/werkzeug/py.typed
 create mode 100644 LICA/venv/lib/python3.11/site-packages/werkzeug/routing/__init__.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/werkzeug/routing/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/werkzeug/routing/__pycache__/converters.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/werkzeug/routing/__pycache__/exceptions.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/werkzeug/routing/__pycache__/map.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/werkzeug/routing/__pycache__/matcher.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/werkzeug/routing/__pycache__/rules.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/werkzeug/routing/converters.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/werkzeug/routing/exceptions.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/werkzeug/routing/map.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/werkzeug/routing/matcher.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/werkzeug/routing/rules.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/werkzeug/sansio/__init__.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/werkzeug/sansio/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/werkzeug/sansio/__pycache__/http.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/werkzeug/sansio/__pycache__/multipart.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/werkzeug/sansio/__pycache__/request.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/werkzeug/sansio/__pycache__/response.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/werkzeug/sansio/__pycache__/utils.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/werkzeug/sansio/http.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/werkzeug/sansio/multipart.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/werkzeug/sansio/request.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/werkzeug/sansio/response.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/werkzeug/sansio/utils.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/werkzeug/security.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/werkzeug/serving.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/werkzeug/test.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/werkzeug/testapp.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/werkzeug/urls.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/werkzeug/user_agent.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/werkzeug/utils.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/werkzeug/wrappers/__init__.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/werkzeug/wrappers/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/werkzeug/wrappers/__pycache__/request.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/werkzeug/wrappers/__pycache__/response.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/werkzeug/wrappers/request.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/werkzeug/wrappers/response.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/werkzeug/wsgi.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/wsproto-1.2.0.dist-info/INSTALLER
 create mode 100644 LICA/venv/lib/python3.11/site-packages/wsproto-1.2.0.dist-info/LICENSE
 create mode 100644 LICA/venv/lib/python3.11/site-packages/wsproto-1.2.0.dist-info/METADATA
 create mode 100644 LICA/venv/lib/python3.11/site-packages/wsproto-1.2.0.dist-info/RECORD
 create mode 100644 LICA/venv/lib/python3.11/site-packages/wsproto-1.2.0.dist-info/WHEEL
 create mode 100644 LICA/venv/lib/python3.11/site-packages/wsproto/__init__.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/wsproto/__pycache__/__init__.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/wsproto/__pycache__/connection.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/wsproto/__pycache__/events.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/wsproto/__pycache__/extensions.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/wsproto/__pycache__/frame_protocol.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/wsproto/__pycache__/handshake.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/wsproto/__pycache__/typing.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/wsproto/__pycache__/utilities.cpython-311.pyc
 create mode 100644 LICA/venv/lib/python3.11/site-packages/wsproto/connection.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/wsproto/events.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/wsproto/extensions.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/wsproto/frame_protocol.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/wsproto/handshake.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/wsproto/py.typed
 create mode 100644 LICA/venv/lib/python3.11/site-packages/wsproto/typing.py
 create mode 100644 LICA/venv/lib/python3.11/site-packages/wsproto/utilities.py
 create mode 120000 LICA/venv/lib64
 create mode 100644 LICA/venv/pyvenv.cfg
achintaggarwal@My-air genAI_experiments % 
achintaggarwal@My-air genAI_experiments % 
achintaggarwal@My-air genAI_experiments % 
achintaggarwal@My-air genAI_experiments % git fetch origin
git rebase origin/main

error: cannot rebase: You have unstaged changes.
error: Please commit or stash them.
achintaggarwal@My-air genAI_experiments % 
achintaggarwal@My-air genAI_experiments % 
achintaggarwal@My-air genAI_experiments % git status
On branch main
Your branch and 'origin/main' have diverged,
and have 4 and 4 different commits each, respectively.
  (use "git pull" to merge the remote branch into yours)

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
	modified:   cv-job-matcher/matchCVToJobs.py

Untracked files:
  (use "git add <file>..." to include in what will be committed)
	.DS_Store
	LICA/.DS_Store
	cv-job-matcher/.DS_Store
	cv-job-matcher/.idea/
	stock_quarterly_guidance/

no changes added to commit (use "git add" and/or "git commit -a")
achintaggarwal@My-air genAI_experiments % cd add ./LICA 
cd: string not in pwd: add
achintaggarwal@My-air genAI_experiments % cd add ./LICA/*
cd: too many arguments
achintaggarwal@My-air genAI_experiments % git add ./LICA/*
The following paths are ignored by one of your .gitignore files:
LICA/requirements.txt
hint: Use -f if you really want to add them.
hint: Turn this message off by running
hint: "git config advice.addIgnoredFile false"
achintaggarwal@My-air genAI_experiments % git add -f LICA/requirements.txt
achintaggarwal@My-air genAI_experiments % git commit -m "WIP: import LICA code"
[main 8adff6e] WIP: import LICA code
 Committer: Achint Aggarwal <achintaggarwal@My-air.local>
Your name and email address were configured automatically based
on your username and hostname. Please check that they are accurate.
You can suppress this message by setting them explicitly:

    git config --global user.name "Your Name"
    git config --global user.email you@example.com

After doing this, you may fix the identity used for this commit with:

    git commit --amend --reset-author

 1 file changed, 7 insertions(+)
 create mode 100644 LICA/requirements.txt
achintaggarwal@My-air genAI_experiments % 
achintaggarwal@My-air genAI_experiments % 
achintaggarwal@My-air genAI_experiments % git fetch origin
achintaggarwal@My-air genAI_experiments % git rebase origin/main
error: cannot rebase: You have unstaged changes.
error: Please commit or stash them.
achintaggarwal@My-air genAI_experiments % git status
On branch main
Your branch and 'origin/main' have diverged,
and have 5 and 4 different commits each, respectively.
  (use "git pull" to merge the remote branch into yours)

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
	modified:   cv-job-matcher/matchCVToJobs.py

Untracked files:
  (use "git add <file>..." to include in what will be committed)
	.DS_Store
	LICA/.DS_Store
	cv-job-matcher/.DS_Store
	cv-job-matcher/.idea/
	stock_quarterly_guidance/

no changes added to commit (use "git add" and/or "git commit -a")
achintaggarwal@My-air genAI_experiments % 
achintaggarwal@My-air genAI_experiments % 
achintaggarwal@My-air genAI_experiments % git add cv-job-matcher/matchCVToJobs.py
git commit -m "WIP: update matchCVToJobs"

[main e8a4c87] WIP: update matchCVToJobs
 Committer: Achint Aggarwal <achintaggarwal@My-air.local>
Your name and email address were configured automatically based
on your username and hostname. Please check that they are accurate.
You can suppress this message by setting them explicitly:

    git config --global user.name "Your Name"
    git config --global user.email you@example.com

After doing this, you may fix the identity used for this commit with:

    git commit --amend --reset-author

 1 file changed, 7 insertions(+), 7 deletions(-)
achintaggarwal@My-air genAI_experiments % 
achintaggarwal@My-air genAI_experiments % 
achintaggarwal@My-air genAI_experiments % git fetch origin
git rebase origin/main

warning: unable to rmdir 'LICA': Directory not empty
warning: unable to rmdir 'LICA': Directory not empty
Successfully rebased and updated refs/heads/main.
achintaggarwal@My-air genAI_experiments % 
achintaggarwal@My-air genAI_experiments % 
achintaggarwal@My-air genAI_experiments % git push --force-with-lease origin main

Enumerating objects: 6212, done.
Counting objects: 100% (6212/6212), done.
Delta compression using up to 8 threads
Compressing objects: 100% (6147/6147), done.
error: RPC failed; HTTP 400 curl 22 The requested URL returned error: 400
send-pack: unexpected disconnect while reading sideband packet
Writing objects: 100% (6209/6209), 33.31 MiB | 8.80 MiB/s, done.
Total 6209 (delta 1428), reused 0 (delta 0), pack-reused 0
fatal: the remote end hung up unexpectedly
Everything up-to-date
achintaggarwal@My-air genAI_experiments % 
achintaggarwal@My-air genAI_experiments % 
achintaggarwal@My-air genAI_experiments % git remote set-url origin git@github.com:rsachint/genAI_experiments.git
achintaggarwal@My-air genAI_experiments % git push --force-with-lease origin main
Enter passphrase for key '/Users/achintaggarwal/.ssh/id_ed25519': 
Enumerating objects: 6212, done.
Counting objects: 100% (6212/6212), done.
Delta compression using up to 8 threads
Compressing objects: 100% (6147/6147), done.
Writing objects: 100% (6209/6209), 33.31 MiB | 873.00 KiB/s, done.
Total 6209 (delta 1426), reused 0 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (1426/1426), completed with 2 local objects.
To github.com:rsachint/genAI_experiments.git
   3203aed..0ef0fc6  main -> main
achintaggarwal@My-air genAI_experiments % 
achintaggarwal@My-air genAI_experiments % 
achintaggarwal@My-air genAI_experiments % 
achintaggarwal@My-air genAI_experiments % 
achintaggarwal@My-air genAI_experiments % git status
On branch main
Your branch is up to date with 'origin/main'.

Untracked files:
  (use "git add <file>..." to include in what will be committed)
	.DS_Store
	LICA/.DS_Store
	cv-job-matcher/.DS_Store
	cv-job-matcher/.idea/
	stock_quarterly_guidance/

nothing added to commit but untracked files present (use "git add" to track)
achintaggarwal@My-air genAI_experiments % 
achintaggarwal@My-air genAI_experiments % 
achintaggarwal@My-air genAI_experiments % 
achintaggarwal@My-air genAI_experiments % 
achintaggarwal@My-air genAI_experiments % 
achintaggarwal@My-air genAI_experiments % cd LICA/.DS_Store 
achintaggarwal@My-air genAI_experiments % git status
achintaggarwal@My-air genAI_experiments % 
achintaggarwal@My-air genAI_experiments % 
achintaggarwal@My-air genAI_experiments % cd LICA/.DS_Store 
cd: not a directory: LICA/.DS_Store
achintaggarwal@My-air genAI_experiments % cd LICA 
achintaggarwal@My-air LICA % cd .DS_Store 
cd: not a directory: .DS_Store
achintaggarwal@My-air LICA % ls
app.py			requirements.txt	root@164.52.193.175	templates		venv
achintaggarwal@My-air LICA % ls plrt
ls: plrt: No such file or directory
achintaggarwal@My-air LICA % 
achintaggarwal@My-air LICA % ls plrt
ls: plrt: No such file or directory
achintaggarwal@My-air LICA % 
achintaggarwal@My-air LICA % ls -lrt
total 16
-rw-r--r--  1 achintaggarwal  staff  2377 May  7 13:55 app.py
drwxr-xr-x  7 achintaggarwal  staff   224 May  7 13:55 root@164.52.193.175
drwxr-xr-x  3 achintaggarwal  staff    96 May  7 13:55 templates
drwxr-xr-x  7 achintaggarwal  staff   224 May  7 13:55 venv
-rw-r--r--  1 achintaggarwal  staff    68 May  7 13:55 requirements.txt
achintaggarwal@My-air LICA % 
achintaggarwal@My-air LICA % 
achintaggarwal@My-air LICA % 
achintaggarwal@My-air LICA % vi requirements.txt 
achintaggarwal@My-air LICA % 
achintaggarwal@My-air LICA % 
achintaggarwal@My-air LICA % 
achintaggarwal@My-air LICA %    
achintaggarwal@My-air LICA % 
achintaggarwal@My-air LICA % npm install -g vercel
vercel login

⠼
npm error code EACCES
npm error syscall mkdir
npm error path /usr/local/lib/node_modules/vercel
npm error errno -13
npm error Error: EACCES: permission denied, mkdir '/usr/local/lib/node_modules/vercel'
npm error     at async mkdir (node:internal/fs/promises:852:10)
npm error     at async /usr/local/lib/node_modules/npm/node_modules/@npmcli/arborist/lib/arborist/reify.js:624:20
npm error     at async Promise.allSettled (index 0)
npm error     at async [reifyPackages] (/usr/local/lib/node_modules/npm/node_modules/@npmcli/arborist/lib/arborist/reify.js:325:11)
npm error     at async Arborist.reify (/usr/local/lib/node_modules/npm/node_modules/@npmcli/arborist/lib/arborist/reify.js:142:5)
npm error     at async Install.exec (/usr/local/lib/node_modules/npm/lib/commands/install.js:150:5)
npm error     at async Npm.exec (/usr/local/lib/node_modules/npm/lib/npm.js:207:9)
npm error     at async module.exports (/usr/local/lib/node_modules/npm/lib/cli/entry.js:74:5) {
npm error   errno: -13,
npm error   code: 'EACCES',
npm error   syscall: 'mkdir',
npm error   path: '/usr/local/lib/node_modules/vercel'
npm error }
npm error
npm error The operation was rejected by your operating system.
npm error It is likely you do not have the permissions to access this file as the current user
npm error
npm error If you believe this might be a permissions issue, please double-check the
npm error permissions of the file and its containing directories, or try running
npm error the command again as root/Administrator.
npm notice
npm notice New major version of npm available! 10.9.2 -> 11.3.0
npm notice Changelog: https://github.com/npm/cli/releases/tag/v11.3.0
npm notice To update run: npm install -g npm@11.3.0
npm notice
npm error A complete log of this run can be found in: /Users/achintaggarwal/.npm/_logs/2025-05-07T08_45_46_108Z-debug-0.log
zsh: command not found: vercel
achintaggarwal@My-air LICA % 
achintaggarwal@My-air LICA % 
achintaggarwal@My-air LICA % 
achintaggarwal@My-air LICA % 
achintaggarwal@My-air LICA % 
achintaggarwal@My-air LICA % 
achintaggarwal@My-air LICA % 
achintaggarwal@My-air LICA % 
achintaggarwal@My-air LICA % 
achintaggarwal@My-air LICA % 
achintaggarwal@My-air LICA % brew install vercel/tap/vercel
vercel login
vercel link --project=gen-ai-experiments --confirm
vercel --prod

==> Auto-updating Homebrew...
Adjust how often this is run with HOMEBREW_AUTO_UPDATE_SECS or disable with
HOMEBREW_NO_AUTO_UPDATE. Hide these hints with HOMEBREW_NO_ENV_HINTS (see `man brew`).
==> Auto-updated Homebrew!
Updated 2 taps (homebrew/core and homebrew/cask).
==> New Formulae
camlpdf                         hexd                            readerwriterqueue               sexpect
elfio                           iccmax                          rofi                            swiftly
girara                          miniflux                        sequoia-chameleon-gnupg         yeet
==> New Casks
aqua-voice                                 font-fzxiheii-z08                          font-wdxl-lubrifont-sc
cloudpouch                                 font-harmonyos-sans                        meru
clover-chord-systems                       font-harmonyos-sans-naskh-arabic           sc-menu
elemental@6                                font-harmonyos-sans-sc                     witsy
font-asta-sans                             font-harmonyos-sans-tc
font-fzhei-b01                             font-wdxl-lubrifont-jp-n

You have 18 outdated formulae installed.

==> Tapping vercel/tap
Cloning into '/usr/local/Homebrew/Library/Taps/vercel/homebrew-tap'...
remote: Repository not found.
fatal: repository 'https://github.com/vercel/homebrew-tap/' not found
Error: Failure while executing; `git clone https://github.com/vercel/homebrew-tap /usr/local/Homebrew/Library/Taps/vercel/homebrew-tap --origin=origin --template= --config core.fsmonitor=false` exited with 128.
zsh: command not found: vercel
zsh: command not found: vercel
zsh: command not found: vercel
achintaggarwal@My-air LICA % 
achintaggarwal@My-air LICA % 
achintaggarwal@My-air LICA % 
achintaggarwal@My-air LICA % 
achintaggarwal@My-air LICA % 
achintaggarwal@My-air LICA % npx vercel link --yes --project=gen-ai-experiments --confirm
Need to install the following packages:
vercel@41.7.2
Ok to proceed? (y) y

npm warn deprecated inflight@1.0.6: This module is not supported, and leaks memory. Do not use it. Check out lru-cache if you want a good and tested way to coalesce async requests by a key value, which is much more comprehensive and powerful.
npm warn deprecated glob@7.2.3: Glob versions prior to v9 are no longer supported
npm warn deprecated uuid@3.3.2: Please upgrade  to version 7 or higher.  Older versions may use Math.random() in certain circumstances, which is known to be problematic.  See https://v8.dev/blog/math-random for details.
Vercel CLI 41.7.2
> NOTE: The Vercel CLI now collects telemetry regarding usage of the CLI.
> This information is used to shape the CLI roadmap and prioritize features.
> You can learn more, including how to opt-out if you'd not like to participate in this program, by visiting the following URL:
> https://vercel.com/docs/cli/about-telemetry
> No existing credentials found. Please log in:
? Log in to Vercel Continue with GitHub
> Success! GitHub authentication complete for rsachint@gmail.com
WARN! `--confirm` is deprecated, please use `--yes` instead
✅  Linked to rsachints-projects/gen-ai-experiments (created .vercel and added it to .gitignore)
achintaggarwal@My-air LICA % 

achintaggarwal@My-air LICA % cd ../
achintaggarwal@My-air genAI_experiments % cd -
~/Documents/GenAI/genAI_experiments/LICA
achintaggarwal@My-air LICA % ls
app.py			requirements.txt	root@164.52.193.175	templates		venv
achintaggarwal@My-air LICA % ls -lrt
total 16
-rw-r--r--  1 achintaggarwal  staff  2377 May  7 13:55 app.py
drwxr-xr-x  7 achintaggarwal  staff   224 May  7 13:55 root@164.52.193.175
drwxr-xr-x  3 achintaggarwal  staff    96 May  7 13:55 templates
drwxr-xr-x  7 achintaggarwal  staff   224 May  7 13:55 venv
-rw-r--r--  1 achintaggarwal  staff    68 May  7 13:55 requirements.txt
achintaggarwal@My-air LICA % 
achintaggarwal@My-air LICA % 
achintaggarwal@My-air LICA % cd ..
achintaggarwal@My-air genAI_experiments % 
achintaggarwal@My-air genAI_experiments % npx vercel --prod
Vercel CLI 41.7.2
? Set up and deploy “~/Documents/GenAI/genAI_experiments”? yes
? Which scope should contain your project? GenAI
? Found project “rsachints-projects/gen-ai-experiments”. Link to it? yes
🔗  Linked to rsachints-projects/gen-ai-experiments (created .vercel and added it to .gitignore)
🔍  Inspect: https://vercel.com/rsachints-projects/gen-ai-experiments/6qLCzMgZoqPPnxh4TsemK6g7r7nF [3s]
✅  Production: https://gen-ai-experiments-p1c9jw5fh-rsachints-projects.vercel.app [3s]
achintaggarwal@My-air genAI_experiments % 
achintaggarwal@My-air genAI_experiments % 
achintaggarwal@My-air genAI_experiments % 
achintaggarwal@My-air genAI_experiments % 
achintaggarwal@My-air genAI_experiments % 
achintaggarwal@My-air genAI_experiments % 
achintaggarwal@My-air genAI_experiments % 
achintaggarwal@My-air genAI_experiments % 
achintaggarwal@My-air genAI_experiments % mkdir -p public
achintaggarwal@My-air genAI_experiments % 
achintaggarwal@My-air genAI_experiments % 
achintaggarwal@My-air genAI_experiments % vi public/index.html
achintaggarwal@My-air genAI_experiments % 
achintaggarwal@My-air genAI_experiments % 
achintaggarwal@My-air genAI_experiments % vi public/app.js
achintaggarwal@My-air genAI_experiments % 
achintaggarwal@My-air genAI_experiments % 
achintaggarwal@My-air genAI_experiments % vi vercel.json
achintaggarwal@My-air genAI_experiments % 
achintaggarwal@My-air genAI_experiments % 
achintaggarwal@My-air genAI_experiments % 
achintaggarwal@My-air genAI_experiments % git add public vercel.json
git commit -m "Add basic frontend stub and Vercel config"
npx vercel --prod

[main c471d37] Add basic frontend stub and Vercel config
 Committer: Achint Aggarwal <achintaggarwal@My-air.local>
Your name and email address were configured automatically based
on your username and hostname. Please check that they are accurate.
You can suppress this message by setting them explicitly:

    git config --global user.name "Your Name"
    git config --global user.email you@example.com

After doing this, you may fix the identity used for this commit with:

    git commit --amend --reset-author

 3 files changed, 49 insertions(+)
 create mode 100644 public/app.js
 create mode 100644 public/index.html
 create mode 100644 vercel.json
Error: Couldn't parse JSON file /Users/achintaggarwal/Documents/GenAI/genAI_experiments/vercel.json.
achintaggarwal@My-air genAI_experiments % 
achintaggarwal@My-air genAI_experiments % 
achintaggarwal@My-air genAI_experiments % rm vercel.json 
achintaggarwal@My-air genAI_experiments % vi vercel.json
achintaggarwal@My-air genAI_experiments % 
achintaggarwal@My-air genAI_experiments % 
achintaggarwal@My-air genAI_experiments % git add vercel.json
git commit -m "Fix vercel.json syntax"
npx vercel --prod
[main 012ee17] Fix vercel.json syntax
 Committer: Achint Aggarwal <achintaggarwal@My-air.local>
Your name and email address were configured automatically based
on your username and hostname. Please check that they are accurate.
You can suppress this message by setting them explicitly:

    git config --global user.name "Your Name"
    git config --global user.email you@example.com

After doing this, you may fix the identity used for this commit with:

    git commit --amend --reset-author

 1 file changed, 2 insertions(+), 4 deletions(-)
Vercel CLI 41.7.2
🔍  Inspect: https://vercel.com/rsachints-projects/gen-ai-experiments/7VgXa6hRUZjsNhL8jYM9DKztZG8j [2s]
✅  Production: https://gen-ai-experiments-1q5d415uy-rsachints-projects.vercel.app [2s]
❗️  Due to `builds` existing in your configuration file, the Build and Development Settings defined in your Project Settings will not apply. Learn More: https://vercel.link/unused-build-settings
achintaggarwal@My-air genAI_experiments % 
achintaggarwal@My-air genAI_experiments % 
achintaggarwal@My-air genAI_experiments % 
achintaggarwal@My-air genAI_experiments % 
achintaggarwal@My-air genAI_experiments % 
achintaggarwal@My-air genAI_experiments % cd LICA 
achintaggarwal@My-air LICA % ls
app.py			requirements.txt	root@164.52.193.175	templates		venv
achintaggarwal@My-air LICA % ls -lrt
total 16
-rw-r--r--  1 achintaggarwal  staff  2377 May  7 13:55 app.py
drwxr-xr-x  7 achintaggarwal  staff   224 May  7 13:55 root@164.52.193.175
drwxr-xr-x  3 achintaggarwal  staff    96 May  7 13:55 templates
drwxr-xr-x  7 achintaggarwal  staff   224 May  7 13:55 venv
-rw-r--r--  1 achintaggarwal  staff    68 May  7 13:55 requirements.txt
achintaggarwal@My-air LICA % 
achintaggarwal@My-air LICA % 
achintaggarwal@My-air LICA % 
achintaggarwal@My-air LICA % 
achintaggarwal@My-air LICA % 
achintaggarwal@My-air LICA % 
achintaggarwal@My-air LICA % 
achintaggarwal@My-air LICA % 
achintaggarwal@My-air LICA % 
achintaggarwal@My-air LICA % cd 
achintaggarwal@My-air ~ % 
achintaggarwal@My-air ~ % 
achintaggarwal@My-air ~ % cd Documents/GenAI/LICA/Sarvam 
achintaggarwal@My-air Sarvam % 
achintaggarwal@My-air Sarvam % 
achintaggarwal@My-air Sarvam % 
achintaggarwal@My-air Sarvam % cp ~/Downloads/app.py .
achintaggarwal@My-air Sarvam % 
achintaggarwal@My-air Sarvam % 
achintaggarwal@My-air Sarvam % 
achintaggarwal@My-air Sarvam % 
achintaggarwal@My-air Sarvam % ls -lrt
total 72
drwxr-xr-x  6 achintaggarwal  staff   192 Apr 30 13:42 venv
-rw-r--r--@ 1 achintaggarwal  staff  5446 May  3 17:47 pipeline.py_nopydub_VAD_working
-rw-r--r--  1 achintaggarwal  staff  6544 May  3 18:29 pipeline.py_webrtc_highlatency_working
-rw-r--r--  1 achintaggarwal  staff  5320 May  3 18:37 pipeline.py_globalpcm_buffer
-rw-r--r--@ 1 achintaggarwal  staff  5324 May  5 13:06 pipeline.py
-rw-r--r--@ 1 achintaggarwal  staff  2377 May  7 19:18 app.py
achintaggarwal@My-air Sarvam % 
achintaggarwal@My-air Sarvam % 
achintaggarwal@My-air Sarvam % diff app.py pipeline.py
1d0
< from flask import Flask, render_template, request, jsonify
2a2,4
> import io
> import time
> import json
3a6
> import threading
5a9,15
> from flask import Flask, request, jsonify
> import wave
> import numpy as np
> import sounddevice as sd
> import soundfile as sf
> import argparse
> import tempfile
7,9c17,23
< app = Flask(__name__)
< load_dotenv()
< API_KEY = os.getenv("SARVAM_API_KEY")
---
> # --- Configuration ---
> def load_api_key():
>     load_dotenv()
>     key = os.getenv("SARVAM_API_KEY")
>     if not key:
>         raise ValueError("Set SARVAM_API_KEY in .env file")
>     return key
11,13c25,29
< @app.route('/')
< def index():
<     return render_template('index.html')
---
> # --- Global audio buffer for reuse ---
> FS = 22050
> MAX_DURATION = 5  # seconds
> MAX_SAMPLES = FS * MAX_DURATION
> pcm_buffer = np.zeros(MAX_SAMPLES, dtype=np.int16)
15,19c31,32
< @app.route('/translate_play', methods=['POST'])
< def translate_and_play():
<     data = request.get_json()
<     role = data.get('role')
<     audio_b64 = data.get('audio')
---
> # --- Audio Utilities with simple VAD trimming ---
> from pydub.silence import detect_nonsilent
21,22c34,43
<     if not API_KEY or not audio_b64 or not role:
<         return jsonify({'error': 'Missing data'}), 400
---
> def record_audio(duration=5.0, fs=16000):
>     print(f"Recording {duration}s audio...")
>     recording = sd.rec(int(duration * fs), samplerate=fs, channels=1)
>     sd.wait()
>     tmp = f"{time.time()}.wav"
>     tmpf = tempfile.NamedTemporaryFile(suffix='.wav', delete=False)
>     tmpf_name = tmpf.name
>     tmpf.close()
>     sf.write(tmpf_name, recording, fs)
>     return tmpf_name
24,28c45,54
<     # Save audio to temp file
<     audio_data = base64.b64decode(audio_b64.split(',')[1])
<     tmp_path = f"/tmp/{role}_input.wav"
<     with open(tmp_path, "wb") as f:
<         f.write(audio_data)
---
> # --- STT / Translate / TTS ---
> def speech_to_text(api_key, path):
>     url = "https://api.sarvam.ai/speech-to-text"
>     headers = {"API-Subscription-Key": api_key}
>     files = {"file": (os.path.basename(path), open(path, "rb"), "audio/wav")}
>     data = {"model": "saarika:v2", "language_code": "unknown", "with_diarization": "false"}
>     r = requests.post(url, headers=headers, files=files, data=data)
>     r.raise_for_status()
>     resp = r.json()
>     return resp.get("transcript", ""), resp.get("language_code", "hi-IN")
30,36c56,62
<     # Step 1: STT (Sarvam API)
<     stt_response = requests.post(
<         "https://api.sarvam.ai/speech-to-text",
<         headers={"API-Subscription-Key": API_KEY},
<         files={"file": ("audio.wav", open(tmp_path, "rb"), "audio/wav")},
<         data={"model": "saarika:v2", "language_code": "unknown"}
<     ).json()
---
> def translate_text(api_key, text, src, tgt):
>     url = "https://api.sarvam.ai/translate"
>     headers = {"Content-Type": "application/json", "API-Subscription-Key": api_key}
>     payload = {"input": text, "source_language_code": src, "target_language_code": tgt, "mode": "formal"}
>     r = requests.post(url, headers=headers, json=payload)
>     r.raise_for_status()
>     return r.json().get("translated_text", "")
38c64,74
<     transcript = stt_response.get("transcript", "")
---
> def text_to_speech(api_key, text, tgt, speaker):
>     url = "https://api.sarvam.ai/text-to-speech"
>     headers = {"Content-Type": "application/json", "API-Subscription-Key": api_key}
>     payload = {"text": text, "target_language_code": tgt, "speaker": speaker,
>                "pitch": 0.0, "pace": 1.0, "loudness": 1.0, "speech_sample_rate": FS}
>     r = requests.post(url, headers=headers, json=payload)
>     r.raise_for_status()
>     audios = r.json().get("audios", [])
>     if not audios:
>         raise ValueError("No audio returned from TTS")
>     return base64.b64decode(audios[0])
40,44c76,98
<     # Step 2: Define language direction
<     if role == "teacher":
<         src, tgt, speaker, target_box = "hi-IN", "pa-IN", "anushka", "student"
<     else:
<         src, tgt, speaker, target_box = "pa-IN", "hi-IN", "karun", "teacher"
---
> # --- HTTP Server for playback with direct buffers ---
> app = Flask(__name__)
> @app.route('/play', methods=['POST'])
> def play_endpoint():
>     data = request.get_json()
>     b64 = data.get('audio_b64')
>     if not b64:
>         return jsonify({'error': 'no audio'}), 400
>     audio_bytes = base64.b64decode(b64)
>     buf = io.BytesIO(audio_bytes)
>     with wave.open(buf, 'rb') as wf:
>         sr = wf.getframerate()
>         chans = wf.getnchannels()
>         width = wf.getsampwidth()
>         frames = wf.readframes(wf.getnframes())
>     # reuse pcm_buffer
>     dtype = {1: np.int8, 2: np.int16, 4: np.int32}[width]
>     audio_data = np.frombuffer(frames, dtype=dtype)
>     if chans > 1:
>         audio_data = data.reshape(-1, chans)
>     # Play directly without a fixed buffer
>     sd.play(audio_data.astype(np.int16), samplerate=sr, blocking=False)
>     return jsonify({'status': 'playing'}), 200
46,56c100,101
<     # Step 3: Translate (Sarvam)
<     translation = requests.post(
<         "https://api.sarvam.ai/translate",
<         headers={"API-Subscription-Key": API_KEY, "Content-Type": "application/json"},
<         json={
<             "input": transcript,
<             "source_language_code": src,
<             "target_language_code": tgt,
<             "mode": "formal"
<         }
<     ).json().get("translated_text", "")
---
> def start_server(port):
>     threading.Thread(target=lambda: app.run(port=port, threaded=True, use_reloader=False), daemon=True).start()
58,67c103,114
<     # Step 4: TTS (Sarvam)
<     tts_response = requests.post(
<         "https://api.sarvam.ai/text-to-speech",
<         headers={"API-Subscription-Key": API_KEY, "Content-Type": "application/json"},
<         json={
<             "text": translation,
<             "target_language_code": tgt,
<             "speaker": speaker
<         }
<     ).json()
---
> # --- Main roles ---
> def run_teacher(api_key, peer_port):
>     print("Press Enter to record speech...")
>     input()
>     wav = record_audio()
>     htxt, _ = speech_to_text(api_key, wav)
>     print(f"Teacher said (HI): {htxt}")
>     ptxt = translate_text(api_key, htxt, 'hi-IN', 'pa-IN')
>     print(f"Translated to Punjabi: {ptxt}")
>     raw = text_to_speech(api_key, ptxt, 'pa-IN', 'anushka')
>     payload = {'audio_b64': base64.b64encode(raw).decode()}
>     requests.post(f"http://127.0.0.1:{peer_port}/play", json=payload)
69d115
<     audio_out_b64 = tts_response.get("audios", [""])[0]
71,76c117,127
<     return jsonify({
<         "original": transcript,
<         "translated": translation,
<         "audio": audio_out_b64,
<         "target_box": target_box
<     })
---
> def run_student(api_key, peer_port):
>     print("Press Enter to record speech...")
>     input()
>     wav = record_audio()
>     ptext, _ = speech_to_text(api_key, wav)
>     print(f"Student said (PA): {ptext}")
>     htxt = translate_text(api_key, ptext, 'pa-IN', 'hi-IN')
>     print(f"Translated to Hindi: {htxt}")
>     raw = text_to_speech(api_key, htxt, 'hi-IN', 'karun')
>     payload = {'audio_b64': base64.b64encode(raw).decode()}
>     requests.post(f"http://127.0.0.1:{peer_port}/play", json=payload)
77a129
> # --- Entry Point ---
79c131,148
<     app.run(host="0.0.0.0", port=5000)
---
>     parser = argparse.ArgumentParser()
>     parser.add_argument('role', choices=['teacher', 'student'])
>     args = parser.parse_args()
>     api_key = load_api_key()
>     if args.role == 'teacher':
>         my_port, peer_port = 8000, 8001
>     else:
>         my_port, peer_port = 8001, 8000
>     start_server(my_port)
>     print(f"Started {args.role} server on port {my_port}, peer at {peer_port}")
>     try:
>         while True:
>             if args.role == 'teacher':
>                 run_teacher(api_key, peer_port)
>             else:
>                 run_student(api_key, peer_port)
>     except KeyboardInterrupt:
>         print("Exiting.")
achintaggarwal@My-air Sarvam % 
achintaggarwal@My-air Sarvam % 
achintaggarwal@My-air Sarvam % 
achintaggarwal@My-air Sarvam % 
achintaggarwal@My-air Sarvam % 
achintaggarwal@My-air Sarvam % 
achintaggarwal@My-air Sarvam % vi app.py 

from flask import Flask, render_template, request, jsonify
import os
import base64
import requests
from dotenv import load_dotenv

app = Flask(__name__)
load_dotenv()
API_KEY = os.getenv("SARVAM_API_KEY")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/translate_play', methods=['POST'])
def translate_and_play():
    data = request.get_json()
    role = data.get('role')
    audio_b64 = data.get('audio')

    if not API_KEY or not audio_b64 or not role:
        return jsonify({'error': 'Missing data'}), 400

    # Save audio to temp file
    audio_data = base64.b64decode(audio_b64.split(',')[1])
    tmp_path = f"/tmp/{role}_input.wav"
    with open(tmp_path, "wb") as f:
        f.write(audio_data)
"app.py" 80L, 2377B
