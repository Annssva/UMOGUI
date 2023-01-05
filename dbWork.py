import bcrypt
import psycopg2
import random
import config

passw ='123'

hashed_password = bcrypt.hashpw(passw.encode(), bcrypt.gensalt())

# метод для авторизации
def authorization(login, password):
    try:
        # подключение к бд
        connection = psycopg2.connect(
            host=config.host,
            user=config.user,
            password=config.password,
            database=config.db_name
        )

        # курсор для выполнения запросов для получения айди по логину
        with connection.cursor() as cursorLog:
            cursorLog.execute("SELECT id_user FROM umo_user WHERE login_user = %s;", (str(login),))
            idUser = cursorLog.fetchone()[0]
            print('ID ', )

            if idUser is not None:
                print(f"айди пользователя: {idUser}")

                # курсор для выполнения запросов для получения пароля по айди
                with connection.cursor() as cursorPass:
                    cursorPass.execute(
                        "SELECT password_user FROM umo_user WHERE id_user = %s;", (idUser,)
                    )
                    passUser = cursorPass.fetchone()[0]
                    print('pass', passUser)
                    print(password.encode())

                    # проверка пароля
                    if bcrypt.checkpw(password.encode(), passUser.encode()):
                        return idUser, login, passUser
                    else:
                        exep = f"Пароль неверный!"
                        return False, exep
            else:
                exep = f"пользователя c логином {login} не существует"
                return False, exep


    except Exception as _ex:
        print("[INFO] Error while working with PostgreSQL", _ex)
        exep = f"Не удалось подключиться к БД или пользователя c логином {login} не существует!"
        return False, exep
    finally:
        if connection:
            connection.close()
            print("[INFO] PostgreSQL connection closed")

def getPostuser(userId):
    try:
        # подключение к бд
        connection = psycopg2.connect(
            host=config.host,
            user=config.user,
            password=config.password,
            database=config.db_name
        )
        # курсор для выполнения запросов для получения должности
        with connection.cursor() as cursorPost:
            cursorPost.execute(
                "SELECT name_role FROM roles WHERE id_role = (SELECT role_user FROM umo_user WHERE id_user = %s);", (userId,)
            )
            userPost = cursorPost.fetchone()[0]
            if userPost is not None:
                print(f"Должность пользователя: {userPost}")
                return userPost
            else:
                print(f"Ошибка должности")

    except Exception as _ex:
        print("[INFO] Error while working with PostgreSQL", _ex)
    finally:
        if connection:
            connection.close()
            print("[INFO] PostgreSQL connection closed")


# получение таблицы институтов
def instsForUser(userLogin, userPassw):
    insts = ()
    try:
        # подключение к бд
        connection = psycopg2.connect(
            host=config.host,
            user=userLogin,
            password=userPassw,
            database=config.db_name
        )
        # курсор для выполнения запросов для получения таблицы

        with connection.cursor() as cursorInsts:
            cursorInsts.execute(
                f"SELECT institute.name_inst, institute.abbreviation_inst, teaching_stuff.surnme_teach,"
                "teaching_stuff.name_teach, teaching_stuff.patronymic_teach, institute.phone_number_inst, institute.email_inst "
                "FROM institute "
                "INNER JOIN teaching_stuff ON teaching_stuff.id_teach = institute.dekan_inst;"
            )
            insts = cursorInsts.fetchall()


    except Exception as _ex:
        print("[INFO] Error while working with PostgreSQL", _ex)
    finally:
        if connection:
            connection.close()
            print("[INFO] PostgreSQL connection closed")

        mass2 = []
        for i in range(len(insts)):
            case = []
            for j in range(len(insts[i])):
                if j != 2 and j != 3 and j != 4 :
                    case.append(insts[i][j])
                if j == 2:
                    case.append(insts[i][2] + ' ' + insts[i][3] + ' ' + insts[i][4])
            mass2.append(case)

        return mass2


