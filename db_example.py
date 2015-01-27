con = MySQLdb.connect(host='10.5.28.89',user='root',passwd='admin',db='cursoverao')
c = con.cursor()
c.execute("INSERT INTO `participantes`(`nome`,`idpc`) VALUES (`inacio`,`000`)")
c.commit()
