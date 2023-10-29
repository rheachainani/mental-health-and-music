import streamlit as st
import pandas as pd
import numpy as np

if 'anxiety_data' not in st.session_state:
    st.session_state.anxiety_data = None

if 'depression_data' not in st.session_state:
    st.session_state.depression_data = None

def main():
    
    action = st.sidebar.radio("Select a section :",('About our Project','Anxiety Symptoms Questionnaire (ASQ)','Beck Depression Inventory (BDI)','Results'))

    if (action == 'About our Project'):

        st.title("About our Project")

        st.subheader("Welcome to our project designed to promote mental well-being through the power of music and professional support. We understand that anxiety and depression can affect anyone, and that's why we offer a unique solution. By taking the ASQ and BDI tests, you'll receive personalized music recommendations to lift your spirits and alleviate mild symptoms. If your results indicate higher levels of anxiety or depression, we provide access to mental health professionals tailored to your preferences. Your mental health journey begins here, with music and support at the heart of it all.")

    if (action == 'Anxiety Symptoms Questionnaire (ASQ)'):
        st.title('Anxiety Symptoms Questionnaire (ASQ)')
        st.write('Please read each item and answer with the number in the scales below that best describes your experience regarding the Intensity and Frequency of these symptoms in the past week :')

        st.write(''' Use the scales below as reference
                 
        Intensity : 
            0 = None
            1-3 = Mild
            4-6 = Moderate
            7-9 = Severe
            10 = Extreme distress
        Frequency : 
            0 = Never
            1-3 = Occasionally
            4-6 = Often
            7-9 = Usually
            10 = All the time''')

        st.write('1. Anxiety')
        i1 = st.slider('Intensity of Anxiety',0,10)
        f1 = st.slider('Frequency of Anxiety',0,10)

        st.write('2. Nervousness')
        i2 = st.slider('Intensity of Nervousness',0,10)
        f2 = st.slider('Frequency of Nervousness',0,10)

        st.write('3. Worrying')
        i3 = st.slider('Intensity of Worrying',0,10)
        f3 = st.slider('Frequency of Worrying',0,10)

        st.write('4. Irritability')
        i4 = st.slider('Intensity of Irritability',0,10)
        f4 = st.slider('Frequency of Irritability',0,10)

        st.write('5. Muscle Tension or Tightness')
        i5 = st.slider('Intensity of Muscle Tension or Tightness',0,10)
        f5 = st.slider('Frequency of Muscle Tension or Tightness',0,10)

        st.write('6. Trouble Relaxing')
        i6 = st.slider('Intensity of Trouble Relaxing',0,10)
        f6 = st.slider('Frequency of Trouble Relaxing',0,10)
        
        st.write('7. Trouble Falling or Staying Asleep (Rate the most troublesome symptom)')
        i7 = st.slider('Intensity of Trouble Falling / Staying Asleep',0,10)
        f7 = st.slider('Frequency of Trouble Falling / Staying Asleep',0,10)

        st.write('8. Fatigue or Lack of Energy')
        i8 = st.slider('Intensity of Fatigue or Lack of Energy',0,10)
        f8 = st.slider('Frequency of Fatigue or Lack of Energy',0,10)

        st.write('9. Problems with Concentration or Attention')
        i9 = st.slider('Intensity of Problems with Concentration or Attention',0,10)
        f9 = st.slider('Frequency of Problems with Concentration or Attention',0,10)

        st.write('10. Trouble Remembering Things')
        i10 = st.slider('Intensity of Trouble Remembering Things',0,10)
        f10 = st.slider('Frequency of Trouble Remembering Things',0,10)

        st.write('11. Shortness of Breath, Chest Tightness or Pain, Pounding/Skipping/Racing Heartbeat (Rate the most troublesome symptom)')
        i11 = st.slider('Intensity of the most troublesome symptom',0,10)
        f11 = st.slider('Frequency of the most troublesome symptom',0,10)

        st.write('12. Stomach Upset, Nausea, Constipation, Diarrhea, or  Irritable Bowels (Rate the most troublesome symptom)')
        i12 = st.slider('Intensity of the most troublesome symptom ',0,10)
        f12 = st.slider('Frequency of the most troublesome symptom ',0,10)
        
        st.write('13. Dizziness, Lightheadedness, Headaches, Trembling or  Shakiness (Rate the most troublesome symptom)')
        i13 = st.slider('Intensity of the most troublesome symptom  ',0,10)
        f13 = st.slider('Frequency of the most troublesome symptom  ',0,10)

        st.write('14. Numbness, Tingling, Excessive Sweating, Flushing or Frequent Urination (Rate the most troublesome symptom)')
        i14 = st.slider('Intensity of the most troublesome symptom   ',0,10)
        f14 = st.slider('Frequency of the most troublesome symptom   ',0,10)

        st.write('15. Feeling Restless, Keyed Up, or On Edge')
        i15 = st.slider('Intensity of Restlessness',0,10)
        f15 = st.slider('Frequency of Restlessness',0,10)

        st.write('16. Anticipating or Fearing Something Bad Might Happen')
        i16 = st.slider('Intensity of Anticipating or Fearing Something Bad Might Happen',0,10)
        f16 = st.slider('Frequency of Anticipating or Fearing Something Bad Might Happen',0,10)

        st.write('17. Trouble Functioning at Home, Work, or Socially Due to Anxiety (Rate the most troublesome symptom)')
        i17 = st.slider('Intensity of the most troublesome symptom    ',0,10)
        f17 = st.slider('Frequency of the most troublesome symptom    ',0,10)

        if st.button('Get score'):

            anxiety_score = round(((i1+i2+i3+i4+i5+i6+i7+i8+i9+i10+i11+i12+i13+i14+i15+i16+i17+f1+f2+f3+f4+f5+f6+f7+f8+f9+f10+f11+f12+f13+f14+f15+f16+f17)/17),2)

            if anxiety_score == 0:
                anxiety_level = 'none'
            elif anxiety_score <= 3 and anxiety_score > 0:
                anxiety_level = 'mild'
            elif anxiety_score <= 6 and anxiety_score > 3:
                anxiety_level = 'moderate'
            elif anxiety_score <= 9 and anxiety_score > 6:
                anxiety_level = 'severe'
            else:
                anxiety_level = 'extreme'
                
            st.success(f'Your anxiety score is : {anxiety_score} - {anxiety_level}')

            st.session_state.anxiety_data = {'score': anxiety_score,'level': anxiety_level}

    if (action == 'Beck Depression Inventory (BDI)'):
        st.title('Beck Depression Inventory (BDI)')
        st.write('Please read each of the questions and select the most appropriate option')

        options1 = ["I do not feel sad","I feel sad","I am sad all the time and I can't snap out of it","I am so sad and unhappy that I can't stand it"]

        opt1 = st.selectbox('Question 1',options1)
        ans1 = options1.index(opt1)

        options2 = ["I am not particularly discouraged about the future","I feel discouraged about the future.","I feel I have nothing to look forward to","I feel the future is hopeless and that things cannot be done"]

        opt2 = st.selectbox('Question 2',options2)
        ans2 = options2.index(opt2)

        options3 = ["I do not feel like a failure","I feel I have failed more than the average person","As I look back on my life, all I can see is a lot of failures"," I feel I am a complete failure as a person"]

        opt3 = st.selectbox('Question 3',options3)
        ans3 = options3.index(opt3)

        options4 = ["I get as much satisfaction out of things as I used to","I don’t enjoy things the way I used to"," I don't get real satisfaction out of anything anymore","I am dissatisfied or bored with everything"]

        opt4 = st.selectbox('Question 4',options4)
        ans4 = options4.index(opt4)

        options5 = ["I don’t feel particularly guilty","I feel guilty a good part of the time","I feel quite guilty most of the time","I feel guilty all of the time"]

        opt5 = st.selectbox('Question 5',options5)
        ans5 = options5.index(opt5)

        options6 = ["I don’t feel I am being punished","I feel I may be punished","I expect to be punished","I feel I am being punished"]

        opt6 = st.selectbox('Question 6',options6)
        ans6 = options6.index(opt6)

        options7 = ["I don’t feel disappointed in myself","I am disappointed in myself","I am disgusted with myself","I hate myself"]

        opt7 = st.selectbox('Question 7',options7)
        ans7 = options7.index(opt7)

        options8 = ["I don’t feel I am any worse than anybody else","I am critical of myself for my weakness or mistakes","I blame myself all the time for my faults","I blame myself for everything bad that happens"]

        opt8 = st.selectbox('Question 8',options8)
        ans8 = options8.index(opt8)

        options9 = ["I don’t have any thoughts of killing myself"," I have thoughts of killing myself, but I would not carry them out","I would like to kill myself","I would kill myself if I had the chance"]

        opt9 = st.selectbox('Question 9',options9)
        ans9 = options9.index(opt9)

        options10 = ["I don’t cry any more than usual","I cry more now than I used to","I cry all the time now","I used to be able to cry , but now I can’t cry even though I want to"]

        opt10 = st.selectbox('Question 10',options10)
        ans10 = options10.index(opt10)

        options11 = ["I am no more irritated by things that I ever was","I am slightly more irritated now than usual","I am quite annoyed or irritated a good deal of the time"," I feel irritated all the time"]

        opt11 = st.selectbox('Question 11',options11)
        ans11 = options11.index(opt11)

        options12 = ["I have not lost interest in other people","I am less interested in other people than I used to be","I have lost most of my interest in other people","I have lost all of my interest in other people"]

        opt12 = st.selectbox('Question 12',options12)
        ans12 = options12.index(opt12)

        options13 = ["I make decisions about as well as I ever could","I put off making decisions more than I used to","I have greater difficulty in making decisions more than I used to","I can't make decisions at all anymore"]

        opt13 = st.selectbox('Question 13',options13)
        ans13 = options13.index(opt13)

        options14 = ["I don’t feel that I look any worse than I used to","I am worried that I am looking old or unattractive","I feel there are permanent changes in my appearance that make me look unattractive","I believe that I look ugly"]

        opt14 = st.selectbox('Question 14',options14)
        ans14 = options14.index(opt14)

        options15 = ["I can work about as well as before"," It takes an extra effort to get started at doing something","I have to push myself very hard to do anything","I can't do any work at all"]

        opt15 = st.selectbox('Question 15',options15)
        ans15 = options15.index(opt15)

        options16 = ["I can sleep as well as usual","I don’t sleep as well as I used to","I wake up 1-2 hours earlier than usual and find it hard to get back to sleep","I wake up several hours earlier than I used to and cannot get back to sleep"]

        opt16 = st.selectbox('Question 16',options16)
        ans16 = options16.index(opt16)

        options17 = ["I don't get more tired than usual","I get tired more easily than I used to","I get tired from doing almost anything","I am too tired to do anything"]

        opt17 = st.selectbox('Question 17',options17)
        ans17 = options17.index(opt17)

        options18 = ["My appetite is no worse than usual","My appetite is not as good as It used to be","My appetite is much worse now","I have no appetite at all anymore"]

        opt18 = st.selectbox('Question 18',options18)
        ans18 = options18.index(opt18)

        options19 = ["I haven't lost much weight, if any, lately"," I have lost more than five pounds","I have lost more than ten pounds","I have lost more than fifteen pounds"]

        opt19 = st.selectbox('Question 19',options19)
        ans19 = options19.index(opt19)

        options20 = ["I am no more worried about my health than usual","I am worried about physical problems like aches, pain, upset stomach or constipation","I am very worried about physical problems and it's hard to think of much else","I am so worried about my physical problems that I cannot think of anything else"]

        opt20 = st.selectbox('Question 20',options20)
        ans20 = options20.index(opt20)

        options21 = ["I have not noticed any recent changes in my interest in sex","I am less interested in sex than I used to be","I have almost no interest in sex","I have lost interest in sex completely"]

        opt21 = st.selectbox('Question 21',options21)
        ans21 = options21.index(opt21)

        if st.button('Get score'):

            depression_score = ans1+ans2+ans3+ans4+ans5+ans6+ans7+ans8+ans9+ans10+ans11+ans12+ans13+ans14+ans15+ans16+ans17+ans18+ans19+ans20+ans21

            if depression_score <= 10:
                depression_level = 'none'
                message = 'These ups and downs are considered normal'
            elif depression_score > 10 and depression_score <= 16:
                depression_level = 'mild'
                message = 'Mild mood disturbances'
            elif depression_score > 16 and depression_score <= 20:
                depression_level = 'moderate'
                message = 'Bordeline clinical depression'
            elif depression_score > 20 and depression_score <= 30:
                depression_level = 'moderate'
                message = 'Moderate depression'
            elif depression_score > 30 and depression_score <= 40:
                depression_level = 'severe'
                message = 'Severe depression'
            else:
                depression_level = 'extreme'
                message = 'Extreme depression'  

            st.success(f'Depression score (out of 63) : {depression_score} - {message}')

            st.session_state.depression_data = {'score': depression_score,'level': depression_level}

    if (action == 'Results'):

        st.title("Results")

        anxiety_level = st.session_state.anxiety_data['level'] if st.session_state.anxiety_data else None
        depression_level = st.session_state.depression_data['level'] if st.session_state.depression_data else None

        if anxiety_level is not None:
            st.write(f'Your anxiety level was : {anxiety_level}')

        if depression_level is not None:
            st.write(f'Your depression level was : {depression_level}')

        user_age = st.number_input("Please enter your age",10,100)

        high = ['severe','extreme']
        low = ['none','mild','moderate']

        st.subheader("Keeping in mind your results, you should...")

        if (anxiety_level in low and depression_level in low):
            df = pd.read_csv('preprocessed google form responses.csv')
            genres = df[(df['persistent_state_of_worry_panic_fear'].isin(low)) &
                            (df['persistent_sadness_tiredness_loss_of_interest'].isin(low)) &
                            (df['age'] >= user_age-10) &
                            (df['age'] <= user_age+10) &
                            (df['music_effects'] == 'Improves')]['favorite_genre'].value_counts()
            g1,g2 = genres.index[0],genres.index[1]

            st.subheader(f"Chill out & Listen to some {g1} & {g2} music!")

            st.write("Here are some top suggestions from our side!")

            image_size = 100

            genre_wise_top_songs = {
                    'Pop' : 'trending_pop.csv',
                    'Instrumental' : 'trending_instrumental.csv',
                    'Devotional' : 'trending_devotional.csv',
                    'Hip-Hop/Rap' : 'trending_hip-hop-rap.csv',
                    'Classical' : 'trending_classical.csv',
                    'Rock' : 'trending_rock.csv',
                    'Electronic/Dance' : 'trending_edm.csv',
                    'R&B (Rhythm and Blues)' : 'trending_r&b.csv',
                    'Bollywood': 'trending_bollywood.csv',
                    'Folk' : 'trending_folk.csv'
                }

            df_genre1 = pd.read_csv(genre_wise_top_songs[g1])
            df_genre2 = pd.read_csv(genre_wise_top_songs[g2])

            markdown_table = "| Cover Art | Song Title | Artist |\n| --- | --- | --- |\n"
            for index, row in df_genre1.iterrows():
                if index >= 4:
                    break
                markdown_table += f"<img src='{row['Cover Art URL']}' width='{image_size}' height='{image_size}'> | {row['Track Name']} | {row['Artist Name']} |\n"
            for index, row in df_genre2.iterrows():
                if index >= 4:
                    break
                markdown_table += f"<img src='{row['Cover Art URL']}' width='{image_size}' height='{image_size}'> | {row['Track Name']} | {row['Artist Name']} |\n"

            st.markdown(markdown_table, unsafe_allow_html=True)

        else:
            st.subheader("Consult a Mental Health Professional")
            st.write("Please fill in the following details to get started towards a better you :")

            df = pd.read_csv('preprocessed data of mental health practitioners.csv')

            location = st.selectbox('Location', ['Mumbai','Chhatisgarh','Delhi NCR','Goa','Chennai & T.N.','Kolkata & W.B.','Bangalore','Assam','Hyderabad','Kerala','Punjab','Madhya Pradesh','Maharashtra','Rajasthan','Gujarat','Uttarakhand','Andhra Pradesh','Jharkhand','Bihar'] )

            gender = st.selectbox("What gender identifying professional would you be most comfortable with?", ['male','female','other'])

            age = st.selectbox("What age range belonging professional would you be most comfortable with?", ['20-29', '30-39', '40-49', '50-59', '60-69'])

            if st.button('Get data'):
                
                data = df[(df.location == location) & (df.gender == gender) & (df.age == age)][['name','title','languages','qualifications','contact','address']]
                if data.empty:
                    st.write(f'Sorry we could not find a trusted mental health professional of age {age}, identifying as {gender} in {location}.')
                else:
                    st.subheader("Here's someone you can reach out for help: ")
                    st.table(data)

if __name__ == '__main__':
    main()
