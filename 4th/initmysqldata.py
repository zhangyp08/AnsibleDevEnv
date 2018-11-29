from mysqloperation import MySQLcaozuo

def inster_data(table, datas):
    db = MySQLcaozuo()
    db.clear(table)
    for data in datas:
        db.insert(table, data)
    db.close()

table_poll_question = "polls_question"
datas_poll_question =[ {'id': 1, 'question_text': 'what is your favorite language?'}]
table_poll_choice = "polls_choice"
datas_poll_choice =[{'id': 1, 'choice_text': 'java', 'votes': 0, 'question_id': 1},
{'id': 2, 'choice_text': 'python', 'votes': 0, 'question_id': 1}]


def init_data():
    inster_data(table_poll_question, datas_poll_question)
    inster_data(table_poll_choice, datas_poll_choice)

if __name__ == '__main__':
    init_data()