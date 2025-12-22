# 'Heavenly Books' Book Fair Data Automation Programme

- This data automation programme allows the seller of Heavenly Books to store their stock data within a Google Sheet, link that data up with the python programme and make automatic adjustments to the stock numbers after each book fair.
- The programme is fully automated and the user will only need to enter certain commands to retrieve the information they are searching for. If the data they enter does not match the criteria, a message will appear guiding them on what the data should look like. New data will then be added into the linked Google Sheet.

## Features
### Existing Features 
- The programme is able to retrieve data from the Google Sheet.

- It allows users to enter new sales figures from a recent book fair.

- The programme can also calculate surplus stock from the Google Sheet. This is done by subtracting the book sales figures from the stock figures. Positive surplus represents books that were not bought, while negative surplus represents books that had to be ordered in for the customer because they had sold out.

- The next feature collects the sales figures from the last five data entries and presents the data as a list to the user.

- The final feature of this data automation programme calculates the stock average for each book and adds 10% to that figure.

## Future Features 
- A future ambition for this project would be to create this data automation on a much bigger scale, not just including the data from a book fair but also the book shop. The book fair data and the book shop data could then be linked and the data added after each book fair could be automatically added to the figures from the shop. Thus further altering the surplus numbers and stock average. A command could be run to tell the user how much stock they should take from the book shop to the fair each month. 

- Another interesting route would be to have the programme forecasting the sales necessary over the next month, or even year, to ensure a profit for a seller.

## Testing 
### Bugs encountered during the coding process

- When I added the command to produce an error message if the user did not enter the correct data, I found that the error message was not appearing in the vscode terminal. After altering the code a few times in an attempt to fix the bug, I realised that I had made the simple error of not saving my code in the python file, so the programme was running an old version that did not produce the error message.

- During the testing stage for the command that converted the strings into integers, a red error message was being thrown in the vscode terminal. All of my code was correct so I could not figure out what mistake I had made. I used ChatGPT to help me realise that I had not indented the code properly. I unfortunately made this mistake a couple of times during this project, but I have ensured that all of the code is now correctly indented.

- Another major bug that I encountered was that my Google Sheet was not being updated with the new figures. To help me with this issue, I looked back at the Love Sandwiches project with Code Institute and found that while I had created the command, I had not made a call to it later in the code. That was fixed by adding 'update_sales_worksheet(sales_data)'.

- I copied my code straight into the PEP8 Python Validator. At first I had quite a few error messages, however they were simple fixes. Mostly regarding whitespace or not enough blank lines between commands. Once I corrected those, there were no errors left in my code as you can see from the image below. 
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/ba86ff1f-8d3f-40db-ba20-747abf72d82a" />


## Deployment 
- I have had many issues when it comes to the deployment of my project. I followed all the steps provided by Code Institute to set up Heroku and upon trying to build my project from the main branch, an error message was thrown. I have attached an image of this error message below. I followed all of the steps provided in the terminal to move my .venv/ into my gitignore file, however, my saved changes are no longer committing to my github repository, I don't believe this is a mistake in the code, but because the changes are taking so long to save that vscode continues to load the commits without anything actually happening. I understand that deploying to Heroku was a main criteria for passing this project, but since I cannot achieve that right now I have decided to include the link to my github repository page, so there is proof of my project. Above you will also see that I have tested my code and it is all correct.
- Despite this obstacle, I will be contacting a tutor to try and fix whatever issue has arisen here because I am completely at a loss as to what to do. Here is the link for my github repository: https://github.com/LaurenForster25/book-fair.git

<img width="940" height="529" alt="image" src="https://github.com/user-attachments/assets/1c9c388c-d514-4b22-895e-12d9fc4e87eb" />

<img width="940" height="529" alt="image" src="https://github.com/user-attachments/assets/4b3e879f-4f86-409d-8f82-d7e087a87b0c" />

## Credits

- Code Institute for providing a data model that I could use to guide me through this project.
- The student care team for helping me with my deployment to Heroku.
- ChatGPT for providing answers to help me fix some minor bugs, where incorrect indentation was used and words were mispelt.
