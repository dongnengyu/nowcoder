# 这里我们使用 mysql-connector-python 驱动，可以使用 pip 进行安装
import mysql.connector

class Pipeline:
    def __init__(self):
        self.conn = mysql.connector.connect(user='root', password='123456',host='127.0.0.1', database='scrapy', )
        self.cursor = self.conn.cursor()


    def process_item(self, item, spider):

        title = item.get('title')
        answer = item.get('answer')

        test = title
        test1 = answer

        for letter in test:
            title =letter

        for letter in test1:
            answer=letter

        insert_sql = """
            insert into stack_questions(title,answer)
            VALUES (%s,%s);
        """

        self.cursor.execute(insert_sql, (title,answer))
        self.conn.commit()
        return item

    def close_spider(self, spider):
        self.cursor.close()
        self.conn.close()