# получение таблицы кафедр
def departsForUser(userLogin, userPassw):
    deps = ()
    try:
        # подключение к бд
        connection = psycopg2.connect(
            host=config.host,
            user=userLogin,
            password=userPassw,
            database=config.db_name
        )
        # курсор для выполнения запросов для получения таблицы

        with connection.cursor() as cursorInsts:
            cursorInsts.execute(
                f"SELECT department.name_depart, department.abbreviation_depart, teaching_stuff.surnme_teach, "
                "teaching_stuff.name_teach, teaching_stuff.patronymic_teach, department.phone_number_depart, "
                "department.email, institute.name_inst "
                "FROM department "
                "INNER JOIN teaching_stuff ON teaching_stuff.id_teach = department.zav_depart "
                "INNER JOIN institute ON institute.id_inst = department.institute_id;"
            )
            deps = cursorInsts.fetchall()

    except Exception as _ex:
        print("[INFO] Error while working with PostgreSQL", _ex)
    finally:
        if connection:
            connection.close()
            print("[INFO] PostgreSQL connection closed")

        mass2 = []
        for i in range(len(deps)):
            case = []
            for j in range(len(deps[i])):
                if j != 2 and j != 3 and j != 4:
                    case.append(deps[i][j])
                if j == 2:
                    case.append(deps[i][2] + ' ' + deps[i][3] + ' ' + deps[i][4])
            mass2.append(case)

        return mass2


# получение таблицы направления
def directForUser(userLogin, userPassw):
    directs = ()
    try:
        # подключение к бд
        connection = psycopg2.connect(
            host=config.host,
            user=userLogin,
            password=userPassw,
            database=config.db_name
        )
        # курсор для выполнения запросов для получения таблицы

        with connection.cursor() as cursorDirect:
            cursorDirect.execute(
                f"SELECT study_direction.id_direction, study_direction.name_direction, institute.name_inst "
                f"FROM study_direction INNER JOIN institute ON institute.id_inst = study_direction.institute_id;"
            )
            directs = cursorDirect.fetchall()

    except Exception as _ex:
        print("[INFO] Error while working with PostgreSQL", _ex)
    finally:
        if connection:
            connection.close()
            print("[INFO] PostgreSQL connection closed")

        return directs

# получение таблицы дисциплин
def discipForUser(userLogin, userPassw, group):
    disciip = []
    idDiscip = ()
    idControl = []
    control = []
    try:
        # подключение к бд
        connection = psycopg2.connect(
            host=config.host,
            user=userLogin,
            password=userPassw,
            database=config.db_name
        )
        # курсор для выполнения запросов для получения таблицы

        with connection.cursor() as cursorDiscipId:
            cursorDiscipId.execute(
                "SELECT discipline_id FROM academic_plan WHERE study_direction_id = (SELECT direction_study_group FROM study_group WHERE group_code = %s);", (group,)
            )
            idDiscip = cursorDiscipId.fetchall()

        ids = []
        for i in range(0, (len(idDiscip))):
            ids.append(idDiscip[i][0])

        with connection.cursor() as cursorDiscip:
            for i in range(len(ids)):
                cursorDiscip.execute(
                    f"SELECT discipline.name_discip, discipline.department_id, discipline.hours_count, control_type.name_control_type "
                    f"FROM discipline "							
                    f"INNER JOIN control_type ON control_type.id_control_type = discipline.control_type_id WHERE id_discipline = {ids[i]}; "
                )
                disciip.append(cursorDiscip.fetchall())

    except Exception as _ex:
        print("[INFO] Error while working with PostgreSQL", _ex)
    finally:
        if connection:
            connection.close()
            print("[INFO] PostgreSQL connection closed")

        mass2 = []

        for i in range(len(disciip)):
            case = []
            for j in range(len(disciip[i][0])):
                case.append(disciip[i][0][j])
            mass2.append(case)

        return mass2

