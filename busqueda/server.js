const express = require('express');
const bodyParser = require('body-parser');
const mongoose = require('mongoose');

const app = express();
const port = 3000;

// Configuración de Mongoose
mongoose.connect('mongodb://localhost:27017/search-microservice', { useNewUrlParser: true, useUnifiedTopology: true });

// Definición del esquema y modelo de Post
const postSchema = new mongoose.Schema({
  title: String,
  content: String
});

// Crear índice de texto en los campos title y content
postSchema.index({ title: 'text', content: 'text' });

const Post = mongoose.model('Post', postSchema);

app.use(bodyParser.json());

// Endpoint para agregar posts
app.post('/posts', async (req, res) => {
  const { title, content } = req.body;

  try {
    const post = new Post({ title, content });
    await post.save();
    res.status(201).json({ id: post._id });
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

// Endpoint para buscar posts
app.get('/search', async (req, res) => {
  const { q } = req.query;

  try {
    const posts = await Post.find(
      { $text: { $search: q } },
      { score: { $meta: 'textScore' } }
    ).sort({ score: { $meta: 'textScore' } });

    res.json(posts);
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

app.listen(port, () => {
  console.log(`Microservicio de búsqueda escuchando en http://localhost:${port}`);
});
