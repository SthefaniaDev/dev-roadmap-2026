import Fastify from 'fastify'
import { randomUUID } from 'node:crypto'

type Contact = {
  id: string
  name: string
  phone: string
}

const contacts: Contact[] = []

const app = Fastify({
  logger: true
})

app.get('/contacts', (request, reply) => {
  return reply.serialize(contacts)
})

app.post('/contacts', (request, reply) => {
  const { name, phone } = request.body as { name: string; phone: string }

  const contact: Contact = {
    id: randomUUID(),
    name,
    phone
  }

  contacts.push(contact)

  return reply.serialize(contact)
})

app.listen({ port: 3000 })


//CRUD