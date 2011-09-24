# -*- coding: utf-8 -*-
"""
モデル定義を行うファイルです。
インストールされたアプリケーションのアプリケーションディレクトリにmodels.pyがあれば、djangoが起動時に自動で読み込みます。
別のファイルに記述する場合にも、models.pyでインポートしておかなければいけません。
"""
from django.db import models
from django.contrib.auth import models as auth_models
from django.utils.translation import ugettext_lazy as _

class Note(models.Model):
    """
    つぶやきデータのモデルです。
    モデルはdjango.db.models.Modelを継承したクラスとして定義します。
    """
    #models.ForeignKeyは別のモデルを参照する関連フィールドです。
    author = models.ForeignKey(auth_models.User)
    #フィールドの第一引数は、人間用のラベルとして利用されます。国際化文字列としてアルファベットで設定を行っていますが、日本語のユニコード文字列として定義しても構いません。
    #ただし、Pythonのソースコードファイルにアスキー以外の文字を記述する場合、ファイルの最初にcodingの指定を行わなければなりません。また、指定通りの文字コードでファイルを保存してください。
    text = models.TextField(_("Note's Text"))
    writed_at = models.DateTimeField(_('Write at'), auto_now_add=True, editable=False)

    def __unicode__(self):
        """
        __で始まるメソッド（クラスの関数）は特殊な意味を持ちます。
        __unicode__メソッドは、そのクラスのインスタンスを文字列として評価する際に呼び出されるメソッドです。
        ユニコード文字列を返すように定義します。
        """
        return self.short_text()
    
    def short_text(self):
        """
        つぶやき(Note.text)の頭から30文字分を返します
        """
        return self.text[:30]
