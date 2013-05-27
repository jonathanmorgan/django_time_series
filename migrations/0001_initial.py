# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Time_Period'
        db.create_table(u'django_time_series_time_period', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('start_date', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('end_date', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('time_period_type', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('time_period_index', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('time_period_category', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('time_period_label', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('aggregate_index', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('project_name', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('project_category', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
        ))
        db.send_create_signal(u'django_time_series', ['Time_Period'])

        # Adding model 'Basic_Time_Series_Data'
        db.create_table(u'django_time_series_basic_time_series_data', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('start_date', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('end_date', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('time_period', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['django_time_series.Time_Period'], null=True, blank=True)),
            ('time_period_type', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('time_period_index', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('time_period_category', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('time_period_label', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('aggregate_index', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('original_id', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('original_name', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('filter_type', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('filter_value', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('match_value', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('match_count', self.gf('django.db.models.fields.IntegerField')(default=0, null=True, blank=True)),
            ('filter_1', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('match_count_1', self.gf('django.db.models.fields.IntegerField')(default=0, null=True, blank=True)),
            ('filter_2', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('match_count_2', self.gf('django.db.models.fields.IntegerField')(default=0, null=True, blank=True)),
            ('filter_3', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('match_count_3', self.gf('django.db.models.fields.IntegerField')(default=0, null=True, blank=True)),
            ('filter_4', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('match_count_4', self.gf('django.db.models.fields.IntegerField')(default=0, null=True, blank=True)),
            ('filter_5', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('match_count_5', self.gf('django.db.models.fields.IntegerField')(default=0, null=True, blank=True)),
            ('filter_6', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('match_count_6', self.gf('django.db.models.fields.IntegerField')(default=0, null=True, blank=True)),
            ('filter_7', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('match_count_7', self.gf('django.db.models.fields.IntegerField')(default=0, null=True, blank=True)),
            ('filter_8', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('match_count_8', self.gf('django.db.models.fields.IntegerField')(default=0, null=True, blank=True)),
            ('filter_9', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('match_count_9', self.gf('django.db.models.fields.IntegerField')(default=0, null=True, blank=True)),
            ('filter_10', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('match_count_10', self.gf('django.db.models.fields.IntegerField')(default=0, null=True, blank=True)),
        ))
        db.send_create_signal(u'django_time_series', ['Basic_Time_Series_Data'])


    def backwards(self, orm):
        # Deleting model 'Time_Period'
        db.delete_table(u'django_time_series_time_period')

        # Deleting model 'Basic_Time_Series_Data'
        db.delete_table(u'django_time_series_basic_time_series_data')


    models = {
        u'django_time_series.basic_time_series_data': {
            'Meta': {'object_name': 'Basic_Time_Series_Data'},
            'aggregate_index': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
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