# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Bar.address'
        db.add_column('mainapp_bar', 'address', self.gf('django.db.models.fields.CharField')(max_length=32, null=True, blank=True), keep_default=False)

        # Adding field 'Bar.phone'
        db.add_column('mainapp_bar', 'phone', self.gf('django.db.models.fields.CharField')(max_length=32, null=True, blank=True), keep_default=False)

        # Adding field 'Bar.website'
        db.add_column('mainapp_bar', 'website', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True), keep_default=False)

        # Adding field 'Bar.email'
        db.add_column('mainapp_bar', 'email', self.gf('django.db.models.fields.EmailField')(max_length=75, null=True, blank=True), keep_default=False)

        # Adding field 'Bar.facebook_page'
        db.add_column('mainapp_bar', 'facebook_page', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True), keep_default=False)

        # Adding field 'Bar.description'
        db.add_column('mainapp_bar', 'description', self.gf('django.db.models.fields.TextField')(null=True, blank=True), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Bar.address'
        db.delete_column('mainapp_bar', 'address')

        # Deleting field 'Bar.phone'
        db.delete_column('mainapp_bar', 'phone')

        # Deleting field 'Bar.website'
        db.delete_column('mainapp_bar', 'website')

        # Deleting field 'Bar.email'
        db.delete_column('mainapp_bar', 'email')

        # Deleting field 'Bar.facebook_page'
        db.delete_column('mainapp_bar', 'facebook_page')

        # Deleting field 'Bar.description'
        db.delete_column('mainapp_bar', 'description')


    models = {
        'mainapp.bar': {
            'Meta': {'object_name': 'Bar'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '32', 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'facebook_page': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '32', 'null': 'True', 'blank': 'True'}),
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
