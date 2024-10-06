<h1> unreliable-news-detection </h1>
Using huggingface transformer embeddings and ml based classification to classify news as reliable or unreliable.

<h2>Dataset</h2>
Dataset is obtained from multiple sources on kaggle<br>
.https://www.kaggle.com/c/fake-news/data <br>
.https://www.kaggle.com/datasets/emineyetm/fake-news-detection-datasets/data<br>

<h2>requirements</h2>
For running the code outside of colab , few dependencies are needed to be present in your environment<br>
they are listed in requirements.tct file included in this repository<br>

<h2>Test.py</h2>
Following texts were used in Test.py<br>

<table>
  <th>test case</th>
  <th>prediction</th>  

  <tr>
    <td>
      <a href="https://www.businesstoday.in/india/story/congress-is-like-chinese-stock-market-shankar-sharma-after-exit-polls-predict-setback-for-bjp-in-haryana- 448911-2024-10-06">Test case 1</a>
    </td>
    <td>
      98.72
    </td>
  </tr>
  <tr>
    <td>
      <a href="https://www.hindustantimes.com/world-news/france-criticizes-israels-attacks-on-lebanon-netanyahu-gives-shame-reply-101728188698079.html">
Test case 2</a>
    </td>
    <td>
      99.66
    </td>
  </tr>
  
  
  
  
  
  
  <li><a href="https://www.businesstoday.in/india/story/congress-is-like-chinese-stock-market-shankar-sharma-after-exit-polls-predict-setback-for-bjp-in-haryana-448911-2024-10-06">Test case 1</a>                        98.72
</li><li><a href="https://www.hindustantimes.com/world-news/france-criticizes-israels-attacks-on-lebanon-netanyahu-gives-shame-reply-101728188698079.html">
Test case 2</a>                                    99.66
</li>
</pre>
</ul>
