# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'HackaCity.partners'
        db.delete_column(u'hackacities_hackacity', 'partners_id')

        # Deleting field 'HackaCity.sponsors'
        db.delete_column(u'hackacities_hackacity', 'sponsors_id')

        # Deleting field 'HackaCity.communities'
        db.delete_column(u'hackacities_hackacity', 'communities_id')

        # Adding field 'HackaContainer.hackacity'
        db.add_column(u'hackacities_hackacontainer', 'hackacity',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['hackacities.HackaCity'], null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'HackaCity.partners'
        db.add_column(u'hackacities_hackacity', 'partners',
                      self.gf('django.db.models.fields.related.ForeignKey')(related_name='partner_of', null=True, to=orm['hackacities.HackaContainer'], blank=True),
                      keep_default=False)

        # Adding field 'HackaCity.sponsors'
        db.add_column(u'hackacities_hackacity', 'sponsors',
                      self.gf('django.db.models.fields.related.ForeignKey')(related_name='sponsor_of', null=True, to=orm['hackacities.HackaContainer'], blank=True),
                      keep_default=False)

        # Adding field 'HackaCity.communities'
        db.add_column(u'hackacities_hackacity', 'communities',
                      self.gf('django.db.models.fields.related.ForeignKey')(related_name='community_of', null=True, to=orm['hackacities.HackaContainer'], blank=True),
                      keep_default=False)

        # Deleting field 'HackaContainer.hackacity'
        db.delete_column(u'hackacities_hackacontainer', 'hackacity_id')


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
        u'hackacities.cities': {
            'Meta': {'object_name': 'Cities'},
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['hackacities.Countries']"}),
            'country_code': ('django.db.models.fields.CharField', [], {'max_length': '3L'}),
            'district': ('django.db.models.fields.CharField', [], {'max_length': '20L'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '35L'}),
            'population': ('django.db.models.fields.IntegerField', [], {})
        },
        u'hackacities.countries': {
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
        u'hackacities.hackacity': {
            'Meta': {'object_name': 'HackaCity'},
            'about': ('django.db.models.fields.TextField', [], {}),
            'city': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['hackacities.Cities']", 'unique': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image_about': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'image_divider_1': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'image_divider_2': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'image_divider_3': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'image_divider_4': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'image_home': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'image_logo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'lead': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'lead_of'", 'to': u"orm['auth.User']"}),
            'member': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'member_of'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['auth.User']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'short_description': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'team': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'team_of'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['auth.User']"})
        },
        u'hackacities.hackacontainer': {
            'Meta': {'object_name': 'HackaContainer'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'hackacity': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['hackacities.HackaCity']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'type': ('django.db.models.fields.CharField', [], {'default': "'C'", 'max_length': '1'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        u'hackacities.languages': {
            'Meta': {'object_name': 'Languages'},
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['hackacities.Countries']"}),
            'country_code': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'official': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'percentage': ('django.db.models.fields.FloatField', [], {})
        }
    }

    complete_apps = ['hackacities']