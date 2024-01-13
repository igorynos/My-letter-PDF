import pymysql
from data import config


class Database:
    def __init__(self, path_to_db=(config.IP, config.PGUSER, config.PGPASSWORD, config.DATABASE, config.PORT)):
        self.path_to_db = path_to_db

    @property
    def connection(self):
        return pymysql.connect(host=self.path_to_db[0],
                               user=self.path_to_db[1],
                               password=self.path_to_db[2],
                               database=self.path_to_db[3],
                               port=self.path_to_db[4])

    def execute(self, sql: str, parameters: tuple = None, fetchone=False, fetchall=False, commit=False):

        if not parameters:
            parameters = tuple()

        connection = self.connection
        cursor = connection.cursor()
        cursor.execute(sql, parameters)

        data = None

        if commit:
            connection.commit()

        if fetchone:
            data = cursor.fetchone()

        if fetchall:
            data = cursor.fetchall()

        connection.close()

        return data

######## USER ############
    def create_table_users(self):
        sql = "CREATE TABLE `users` (\
                `id` int(11) NOT NULL PRIMARY KEY,\
                `name` text DEFAULT NULL,\
                `adress` text DEFAULT NULL,\
                `phone` text DEFAULT NULL,\
                `email` text DEFAULT NULL,\
                `inn` text DEFAULT NULL,\
                `pasport` text DEFAULT NULL,\
                `born` text DEFAULT NULL,\
                `comment` text DEFAULT NULL\
            )"
        self.execute(sql, commit=True)

    def add_user(self, id: int,
                 name: str,
                 adress='',
                 phone='',
                 email='',
                 inn='',
                 pasport='',
                 born='',
                 comment=''):
        sql = "INSERT IGNORE INTO users VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);"
        parameters = (id, name, adress, phone,
                      email, inn, pasport, born, comment)
        self.execute(sql, parameters=parameters, commit=True)

    def update_user(self, id, dict_oper):
        for data in dict_oper.items():
            if data[1] == "Пропустить":
                data = list(data)
                data[1] = ''
            try:
                sql = f"UPDATE users SET {data[0]}=%s WHERE id=%s;"
                self.execute(sql, parameters=(data[1], id), commit=True)
            except:
                pass

######## CONT USER ###########

    def create_table_cont_users(self):
        sql = "CREATE TABLE `cont_users` (\
                `cont_id` int(11) DEFAULT NULL,\
                `cont_user` int(11) DEFAULT NULL,\
                `cont_org` text DEFAULT NULL,\
                `cont_ogrn` text DEFAULT NULL,\
                `cont_adress` text DEFAULT NULL,\
                `cont_phone` text DEFAULT NULL,\
                `cont_email` text DEFAULT NULL,\
                `cont_inn` text DEFAULT NULL,\
                `cont_comment` text DEFAULT NULL,\
                `cont_fio` text DEFAULT NULL,\
                `cont_headstatus` text DEFAULT NULL,\
                `cont_fiocont` text DEFAULT NULL,\
                `cont_link` text DEFAULT NULL,\
                KEY `cont_users_FK` (`cont_user`),\
                CONSTRAINT `cont_users_FK` FOREIGN KEY (`cont_user`) REFERENCES `users` (`id`)\
            )"

        self.execute(sql, commit=True)

    def add_cont_user(self,
                      cont_id=int,
                      cont_user=None,
                      cont_org='',
                      cont_ogrn='',
                      cont_adress='',
                      cont_phone='',
                      cont_email='',
                      cont_inn='',
                      cont_comment='',
                      cont_fio='',
                      cont_headstatus='',
                      cont_fiocont='',
                      cont_link=''):
        sql = "INSERT IGNORE INTO cont_users VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"
        parameters = (cont_id, cont_user, cont_org, cont_ogrn, cont_adress, cont_phone,
                      cont_email, cont_inn, cont_comment, cont_fio, cont_headstatus, cont_fiocont, cont_link)
        self.execute(sql, parameters=parameters, commit=True)

    def update_cont_user(self, cont_id, dict_oper):
        for data in dict_oper.items():
            if data[1] == "Пропустить":
                data = list(data)
                data[1] = ''
            try:
                sql = f"UPDATE cont_users SET {data[0]}=%s WHERE cont_id=%s;"
                self.execute(sql, parameters=(data[1], cont_id), commit=True)
            except:
                pass

    def delete_cont_user(self, cont_id):
        sql = f"DELETE from cont_users WHERE cont_id=%s;"
        self.execute(sql, parameters=(cont_id), commit=True)


######## Template ###########

    def create_table_template(self):
        sql = "CREATE TABLE `template` (\
  `id` int(11) DEFAULT NULL,\
  `name` varchar(100) DEFAULT NULL,\
  `link` varchar(100) DEFAULT NULL\
) ENGINE=InnoDB DEFAULT CHARSET=utf8;"

        self.execute(sql, commit=True)

    def add_template(self, name: str, link: str, template_id: int):
        sql = "INSERT IGNORE INTO template VALUES (%s, %s, %s);"
        parameters = (template_id, name, link)
        self.execute(sql, parameters=parameters, commit=True)

    def update_template(self, id, link):
        sql = f"UPDATE template SET link=%s WHERE id=%s;"
        self.execute(sql, parameters=(link, id), commit=True)

    def delete_template(self, id):
        sql = f"DELETE from template WHERE id=%s;"
        self.execute(sql, parameters=(id), commit=True)
