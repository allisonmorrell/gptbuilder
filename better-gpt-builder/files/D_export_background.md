STEPS: **EACH MUST BE SEPARATE CALL TO THE `python`**, await results for each until done:
* Create dir with GPT Name (here called `Name`).
* Move to `Name`:
    * `specifications.txt`
    * If there are uploaded or created files, move all to new dir `Name/files`
* Write config info to `Name/configuration.txt`
* Create `Name/instructions.txt`
* For about each 50 lines of instructions, **separately** call `python` to append to `Name/instructions.txt`
* When done, zip folder and provide download