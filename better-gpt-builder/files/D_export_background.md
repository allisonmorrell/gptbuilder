STEPS: **EACH MUST BE IN A SEPARATE CALL TO THE `python` TOOL**, wait for results before continuing:
* Create directory named after the user's GPT (here called `Name`).
* Move `specifications.txt` to `Name`
* If there are uploaded or created files: 1) create `files` within `Name`, 2) move all to `Name/files`
* Write config info to `Name/configuration.txt`
* Create `Name/instructions.txt`
* For about each 50 lines of instructions, **separately** call `python` to append to `Name/instructions.txt`