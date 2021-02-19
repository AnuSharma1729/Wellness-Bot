from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import random
gifs = [
    'https://media.discordapp.net/attachments/803257943645880323/805302433390788648/giphy_5.gif',
    'https://tenor.com/y6hl.gif', 'https://tenor.com/wWX9.gif',
    'https://tenor.com/J1JC.gif', 'https://tenor.com/Z5lt.gif'
]

stress_keywords = [
    'stress', 'anxiety', 'anxious', 'stressed', 'tired', 'scared', 'afraid',
    'fear', 'need help', 'need support', 'trauma'
]
depression_keywords = [
    'end my life', 'depression', 'anxiety', 'anxious', 'depressed',
    'I want to die', 'self harm', 'cut myself', "I don't want to live", 'sad',
    'mental health', 'suicide', 'kill myself', 'hopeless', 'failure', 'loser'
]
school_keywords = [
    'school', 'homework', 'test', 'quiz', 'paper', 'subject', 'asessment',
    'exams'
]


def get_depression_response():
    intro = "Hey! Are you okay? If you're going through something, you're not alone and help is available and . Here are some resources:"
    resource1 = "  -  National Suicide Prevention Lifeline: call 800-273-8255 or visit https://suicidepreventionlifeline.org/"
    resource2 = "  -  If you want to talk to people, check out this Discord: https://discord.gg/ZUJ3zJRR"
    resource3 = "  -  Remember someone out there definitely loves you 3000: "
    resource3 = resource3 + random.choice(gifs)
    return "{intro}\n\n{resource1}\n{resource2}\n{resource3}".format(
        intro=intro,
        resource1=resource1,
        resource2=resource2,
        resource3=resource3)


def contains_depression_traces(message_content):
    depression_keywords = [
        'hate myself', 'my life', 'end my life', 'depression', 'anxiety',
        'anxious', 'depressed', 'I want to die', 'self harm', 'cut myself',
        "I don't want to live", 'sad', 'mental health', 'suicide',
        'kill myself'
    ]
    sentiment_analyzer = SentimentIntensityAnalyzer()
    sentiment_dict = sentiment_analyzer.polarity_scores(message_content)
    negative_sentiment = sentiment_dict['neg']
    positive_sentiment = sentiment_dict['pos']
    if negative_sentiment > .93:
        return True
    message_is_depressing = negative_sentiment > .75 or (
        negative_sentiment > .5 and positive_sentiment < .5)
    for word in depression_keywords:
        if word in message_content:
            print(negative_sentiment)
            return message_is_depressing
    return False


def get_stress_response():
    intro = "Hey! Don't stress out. What's bothering you? School, work, relationships? "
    intro = intro + random.choice(gifs)
    return intro


def contains_stress_traces(message_content):
    sentiment_analyzer = SentimentIntensityAnalyzer()
    sentiment_dict = sentiment_analyzer.polarity_scores(message_content)
    negative_sentiment = sentiment_dict['neg']
    positive_sentiment = sentiment_dict['pos']
    print(negative_sentiment)
    print(positive_sentiment)
    message_is_stressed = negative_sentiment > .75 or (
        negative_sentiment > .5 and positive_sentiment < .5)
    for word in stress_keywords:
        if word in message_content:
            return message_is_stressed
    return False


def contains_school_traces(message_content):
    schoolFound = False
    stressFound = False
    for word in school_keywords:
        if word in message_content:
            schoolFound = True
    for word in stress_keywords:
        if word in message_content:
            stressFound = True
    return schoolFound and stressFound


def contains_jobfinding_traces(message_content):
    jobfind_keywords = [
        'looking for a job', 'searching for a job', 'need a job',
        'dont have a job', 'out of work'
    ]
    for word in jobfind_keywords:
        if word in message_content:
            return True
    return False


def contains_jobarea_traces(message_content):
    jobfind_keywords = [
        'estee lauder', 'google cloud', 'webdeveloper', 'programmer', 'google',
        'engineer', 'microsoft'
    ]
    # salary_keywords = ['10k','20k','30k','40k','50k','60k']
    # distance_keywords = ['5 mi','10 mi', '20 mi', 'anywhere']
    for word in jobfind_keywords:
        if word in message_content:
            return True
    return False


def contains_schooltopic_traces(message_content):
    topic_keywords = [
        'geometry', 'triangles', 'biology', 'trigonometry', 'math'
    ]
    for word in topic_keywords:
        if word in message_content:
            return True
    return False


def contains_jobmanage_traces(message_content):
    manage_keywords = ['miscommunication', 'disorganized', 'overworked']
    for word in manage_keywords:
        if word in message_content:
            return True
    return False


def contains_relationship_traces(message_content):
    relationship_keywords = [
        'romantic', 'partner', 'special someone', 'friend', 'boyfriend',
        'girlfriend', 'relationship', 'bae', 'boo'
    ]
    sentiment_analyzer = SentimentIntensityAnalyzer()
    sentiment_dict = sentiment_analyzer.polarity_scores(message_content)
    negative_sentiment = sentiment_dict['neg']
    positive_sentiment = sentiment_dict['pos']
    message_has_stress = negative_sentiment > .25 and positive_sentiment < .25
    for word in relationship_keywords:
        if word in message_content and message_has_stress:
            return True
    return False