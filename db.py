import pymysql

def get_conn():
    return pymysql.connect(
        host='localhost', user='root', password='7751408ccb', database='taobao_fashion', charset='utf8mb4'
    )

def insert_item(item):
    conn = get_conn()
    try:
        with conn.cursor() as cursor:
            sql = '''
                INSERT INTO taobao_fashion (name, price, brand, sales, shop, url)
                VALUES (%s, %s, %s, %s, %s, %s)
            '''
            price = item.get('price', '')
            # 处理空字符串
            price = float(price) if price not in ('', None) else None
            print(f"插入的数据: {item}")
            cursor.execute(sql, (
                item.get('name', ''),
                price,
                item.get('brand', ''),
                item.get('sales', ''),
                item.get('shop', ''),
                item.get('url', '')
            ))
        conn.commit()
    except Exception as e:
        print(f'插入数据库出错: {e}, 插入的数据: {item}')
    finally:
        conn.close()