# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Basic_Time_Series_Data.create_date'
        db.add_column(u'django_time_series_basic_time_series_data', 'create_date',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.datetime(2013, 9, 10, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'Basic_Time_Series_Data.last_update'
        db.add_column(u'django_time_series_basic_time_series_data', 'last_update',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now=True, default=datetime.datetime(2013, 9, 10, 0, 0), blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Basic_Time_Series_Data.create_date'
        db.delete_column(u'django_time_series_basic_time_series_data', 'create_date')

        # Deleting field 'Basic_Time_Series_Data.last_update'
        db.delete_column(u'django_time_series_basic_time_series_data', 'last_update')


    models = {
        u'django_time_series.basic_time_series_data': {
            'Meta': {'object_name': 'Basic_Time_Series_Data'},
            'aggregate_index': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'create_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'end_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'filter_1': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'filter_10': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'filter_2': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'filter_3': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'filter_4': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'filter_5': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'filter_6': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'filter_7': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'filter_8': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'filter_9': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'filter_type': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'filter_value': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_update': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'match_count': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'match_count_1': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'match_count_10': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'match_count_2': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'match_count_3': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'match_count_4': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'match_count_5': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'match_count_6': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'match_count_7': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'match_count_8': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'match_count_9': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'match_value': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'original_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'original_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'start_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'time_period': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['django_time_series.Time_Period']", 'null': 'True', 'blank': 'True'}),
            'time_period_category': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'time_period_index': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'time_period_label': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'time_period_type': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        u'django_time_series.time_period': {
            'Meta': {'object_name': 'Time_Period'},
            'aggregate_index': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'end_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'project_category': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'project_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'start_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'time_period_category': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'time_period_index': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'time_period_label': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'time_period_type': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['django_time_series']