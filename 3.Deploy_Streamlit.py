import streamlit as st
import pandas as pd

#streamline run file_name in cmd.
st.title('title-> hello world')
st.header('header-> hello world')
st.subheader('sub-header-> hello world')
st.text('text-> hello world')
#markdown
st.subheader('Markdown')
st.markdown('# hey')
st.markdown('## hey')
st.markdown('### hey')
st.markdown('#### hey')
#success,info,warning,error
st.success('success!')
st.info('information!')
st.warning('warning!')
st.error('error!')
#exception
st.subheader('Exception')
st.exception(ZeroDivisionError('Division not possible with zero!'))
#help -> provides documentation
st.subheader('Help')
st.help(ZeroDivisionError)
#arithemetic operation
st.subheader('Arithemetic Operation')
st.write(5*6)
#code command
st.subheader('Code')
st.code('x=10\n'
        'for in range(x):\n'
        '\tprint(i)')
#checkbox
st.subheader('Checkbox')
st.checkbox('Male')
if st.checkbox('Female'):
    st.write('your female')
#radio -> enable to select one
st.subheader('Radio')
st.radio('select:',('male','female','other'))
#selectbox
st.subheader('Select Box:')
sel_box = st.selectbox('Data Science:',['DA','DL','ML','NLP','DV','CV','IP','WS'])
st.write('you have selected:',sel_box)
#multi-select box-> allows selection of multiple items
st.subheader('Select Multiple Boxes:')
msel_box = st.multiselect('Data Science:',['DA','DL','ML','NLP','DV','CV','IP','WS'])
st.write('you have selected:',len(msel_box),'courses')
#button
st.subheader('Button')
st.button('Click me!')
#slider
st.subheader('Slider')
vol = st.slider('Select req vol:',1,100,step=1)
st.write('vol is:',vol)
#taking input from user
st.subheader('Taking input:')
name = st.text_input('Name:') #name
if (name):
    st.write('Hey,',name)
st.text_input('Password:',type='password') #password
st.subheader('Text Area')
about = st.text_area('Write about yourself.') #text area
st.write(about)
st.subheader('Number Input')
st.number_input('age:',18,100) #number
st.subheader('Date Input')
st.date_input('Date:') #date
st.subheader('Time Input')
st.time_input('Time:') #time

#uploading and loading csv files
st.subheader('Uploading CSV file')
df = st.file_uploader('upload the csv file:',type=['csv','xlsx']) #uploading
st.subheader('Loading CSV file')
df = pd.read_csv('ChicagoCensusData1.csv')#loading
if df is not None:
   st.table(df.head())

#dealing with images
st.subheader('Dealing with Images')
img = st.file_uploader('upload image',type=['png','jpeg'])
if img is not None:
    st.image(img)

#dealing with videos
st.subheader('Dealing with Videos')
vid = st.file_uploader('upload image',type=['mkv','mp4'])
if vid is not None:
    st.video(vid,start_time=0)

#dealing with audio
st.subheader('Dealing with Audio')
aud = st.file_uploader('upload audio',type=['mp3','wav'])
if aud is not None:
    st.audio(aud.read())