# Метод для выведения нахождений преподавателя
def searchTeach(userLogin, userPassw, surname):
    disciip = []
    try:
        # подключение к бд
        connection = psycopg2.connect(
            host=config.host,
            user=userLogin,
            password=userPassw,
            database=config.db_name
        )
        # курсор для выполнения запросов для получения таблицы

        with connection.cursor() as cursorDiscipId:
            cursorDiscipId.execute(
                "SELECT lesson.date_less, lesson.couple_numb, lesson.cabinet_numb "
                "FROM discipline_teaching_staff "
                "INNER JOIN lesson ON lesson.teach_discip_id = discipline_teaching_staff.id_teach_discip "
                "INNER JOIN teaching_stuff ON teaching_stuff.id_teach = discipline_teaching_staff.teaching_staff_id "
                "WHERE teaching_stuff.surnme_teach = %s AND lesson.date_less >= CURRENT_DATE "
                " ORDER BY lesson.date_less ASC;", (surname,)
            )
            place = cursorDiscipId.fetchall()

    except Exception as _ex:
        print("[INFO] Error while working with PostgreSQL", _ex)
    finally:
        if connection:
            connection.close()
            print("[INFO] PostgreSQL connection closed")

        return place

# получение таблицы плана дисциплин
def acPlanForUser(userLogin, userPassw, group):
    try:
        # подключение к бд
        connection = psycopg2.connect(
            host=config.host,
            user=userLogin,
            password=userPassw,
            database=config.db_name
        )
        # курсор для выполнения запросов для получения таблицы

        with connection.cursor() as cursorDirectId:
            cursorDirectId.execute(
                "SELECT discipline.name_discip, academic_plan.semestr_numb "
                "FROM academic_plan "
                "INNER JOIN discipline ON discipline.id_discipline = academic_plan.discipline_id "
                "WHERE academic_plan.study_direction_id =  "
	            "(SELECT direction_study_group FROM study_group WHERE group_code = %s) "
                "ORDER BY academic_plan.semestr_numb ASC;", (group,)
            )
            planMass = cursorDirectId.fetchall()

    except Exception as _ex:
        print("[INFO] Error while working with PostgreSQL", _ex)
    finally:
        if connection:
            connection.close()
            print("[INFO] PostgreSQL connection closed")

        return planMass

# получение таблицы преподавателей
def teachForUser(userLogin, userPassw, group):
    try:
        # подключение к бд
        connection = psycopg2.connect(
            host=config.host,
            user=userLogin,
            password=userPassw,
            database=config.db_name
        )
        # курсор для выполнения запросов для получения таблицы

        with connection.cursor() as cursorTeach:
            cursorTeach.execute(
                "SELECT name_teach, surnme_teach, patronymic_teach, email_teach FROM teaching_stuff WHERE institute_id = "
                "(SELECT institute_group FROM study_group WHERE group_code = %s);", (group,)
            )
            teach = cursorTeach.fetchall()

    except Exception as _ex:
        print("[INFO] Error while working with PostgreSQL", _ex)
    finally:
        if connection:
            connection.close()
            print("[INFO] PostgreSQL connection closed")

        return teach


# получение таблицы расписания
def timetableForUser(userLogin, userPassw, group):
    try:
        # подключение к бд
        connection = psycopg2.connect(
            host=config.host,
            user=userLogin,
            password=userPassw,
            database=config.db_name
        )
        # курсор для выполнения запросов для получения таблицы

        with connection.cursor() as cursorLessonId:
            cursorLessonId.execute( # функция в которой юзается view
                "select * from timetableForUser(%s);", (group,)
            )
            timeTable = cursorLessonId.fetchall()

            masstimeTable = []

            for i in range(len(timeTable)):
                case = []
                for j in range(len(timeTable[i])):
                    if j != 4 and j != 5 and j != 6:
                        case.append(str(timeTable[i][j]))
                    else:
                        continue
                    if j == 3:
                        case.append(timeTable[i][4] + ' ' + timeTable[i][5] + ' ' + timeTable[i][6])
                masstimeTable.append(case)

    except Exception as _ex:
        print("[INFO] Error while working with PostgreSQL", _ex)
    finally:
        if connection:
            connection.close()
            print("[INFO] PostgreSQL connection closed")

        return masstimeTable


