# -*- coding: utf-8 -*-
"""
ビュー関数を定義するファイルです。
"""
# Create your views here.
#from snsuser.models import SnsUser
from microblog.models import Note
from forms import NoteForm
from django.views.generic.list_detail import object_list
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse

#def user_view(request, username):
#    user = SnsUser.objects.filter(username=username)
#    friends = [u.id for u in user.friends] + [user.id]
#    query_set = Node.objects.filter(author__in=friends).order_by('-id')
#    return object_list(request, queryset=query_set, paginate_by=20, allow_empty=True,
#                       extra_context=dict(friends=friends))

#ログインしていない場合にはログイン画面へ飛ばすデコレータです
@login_required
def post_note(request):
    """
    つぶやき投稿用のビュー関数です。このままのコードで、GETメソッドで呼び出すとエラーが発生します（formを定義せずに利用することになるため）
    """
    if request.method == 'POST':
        #ユーザをあらかじめ設定したNoteのインスタンスを作成します（まだデータベースに登録はされません）
        #request.userは入力値ではなくログイン情報からユーザを参照する方法です
        note = Note(author_id=request.user.id)
        #NoteFormはNoteモデルクラスから生成される検証フォームですが、ユーザを入力値として受け取らないように定義されています。
        #そのため、デフォルト値としてユーザをあらかじめ設定したNoteのインスタンスをinstanceとして設定しています。
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            #入力検証に問題がなければ、入力フォームから直にNoteデータをデータベースに登録します。
            form.save()
            #データを登録後、urls.pyからmicroblog_homeという名前が設定されているURLConfを探しだし、URL化してリダイレクトしています
            return HttpResponseRedirect(reverse('microblog_home'))
    else:
      form = NoteForm() #GETメソッドで呼ばれた場合のためにformを空のNoteFormで初期化
    return render_to_response('microblog/note_list.html', context_instance=RequestContext(request, {'form': form}))
