import sqlite3
def create_database():

    db = sqlite3.connect('LM_DB.db')
    try:
        cursorobj = db.cursor()
        cursorobj.execute('''CREATE TABLE staff(
        employee_id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name varchar(30) NOT NULL,
        last_name varchar(30) NOT NULL,
        phone varchar(11) NOT NULL,
        email varchar(30) NOT NULL,
        designation varchar(20) NOT NULL,
        password varchar(20) NOT NULL,
        role varchar(8) NOT NULL,
        gender varchar(8) NOT NULL,
        number_of_entitled_leave int(3));''')

        cursorobj.execute('''CREATE TABLE leave (
        leave_id INTEGER PRIMARY KEY AUTOINCREMENT,
        employee_id varchar(30),
        start_date varchar(30) NOT NULL,
        end_date varchar(30) NOT NULL,
        type_of_leave text NOT NULL,
        reason_for_leave text NOT NULL,
        leave_status varchar(20) NOT NULL,
        date_applied varchar(30));''')
    except :
        db.rollback()
        return False
    finally:
        db.close()
    return True

def add_new(fn ,ln ,ph ,em ,dn ,pw,rl,gn):
    auth,_= authenticate(em,pw)
    if auth:
        return False
    else:
        db = sqlite3.connect('LM_DB.db')
        try:
            cursorobj = db.cursor()
            cursorobj.execute('INSERT INTO staff (first_name ,last_name ,phone ,email ,designation ,password,role,gender ,number_of_entitled_leave) VALUES(?,?,?,?,?,?,?,?,?)',(fn ,ln ,ph ,em ,dn ,pw,rl,gn,35 ))
            db.commit()
        except :
            db.rollback()
            db.close()
            return False
        db.close()
        return True

def authenticate(em,pw):
    db = sqlite3.connect('LM_DB.db')
    cursorobj = db.cursor()
    cursorobj.execute('SELECT * FROM staff WHERE email = ? AND password = ? ', (em, pw))
    user_data = cursorobj.fetchone()
    if user_data is None:
        return False,[]
    else:
        return True,user_data
def getAlluser(role=()):
    """retrieves All user records from database"""
    db = sqlite3.connect('LM_DB.db')
    cursorobj = db.cursor()
    cursorobj.execute('SELECT * FROM staff WHERE role = ? or role = ? ', (role))
    user_data = cursorobj.fetchall()
    return user_data

def getuserbymail(em):
    # retrieves user records from database
    db = sqlite3.connect('LM_DB.db')
    cursorobj = db.cursor()
    cursorobj.execute('SELECT * FROM staff WHERE email = ? ', (em,))
    user_data = cursorobj.fetchone()
    db.close()
    if user_data is None:
        return False, []
    else:
        return True, user_data

def getuserbyid(id):
    # retrieves user records from database
    db = sqlite3.connect('LM_DB.db')
    cursorobj = db.cursor()
    cursorobj.execute('SELECT * FROM staff WHERE employee_id = ? ', (id,))
    user_data = cursorobj.fetchone()
    db.close()
    if user_data is None:
        return []
    else:
        return user_data
def update_staff(fn ,ln ,ph ,em ,dn ,pw,rl,gn,id):
    # update user records from database
    db = sqlite3.connect('LM_DB.db')
    try:
        cursorobj = db.cursor()
        cursorobj.execute("""UPDATE staff
                            SET first_name = ? , 
                                last_name = ? ,
                                phone = ? ,
                                email = ? ,
                                designation = ? ,
                                password = ? ,
                                role = ? ,
                                gender = ? 
                            WHERE 
                                employee_id = ?""",(fn, ln, ph, em, dn, pw, rl, gn,id))
        db.commit()
    except :
        db.rollback()
        db.close()
        return False
    db.close()
    return True

def remove_staff(em):
    # delete user records from database
    db = sqlite3.connect('LM_DB.db')
    cursorobj = db.cursor()
    cursorobj.execute('DELETE FROM staff WHERE email = ? ', (em,))
    db.commit()
    db.close()
def leaveexist(employeepid):
    try:
        db = sqlite3.connect('LM_DB.db')
        cursorobj = db.cursor()
        cursorobj.execute('SELECT * FROM leave WHERE employee_id = ? AND leave_status = ? OR leave_status = ? ;',(employeepid,"pending","active"))
        exist=cursorobj.fetchone()
        db.close()
        if exist == None:
            return False
        else :
            return True
    except :
        db.rollback()
        db.close()
        return False