# метод для выведения информации об учебной группе
def groupForUser(userLogin, userPassw, group):
    try:
        # подключение к бд
        connection = psycopg2.connect(
            host=config.host,
            user=userLogin,
            password=userPassw,
            database=config.db_name
        )
        # курсор для выполнения запросов для получения таблицы

        with connection.cursor() as cursorLessonId:
            cursorLessonId.execute(
                "SELECT study_group.group_code, institute.name_inst, study_group.direction_study_group, study_group.students_count_group "
                "FROM study_group "
                "INNER JOIN institute ON study_group.institute_group = institute.id_inst"
                " WHERE study_group.group_code =  %s;", (group,)
            )
            group = cursorLessonId.fetchall()

    except Exception as _ex:
        print("[INFO] Error while working with PostgreSQL", _ex)
    finally:
        if connection:
            connection.close()
            print("[INFO] PostgreSQL connection closed")
        return group

# метод для возврата таблиц
def methodistsTable(userLogin, userPassw):
    try:
        # подключение к бд
        connection = psycopg2.connect(
            host=config.host,
            user=userLogin,
            password=userPassw,
            database=config.db_name
        )
        # курсор для выполнения запросов для получения таблицы
        with connection.cursor() as cursorInstitute:
            cursorInstitute.execute(
                f"SELECT * FROM institute;"
            )
            inst = cursorInstitute.fetchall()
        with connection.cursor() as cursorDepart:
            cursorDepart.execute(
                f"SELECT * FROM department;"
            )
            depart = cursorDepart.fetchall()
        with connection.cursor() as cursorDirect:
            cursorDirect.execute(
                f"SELECT * FROM study_direction;"
            )
            direct = cursorDirect.fetchall()
        with connection.cursor() as cursorDiscip:
            cursorDiscip.execute(
                f"SELECT * FROM discipline;"
            )
            discip = cursorDiscip.fetchall()
        with connection.cursor() as cursorPlan:
            cursorPlan.execute(
                f"SELECT * FROM academic_plan;"
            )
            plan = cursorPlan.fetchall()
        with connection.cursor() as cursorTeach:
            cursorTeach.execute(
                f"SELECT * FROM teaching_stuff;"
            )
            teach = cursorTeach.fetchall()
        with connection.cursor() as cursorDiscTeach:
            cursorDiscTeach.execute(
                f"SELECT * FROM discipline_teaching_staff;"
            )
            discTeach = cursorDiscTeach.fetchall()
        with connection.cursor() as cursorGroup:
            cursorGroup.execute(
                f"SELECT * FROM study_group;"
            )
            group = cursorGroup.fetchall()
        with connection.cursor() as cursorControl:
            cursorControl.execute(
                f"SELECT * FROM control_type;"
            )
            control = cursorControl.fetchall()
        with connection.cursor() as cursorLesson:
            cursorLesson.execute(
                f"SELECT * FROM lesson_type;"
            )
            less = cursorLesson.fetchall()
        with connection.cursor() as cursorLessons:
            cursorLessons.execute(
                f"SELECT * FROM lesson;"
            )
            lesson = cursorLessons.fetchall()
        with connection.cursor() as cursorTimeT:
            cursorTimeT.execute(
                f"SELECT * FROM timetable;"
            )
            timet = cursorTimeT.fetchall()


    except Exception as _ex:
        print("[INFO] Error while working with PostgreSQL", _ex)
    finally:
        if connection:
            connection.close()
            print("[INFO] PostgreSQL connection closed")
        return inst, depart, direct, discip, plan, teach, discTeach, group, control, less, lesson, timet

