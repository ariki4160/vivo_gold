# -*- coding: utf-8 -*-
"""
入力値検証用のフォームを定義するファイルです。ファイル名に規則はありませんが、慣例でforms.pyに記述します。
"""
from django.forms import ModelForm
from models import Note

class NoteForm(ModelForm):
    """
    django.forms.ModelFormを継承したクラスは、モデルを元に自動で入力フォームを作成したい場合に利用します。
    """
    class Meta:
        #この検証フォームはNoteモデルをベースに自動で生成することを宣言しています
        model = Note
        #modelに指定されているモデルのフィールドのうち、
        #authorというフィールドについては検証対象から外す（HTMLのinput要素も出さない）ことを宣言しています。
        exclude = ('author',)
