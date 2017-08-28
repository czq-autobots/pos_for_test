#coding=utf-8

import psycopg2,sys
reload(sys)
sys.setdefaultencoding('utf-8')

class DeleteMb():
    def deletemb(self):
        # 数据库连接参数

        conn = psycopg2.connect(database="trade", user="crm", password="crm", host="192.168.34.11", port="5432")
        cur = conn.cursor()
        cur.execute("delete from trade.card where membership_id in (select id from trade.membership where brand_id = 180274321 and mobile ='18365652222');")
        cur.execute("delete from trade.coupon where membership_id in (select id from trade.membership where brand_id = 180274321 and mobile ='18365652222');")
        cur.execute("delete from trade.membership where id in (select id from trade.membership where brand_id = 180274321 and mobile ='18365652222');")
        #cur.execute("delete from trade.weixin_scope where brand_id = 180000247 and weixin_id ='oyiiqvwDofE4zEp_2iSbxvq5ZK0k';")

        #conn1=psycopg2.connect(database="weixin", user="weixin", password="weixin", host="192.168.34.12", port="5432")

        #cur1 = conn1.cursor()

        #cur1.execute("delete from weixin.membership where brand_id = 180000247 and weixin_id ='oyiiqvwDofE4zEp_2iSbxvq5ZK0k';")


        #conn1.commit()

        #cur1.close()

        #conn1.close()

        conn.commit()  #oyiiqvwDofE4zEp_2iSbxvq5ZK0k

        cur.close()
        conn.close()

    def init_card(self):
        conn = psycopg2.connect(database="trade", user="crm", password="crm", host="192.168.34.11", port="5432")
        cur = conn.cursor()
        cur.execute("INSERT INTO trade.card_batch VALUES ('666666666', '2017-08-25', '0', '0', '120457', '180274321', '3', '2017-08-25 15:15:27', '1', '1');")
        cur.execute("INSERT INTO trade.card_record VALUES ('666666666', '6201200561666938', '32336201200561666938=000001000031009950 ', 'f', '666666666');")
        conn.commit()
        cur.close()
        conn.close()

    def del_card(self):
        conn = psycopg2.connect(database="trade", user="crm", password="crm", host="192.168.34.11", port="5432")
        cur = conn.cursor()
        cur.execute("delete from trade.card_batch where batch_id='666666666';")
        cur.execute("delete from trade.card_record where id='666666666';	")
        conn.commit()
        cur.close()
        conn.close()


if __name__=='__main__':
    mb=DeleteMb()
    mb.deletemb()
