# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Survey'
        db.create_table(u'surveys_survey', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('email_subject', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('email_content', self.gf('h4il.html.HTMLField')(null=True, blank=True)),
            ('q13e', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'surveys', ['Survey'])

        # Adding model 'SurveyAnswer'
        db.create_table(u'surveys_surveyanswer', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(default='xsatcosivsujftotqskbiarjmciyfkjjdmtgruit', max_length=50)),
            ('survey', self.gf('django.db.models.fields.related.ForeignKey')(related_name='answers', to=orm['surveys.Survey'])),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='survey_answers', to=orm['users.HackitaUser'])),
            ('answered_at', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('data', self.gf('django.db.models.fields.TextField')(default='{}', null=True, blank=True)),
        ))
        db.send_create_signal(u'surveys', ['SurveyAnswer'])

        # Adding unique constraint on 'SurveyAnswer', fields ['survey', 'user']
        db.create_unique(u'surveys_surveyanswer', ['survey_id', 'user_id'])


    def backwards(self, orm):
        # Removing unique constraint on 'SurveyAnswer', fields ['survey', 'user']
        db.delete_unique(u'surveys_surveyanswer', ['survey_id', 'user_id'])

        # Deleting model 'Survey'
        db.delete_table(u'surveys_survey')

        # Deleting model 'SurveyAnswer'
        db.delete_table(u'surveys_surveyanswer')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'surveys.survey': {
            'Meta': {'object_name': 'Survey'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'email_content': ('h4il.html.HTMLField', [], {'null': 'True', 'blank': 'True'}),
            'email_subject': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'q13e': ('django.db.models.fields.TextField', [], {})
        },
        u'surveys.surveyanswer': {
            'Meta': {'unique_together': "(('survey', 'user'),)", 'object_name': 'SurveyAnswer'},
            'answered_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'data': ('django.db.models.fields.TextField', [], {'default': "'{}'", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'default': "'qnvoiwxlxehtrvxsttlddnnoxaywifhlusmkdnuw'", 'max_length': '50'}),
            'survey': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'answers'", 'to': u"orm['surveys.Survey']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'survey_answers'", 'to': u"orm['users.HackitaUser']"})
        },
        u'users.hackitauser': {
            'Meta': {'object_name': 'HackitaUser'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'english_first_name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'english_last_name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'forms_filled': ('django.db.models.fields.IntegerField', [], {'default': '0', 'db_index': 'True'}),
            'gender': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'hebrew_first_name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'hebrew_last_name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_form_filled': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        }
    }

    complete_apps = ['surveys']