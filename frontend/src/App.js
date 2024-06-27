import React, { useEffect, useState } from 'react';
import axios from 'axios';

function App() {
  const [articles, setArticles] = useState([]);

  useEffect(() => {
    // Fetch data from Django backend API
    axios.get('http://localhost:8000/api/articles/')
      .then(response => setArticles(response.data))
      .catch(error => console.error('Error fetching data:', error));
  }, []);

  return (
    <div>
      <h1>News Articles</h1>
      {articles.map(article => (
        <div key={article.id}>
          <h2>{article.title}</h2>
          <p>{article.content}</p>
          <p>{article.summary}</p>
          <p><strong>Published At:</strong> {new Date(article.published_at).toLocaleString()}</p>
          <button>Take the Quiz</button>
        </div>
      ))}
    </div>
  );
}

export default App;