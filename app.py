''' Initialize a web app to explain the game '''


import streamlit as st

st.title("The Pretzel Game")

st.header("Demonstration")

st.header("Rules")

st.markdown("<p style='text-align: justify;'>Players take turns performing moves that simplify a randomly generated pretzel link. The game ends when the given link is made into the unlink, of which some examples are shown below. The player that makes the last move wins. You will be the player that moves first, and a computer of your choosing (one that plays randomly or one that plays better) will be the player that moves second.</p>", unsafe_allow_html=True)

st.subheader("Skein Relations")

st.markdown("<p style='text-align: justify;'>The simplifying moves that players perform are called simplifying skein relations: transformations to tiny regions of a pretzel link that leave the rest of the link unchanged. Intuitively, this means that crossings are undone in a systematic way via the deletion of the link at a crossing followed by a rejoining of strands. This process is illustrated below along with the different types of crossings that result.</p>", unsafe_allow_html=True)

st.subheader("Inputting Moves")

st.markdown("<p style='text-align: justify;'>You will be required to input moves at the start of every turn. To make a move, you'd need to specify two non-negative integers: index and operation. The index, read from left to right and started at 0, is the tangle that needs to be modified. The operation is 0 if the applied simplification removes the tangle and 1 if the applied simplification reduces the number of crossings on the tangle by 1.</p>", unsafe_allow_html=True)

st.header("Play")

st.markdown("<p style='text-align: justify;'>The link to play the game in the command-line can be found below. An expository paper on knot theory is also included below, which explains the ideas behind pretzel links and the game in greater depth.</p>", unsafe_allow_html=True)

st.download_button("Paper", "paper.pdf")

