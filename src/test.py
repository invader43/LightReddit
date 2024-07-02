# for testing db for now
# from LightReddit import db
# from LightReddit.models import Comment , Post

# db.drop_all()
# db.create_all()


from faker import Faker
Faker.seed(0)
fake = Faker()

for _ in range(5):
    print(fake.address())

# newpost = Post(content="hey this a post")
