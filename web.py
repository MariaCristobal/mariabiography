import streamlit as st
import datetime 

st.set_page_config(page_title="Maria's Biography", page_icon="💗", layout="wide")

if 'toggle_state' not in st.session_state:
    st.session_state.toggle_state = False

# Define a function to toggle the state
def Drawing_button():
    st.session_state.toggle_state = not st.session_state.toggle_state
    
import streamlit as st



# Display the name dynamically
st.markdown(
    f"""
    <div style="text-align: center; font-size: 40px;">
        <strong>-Maria's Biography-</strong>  
    </div>
    """,
    unsafe_allow_html=True,
)
    
with st.container(): 
     st.write("---") 
     left_column, right_column = st.columns(2) 
     
     with left_column: #left column
        

        st.markdown("""
            <div style="text-align: center; font-size: 25px;">
               <strong>Get to know me</strong>
            </div>
        """, unsafe_allow_html=True)
        
        st.write("I hope this biography will help you know this person more")

        
        st.text_input("My Name", "Maria Kristina Cassandra G. Cristobal")
        
        st.write("---") 
        
        st.markdown("""
            <div style="text-align: center; font-size: 25px;">
               <strong>What I do</strong>
            </div>
        """, unsafe_allow_html=True)
         
        
        
        st.text_area("","""-Singing
-Playing piano, guitar and violin
-Studying
-Listening christian songs
-Reading Wattpad stories""", height=125 )
        st.write("---")
        
        st.markdown("""
            <div style="text-align: center; font-size: 25px;">
               <strong>My ahievements</strong>
                </di
            
        """, unsafe_allow_html=True)
        st.text_area("discription", """My parents molded me to what I am now. I've always wanted to know what I am passionate about and that comes singing and playing instruments. Singing and playing instruments has given me opportunities that I never knew that it could give me joy. It makes me feel relief and can understand the flow of music in my ears. Beside singing and playing instruments, I also compete in academic activities such as singing, research and other school competitions. I once stopped everything, being the competent woman. Cause everything has a season, and its purpose as well.
           """, height = 330)
        
            
            
            
        st.write("---")  
        st.markdown("""
            <div style="text-align: center; font-size: 25px;">
               <strong>Social Media Accounts</strong>
            </div>
        """, unsafe_allow_html=True)
        st.write("[Facebook](https://www.facebook.com/cassyy.cristobal)")
        st.write("[Instagram](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.instagram.com%2Fmariabellsss%3Figsh%3DdndmdWJkcWhzcXdm%26fbclid%3DIwZXh0bgNhZW0CMTAAAR3VnPbziVp0tcK3CKW2D1QDxQ43jtrKN5iK37nGM2pP7cMgz86AgvYsB4o_aem_uWzv8kseFVEUpsM8rPx2TA&h=AT1tqQNQm0WJMb4JwLEYHDonpCdkfBXeiKZxiciwbChvFqdM6uMbq5QxBjmDTGVGqZe5IMZDyQ8cjbja6N2LZcue_s3JEkqeSgUC8FR7jKV04otHN098l9RriecJuAzq8tKNc9JM4_b692LF61C8zw)")         
            
            
            
     with right_column: #right column
        st.markdown("""
            <div style="text-align: center; font-size: 25px;">
               <strong>ABOUT ME</strong>
            </div>
        """, unsafe_allow_html=True)
        
        st.text_area("", """Hi, I'm Maria Kristina Cassandra G. Cristobal. I am doin' good.  My social and intellectual lives are balanced. In order to be a more creative and effective student, I also make sure to have free time for reviews. I always believe that for with God nothing shall be impossible. Just trust Him and follow His will. Everything will follow such as blessings, any kinds of blessings. 


I am currently a dedicated student at Surigao Del Norte State University, motivated by an unrelenting will to make my dreams come true. I'm constantly looking for new approaches to achieve my goals and possibilities. My perseverance and hard effort are my main assets since they enable me to overcome obstacles and maintain focus on my long-term objectives. These attributes support my dedication to both academic and personal development, guaranteeing that I always aim for excellence in all that I do. I'm still driven to attain the success I've always dreamed of because I have a clear vision of the future.


In my vacant time, I enjoy reading wattpad story, watching movies, videos in Tiktok and vlogs in Fb and specially I enjoy singing and listening music. This can help me deal with stress and divert my attention from what I'm dealing with in real life.


All I can say is that I am truly blessed to what I am today. Blessed in the sense that through ups and downs I can face it with the help of God. Those feelings such as happiness, sadness, love, excitement, blessed, disappointments, angry and others helps me realize that I am a norma person that exist.""", height = 330)
        
      
        
        st.radio("Gender", ["Male", "Female"])
        st.subheader("Family Background")  
        mother = st.text_input("Mother's name", "Cleofe G. Cristobal")
        mbday = st.date_input("Mother's Birthday", datetime.date(1983, 11, 1))
        father = st.text_input("Father's Name", "Raymond F. Cristobal")
        mbday = st.date_input("Father's Birthday", datetime.date(1981, 9, 12)) 
        st.subheader("Educational Attainment")

        elem = st.text_input("Elementary", "Himama-ug Elementary School")
        shs = st.text_input("Senior High School", "Tagana-an National High School")
        college = st.text_input("College", "Surigao del Norte State University")
        st.write("---")