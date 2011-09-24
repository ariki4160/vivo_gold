# -*- coding: utf-8 -*-
"""
自動管理インターフェースでどのモデルを管理対象にするかを指定するファイルです。
インストールされたアプリケーションのアプリケーションディレクトリにadmin.pyがあれば、djangoが起動時に自動で読み込みます。
"""
from django.contrib import admin
from models import Note

class NoteOptions(admin.ModelAdmin):
    """
    django.contrib.admin.ModelAdminを継承し、設定を行います。
    クラス名の命名規則はありませんが、どのモデル用のものなのかわかりやすい名前にすると良いでしょう。
    設定の詳細は日本語ドキュメントを参照してください。 http://djangoproject.jp/doc/ja/1.0/ref/contrib/admin.html#ref-contrib-admin
    """
    #モデル毎のデータ一覧で表示する項目を指定しています
    list_display = ('author', 'short_text',)
    pass

#自動管理インターフェースに、モデルと設定のクラスを登録します。
admin.site.register(Note, NoteOptions)
