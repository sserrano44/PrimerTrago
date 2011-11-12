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

        # Adding model 'SubNeighborhood'
        db.create_table('mainapp_subneighborhood', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('city', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mainapp.City'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=32)),
        ))
        db.send_create_signal('mainapp', ['SubNeighborhood'])

        # Adding model 'Bar'
        db.create_table('mainapp_bar', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('neighborhood', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mainapp.Neighborhood'])),
            ('sub_neighborhood', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mainapp.SubNeighborhood'], null=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=32, null=True, blank=True)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=32, null=True, blank=True)),
            ('website', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75, null=True, blank=True)),
            ('facebook_page', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('image', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal('mainapp', ['Bar'])

        # Adding model 'HappyHour'
        db.create_table('mainapp_happyhour', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('bar', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mainapp.Bar'])),
            ('monday', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('tuesday', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('wednesday', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('thursday', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('friday', self.gf('django.db.models.fields.BooleanField')(default=False)),
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

        # Deleting model 'SubNeighborhood'
        db.delete_table('mainapp_subneighborhood')

        # Deleting model 'Bar'
        db.delete_table('mainapp_bar')

        # Deleting model 'HappyHour'
        db.delete_table('mainapp_happyhour')


    models = {
        'mainapp.bar': {
            'Meta': {'object_name': 'Bar'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '32', 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'facebook_page': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'neighborhood': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mainapp.Neighborhood']"}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '32', 'null': 'True', 'blank': 'True'}),
            'sub_neighborhood': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mainapp.SubNeighborhood']", 'null': 'True', 'blank': 'True'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        'mainapp.city': {
            'Meta': {'object_name': 'City'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '32'})
        },
        'mainapp.happyhour': {
            'Meta': {'object_name': 'HappyHour'},
            'bar': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mainapp.Bar']"}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'friday': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'hour_end': ('django.db.models.fields.TimeField', [], {}),
            'hour_start': ('django.db.models.fields.TimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'monday': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'thursday': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'tuesday': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'wednesday': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'mainapp.neighborhood': {
            'Meta': {'object_name': 'Neighborhood'},
            'city': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mainapp.City']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '32'})
        },
        'mainapp.subneighborhood': {
            'Meta': {'object_name': 'SubNeighborhood'},
            'city': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mainapp.City']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '32'})
        }
    }

    complete_apps = ['mainapp']
