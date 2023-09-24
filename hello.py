import streamlit as st
from PIL import Image
import pandas as pd
import numpy as np

# Set a title with a space theme
st.title('Beyond the Darkness Chatrooms')

image = Image.open('logo-hack.jpg')
col1, col2, col3, col4, col5, col6, col7, col8, col9, col10, col11, col12, col13, col14, col15 = st.columns([1,1,1,1,1,1,1,6,1,1,1,1,1,1,1])

with col1:
    st.write("")
with col2:
    st.write("")
with col3:
    st.write("")
with col4:
    st.write("")
with col5:
    st.write("")
with col6:
    st.write("")
with col7:
    st.write("")
with col8:
    st.image("logo-hack.jpg")
with col9:
    st.write("")
with col10:
    st.write("")
with col11:
    st.write("")
with col12:
    st.write("")
with col13:
    st.write("")
with col14:
    st.write("")
with col15:
    st.write("")

st.write('''Welcome to the Beyond the Darkness chatrooms, where you can free yourself from all worries and problems
with the help of others in your similar situation. Suicide should never be a consideration for any person, no matter the situation or scenario or recent concurring events.
The Beyond the Darkness chatrooms were created to give everyone the chance to express, explore, and enjoy with the company of others.
Remember to be respectful and considerate as others are going through a rough time and need compassion and sympathy.''')

st.button('Download App')

st.header("Our Mission/Story")
st.write("""On a scorching summer evening, the heart-wrenching news shattered my world - my dear friend, Alex, had taken their own life. The sheer shock and anguish that engulfed me were beyond words, a swirling maelstrom of emotions that threatened to drown me in despair. I grappled with an immense sense of loss and an overwhelming burden of guilt. The weight of the 'what ifs' and 'could have beens' pressed down on me relentlessly. What more could I have done to support Alex during their darkest moments?
Alex, a luminous soul, had the rare gift of lighting up any room with their infectious laughter and boundless kindness. Together, we embarked on countless adventures, weaving dreams that danced in the moonlight. It was utterly inconceivable that they were now absent from our lives, a void that seemed impossible to fill. Little did I know that behind their radiant smile hid a silent, relentless battle with mental health. They had concealed their turmoil from even their closest confidants, including myself.
As the waves of grief crashed over me, I felt an urgent need to transmute this anguish into a force for good. I couldn't bear the thought of anyone else suffering in the shadowy depths of solitude, feeling as utterly isolated as my beloved friend. It was in that dark hour that the seed of inspiration took root within me, birthing the concept of the Suicide Prevention Chatrooms app.
The app's mission was unequivocal - to serve as a lifeline, a sanctuary, for individuals in crisis. It aimed to bridge the chasm of despair by connecting those in need with empathetic volunteers and compassionate peers. Together, they would forge a haven where understanding flowed freely, and guidance was offered without judgment. It was my solemn vow to ensure that no one else would have to tread the desolate path that Alex had traversed.
Though I couldn't turn back the hands of time and bring my friend back, I was resolute in my determination to pay tribute to their memory by being a beacon of hope for others. The Suicide Prevention Chatrooms app stood as a testament to Alex's enduring legacy, a testament to their indomitable spirit.
Through the app, I sought to weave a tapestry of community, where individuals could openly share their pain, finding solace in knowing they were not alone. The overarching goal was to nurture resilience, to offer a lifeline that led away from the precipice of despair and toward the shores of renewal.
Every day, as I toiled tirelessly on the app's development, I felt Alex's presence beside me, a whispered voice in the wind guiding me toward a future bathed in compassion and understanding. In their memory, I was determined to make a difference, to extend a lifeline to those teetering on the brink of darkness.
In the heart of this endeavor, I found solace, a sliver of light amidst the shadows, a testament to the enduring power of human connection and the unwavering strength of the human spirit.""")

# Set a space-themed background image
image = Image.open('space.jpg')
st.image(image)

# Define some fake reviews and ratings
fake_reviews = [
    {"review": "This app is amazing! It really helped me during my tough times.", "rating": 5},
    {"review": "I found the chatrooms to be supportive and comforting.", "rating": 4},
    {"review": "Not bad, but could use some improvements in terms of user interface.", "rating": 3},
    {"review": "Great initiative, but sometimes the response time is slow.", "rating": 4},
    {"review": "The app crashes frequently. Needs more stability.", "rating": 2},
]

# Define fake replies
fake_replies = [
    "Thank you for your kind words! We're glad to hear that the app was helpful for you during tough times.",
    "We appreciate your positive feedback. Our aim is to provide a supportive and comforting environment for users.",
    "Thank you for your feedback. We are continually working on improving the user interface to make the app better for you.",
    "We understand your concern. We're actively addressing response time issues to provide faster support.",
    "We apologize for the stability issues you've experienced. Our development team is working hard to fix these problems.",
]

# Display existing fake reviews with custom styling and fake replies
st.header("User Reviews")
if not fake_reviews:
    st.write("No reviews yet. Be the first to write one!")
else:
    for i, (review_data, reply) in enumerate(zip(fake_reviews, fake_replies), 1):
        st.subheader(f"Review #{i}")
        st.write(f"Rating: {review_data['rating']}/5")
        st.write(f"Review: {review_data['review']}")
        st.write(f"Reply: {reply}")

# Contact information
st.header("Contact Us")
st.write("If you have any questions or concerns, please feel free to contact us at support@beyonddark.com")

# Footer
st.text("Copyright © 2023 Beyond the Darkness. All rights reserved.")
