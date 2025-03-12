# March Madness Bracket App 

This web application will allow users to create, select and track their March Madness Brackets. Users are able to register, login/logout, pick teams, follow the tournament to see how their predictions did. It will also display a leader board so users can see where they rank during the tournament 

## Features.. so far 
- User Authentication: registration, login/logout, profile management
- Bracket Selection: Users can pick their own teams
- Automated matchups: First round matchups are generated automatically by the computer 
- Django Admin Panel: for managing databases 

## Instructions: 
1. **Clone the Repository**  
git clone https://github.com/shelby-wolfe/MarchMadnessRedo.git  
cd MarchMadnessRedo  

2. **Virtual Environment and Dependencies**  
python -m venv venv  - **create virtual environment**  
source venv/bin/activate - **run environment**   
pip install -r requirements.txt - **install dependencies**   

3. **Migrations/Admin Panel**  
python manage.py migrate - **make migrations**  
python manage.py createsuperuser - **create admin acct**  

4. **Run Server**  
python manage.py runserver  



