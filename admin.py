from django.contrib import admin
from iSkyLIMS_core.models import *

class LaboratoryAdmin (admin.ModelAdmin):
    list_display = ['labName' , 'labCoding' , 'labLocation' ]

class MoleculeTypeAdmin( admin.ModelAdmin):
    list_display = ('moleculeType',)

class ProtocolsAdmin(admin.ModelAdmin):
    list_display = ('type', 'name', 'description')

class ProtocolTypeAdmin( admin.ModelAdmin):
    list_display = ('molecule','protocol_type')


class ProtocolParametersAdmin (admin.ModelAdmin):
    list_display = ('protocol_id', 'parameterName', 'parameterOrder', 'parameterUsed', 'parameterMinValue', 'parameterMaxValue', 'parameterDescription')

class SampleTypeAdmin(admin.ModelAdmin):
    list_display = ('sampleType',)




class SpeciesAdmin (admin.ModelAdmin):
    list_display= ('spicesName', 'refGenomeName', 'refGenomeSize' , 'refGenomeID' )

class StatesForMoleculeAdmin (admin.ModelAdmin):
    list_display = ('moleculeStateName',)

class StatesForSampleAdmin (admin.ModelAdmin):
    list_display = ('sampleStateName',)

admin.site.register(Laboratory, LaboratoryAdmin)

admin.site.register(MoleculeType,MoleculeTypeAdmin)
admin.site.register(ProtocolType,ProtocolTypeAdmin)
admin.site.register(Protocols,ProtocolsAdmin)
admin.site.register(ProtocolParameters,ProtocolParametersAdmin)
admin.site.register(SampleType, SampleTypeAdmin)
admin.site.register(Species, SpeciesAdmin)
admin.site.register(StatesForMolecule, StatesForMoleculeAdmin)
admin.site.register(StatesForSample, StatesForSampleAdmin)
