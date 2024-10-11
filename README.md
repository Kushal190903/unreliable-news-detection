<h1> Unreliable news detection <a href="https://unreliable-news-detection-tgbckzek6wuysrturqjaw7.streamlit.app/">(app)</a> </h1>
Using huggingface transformer embeddings and ml based classification to classify news as reliable or unreliable.

<h2>Dataset</h2>
Dataset is obtained from multiple sources on kaggle<br>
<ul>
  <li>https://www.kaggle.com/c/fake-news/data</li>
  <li>https://www.kaggle.com/datasets/emineyetm/fake-news-detection-datasets/data<</li>
</ul>

<h2>requirements</h2>
For running the code outside of colab , few dependencies are needed to be present in your environment<br>
They are listed in requirements.txt file included in this repository<br>
Install them using <pre>pip install -r requirements.txt </pre> in your virtual environment

<h2>Test.ipynb</h2>
Following texts were used in Test.py<br>

<table>
  <th>test case</th>
  <th>prediction</th> 
  <th>confidence score(for being reliable)</th>

  <tr>
    <td>
      <a href="https://www.businesstoday.in/india/story/congress-is-like-chinese-stock-market-shankar-sharma-after-exit-polls-predict-setback-for-bjp-in-haryana- 448911-2024-10-06">Test case 1</a>
    </td>
    <td>
      Reliable
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
      Reliable
    </td>
    <td>
      99.66
    </td>
  </tr>
  <tr>
    <td>
      <a href="https://sports.ndtv.com/football/real-madrid-beat-villarreal-but-dani-carvajal-suffers-knee-injury-6726606">Test case 3</a>
    </td>
    <td>
      Reliable
    </td>
    <td>
      99.81
    </td>
    
  </tr>
  <tr>
    <td>
      <a href="https://www.moneycontrol.com/entertainment/bigg-boss-18-heres-a-list-of-confirmed-contestants-for-this-years-time-ka-taandav-article-12836104.html">
        Test case 4</a>
    </td>
    <td>
      Unreliable
    </td>
    <td>
      24.04
    </td>
  </tr>
  <tr>
    <td>
      <a href="https://www.space.com/spacex-falcon-heavy-europa-clipper-launch-webcast">Test case 4</a>
    </td>
    <td>
      Reliable
    </td>
    <td>
      98.72
    </td>
  </tr>
  <tr>
    <td>
      <a href="https://www.hindustantimes.com/opinion/the-government-will-not-recognise-marital-rape-as-a-crime-101728143351843.html">Test case 5</a>
    </td>
    <td>
      Reliable
    </td>
    <td>
      53.19
    </td>
  </tr>
  <tr>
    <td>
      <a href="https://www.hindustantimes.com/opinion/delhiberlin-partnership-has-kept-pace-with-india-s-rise-101727881406288.html">Test case 6</a>
    </td>
    <td>
      Unreliable
    </td>
    <td>
      1.01
    </td>
  
  
  
</table>
  
  
  
  
