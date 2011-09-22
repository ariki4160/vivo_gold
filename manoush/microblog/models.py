<<<<<<< HEAD
# -*- coding: utf-8 -*-
"""
モデル定義を行うファイルです。
インストールされたアプリケーションのアプリケーションディレクトリにmodels.pyがあれば、djangoが起動時に自動で読み込みます。
別のファイルに記述する場合にも、models.pyでインポートしておかなければいけません。
"""
from django.db import models

class Note(models.Model):
    """
    つぶやきデータのモデルです。
    モデルはdjango.db.models.Modelを継承したクラスとして定義します。
    """
    #models.ForeignKeyは別のモデルを参照する関連フィールドです。
    author = models.CharField(max_length=30)
    #フィールドの第一引数は、人間用のラベルとして利用されます。国際化文字列としてアルファベットで設定を行っていますが、日本語のユニコード文字列として定義しても構いません。
    #ただし、Pythonのソースコードファイルにアスキー以外の文字を記述する場合、ファイルの最初にcodingの指定を行わなければなりません。また、指定通りの文字コードでファイルを保存してください。
    text = models.TextField()
    writed_at = models.DateTimeField()
=======
from django.db import models

# Create your models here.
>>>>>>> 9c24b07f0bd1e35ac34f9a7c9fca94cb194406cb
