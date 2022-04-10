import psycopg2



data1 = {'photo': '12345', 'location_name': 'Ufa', 'description': 'capital city of Rebuplic of Bashkortostan', 'tour_price': 10000}
data2 = ['1234', 'Ufa-1', 'Capital city', 10001]


def sql_start():
    global conn, cur
    conn = psycopg2.connect(dbname='testdb', user='postgres', password='A8nDIVDh23')
    cur = conn.cursor()
    if conn:
        print('connection is ok')
    cur.execute(
        "CREATE TABLE IF NOT EXISTS traveltours (tour_id SERIAL PRIMARY KEY ,photo text, location_name text, description text, tour_price int);")
    conn.commit()

async def sql_add_line(state):
    async with state.proxy() as data:
        cur.execute("insert into traveltours (photo, location_name, description, tour_price) values (%s, %s, %s, %s)", tuple(data.values()))
        conn.commit()

