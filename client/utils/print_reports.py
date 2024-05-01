from utils.PDF import PDF
from utils.formatter import format_number, format_date
from src.api.results_controller import get_result_by_id
from src.api.tests_controller import get_test_tasks
from src.api.tasks_controller import get_task_by_id
from src.api.users_controller import get_user_data_by_id


def print_results(file_name, item) -> None:
    '''
    Формирование PDF файла с результатом.

    Args:
        file_name (str): Имя файла.
        item (QListWidgetItem): Элемент QListWidget, откуда брать
        информацию для парсинга в pdf.
    '''
    text = item.text().split('\t')
    # Удаляем символ №
    result_id = text[1][2:]

    result = get_result_by_id(result_id)

    pdf = PDF(logo_path='client/gui/resources/img/logo_black.png',
              title="Отчет о результате тестирования")
    pdf.add_page()

    pdf.cell(40, 10, "ID Результата:", ln=0)
    pdf.tab(tab_size=5)
    pdf.cell(40, 10, f"{result_id}", ln=1)

    points = format_number(result["points"])
    num_tasks = len(get_test_tasks(result['test_id']))
    pdf.cell(40, 10, "Результат:", ln=0)
    pdf.tab(tab_size=5)
    pdf.cell(40, 10, f"{points}/{num_tasks}", ln=1)

    user_id = result["user_id"]
    user_data = get_user_data_by_id(user_id)
    fio = f'{user_data["lastname"]} {user_data["firstname"]} {user_data["midname"]}'
    pdf.cell(40, 10, "Студент:", ln=0)
    pdf.tab(tab_size=5)
    pdf.cell(40, 10, f"#{user_id} {fio}", ln=1)

    test_id = result["test_id"]
    pdf.cell(40, 10, "ID Теста:", ln=0)
    pdf.tab(tab_size=5)
    pdf.cell(40, 10, f"{test_id}", ln=1)

    created_at = format_date(result['created_at'])
    pdf.cell(40, 10, f"Время окончания тестирования: {created_at}", ln=1)

    time = result["time_spent"]
    minutes = time // 60
    seconds = time % 60
    pdf.cell(40, 10, "Затраченное время:", ln=0)
    pdf.tab(tab_size=5)
    pdf.cell(40, 10, f"{minutes:02}:{seconds:02}", ln=1)

    pdf.ln(5)
    pdf.cell(40, 10, "Вопросы и ответы:", ln=1)
    pdf.ln(5)
    answers = result["answers"]
    for i, answer in enumerate(answers):
        # Цвет ячейки
        if answer["correct"] is True:
            pdf.set_fill_color(168, 255, 196)
            pdf.set_draw_color(10, 207, 131)
        else:
            pdf.set_fill_color(255, 207, 201)
            pdf.set_draw_color(255, 92, 74)
        # Отступ
        pdf.tab()
        pdf.cell(10, 10, f"{i}", ln=0)
        task = get_task_by_id(answer["task_id"])["question"]
        answ = answer["answer"]
        if isinstance(answ, list):
            answ = "; ".join(answ)
        # Ячейка с переносом строки
        pdf.multi_cell(150, 10, f"{task}", new_x="LMARGIN")
        pdf.cell(20, 10, "Ответ:")
        pdf.multi_cell(150, 10, f"{answ}", border=1, fill=True)
        pdf.ln(5)

    pdf.output(f"{file_name}.pdf")
