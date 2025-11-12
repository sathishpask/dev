# Note: Requires 'wordcloud' library (pip install wordcloud)

import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud 

# Create a simple example dataset (replace this with your actual dataset)
data = {'sender': ['sender1', 'sender2', 'sender1', 'sender3'],
        'content': ['Hello,howareyou?', 'Meetingtomorrow?', 'Importantupdate', 'Check this out!']}
email_data = pd.DataFrame(data)

# Display the dataset
print("Email Dataset:")
print(email_data)

# Check for missing values
print("\nMissing Values:")
print(email_data.isnull().sum())

# Visualize the distribution of email lengths
email_data['email_length'] = email_data['content'].apply(len)
plt.figure(figsize=(10, 6))
plt.hist(email_data['email_length'], bins=30, edgecolor='black')
plt.title('Distribution of Email Lengths')
plt.xlabel('Email Length')
plt.ylabel('Frequency')
plt.show()

# Visualize the count of emails per sender
plt.figure(figsize=(8, 5))
email_data['sender'].value_counts().plot(kind='bar', color='skyblue')
plt.title('Count of Emails per Sender')
plt.xlabel('Sender')
plt.ylabel('Count')
plt.show()

# Visualize the most common words in emails
all_emails = ' '.join(email_data['content']) 
wordcloud = WordCloud(width=800, height=400,
                      background_color='white').generate(all_emails)
plt.figure(figsize=(10, 6))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title('Word Cloud of Email Content')
plt.show()
