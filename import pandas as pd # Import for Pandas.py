import pandas as pd # Import for Pandas
import numpy as np # Import for Numpy
import matplotlib # Import for Matplotlib
import matplotlib.pyplot as plt # Import for Matplotlib Pyplot
import seaborn as sns # Import for Seaborn

df1 = pd.read_json("/Users/gm/Desktop/Spotify/MyData 2/Streaming_History_Audio_2016-2018_0.json") # Load the JSON File into a dataframe
df2 = pd.read_json("/Users/gm/Desktop/Spotify/MyData 2/Streaming_History_Audio_2018-2019_1.json")
df3 = pd.read_json("/Users/gm/Desktop/Spotify/MyData 2/Streaming_History_Audio_2019-2021_2.json")
df4 = pd.read_json("/Users/gm/Desktop/Spotify/MyData 2/Streaming_History_Audio_2021-2022_3.json")
df5 = pd.read_json("/Users/gm/Desktop/Spotify/MyData 2/Streaming_History_Audio_2022-2023_4.json")
df6 = pd.read_json("/Users/gm/Desktop/Spotify/MyData 2/Streaming_History_Audio_2023_5.json")

spotify_stream_df = pd.concat([df1,df2,df3,df4,df5,df6], ignore_index=True) # To concatenate the two dataframes

unique_artists = spotify_stream_df["master_metadata_album_artist_name"].nunique() # Count number of unique artist in dataset
total_artists = spotify_stream_df["master_metadata_album_artist_name"].count() # Count total artist in dataset
unique_artist_percentage = unique_artists/total_artists*100 # Get the percentage of the unique
unique_artist_percentage

top_10_artist_df = spotify_stream_df.groupby(["master_metadata_album_artist_name"])[["ms_played"]].sum().sort_values(by="ms_played",ascending=False)
top_10_artist_df.head(30)

unique_artist_list = np.array([unique_artists, total_artists-unique_artists]) # Make an array out of the results
unique_artist_list_labels = [" Unique Artists", "Non Unique Artists"] # Make a lable for them

fig, ax = plt.subplots(figsize=(12,6))
ax.pie(unique_artist_list, labels= unique_artist_list_labels, autopct='%1.1f%%',explode=[0.05,0.05] ,startangle=180, shadow = True)
plt.title("Unique Artist Percentage")