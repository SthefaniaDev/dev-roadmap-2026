import {createPostValidator} from '#validators/post'
import type (HttpContext) from '@adonisjs/core/http'

export default class PostController{
  async index({auth}:HttpContext){
    const posts = await.user?.related('posts').query()
    return posts
  }

  async store({request}:HttContext) {
    const {name} = await request.validateUsing(createPostValidator)
  }

aync show({params}: HttpContext)
  const 
}


return posts
}

async store({ request, auth }: HttpContext) {
  const { title, body } = await request.validateUsing(createPostValidator)
  const post = await auth.user?.related('posts').create({ title, body })
  return post
}

async show({ params, response }: HttpContext) {
  try {
    const post = await Post.findByOrFail('id', params.id)
    return post
  } catch {
    return response.json({ error: 'post not found' })
  }
}

async update({ params, request }: HttpContext) {}

async destroy({ params }: HttpContext) {}