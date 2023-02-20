from sqlalchemy import create_engine, text
import os

db_connection = os.environ['DB_CONNECTION']

engine = create_engine(
  db_connection,
  connect_args={
    "ssl": {
      "ssl_ca": "/etc/ssl/cert.pem"
      }
  })

# with engine.connect() as conn:
#   result = conn.execute(text("select * from jobs"))

#   result_dicts = []
#   for row in result.all():
#     result_dicts.append(dict(row._mapping))

#   print(result_dicts)

def jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    jobs = []
    for row in result.all():
      jobs.append(dict(row._mapping))
    return jobs