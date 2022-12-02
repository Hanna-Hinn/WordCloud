
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS

file = open("words.txt", "r")
words = file.read()

word_cloud = WordCloud(
    width=1584,
    height=396,
    # random_state=1,
    # background_color="white",
    # colormap="Pastel1",
    # collocations=False,
    # stopwords=STOPWORDS,
).generate(words)

plt.imshow(word_cloud)
plt.axis("off")
plt.show()
