from SqlConnection import create_db_connection
import mysql
#conn=create_db_connection() # connect to Database
def get_AOO(userInput, stateInput):
    conn = create_db_connection()
    cursor = conn.cursor()
    # Call the SQL Server procedure getA00 with input parameters
    cursor.callproc('get_AOO', [userInput, stateInput])
    # Fetch the results (if any)
    results = []
    # for result in cursor.stored_results():
    #     results.extend(result.fetchone())
    for result in cursor.stored_results():
        row = result.fetchone()
        if row is not None:
            results.extend(row)
    # Close the cursor and the connection
    cursor.close()
    conn.close()

    return results
def get_VOO(userInput, stateInput):
    conn = create_db_connection()
    cursor = conn.cursor()
    # Call the SQL Server procedure getA00 with input parameters
    cursor.callproc('get_VOO', [userInput, stateInput])
    # Fetch the results (if any)
    results = []
    # for result in cursor.stored_results():
    #     results.extend(result.fetchone())
    for result in cursor.stored_results():
        row = result.fetchone()
        if row is not None:
            results.extend(row)
    # Close the cursor and the connection
    cursor.close()
    conn.close()

    return results
def get_VVI(userInput, stateInput):
    conn = create_db_connection()
    cursor = conn.cursor()
    # Call the SQL Server procedure getA00 with input parameters
    cursor.callproc('get_VVI', [userInput, stateInput])
    # Fetch the results (if any)
    results = []
    # for result in cursor.stored_results():
    #     results.extend(result.fetchone())
    for result in cursor.stored_results():
        row = result.fetchone()
        if row is not None:
            results.extend(row)

    # Close the cursor and the connection
    cursor.close()
    conn.close()

    return results
def get_AAI(userInput, stateInput):
    conn = create_db_connection()
    cursor = conn.cursor()
    # Call the SQL Server procedure getA00 with input parameters
    cursor.callproc('get_AAI', [userInput, stateInput])
    # Fetch the results (if any)
    results = []
    # for result in cursor.stored_results():
    #     results.extend(result.fetchone())
    for result in cursor.stored_results():
        row = result.fetchone()
        if row is not None:
            results.extend(row)

    # Close the cursor and the connection
    cursor.close()
    conn.close()

    return results


def set_AOO(idState, idlogin, UpperLimitRate, LowerRateLimit, AtrialAmplitude, AtrialPulseWidth):
    try:
        # Establish a connection to the MySQL database
        conn = create_db_connection()
        cursor = conn.cursor()

        # Call the stored procedure with input parameters
        cursor.callproc('set_AOO',
                        (idState, idlogin, UpperLimitRate, LowerRateLimit, AtrialAmplitude, AtrialPulseWidth))

        # Commit the changes (if needed)
        conn.commit()

        # Close the cursor and the connection
        cursor.close()
        conn.close()

    except mysql.connector.Error as err:
        print(f"Error: {err}")


def set_AAI(idState, idlogin, UpperLimitRate, LowerLimitRate, AtrialAmplitude, AtrialPulseWidth, ARP):
    try:
        # Establish a connection to the MySQL database
        conn = create_db_connection()
        cursor = conn.cursor()

        # Call the stored procedure with input parameters
        cursor.callproc('set_AAI',
                        (idState, idlogin, UpperLimitRate, LowerLimitRate, AtrialAmplitude, AtrialPulseWidth, ARP))

        # Commit the changes (if needed)
        conn.commit()

        # Close the cursor and the connection
        cursor.close()
        conn.close()

    except mysql.connector.Error as err:
        print(f"Error: {err}")


def set_VOO(stateID, userID, UpperLimitRate, LowerLimitRate, VentricalAmplitude, VentricalPulseWidth):
    try:
        # Establish a connection to the MySQL database
        conn = create_db_connection()
        cursor = conn.cursor()

        # Call the stored procedure with input parameters
        cursor.callproc('set_VOO',
                        (stateID, userID, UpperLimitRate, LowerLimitRate, VentricalAmplitude, VentricalPulseWidth))

        # Commit the changes (if needed)
        conn.commit()

        # Close the cursor and the connection
        cursor.close()
        conn.close()

    except mysql.connector.Error as err:
        print(f"Error: {err}")


def set_VVI(idState, idlogin, UpperLimitRate, LowerLimitRate, VentricularAmplitude, VentricularPulseWidth, VRP):
    try:
        # Establish a connection to the MySQL database
        conn = create_db_connection()
        cursor = conn.cursor()

        # Call the stored procedure with input parameters
        cursor.callproc('set_VVI', (
        idState, idlogin, UpperLimitRate, LowerLimitRate, VentricularAmplitude, VentricularPulseWidth, VRP))

        # Commit the changes (if needed)
        conn.commit()

        # Close the cursor and the connection
        cursor.close()
        conn.close()

    except mysql.connector.Error as err:
        print(f"Error: {err}")

### Update
def update_AOO(idState, idlogin, UpperLimitRate, LowerRateLimit, AtrialAmplitude, AtrialPulseWidth):
    try:
        # Establish a connection to the MySQL database
        conn = create_db_connection()
        cursor = conn.cursor()

        # Call the stored procedure with input parameters
        cursor.callproc('update_AOO',
                        (idState, idlogin, UpperLimitRate, LowerRateLimit, AtrialAmplitude, AtrialPulseWidth))

        # Commit the changes (if needed)
        conn.commit()

        # Close the cursor and the connection
        cursor.close()
        conn.close()

    except mysql.connector.Error as err:
        print(f"Error: {err}")


def update_AAI(idState, idlogin, UpperLimitRate, LowerLimitRate, AtrialAmplitude, AtrialPulseWidth, ARP):
    try:
        # Establish a connection to the MySQL database
        conn = create_db_connection()
        cursor = conn.cursor()

        # Call the stored procedure with input parameters
        cursor.callproc('update_AAI',
                        (idState, idlogin, UpperLimitRate, LowerLimitRate, AtrialAmplitude, AtrialPulseWidth, ARP))

        # Commit the changes (if needed)
        conn.commit()

        # Close the cursor and the connection
        cursor.close()
        conn.close()

    except mysql.connector.Error as err:
        print(f"Error: {err}")


def update_VOO(stateID, userID, UpperLimitRate, LowerLimitRate, VentricalAmplitude, VentricalPulseWidth):
    try:
        # Establish a connection to the MySQL database
        conn = create_db_connection()
        cursor = conn.cursor()

        # Call the stored procedure with input parameters
        cursor.callproc('update_VOO',
                        (stateID, userID, UpperLimitRate, LowerLimitRate, VentricalAmplitude, VentricalPulseWidth))

        # Commit the changes (if needed)
        conn.commit()

        # Close the cursor and the connection
        cursor.close()
        conn.close()

    except mysql.connector.Error as err:
        print(f"Error: {err}")


def update_VVI(idState, idlogin, UpperLimitRate, LowerLimitRate, VentricularAmplitude, VentricularPulseWidth, VRP):
    try:
        # Establish a connection to the MySQL database
        conn = create_db_connection()
        cursor = conn.cursor()

        # Call the stored procedure with input parameters
        cursor.callproc('update_VVI', (
        idState, idlogin, UpperLimitRate, LowerLimitRate, VentricularAmplitude, VentricularPulseWidth, VRP))

        # Commit the changes (if needed)
        conn.commit()

        # Close the cursor and the connection
        cursor.close()
        conn.close()

    except mysql.connector.Error as err:
        print(f"Error: {err}")



