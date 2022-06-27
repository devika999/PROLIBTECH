@app.route('/andview_studnetproject_search',methods=['post'])
def andview_studnetproject_search():
    search = request.form['search_project']
    dept_id = request.form['dept_id']
    db = Db()

    res=search.split(" ")
    print(res)
    # ss = db.select(" SELECT project.project_id,project.title,student.s_name,college.c_name,project.p_year FROM project INNER JOIN student ON project.stud_id=student.login_id INNER JOIN college ON student.college_id=college.college_id where project.`title` LIKE '%" + search + "%' or project.`p_year`LIKE '%" + search + "%'")
    # ss = db.select(" SELECT project.project_id,project.title,student.s_name,college.c_name,project.p_year FROM project INNER JOIN student ON project.stud_id=student.login_id INNER JOIN college ON student.college_id=college.college_id where project.`title` LIKE '%" + search + "%' or project.`p_year`LIKE '%" + search + "%'")

    pid=[]
    ls=[]
    for i in res:
        if i!='':
            Q="SELECT distinct `key_words`.`pid`,key_words.count, project.project_id,project.title,student.s_name,college.c_name,project.p_year FROM project INNER JOIN student ON project.stud_id=student.login_id INNER JOIN college ON student.college_id=college.college_id INNER JOIN `key_words`  ON `project`.`project_id`=`key_words`.`pid` WHERE  student.dept_id='"+dept_id+"' and (`key_words`.`key` LIKE '%" + i + "%'  OR( `project`.title LIKE '%"+i+"%')OR( `project`.project_area LIKE '%"+i+"%'))   ORDER BY `count` DESC"
            ss=db.select(Q)
            print(Q)
            for i in ss:

                if i["project_id"] in pid:
                    print("---")
                    pass
                else:
                    pid.append(i["project_id"])
                    a={'title':i["title"],'s_name':i["s_name"],'c_name':i["c_name"],'p_year':i["p_year"],'project_id':i["project_id"]}
                    print("---",a)
                    ls.append(a)



    print(ls)
    print(len(ls))
    return jsonify(status="ok",data=ls)






@app.route('/andview_studnetproject_search',methods=['post'])
def andview_studnetproject_search():
    search = request.form['search_project']
    dept_id = request.form['dept_id']
    db = Db()

    res=search.split(" ")
    print(res)
    # ss = db.select(" SELECT project.project_id,project.title,student.s_name,college.c_name,project.p_year FROM project INNER JOIN student ON project.stud_id=student.login_id INNER JOIN college ON student.college_id=college.college_id where project.`title` LIKE '%" + search + "%' or project.`p_year`LIKE '%" + search + "%'")
    # ss = db.select(" SELECT project.project_id,project.title,student.s_name,college.c_name,project.p_year FROM project INNER JOIN student ON project.stud_id=student.login_id INNER JOIN college ON student.college_id=college.college_id where project.`title` LIKE '%" + search + "%' or project.`p_year`LIKE '%" + search + "%'")

    pid=[]
    ls=[]
    for i in res:
        if i!='':
            Q="SELECT distinct `key_words`.`pid`,key_words.count, project.project_id,project.title,student.s_name,college.c_name,project.p_year FROM project INNER JOIN student ON project.stud_id=student.login_id INNER JOIN college ON student.college_id=college.college_id INNER JOIN `key_words`  ON `project`.`project_id`=`key_words`.`pid` WHERE  student.dept_id='"+dept_id+"' and (`key_words`.`key` LIKE '%" + i + "%'  OR( `project`.title LIKE '%"+i+"%')OR( `project`.project_area LIKE '%"+i+"%'))   ORDER BY `count` DESC"
            ss=db.select(Q)
            print(Q)
            for i in ss:

                if i["project_id"] in pid:
                    print("---")
                    pass
                else:
                    pid.append(i["project_id"])
                    a={'title':i["title"],'s_name':i["s_name"],'c_name':i["c_name"],'p_year':i["p_year"],'project_id':i["project_id"]}
                    print("---",a)
                    ls.append(a)



    print(ls)
    print(len(ls))
    return jsonify(status="ok",data=ls)