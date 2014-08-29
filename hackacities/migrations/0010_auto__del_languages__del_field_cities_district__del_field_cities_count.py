# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Languages'
        db.delete_table(u'hackacities_languages')

        # Deleting field 'Cities.district'
        db.delete_column(u'hackacities_cities', 'district')

        # Deleting field 'Cities.country_code'
        db.delete_column(u'hackacities_cities', 'country_code')

        # Deleting field 'Cities.population'
        db.delete_column(u'hackacities_cities', 'population')


        # Changing field 'Cities.id'
        db.alter_column(u'hackacities_cities', u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True))
        # Deleting field 'Countries.life_expectancy'
        db.delete_column(u'hackacities_countries', 'life_expectancy')

        # Deleting field 'Countries.code2'
        db.delete_column(u'hackacities_countries', 'code2')

        # Deleting field 'Countries.region'
        db.delete_column(u'hackacities_countries', 'region')

        # Deleting field 'Countries.local_name'
        db.delete_column(u'hackacities_countries', 'local_name')

        # Deleting field 'Countries.gnp'
        db.delete_column(u'hackacities_countries', 'gnp')

        # Deleting field 'Countries.head_of_state'
        db.delete_column(u'hackacities_countries', 'head_of_state')

        # Deleting field 'Countries.gnp_old'
        db.delete_column(u'hackacities_countries', 'gnp_old')

        # Deleting field 'Countries.government_form'
        db.delete_column(u'hackacities_countries', 'government_form')

        # Deleting field 'Countries.capital'
        db.delete_column(u'hackacities_countries', 'capital')

        # Deleting field 'Countries.surface_area'
        db.delete_column(u'hackacities_countries', 'surface_area')

        # Deleting field 'Countries.independence_year'
        db.delete_column(u'hackacities_countries', 'independence_year')

        # Deleting field 'Countries.population'
        db.delete_column(u'hackacities_countries', 'population')


    def backwards(self, orm):
        # Adding model 'Languages'
        db.create_table(u'hackacities_languages', (
            ('language', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('country', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['hackacities.Countries'])),
            ('official', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('country_code', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('percentage', self.gf('django.db.models.fields.FloatField')()),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'hackacities', ['Languages'])

        # Adding field 'Cities.district'
        db.add_column(u'hackacities_cities', 'district',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=20L),
                      keep_default=False)

        # Adding field 'Cities.country_code'
        db.add_column(u'hackacities_cities', 'country_code',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=3L),
                      keep_default=False)

        # Adding field 'Cities.population'
        db.add_column(u'hackacities_cities', 'population',
                      self.gf('django.db.models.fields.IntegerField')(default=''),
                      keep_default=False)


        # Changing field 'Cities.id'
        db.alter_column(u'hackacities_cities', 'id', self.gf('django.db.models.fields.IntegerField')(primary_key=True))
        # Adding field 'Countries.life_expectancy'
        db.add_column(u'hackacities_countries', 'life_expectancy',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Countries.code2'
        db.add_column(u'hackacities_countries', 'code2',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=2L),
                      keep_default=False)

        # Adding field 'Countries.region'
        db.add_column(u'hackacities_countries', 'region',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=26L),
                      keep_default=False)

        # Adding field 'Countries.local_name'
        db.add_column(u'hackacities_countries', 'local_name',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=45L),
                      keep_default=False)

        # Adding field 'Countries.gnp'
        db.add_column(u'hackacities_countries', 'gnp',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Countries.head_of_state'
        db.add_column(u'hackacities_countries', 'head_of_state',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=60L, blank=True),
                      keep_default=False)

        # Adding field 'Countries.gnp_old'
        db.add_column(u'hackacities_countries', 'gnp_old',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Countries.government_form'
        db.add_column(u'hackacities_countries', 'government_form',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=45L),
                      keep_default=False)

        # Adding field 'Countries.capital'
        db.add_column(u'hackacities_countries', 'capital',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Countries.surface_area'
        db.add_column(u'hackacities_countries', 'surface_area',
                      self.gf('django.db.models.fields.FloatField')(default=''),
                      keep_default=False)

        # Adding field 'Countries.independence_year'
        db.add_column(u'hackacities_countries', 'independence_year',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Countries.population'
        db.add_column(u'hackacities_countries', 'population',
                      self.gf('django.db.models.fields.IntegerField')(default=''),
                      keep_default=False)


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
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '35L'})
        },
        u'hackacities.countries': {
            'Meta': {'object_name': 'Countries'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '3L', 'primary_key': 'True'}),
            'continent': ('django.db.models.fields.CharField', [], {'max_length': '13L'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '52L'})
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
            'type': ('django.db.models.fields.CharField', [], {'default': "'S1'", 'max_length': '2'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['hackacities']