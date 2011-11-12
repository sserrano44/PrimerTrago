# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'City'
        db.create_table('mainapp_city', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=32)),
        ))
        db.send_create_signal('mainapp', ['City'])

        # Adding model 'Neighborhood'
        db.create_table('mainapp_neighborhood', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('city', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mainapp.City'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=32)),
        ))
        db.send_create_signal('mainapp', ['Neighborhood'])

        # Adding model 'Bar'
        db.create_table('mainapp_bar', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=32)),
        ))
        db.send_create_signal('mainapp', ['Bar'])

        # Adding model 'HappyHour'
        db.create_table('mainapp_happyhour', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('bar', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mainapp.Bar'])),
            ('day', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('hour_start', self.gf('django.db.models.fields.TimeField')()),
            ('hour_end', self.gf('django.db.models.fields.TimeField')()),
            ('description', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('mainapp', ['HappyHour'])


    def backwards(self, orm):
        
        # Deleting model 'City'
        db.delete_table('mainapp_city')

        # Deleting model 'Neighborhood'
        db.delete_table('mainapp_neighborhood')

        # Deleting model 'Bar'
        db.delete_table('mainapp_bar')

        # Deleting model 'HappyHour'
        db.delete_table('mainapp_happyhour')


    models = {
        'mainapp.bar': {
            'Meta': {'object_name': 'Bar'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '32'})
        },
        'mainapp.city': {
            'Meta': {'object_name': 'City'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '32'})
        },
        'mainapp.happyhour': {
            'Meta': {'object_name': 'HappyHour'},
            'bar': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mainapp.Bar']"}),
            'day': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'hour_end': ('django.db.models.fields.TimeField', [], {}),
            'hour_start': ('django.db.models.fields.TimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'mainapp.neighborhood': {
            'Meta': {'object_name': 'Neighborhood'},
            'city': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mainapp.City']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '32'})
        }
    }

    complete_apps = ['mainapp']
