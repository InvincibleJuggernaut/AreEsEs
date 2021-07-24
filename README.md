# AreEsEs

<h2>Introduction</h2>

<p> AreEsEs is a utility tool made using Python for reading Reddit RSS feeds. It is different from the well-known RSS readers because of the fact that it loads the comments along with the post contents instead of having to browse through comments in an external browser. That said, it is quite bland and primitive. It is not capable of loading images and just displays the contents in plaintext without any formatting.
  </p>

<h2>Usage</h2>

<ul>
  <li>Clone this repository using:</li>
   
  ```
  git clone https://github.com/InvincibleJuggernaut/AreEsEs.git
  ```
  <li>Enter the downloaded folder using:</li>
  
  ```
  cd AreEsEs
  ```
  <li>Install the required dependencies using:</li>
  
  ```
  pip3 install -r requirements.txt
  ```
  <li> Edit the file <i>parse.py</i> with your preferred subreddits in <a href="https://github.com/InvincibleJuggernaut/AreEsEs/blob/b7d362247bf006365a7de4ae814063036d09aeb8/parse.py#L8">this</a> line. For example, if you want to read RSS feeds from the subreddits <i>github</i>, <i>popular</i> and <i>earth</i>, the line would look something like this:</li>
  
    subreddits = ['github', 'popular', 'earth']

  <li> Run the program using:</li>
  
  ```
  python3 parse.py
  ```
  
  </ul>