# метод для выведения информации о старосте в учебной группе
def findCaptain(userLogin, userPassw, group):
    try:
        # подключение к бд
        connection = psycopg2.connect(
            host=config.host,
            user=userLogin,
            password=userPassw,
            database=config.db_name
        )
        # курсор для выполнения запросов для получения таблицы

        with connection.cursor() as cursorLessonId:
            cursorLessonId.execute(
                "SELECT surname_stud, first_name_stud, patronymic_stud, email_stud FROM student "
                "WHERE captain = 'TRUE' AND stud_group_code = %s;", (group,)
            )
            captain = cursorLessonId.fetchall()

    except Exception as _ex:
        print("[INFO] Error while working with PostgreSQL", _ex)
    finally:
        if connection:
            connection.close()
            print("[INFO] PostgreSQL connection closed")
        return captain

    # процедура добавления плана
def addPlan(userLogin, userPassw, idPlan, idDiscip, semestr, idDirect):
    try:
        # подключение к бд
        connection = psycopg2.connect(
            host=config.host,
            user=userLogin,
            password=userPassw,
            database=config.db_name
        )
        # курсор для выполнения запросов для получения таблицы

        with connection.cursor() as cursorAddPlan:
            cursorAddPlan.execute( # процедура
                "CALL add_plan(%s, %s, %s, %s);", (idPlan, idDiscip, semestr, idDirect)
            )

    except Exception as _ex:
        print("[INFO] Error while working with PostgreSQL", _ex)
    finally:
        if connection:
            connection.commit()
            connection.close()
            print("[INFO] PostgreSQL connection closed")

    # процедура добавления занятия
def addLess(userLogin, userPassw, id_lesson, date_less, couple, cabinet, lesson_type, teach_discip, semestr):
    try:
        # подключение к бд
        connection = psycopg2.connect(
            host=config.host,
            user=userLogin,
            password=userPassw,
            database=config.db_name
        )
        # курсор для выполнения запросов для получения таблицы

        with connection.cursor() as cursorAddPlan:
            cursorAddPlan.execute( # процедура
                "CALL add_lesson(%s, %s, %s, %s, %s, %s, %s);", (id_lesson, date_less, couple, cabinet, lesson_type, teach_discip, semestr)
            )

    except Exception as _ex:
        print("[INFO] Error while working with PostgreSQL", _ex)
    finally:
        if connection:
            connection.commit()
            connection.close()
            print("[INFO] PostgreSQL connection closed")


    # процедура добавления расписания
def addTimeT(userLogin, userPassw, id_timeTable, group_code, id_lesson):
    try:
        # подключение к бд
        connection = psycopg2.connect(
            host=config.host,
            user=userLogin,
            password=userPassw,
            database=config.db_name
        )
        # курсор для выполнения запросов для получения таблицы

        with connection.cursor() as cursorAddTimeT:
            cursorAddTimeT.execute( # процедура
                "CALL add_timetable(%s, %s, %s);", (id_timeTable, group_code, id_lesson)
            )

    except Exception as _ex:
        print("[INFO] Error while working with PostgreSQL", _ex)
    finally:
        if connection:
            connection.commit()
            connection.close()
            print("[INFO] PostgreSQL connection closed")

    # процедура добавления занятия
def addTeachDiscip(userLogin, userPassw, id_teach_discip, id_teach, id_discip):
    try:
        # подключение к бд
        connection = psycopg2.connect(
            host=config.host,
            user=userLogin,
            password=userPassw,
            database=config.db_name
        )
        # курсор для выполнения запросов для получения таблицы

        with connection.cursor() as cursorAddTimeT:
            cursorAddTimeT.execute( # процедура
                "CALL add_teach_discip(%s, %s, %s);", (id_teach_discip, id_teach, id_discip)
            )

    except Exception as _ex:
        print("[INFO] Error while working with PostgreSQL", _ex)
    finally:
        if connection:
            connection.commit()
            connection.close()
            print("[INFO] PostgreSQL connection closed")