def applyleave(employeepid,startddate,enddate,leavetype,leavereason):
    from datetime import datetime
    if leaveexist(employeepid):
        return False
    elif not leaveexist(employeepid):
        try:
            db = sqlite3.connect('LM_DB.db')
            cursorobj = db.cursor()
            cursorobj.execute('INSERT INTO leave (employee_id,start_date,end_date,type_of_leave,reason_for_leave,leave_status,date_applied) values(?,?,?,?,?,?,?)',(employeepid,startddate,enddate,leavetype,leavereason,"pending",datetime.now()))
            db.commit()
            db.close()
            return True
        except:
            db.rollback()
            db.close()
            return False
def withdraw_leave(employeeid):
    db = sqlite3.connect('LM_DB.db')
    try:
        cursorobj = db.cursor()
        cursorobj.execute('UPDATE leave SET leave_status = ? WHERE employee_id = ? ;',("withdrawn",employeeid))
        db.commit()
    except :
        db.rollback()
        db.close()
        return False
    db.close()
    return True
def cancel_leave(employeeid):
    db = sqlite3.connect('LM_DB.db')
    try:
        cursorobj = db.cursor()
        cursorobj.execute('UPDATE leave SET leave_status = ? WHERE employee_id = ? ;',("canceled",employeeid))
        db.commit()
    except :
        db.rollback()
        db.close()
        return False
    db.close()
    return True
def withdraw_leave(employeeid):
    db = sqlite3.connect('LM_DB.db')
    try:
        cursorobj = db.cursor()
        cursorobj.execute('UPDATE leave SET leave_status = ? WHERE employee_id = ? ;',("withdrawn",employeeid))
        db.commit()
    except :
        db.rollback()
        db.close()
        return False
    db.close()
    return True
def active_leave(employeeid):
    db = sqlite3.connect('LM_DB.db')
    try:
        cursorobj = db.cursor()
        cursorobj.execute('UPDATE leave SET leave_status = ? WHERE employee_id = ? ;',("active",employeeid))
        db.commit()
    except :
        db.rollback()
        db.close()
        return False
    db.close()
    return True
def getleavehistory(employeestatus):
    """    retrieves user leave history records from database"""
    db = sqlite3.connect('LM_DB.db')
    try:
        cursorobj = db.cursor()
        cursorobj.execute('SELECT * FROM leave WHERE employee_id = ? and leave_status = ? or leave_status = ? or leave_status = ? or leave_status = ? or leave_status = ? ', (employeestatus))
        user_data = cursorobj.fetchall()
        db.close()
        if user_data is None:
            return False, []
        else:
            return True, user_data
    except Exception as e:
        db.rollback()
        db.close()
        return False,e
def getLeaveEntitled(employeeid):
    db = sqlite3.connect('LM_DB.db')
    cursorobj = db.cursor()
    cursorobj.execute('SELECT number_of_entitled_leave FROM staff WHERE employee_id = ?;', employeeid)
    leavecount, = cursorobj.fetchone()
    db.close()
    return leavecount
def acceptLeave(employeeid,days):
    db = sqlite3.connect('LM_DB.db')
    cursorobj = db.cursor()
    cursorobj.execute('UPDATE leave SET number_of_entitled_leave = ? WHERE employee_id = ?;',days,employeeid)
    db.close()
def reject_leave(employeeid):
    db = sqlite3.connect('LM_DB.db')
    try:
        cursorobj = db.cursor()
        cursorobj.execute('UPDATE leave SET leave_status = ? WHERE employee_id = ? ;',("declined",employeeid))
        db.commit()
    except :
        db.rollback()
        db.close()
        return False
    db.close()
    return True
def getAllRequest(status):
    try:
        db = sqlite3.connect('LM_DB.db')
        cursorobj = db.cursor()
        cursorobj.execute('SELECT * FROM leave WHERE leave_status = ? or leave_status = ? or leave_status = ? or leave_status = ? or leave_status = ?;',status)
        allrequest = cursorobj.fetchall()
        db.close()
        if allrequest is None:
            return False, []
        else:
            return True, allrequest
    except Exception as e:
        db.rollback()
        db.close()
        return False, e