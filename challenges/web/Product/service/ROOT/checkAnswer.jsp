<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
    pageEncoding="ISO-8859-1"%>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1">
<title>Insert title here</title>
</head>
<body>

<%

	String answer = request.getParameter("answer");
	
	if(answer == null || answer.equals("")){
		response.sendRedirect("index.jsp?check=noinput");
	}

	else if(answer.equals("999108") || answer.equals("999,108")){
		out.println("GCTF{Y0u_4r3_4_m4Th_g0D}");
	}
	
	else{
		response.sendRedirect("index.jsp?check=wrong");
	}
%>

</body>
</html>