def addUser(userLogin, userPassw, id_User, login, passw, role):
    # хэширование пароля
    passw = bcrypt.hashpw(passw.encode(), bcrypt.gensalt())
    try:
        # подключение к бд
        connection = psycopg2.connect(
            host=config.host,
            user=userLogin,
            password=userPassw,
            database=config.db_name
        )
        # курсор для выполнения запросов для получения таблицы

        with connection.cursor() as cursorAddTimeT:
            cursorAddTimeT.execute(# процедура
                "CALL create_user(%s, %s, %s, %s);", (id_User, str(login), str(passw.decode()), role)
            )

    except Exception as _ex:
        print("[INFO] Error while working with PostgreSQL", _ex)
    finally:
        if connection:
            connection.commit()
            connection.close()
            print("[INFO] PostgreSQL connection closed")


def dellUser(userLogin, userPassw, login):
    try:
        # подключение к бд
        connection = psycopg2.connect(
            host=config.host,
            user=userLogin,
            password=userPassw,
            database=config.db_name
        )
        # курсор для выполнения запросов для получения таблицы

        with connection.cursor() as cursorAddTimeT:
            cursorAddTimeT.execute( # при этом действии срабатывает триггерная функция
                "DELETE FROM umo_user WHERE login_user = %s;", (str(login),)
            )

    except Exception as _ex:
        print("[INFO] Error while working with PostgreSQL", _ex)
    finally:
        if connection:
            connection.commit()
            connection.close()
            print("[INFO] PostgreSQL connection closed")


def searchTimetable(userLogin, userPassw, group):
    try:
        # подключение к бд
        connection = psycopg2.connect(
            host=config.host,
            user=userLogin,
            password=userPassw,
            database=config.db_name
        )
        # курсор для выполнения запросов для получения таблицы

        with connection.cursor() as cursor:
            cursor.execute( # тут используется индекс
                "SELECT * FROM timetable WHERE group_code = %s", (str(group),)
            )
            timetable = cursor.fetchall()

    except Exception as _ex:
        print("[INFO] Error while working with PostgreSQL", _ex)
    finally:
        if connection:
            connection.commit()
            connection.close()
            print("[INFO] PostgreSQL connection closed")
        return timetable

def searchLesson(userLogin, userPassw, id):
    try:
        # подключение к бд
        connection = psycopg2.connect(
            host=config.host,
            user=userLogin,
            password=userPassw,
            database=config.db_name
        )
        # курсор для выполнения запросов для получения таблицы

        with connection.cursor() as cursor:
            cursor.execute( # тут используется индекс
                "SELECT * FROM lesson WHERE id_lesson = %s", (id,)
            )
            lesson = cursor.fetchall()

    except Exception as _ex:
        print("[INFO] Error while working with PostgreSQL", _ex)
    finally:
        if connection:
            connection.commit()
            connection.close()
            print("[INFO] PostgreSQL connection closed")
        return lesson

def transferStud(userLogin, userPassw, id, group):
    try:
        # подключение к бд
        connection = psycopg2.connect(
            host=config.host,
            user=userLogin,
            password=userPassw,
            database=config.db_name
        )
        # курсор для выполнения запросов для получения таблицы

        with connection.cursor() as cursor:
            cursor.execute( # тут транзакция
                "BEGIN;"
                
                "UPDATE study_group SET students_count_group = students_count_group - 1 "
                "WHERE group_code = "
	            "(SELECT stud_group_code FROM student WHERE id_stud = %s); "
                
                "UPDATE student SET stud_group_code = %s "
                "WHERE id_stud = %s; "
                
                "UPDATE study_group SET students_count_group = students_count_group + 1 "
	            "WHERE group_code = %s; "
                
                "COMMIT;", (id, group, id, group, )
            )

    except Exception as _ex:
        print("[INFO] Error while working with PostgreSQL", _ex)
    finally:
        if connection:
            connection.commit()
            connection.close()
            print("[INFO] PostgreSQL connection closed")


