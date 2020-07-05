`winpty sqlite3`

csv import

```
$ sqlite3 db.sqlite
```

```
.mode csv
.import test.csv table_name
```

----



dumpdata

```
python manage.py dumpdata --indent 4 app_name.model_name > test.json
```



---



loaddata

```
python manage.py loaddata app_name/test.json
```

-  반드시 파일 위치는 app/fixtures/app/  안에 있어야 함



```
i9i91@DESKTOP-B5GL7LM MINGW64 ~/OneDrive/바탕 화면/github 저장내용/portfolio.io/githubservice (heejungnew)
$ sqlite3 db.sqlite3
SQLite version 3.32.3 2020-06-18 14:00:33
Enter ".help" for usage hints.
sqlite> .tables
accounts_user                   django_session
accounts_user_groups            mains_comment
accounts_user_user_permissions  mains_post
auth_group                      mains_post_like_users
auth_group_permissions          portfolios_color
auth_permission                 portfolios_github
django_admin_log                portfolios_skill
django_content_type             portfolios_usercontent
django_migrations
sqlite> .mode csv
sqlite> .import Application_Data.csv portfolios.
sqlite> .import Application_Data.csv portfolios.Skill
sqlite> .import Application_Data.csv portfolios.Skill
CREATE TABLE portfolios.Skill(...) failed: unknown database portfolios
sqlite> .import Application_Data.csv portfolios_skill
Application_Data.csv:1: INSERT failed: datatype mismatch
sqlite>
sqlite> .exit

i9i91@DESKTOP-B5GL7LM MINGW64 ~/OneDrive/바탕 화면/github 저장내용/portfolio.io/githubservice (heejungnew)
$ python manage.py dumpdata --indent 4 > skills.json
Traceback (most recent call last):
  File "manage.py", line 15, in <module>
    execute_from_command_line(sys.argv)
  File "C:\Users\i9i91\AppData\Local\Programs\Python\Python37\lib\site-packages\django\core\management\__init__.py", line 381, in execute_from_command_line
    utility.execute()
  File "C:\Users\i9i91\AppData\Local\Programs\Python\Python37\lib\site-packages\django\core\management\__init__.py", line 375, in execute
    self.fetch_command(subcommand).run_from_argv(self.argv)
  File "C:\Users\i9i91\AppData\Local\Programs\Python\Python37\lib\site-packages\django\core\management\base.py", line 316, in run_from_argv
    self.execute(*args, **cmd_options)
  File "C:\Users\i9i91\AppData\Local\Programs\Python\Python37\lib\site-packages\django\core\management\base.py", line 350, in execute
    self.check()
  File "C:\Users\i9i91\AppData\Local\Programs\Python\Python37\lib\site-packages\django\core\management\base.py", line 379, in check
    include_deployment_checks=include_deployment_checks,
  File "C:\Users\i9i91\AppData\Local\Programs\Python\Python37\lib\site-packages\django\core\management\base.py", line 366, in _run_checks
    return checks.run_checks(**kwargs)
  File "C:\Users\i9i91\AppData\Local\Programs\Python\Python37\lib\site-packages\django\core\checks\registry.py", line 71, in run_checks
    new_errors = check(app_configs=app_configs)
  File "C:\Users\i9i91\AppData\Local\Programs\Python\Python37\lib\site-packages\django\core\checks\urls.py", line 40, in 
check_url_namespaces_unique
    all_namespaces = _load_all_namespaces(resolver)
  File "C:\Users\i9i91\AppData\Local\Programs\Python\Python37\lib\site-packages\django\core\checks\urls.py", line 57, in 
_load_all_namespaces
    url_patterns = getattr(resolver, 'url_patterns', [])
  File "C:\Users\i9i91\AppData\Local\Programs\Python\Python37\lib\site-packages\django\utils\functional.py", line 37, in 
__get__
    res = instance.__dict__[self.name] = self.func(instance)
  File "C:\Users\i9i91\AppData\Local\Programs\Python\Python37\lib\site-packages\django\urls\resolvers.py", line 533, in url_patterns
    patterns = getattr(self.urlconf_module, "urlpatterns", self.urlconf_module)
  File "C:\Users\i9i91\AppData\Local\Programs\Python\Python37\lib\site-packages\django\utils\functional.py", line 37, in 
__get__
    res = instance.__dict__[self.name] = self.func(instance)
  File "C:\Users\i9i91\AppData\Local\Programs\Python\Python37\lib\site-packages\django\urls\resolvers.py", line 526, in urlconf_module
    return import_module(self.urlconf_name)
  File "C:\Users\i9i91\AppData\Local\Programs\Python\Python37\lib\importlib\__init__.py", line 127, in import_module     
    return _bootstrap._gcd_import(name[level:], package, level)
  File "<frozen importlib._bootstrap>", line 1006, in _gcd_import
  File "<frozen importlib._bootstrap>", line 983, in _find_and_load
  File "<frozen importlib._bootstrap>", line 967, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 677, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 728, in exec_module
  File "<frozen importlib._bootstrap>", line 219, in _call_with_frames_removed
  File "C:\Users\i9i91\OneDrive\바탕 화면\github 저장내용\portfolio.io\githubservice\githubservice\urls.py", line 20, in 
<module>
    from mains import views
  File "C:\Users\i9i91\OneDrive\바탕 화면\github 저장내용\portfolio.io\githubservice\mains\views.py", line 8, in <module>
    from portfolios.forms import UsercontentForm
  File "C:\Users\i9i91\OneDrive\바탕 화면\github 저장내용\portfolio.io\githubservice\portfolios\forms.py", line 98       
    exclude =('user',)`
                      ^
SyntaxError: invalid syntax

i9i91@DESKTOP-B5GL7LM MINGW64 ~/OneDrive/바탕 화면/github 저장내용/portfolio.io/githubservice (heejungnew)
$ python manage.py dumpdata --indent 4 > skills.json

i9i91@DESKTOP-B5GL7LM MINGW64 ~/OneDrive/바탕 화면/github 저장내용/portfolio.io/githubservice (heejungnew)
$ python manage.py dumpdata --indent 4 portfolios.Skill > skills.json
```

http://throughkim.kr/2016/03/29/make-and-load-fixture/