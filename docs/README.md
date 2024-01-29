# gptbuilder
Repository of my thoughts on creating GPTs, and instructions and files for [Better GPT Builder](https://chat.openai.com/g/g-0CAiaGJje-better-gpt-builder).

If you are willing to share your conversation transcript to improve this tool, or if you want to showcase your GPT in the list below, please open an issue or [submit this form](https://forms.gle/he2qFcpdjdrEBpaq6).

# Better GPT Builder
**[Better GPT Builder](https://chat.openai.com/g/g-0CAiaGJje-better-gpt-builder)** is an ongoing experiment in exploring the potential of structured interaction and workflows using GPTs. I'm trying to push the limits of how much you can reasonably reliably direct the behaviour of a chatbot with just instructions, code and files. You can see the instructions [here](https://github.com/allisonmorrell/gptbuilder/blob/main/better-gpt-builder/instructions.md).

## What - a GPT to build GPTs
Better GPT Builder implements some of my thoughts on ways to design good GPTs and the best way to work with language models. 

It walks the user through a process from brainstorming, outlining desired behaviour, writing instructions and providing download links for the final content that they can paste into the OpenAI configuration panel when creating a GPT.

## Why this repository?
I believe that more people should share their prompts and thinking process for the sake of all being able to develop the best techniques.

In any case, there's **no 100% reliable way of protecting prompts** from someone who asks in the right way. I don't think building GPTs will be some huge business opportunity. Instead, I hope people will share their ideas and techniques so that everyone can get the most value out of these tools. There should be open-source GPTs, the same as any other useful software thing!

## Example GPTs created by Better GPT Builder
* **[ArtMuse](https://chat.openai.com/g/g-kY3woUU1m-artmuse)**: A conversational AI designed to spark creativity and offer visual art inspirations through dialogue and DALL-E visualizations.
    * Creation [transcript](https://chat.openai.com/share/bc93a6ac-311e-41b6-b3ae-62e2879c5ad2) dated November 14, 2023
* **[Career Assistant](https://chat.openai.com/g/g-EbYpo1ISQ-career-assistant)**: Coaches user on resume and LinkedIn profile updates, and general advice and help.
    * Creation [transcript](https://chat.openai.com/share/87b84ae4-b229-4347-b4da-a8e800054e50) first iteration
    * Builder improvement [transcript](https://chat.openai.com/share/c0b187de-af40-47da-81a9-5175508bee0c)
* **[Photo Era Identifier](https://chat.openai.com/g/g-iAP1EJ5Bn-photo-era-identifier)**: Identifies photo eras with historical context.
    * Creation [transcript](https://chat.openai.com/share/620cf78c-c48f-47ce-857d-7205d6115fbe) (this demonstrates a capacity to execute multiple steps in a row upon request)

## Why - enhancing the GPT creation process
I started this project because I find OpenAI's chatbot interface for creating GPTs frustrating in various ways. It tends to result in fairly short and general instructions that don't capture most of what the user says. It can't seem to follow direct instructions like "put exactly this text into the instructions". It will also overwrite previous instructions and lacks versioning.

## How - a structured approach
In my experience, GPTs tend to struggle with lengthy and specific instructions. Better GPT Builder is designed to proceed step by step through a specific workflow, using several techniques to attempt to stay on track: 
1. The instructions use lettered stages and numbered substages.
2. The instructions direct the GPT to 'silently read' specific uploaded files using Code Interpreter at specific stages before proceeding. Those files contain more instructions.
3. The instructions direct the GPT to use a specific format for all responses, and that format includes a reference to the letter and number of the current stage.

So far this has resulted in pretty consistent behaviour. If it goes off the rails in a chat, **please consider submitting an issue so I can look at it.** Taken together, this permits the GPT to fairly reliable proceed through a linear process, where it decides when to move on through stages, and causes additional instructions to be injected through reading files.


# GPTs: A terrible name for a fun thing

## Background on GPTs
For background on how to create a GPT, see [OpenAI's article](https://help.openai.com/en/articles/8554397-creating-a-gpt).

Simon Willison - [Exploring GPTs: ChatGPT in a trench coat?](https://simonwillison.net/2023/Nov/15/gpts/)
* explanation of creator and configuration panel
* also contains full prompt for creator

Ethan Mollick's article [Almost an Agent: What GPTs can do](https://www.oneusefulthing.org/p/almost-an-agent-what-gpts-can-do) is a great backgrounder on the possibilities for using GPTs.


## What's the point of GPTs? 
In my opinion, many of the most valuable applications of generative AI will not be chatbots. Chatbots often lack affordances - they don't tell the user what they can or should do. 

Further, the best chatbots incorporate more structure behind the scenes - for example, displaying documents to the user, presenting the user with action buttons, and overall using the chatbot UI to facilitate a well-designed workflow and application features. If you know what you want to do, you can get far with this approach. Personally I've used [Chainlit](https://docs.chainlit.io/get-started/overview) to build these. 

Does this mean that GPTs are useless? No! They're a great starting point for exploration of the potential applications for generative AI, in terms of: 
* **What is desirable:** what do users get more excited about? How do they want AI to help them?
* **What is possible:** in what cases are chatbots good enough? How far can you get with just instructions?

Most importantly, GPTs are a low-barrier opportunity for users to create tools that help them and others. 

## Weird things about GPTs

Sadly, OpenAI often messes around with GPTs in potentially consequential ways without telling anyone. I will try to keep track of those here. I may also start maintaining copies of the system prompts.

* 2023-11-14 (about) - code interpreter force truncates file output to 500 characters
* 2023-11-14 - started sometimes copying full knowledge file(s) into instructions, and telling it to avoid browsing if knowledge is there
* 2023-11-15 - noticed that files generated in preview pane remain saved in mnt/data directory in shared GPT, even though they don't appear in the list. If edited, they're still not in the list, but still stay in there. Definitely a bug.
* 2023-11-15 - setting to turn off using data to train model disappeared
* 2023-11-19 - code execution state doesn't seem to reset nearly so often, can switch out of and back to thread
* 2023-11-19 - has lately been willing to write really, really long messages with many python calls lately
* 2023-11-19 - text file output is truncated less often but still sometimes to 1000 characters and sometimes 500
* 2023-11-19 - GPT builder chat doesn't take up GPT-4 usage, will happily generate images over and over
* 2023-11-19 - option to turn off using data to train models has reappeared in config panel for some GPTs and not others
* 2023-11-20 - the configuration panel will accept .zip files, then code interpreter can unzip and read them. They will appear blank to the files browser however.
* 2024-01-14 - instructions for browser significantly changed from previous, could affect operation of GPTs which use browser
* 2024-01-15 - no setting apparently available for controlling use of data on newly created GPT, Additional Settings still exists on Better GPT Builder