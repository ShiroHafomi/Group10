from flask import Blueprint, render_template,current_app, url_for,redirect,request,flash
from flask_login import login_required, current_user
from . import db
from .models import User


admin = Blueprint('admin', __name__)

@admin.route('/admin/users')
@login_required
def admin_users():
    if not current_user.is_admin:
        return redirect(url_for('views.home'))
    
    # if not current_user.is_active:
    #     return redirect(url_for('auth.login')) 
    
    users = User.query.all()  
    return render_template('Admin.html', user=users)

@admin.route('/admin/edit-user/<int:user_id>', methods=['GET', 'POST'])
@login_required
def edit_user(user_id):
    if not current_user.is_admin:
        return redirect(url_for('views.home'))
    user = User.query.get_or_404(user_id)
    if request.method == 'POST':
        user.email = request.form.get('email')
        user.first_name = request.form.get('first_name')
        user.is_admin = request.form.get('is_admin') == 'on'  
        db.session.commit() 
        flash('User updated successfully!', category='success')
        return redirect(url_for('admin.admin_users'))  
    
    return render_template('edit_user.html', users=user)

@admin.route('/admin/delete-user/<int:user_id>')
@login_required
def delete_user(user_id):
    if not current_user.is_admin:
        return redirect(url_for('views.home'))
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    flash('User deleted successfully!', category='success')
    return redirect(url_for('admin.admin_users'))