# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Event'
#        db.create_table(u'hackaglobal_event', (
#            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
#            ('creator', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
#            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
#            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
#            ('address', self.gf('django.db.models.fields.CharField')(max_length=100)),
#            ('country', self.gf('django.db.models.fields.CharField')(max_length=50)),
#            ('city', self.gf('django.db.models.fields.CharField')(max_length=50)),
#            ('zip', self.gf('django.db.models.fields.CharField')(max_length=10)),
#            ('latitude', self.gf('django.db.models.fields.FloatField')()),
#            ('longitude', self.gf('django.db.models.fields.FloatField')()),
#            ('website', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
#            ('start', self.gf('django.db.models.fields.DateTimeField')()),
#            ('end', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
#            ('tags', self.gf('hackaglobal.models.Tag')()),
#        ))
        db.send_create_signal(u'hackaglobal', ['Event'])

        # Adding model 'Attendee'
#        db.create_table(u'hackaglobal_attendee', (
#            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
#            ('attendee', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
#            ('type', self.gf('django.db.models.fields.CharField')(default='A', max_length=1)),
#            ('event', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['hackaglobal.Event'])),
#        ))
        db.send_create_signal(u'hackaglobal', ['Attendee'])

        # Adding model 'Staff'
#        db.create_table(u'hackaglobal_staff', (
#            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
#            ('staff', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True, blank=True)),
#            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
#            ('description', self.gf('django.db.models.fields.TextField')()),
#            ('url', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
#            ('imgurl', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
#            ('type', self.gf('django.db.models.fields.CharField')(default='M', max_length=1)),
#            ('event', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['hackaglobal.Event'])),
#        ))
        db.send_create_signal(u'hackaglobal', ['Staff'])


    def backwards(self, orm):
        # Deleting model 'Event'
        db.delete_table(u'hackaglobal_event')

        # Deleting model 'Attendee'
        db.delete_table(u'hackaglobal_attendee')

        # Deleting model 'Staff'
        db.delete_table(u'hackaglobal_staff')


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
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'hackaglobal.attendee': {
            'Meta': {'object_name': 'Attendee'},
            'attendee': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'event': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['hackaglobal.Event']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'default': "'A'", 'max_length': '1'})
        },
        u'hackaglobal.event': {
            'Meta': {'object_name': 'Event'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'end': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.FloatField', [], {}),
            'longitude': ('django.db.models.fields.FloatField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'start': ('django.db.models.fields.DateTimeField', [], {}),
            'tags': ('hackaglobal.models.Tag', [], {}),
            'website': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'zip': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        },
        u'hackaglobal.staff': {
            'Meta': {'object_name': 'Staff'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'event': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['hackaglobal.Event']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imgurl': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'staff': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'default': "'M'", 'max_length': '1'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['hackaglobal']