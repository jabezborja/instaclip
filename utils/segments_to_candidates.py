import json

def segments_to_candidates(client, segments, reproduce=3):

    segment_candidates = []
    
    for _ in range(reproduce):
        response = client.chat.completions.create(
            model="gpt-3.5-turbo-0125",
            response_format={ "type": "json_object" },
            messages=[
                {
                    "role": "system",
                    "content": """
                        Identify the best possible good segments to put as a short-form content in the transcription provided by Whisper JSON segments. List down the top 5 best segments with their timestamps that you know there a good context for people watching the short-form content.
                        Find a great one segment among those five. On the best segment that you selected, list down all of the topics. Choose one best topic. Get that best topic and create a 30-second short-form content based on the transcription.

                        Please return a JSON object where 'discussion' are array of discussion in the best topic on a 30-second short-form content, inside the important array of discussion, there must be a JSON for every discussion, where in there 'text' is the keynote; where 'start' is the video timestamp start; where 'end' is the video timestamp end
                    """
                },
                {"role": "user", "content": segments}
            ]
        )

        segment_candidates.append(json.loads(response.choices[0].message.content))

    return segment_candidates