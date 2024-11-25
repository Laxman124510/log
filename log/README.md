Role-Based Access Control (RBAC) User Interface
This project demonstrates a simple Role-Based Access Control (RBAC) system with a user-friendly interface. The application provides a secure login, displays user roles and permissions, and restricts access to actions based on assigned roles.

Features
Role-Based Access: Users are assigned roles such as admin, manager, or viewer.
Permissions Management: Each role has specific permissions, such as viewing, editing, or deleting users.
User Authentication: Secure login using Flask-Login.
Access Control: Only authorized users can perform certain actions.
Responsive UI: Clean and intuitive interface styled with CSS.

How It Works
User Authentication:

Users login with a username and password.
The application validates the credentials against a mock database.
Role Assignment:

Each user is assigned a role:
admin: Full access (view, edit, delete).
manager: Limited access (view, edit).
viewer: Read-only access (view only).
Access Control:

Permissions are granted based on roles.
Unauthorized actions are denied, with error messages displayed.
User Interface:

Login Page: Users enter their credentials.
Dashboard: Displays the user’s role and available actions.
Action Links: Restricted links for role-specific operations.
