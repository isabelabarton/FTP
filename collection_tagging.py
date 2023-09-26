import os
import openai

# Specify the folder path
folder_path = "FOLDER_PATH"
api_endpoint = "https://api.openai.com/v1/chat/completions"
api_key = "API_KEY"


# Function to generate OpenAI GPT response
def generate_response(gpt_prompt):
    openai.api_key = api_key
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=gpt_prompt,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.7,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )

    if 'choices' in response and len(response['choices']) > 0:
        return response['choices'][0]['text'].strip()

    return None


# Loop through each file in the folder
for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)
    if os.path.isfile(file_path):
        # Read the contents of the file
        with open(file_path, 'r') as file:
            contents = file.read()

        # Generate OpenAI GPT response
        taggingPrompt = "You are a historian who owns a website called FromThePage, a crowdsourcing platform for archives and " \
                 "libraries where volunteers transcribe, index, and describe historic documents. There are many different " \
                 "types of collections that users need to be able to easily access. Each collection needs 2-4 different tags " \
                 "to briefly describe its contents to users. You will be provided with a list called POSSIBLE_TAGS that " \
                 "contains all of the possible tags available to describe the collections with each individual tag separated " \
                 "by a comma. You will also be provided with context that hold a file/collection’s contents. Based on the " \
                 "contents, please accurately provide 2-4 of the following tags to describe the contents with each tag " \
                 "separated by a comma. If none work, please output ‘NOT ENOUGH INFORMATION’, otherwise, please " \
                "print only the tags that you've identified. Do not come up with " \
                " new tags if you cannot find any in the POSSIBLE_TAGS list that works'.For each new contents that you " \
                 "read, forget all information about all other files. \n" \
                        "POSSIBLE_TAGS: 'African-American History', " \
                  "'Agriculture and Farming', 'Arts', 'Australia', 'Book of Hours', 'Book History', 'Catholicism', " \
                  "'City Council', 'China', 'Civil Rights', 'Civil War and Reconstruction', 'Cookbooks', " \
                  "'Communism', 'Correspondence', 'Diaries', 'Disability and Illness', 'Education', 'England', " \
                 "'Family Papers', 'Federal Writers Project', 'Field notes', 'Financial', 'Gold Rush', 'Government Records', " \
                 "'Health and Medicine', 'Historic sites', 'Holocaust', 'Immigration and naturalization', 'Imprisonment', " \
                 "'Indigenous History', 'Judaica', 'Legal', 'LGBTQ', 'Linguistics and Anthropology', 'Literature', 'Logs', " \
                 "'Maritime', 'Mexican-American War', 'Military', 'Mormonism', 'Natural Disasters', 'Natural Sciences', " \
                 "'Newspapers', 'Oral History', 'Parks', 'Philosophy', 'Railroads', 'Religion', 'Science', 'Slavery', " \
                 "'Society', 'Sports', 'The Revolution and Early America', 'Technology', 'Travel', 'University', " \
                 "'US Presidents', 'Vital Records', 'Women's History', 'World War I', 'World War II', 'Zines', " \
                 "'Photographs and Images', 'Latin America History', 'Finding Aids and Catalogs', 'Labor'" \
                 "\n CONTENTS = " + contents

        datePrompt = "You are a historian who owns a website called FromThePage, a crowdsourcing platform for " \
                     "archives and libraries where volunteers transcribe, index, and describe historic documents. " \
                     "There are collections that originate from the 14th century all the way to the 21st century. " \
                     "You are an expert at identifying which century a collections comes from based on the contents" \
                     "of the files that you are provided. If there is not enough information in the contents of the " \
                     "file to identify which century the collection originates from, please output 'NOT ENOUGH" \
                     "INFORMATION', otherwise, please output only the century that you've identified." \
                     "CONTENTS = " + contents

        gptResponse1 = generate_response(taggingPrompt)
        gptResponse2 = generate_response(datePrompt)

        """
        print("File: " + filename + "\n")
        print("Contents: " + contents + "\n")
        print("ChatGPT Tags: " + gptResponse1 + "\n")
        print("ChatGPT Date: " + gptResponse2 + "\n")
        print()
        print("-------------------------------------")
        print()
        """

        output_file = open("outputs.txt", "a")
        # Print the filename, file contents, and generated GPT response
        output_file.write("" + "\n")
        output_file.write("File: " + filename + "\n")
        output_file.write("Contents: " + contents + "\n")
        output_file.write("ChatGPT Tags: " + gptResponse1 + "\n")
        output_file.write("ChatGPT Date: " + gptResponse2 + "\n")
        output_file.write("----------------------------" + "\n")

        output_file.close()

