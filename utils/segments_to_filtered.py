import json

def segments_to_filtered(client, segments):
    
    response = client.chat.completions.create(
        model="gpt-3.5-turbo-0125",
        response_format={ "type": "json_object" },
        messages=[
            {"role": "system", "content": "Identify the best possible good segments to put as a short-form content in the transcription provided by Whisper JSON segments. List down the top 5 best segments with their timestamps that you know there a good context for people watching the short-form content."},
            {"role": "system", "content": "Now, find a great one segment among those five"},
            {"role": "system", "content": "On the best segment that you selected, list down all of the topics"},
            {"role": "system", "content": "Now, choose one best topic"},
            {"role": "system", "content": "Now, get that best topic and create a 30-second short-form content based on the transcription."},
            {"role": "system", "content": "Please return a JSON object where 'discussion' are array of discussion in the best topic on a 30-second short-form content, inside the important array of discussion, there must be a JSON for every discussion, where in there 'text' is the keynote; where 'start' is the video timestamp start; where 'end' is the video timestamp end"},
            {"role": "user", "content": segments}
        ]
    )

    data = json.loads(response.choices[0].message.content)

    return data