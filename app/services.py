from .database import get_connection

def call_sp_get_employees():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("EXEC sp_GetEmployees")

    columns = [column[0] for column in cursor.description]
    rows = cursor.fetchall()

    result = []
    for row in rows:
        result.append(dict(zip(columns, row)))

    cursor.close()
    conn.close()

    return result


def call_sp_get_employee_by_id(employee_id: int):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("EXEC sp_GetEmployeeById ?", employee_id)

    columns = [column[0] for column in cursor.description]
    row = cursor.fetchone()

    cursor.close()
    conn.close()

    if row:
        return dict(zip(columns, row))
    return None
