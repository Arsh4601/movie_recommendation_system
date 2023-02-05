import streamlit as st
import pickle
import pandas as pd
import requests

st.set_page_config(page_title="Movie Recommendation")
st.title("Movie Recommender System")

movies=pd.read_csv("final_df.csv")

movie_list=movies["title"].values

similar=pickle.load(open("similar.pkl","rb"))

def fetch_poster(movie_id):

    response=requests.get("https://api.themoviedb.org/3/movie/{}?api_key=7b22b5192264fad7ba6cb3e18adfa88e&language=en-US".format(movie_id))

    data=response.json()

    return "https://image.tmdb.org/t/p/original"+data["poster_path"]

def recommend(movie):
    
    for i in movies["title"]:
        
        if i.lower().find(movie.lower())!=-1:
            
            nmovie=i        
            break

    movie_index=movies[movies["title"]==nmovie].index[0]
    distance=similar[movie_index]
    movie_recommend=sorted(list(enumerate(distance)),reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies=[]
    recommended_movies_poster=[]
    
    for i in movie_recommend:

              
        recommended_movies.append(movies.iloc[i[0]].title)        
        recommended_movies_poster.append(fetch_poster(movies.iloc[i[0]].movie_id))
    
    return recommended_movies,recommended_movies_poster

movie_select = st.selectbox("Select your movie ",movie_list)

if(st.button("Recommend")):

    st.write("Movie Selected is: ",movie_select)
    names,posters=recommend(movie_select)

    
    col1, col2, col3,col4,col5 = st.columns(5,gap="medium")

    with col1:        
        
        st.write(names[0])
        st.image(posters[0])
        
        

    
    with col2:        
        
        st.write(names[1])        
        st.image(posters[1])
        
        
    
    with col3:
        
        st.write(names[2])       
        st.image(posters[2])
       
       

    with col4:
        
        st.write(names[3])        
        st.image(posters[3])
        
       
    
    with col5:
        
        st.write(names[4])        
        st.image(posters[4])
        
       

    

        



