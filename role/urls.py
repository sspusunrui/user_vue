from django.urls import path

from role.views import ListAllView, SearchView, SaveView, ActionView, MenusView, GrantMenu

urlpatterns = [
    path('listAll', ListAllView.as_view(), name='listAll'),
    path('search', SearchView.as_view(), name='search'),
    path('save', SaveView.as_view(), name='save'),  # 添加或者修改角色信息
    path('action', ActionView.as_view(), name='action'),  # 角色信息操作
    path('menus', MenusView.as_view(), name='menus'),  # 根据角色查询菜单权限
    path('grant', GrantMenu.as_view(), name='grant'),  # 角色权限授权
]
