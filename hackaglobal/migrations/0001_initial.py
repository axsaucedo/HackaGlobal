# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Event'
        db.create_table(u'hackaglobal_event', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('hackacity', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['hackaglobal.HackaCity'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('zip', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
            ('latitude', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('longitude', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('website', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('start', self.gf('django.db.models.fields.DateTimeField')()),
            ('end', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'hackaglobal', ['Event'])

        # Adding model 'Attendee'
        db.create_table(u'hackaglobal_attendee', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('attendee', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('type', self.gf('django.db.models.fields.CharField')(default='A', max_length=1)),
            ('event', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['hackaglobal.Event'])),
        ))
        db.send_create_signal(u'hackaglobal', ['Attendee'])

        # Adding model 'Staff'
        db.create_table(u'hackaglobal_staff', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('staff', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('imgurl', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('type', self.gf('django.db.models.fields.CharField')(default='M', max_length=1)),
            ('event', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['hackaglobal.Event'])),
        ))
        db.send_create_signal(u'hackaglobal', ['Staff'])

        # Adding model 'HackaContainer'
        db.create_table(u'hackaglobal_hackacontainer', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('photo', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('type', self.gf('django.db.models.fields.CharField')(default='C', max_length=1)),
        ))
        db.send_create_signal(u'hackaglobal', ['HackaContainer'])

        # Adding model 'HackaCity'
        db.create_table(u'hackaglobal_hackacity', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('lead', self.gf('django.db.models.fields.related.ForeignKey')(related_name='lead_of', to=orm['auth.User'])),
            ('photo', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('short_description', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('about', self.gf('django.db.models.fields.TextField')()),
            ('city', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['hackaglobal.Cities'], unique=True)),
            ('sponsors', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='sponsor_of', null=True, to=orm['hackaglobal.HackaContainer'])),
            ('communities', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='community_of', null=True, to=orm['hackaglobal.HackaContainer'])),
            ('partners', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='partner_of', null=True, to=orm['hackaglobal.HackaContainer'])),
        ))
        db.send_create_signal(u'hackaglobal', ['HackaCity'])

        # Adding M2M table for field team on 'HackaCity'
        m2m_table_name = db.shorten_name(u'hackaglobal_hackacity_team')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('hackacity', models.ForeignKey(orm[u'hackaglobal.hackacity'], null=False)),
            ('user', models.ForeignKey(orm[u'auth.user'], null=False))
        ))
        db.create_unique(m2m_table_name, ['hackacity_id', 'user_id'])

        # Adding M2M table for field member on 'HackaCity'
        m2m_table_name = db.shorten_name(u'hackaglobal_hackacity_member')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('hackacity', models.ForeignKey(orm[u'hackaglobal.hackacity'], null=False)),
            ('user', models.ForeignKey(orm[u'auth.user'], null=False))
        ))
        db.create_unique(m2m_table_name, ['hackacity_id', 'user_id'])

        # Adding model 'Cities'
        db.create_table(u'hackaglobal_cities', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=35L)),
            ('country_code', self.gf('django.db.models.fields.CharField')(max_length=3L)),
            ('district', self.gf('django.db.models.fields.CharField')(max_length=20L)),
            ('population', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'hackaglobal', ['Cities'])

        # Adding model 'Countries'
        db.create_table(u'hackaglobal_countries', (
            ('code', self.gf('django.db.models.fields.CharField')(max_length=3L, primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=52L)),
            ('continent', self.gf('django.db.models.fields.CharField')(max_length=13L)),
            ('region', self.gf('django.db.models.fields.CharField')(max_length=26L)),
            ('surface_area', self.gf('django.db.models.fields.FloatField')()),
            ('independence_year', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('population', self.gf('django.db.models.fields.IntegerField')()),
            ('life_expectancy', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('gnp', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('gnp_old', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('local_name', self.gf('django.db.models.fields.CharField')(max_length=45L)),
            ('government_form', self.gf('django.db.models.fields.CharField')(max_length=45L)),
            ('head_of_state', self.gf('django.db.models.fields.CharField')(max_length=60L, blank=True)),
            ('capital', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('code2', self.gf('django.db.models.fields.CharField')(max_length=2L)),
        ))
        db.send_create_signal(u'hackaglobal', ['Countries'])

        # Adding model 'Languages'
        db.create_table(u'hackaglobal_languages', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('country_code', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('language', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('official', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('percentage', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal(u'hackaglobal', ['Languages'])


    def backwards(self, orm):
        # Deleting model 'Event'
        db.delete_table(u'hackaglobal_event')

        # Deleting model 'Attendee'
        db.delete_table(u'hackaglobal_attendee')

        # Deleting model 'Staff'
        db.delete_table(u'hackaglobal_staff')

        # Deleting model 'HackaContainer'
        db.delete_table(u'hackaglobal_hackacontainer')

        # Deleting model 'HackaCity'
        db.delete_table(u'hackaglobal_hackacity')

        # Removing M2M table for field team on 'HackaCity'
        db.delete_table(db.shorten_name(u'hackaglobal_hackacity_team'))

        # Removing M2M table for field member on 'HackaCity'
        db.delete_table(db.shorten_name(u'hackaglobal_hackacity_member'))

        # Deleting model 'Cities'
        db.delete_table(u'hackaglobal_cities')

        # Deleting model 'Countries'
        db.delete_table(u'hackaglobal_countries')

        # Deleting model 'Languages'
        db.delete_table(u'hackaglobal_languages')


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
        u'hackaglobal.cities': {
            'Meta': {'object_name': 'Cities'},
            'country_code': ('django.db.models.fields.CharField', [], {'max_length': '3L'}),
            'district': ('django.db.models.fields.CharField', [], {'max_length': '20L'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '35L'}),
            'population': ('django.db.models.fields.IntegerField', [], {})
        },
        u'hackaglobal.countries': {
            'Meta': {'object_name': 'Countries'},
            'capital': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'code': ('django.db.models.fields.CharField', [], {'max_length': '3L', 'primary_key': 'True'}),
            'code2': ('django.db.models.fields.CharField', [], {'max_length': '2L'}),
            'continent': ('django.db.models.fields.CharField', [], {'max_length': '13L'}),
            'gnp': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'gnp_old': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'government_form': ('django.db.models.fields.CharField', [], {'max_length': '45L'}),
            'head_of_state': ('django.db.models.fields.CharField', [], {'max_length': '60L', 'blank': 'True'}),
            'independence_year': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'life_expectancy': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'local_name': ('django.db.models.fields.CharField', [], {'max_length': '45L'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '52L'}),
            'population': ('django.db.models.fields.IntegerField', [], {}),
            'region': ('django.db.models.fields.CharField', [], {'max_length': '26L'}),
            'surface_area': ('django.db.models.fields.FloatField', [], {})
        },
        u'hackaglobal.event': {
            'Meta': {'object_name': 'Event'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'end': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'hackacity': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['hackaglobal.HackaCity']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'longitude': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'start': ('django.db.models.fields.DateTimeField', [], {}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'zip': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'})
        },
        u'hackaglobal.hackacity': {
            'Meta': {'object_name': 'HackaCity'},
            'about': ('django.db.models.fields.TextField', [], {}),
            'city': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['hackaglobal.Cities']", 'unique': 'True'}),
            'communities': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'community_of'", 'null': 'True', 'to': u"orm['hackaglobal.HackaContainer']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lead': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'lead_of'", 'to': u"orm['auth.User']"}),
            'member': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'member_of'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['auth.User']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'partners': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'partner_of'", 'null': 'True', 'to': u"orm['hackaglobal.HackaContainer']"}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'short_description': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'sponsors': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'sponsor_of'", 'null': 'True', 'to': u"orm['hackaglobal.HackaContainer']"}),
            'team': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'team_of'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['auth.User']"})
        },
        u'hackaglobal.hackacontainer': {
            'Meta': {'object_name': 'HackaContainer'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'type': ('django.db.models.fields.CharField', [], {'default': "'C'", 'max_length': '1'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        u'hackaglobal.languages': {
            'Meta': {'object_name': 'Languages'},
            'country_code': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'official': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'percentage': ('django.db.models.fields.FloatField', [], {})
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
        },
        u'taggit.tag': {
            'Meta': {'object_name': 'Tag'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '100'})
        },
        u'taggit.taggeditem': {
            'Meta': {'object_name': 'TaggedItem'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'taggit_taggeditem_tagged_items'", 'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'tag': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'taggit_taggeditem_items'", 'to': u"orm['taggit.Tag']"})
        }
    }

    complete_apps = ['hackaglobal']