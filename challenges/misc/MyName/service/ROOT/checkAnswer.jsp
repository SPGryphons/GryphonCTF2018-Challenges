<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
    pageEncoding="ISO-8859-1"%>
<%@ page import="java.io.*"%>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1">
<title>Insert title here</title>
</head>
<body>

<%

	String answer = request.getParameter("answer");
	
	answer = answer.toLowerCase();

	if(answer == null || answer.equals("")){
		response.sendRedirect("index.jsp?check=noinput");
	}

	else if(answer.equals("cassidy")){
		out.println("GCTF{F1V3_N1GHT5_4T_FR3ddY'5}");
	}
	
	else{
		response.sendRedirect("index.jsp?check=wrong");
	}
%>

</body>
</html>