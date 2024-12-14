import matplotlib.pyplot as plt
from wordcloud import WordCloud

text = "I love python coding python because python is easy and interesting, the study any python learn and simple"

wordcloud = WordCloud(width=800, height=400).generate(text)

plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.title("Word Tree Visualization")
plt.show()
