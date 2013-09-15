from __future__ import unicode_literals

'''
Copyright 2012, 2013 Jonathan Morgan

This file is part of http://github.com/jonathanmorgan/python_utilities.

python_utilities is free software: you can redistribute it and/or modify
it under the terms of the GNU Lesser General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

python_utilities is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU Lesser General Public License
along with http://github.com/jonathanmorgan/python_utilities.  If not, see
<http://www.gnu.org/licenses/>.
'''

'''
Contains django abstract model class for creating and storing time-series data
   in a database.  For now, will have an abstract class and then a concrete
   implementation of it that can be used for generic time-series data. If you
   are serious about this, you should extend the abstract class and then add on
   the different pieces of data you want to capture per time slice in a child
   class.
'''

# imports
import datetime

# django
from django.db import models
import django.utils.encoding
from django.utils.encoding import python_2_unicode_compatible

# python_utilities
from python_utilities.exceptions.exception_helper import ExceptionHelper

@python_2_unicode_compatible
class Time_Period( models.Model ):

    #============================================================================
    # constants-ish
    #============================================================================

    # time period types
    TIME_PERIOD_HOURLY = "hourly"

    #============================================================================
    # Django model fields
    #============================================================================
    
    start_date = models.DateTimeField( null = True, blank = True )
    end_date = models.DateTimeField( null = True, blank = True )
    time_period_type = models.CharField( max_length = 255, null = True, blank = True ) # - hourly, by minute, etc.
    time_period_index = models.IntegerField( null = True, blank = True )
    time_period_category = models.CharField( max_length = 255, null = True, blank = True )
    time_period_label = models.CharField( max_length = 255, null = True, blank = True ) # could give each hour, etc. a separate identifier "start+1", "start+2", etc. - not naming _id to start, so you leave room for this to be a separate table.
    aggregate_index = models.IntegerField( null = True, blank = True ) # a separate index you can use to keep track of overall order within a time-series that you separate out into multiple types - "before" and "after", for example - time_period_index can be counter within before or after, aggregate index can be unique through both before and after.
    project_name = models.CharField( max_length = 255, null = True, blank = True )
    project_category = models.CharField( max_length = 255, null = True, blank = True )

    #============================================================================
    # Instance variables
    #============================================================================
    
    
    #============================================================================
    # meta class
    #============================================================================

    # meta class so we know this is an abstract class.
    #class Meta:
    #    abstract = True

    # add string output method.
    

    #============================================================================
    # class methods
    #============================================================================


    #============================================================================
    # instance methods
    #============================================================================


    def __str__(self):
        
        # return reference
        string_OUT = ""
        
        # id?
        if ( ( self.id ) and ( self.id != None ) and ( self.id > 0 ) ):
        
            string_OUT += str( self.id )
        
        #-- END check to see if id --#
        
        # start date?
        if( self.start_date ):
        
            string_OUT += " - " + str( self.start_date )
        
        #-- END check to see if start_date --#

        # end date?
        if( self.end_date ):
        
            string_OUT += " --> " + str( self.end_date )
        
        #-- END check to see if end_date --#
        
        # category.
        if ( self.time_period_category ):
        
            string_OUT += " - " + self.time_period_category
        
        #-- END check to see if time_period_category --#

        # label.
        if ( self.time_period_label ):
        
            string_OUT += " - " + self.time_period_label
        
        #-- END check to see if time_period_label --#

        return string_OUT

    #-- END __str__() method --#


#-- END abstract class AbstractTimeSeriesData --#


@python_2_unicode_compatible
class AbstractTimeSeriesDataModel( models.Model ):

    #============================================================================
    # constants-ish
    #============================================================================

    # time period types
    TIME_PERIOD_HOURLY = "hourly"

    #============================================================================
    # Django model fields
    #============================================================================
    
    start_date = models.DateTimeField( null = True, blank = True )
    end_date = models.DateTimeField( null = True, blank = True )
    time_period = models.ForeignKey( Time_Period, null = True, blank = True )
    time_period_type = models.CharField( max_length = 255, null = True, blank = True ) # - hourly, by minute, etc.
    time_period_index = models.IntegerField( null = True, blank = True )
    time_period_category = models.CharField( max_length = 255, null = True, blank = True )
    time_period_label = models.CharField( max_length = 255, null = True, blank = True ) # could give each hour, etc. a separate identifier "start+1", "start+2", etc. - not naming _id to start, so you leave room for this to be a separate table.
    aggregate_index = models.IntegerField( null = True, blank = True ) # a separate index you can use to keep track of overall order within a time-series that you separate out into multiple types - "before" and "after", for example - time_period_index can be counter within before or after, aggregate index can be unique through both before and after.
    original_id = models.CharField( max_length = 255, null = True, blank = True )
    original_name = models.CharField( max_length = 255, null = True, blank = True )
    filter_type = models.CharField( max_length = 255, null = True, blank = True ) # - place to keep track of different filter types, if you want.  Example: "text_contains"
    filter_value = models.CharField( max_length = 255, null = True, blank = True )
    match_value = models.CharField( max_length = 255, null = True, blank = True )
    match_count = models.IntegerField( null = True, blank = True, default = 0 )
    filter_1 = models.BooleanField( default = False )
    match_count_1 = models.IntegerField( null = True, blank = True, default = 0 )
    filter_2 = models.BooleanField( default = False )
    match_count_2 = models.IntegerField( null = True, blank = True, default = 0 )
    filter_3 = models.BooleanField( default = False )
    match_count_3 = models.IntegerField( null = True, blank = True, default = 0 )
    filter_4 = models.BooleanField( default = False )
    match_count_4 = models.IntegerField( null = True, blank = True, default = 0 )
    filter_5 = models.BooleanField( default = False )
    match_count_5 = models.IntegerField( null = True, blank = True, default = 0 )
    filter_6 = models.BooleanField( default = False )
    match_count_6 = models.IntegerField( null = True, blank = True, default = 0 )
    filter_7 = models.BooleanField( default = False )
    match_count_7 = models.IntegerField( null = True, blank = True, default = 0 )
    filter_8 = models.BooleanField( default = False )
    match_count_8 = models.IntegerField( null = True, blank = True, default = 0 )
    filter_9 = models.BooleanField( default = False )
    match_count_9 = models.IntegerField( null = True, blank = True, default = 0 )
    filter_10 = models.BooleanField( default = False )
    match_count_10 = models.IntegerField( null = True, blank = True, default = 0 )
    create_date = models.DateTimeField( auto_now_add = True )
    last_update = models.DateTimeField( auto_now = True )

    #============================================================================
    # Instance variables
    #============================================================================
    
    
    m_exception_helper = ExceptionHelper()
    
    
    #============================================================================
    # meta class
    #============================================================================

    # meta class so we know this is an abstract class.
    class Meta:
        abstract = True

    # add string output method.
    

    #============================================================================
    # class methods
    #============================================================================


    @classmethod
    def get_instance( cls,
                      original_name_IN = "",
                      original_id_IN = "",
                      start_dt_IN = None,
                      end_dt_IN = None,
                      time_period_type_IN = "",
                      time_period_category_IN = "",
                      time_period_index_IN = -1,
                      update_existing_IN = True,
                      *args,
                      **kwargs ):

        '''
        Accepts a subreddit full ID; start and end datetime; time period
           type, category and index; and flag telling whether we are updating
           existing.  If not updating existing, returns new instance.  If
           updating, uses values to filter time-series records to find existing
           record for a given subreddit in a given set.  If you are working with
           existing time-series records created with make_data, to make it more
           likely you'll get matches, pass the same values to these parameters
           that you did when you created the data (so same time period type, time
           period category, start and end date of the period, and index within
           category).  If it finds none or more than one, returns None.
                    
        Parameters:
        - original_name_IN - name of row we are trying to find time-series record(s) for.
        - original_id_IN - original ID of row we are trying to find time-series record(s) for.
        - start_dt_IN - datetime.datetime instance of date and time on which you want to start deriving time-series data.
        - end_dt_IN - datetime.datetime instance of date and time on which you want to stop deriving time-series data.
        - time_period_type_IN - (optional) time period type value you want stored in each time-series record.  Defaults to empty string.
        - time_period_category_IN - (optional) category used in labeling.  If set, this was stored in time_period_category, appended to the front of an integer counter that counts up each time period, which was then stored in time_period_label.
        '''
        
        # return reference
        instance_OUT = None
        
        # declare variables
        me = "get_instance"
        update_existing = False
        row_match_rs = None
        debug_flag = True
        
        # updating existing?
        update_existing = update_existing_IN

        # Are we updating?
        if ( ( update_existing ) and ( update_existing != None ) and ( update_existing == True ) ):

            print( "In " + me )

            # first, see if we can find a match for this row.  Can filter on
            #    start date, end date, original name, original ID, category,
            #    type, and/or index.
            row_match_rs = cls.lookup_records( original_name_IN = original_name_IN,
                                               original_id_IN = original_id_IN,
                                               start_dt_IN = start_dt_IN,
                                               end_dt_IN = end_dt_IN,
                                               time_period_type_IN = time_period_type_IN,
                                               time_period_category_IN = time_period_category_IN,
                                               time_period_index_IN = time_period_index_IN )
            
            # check to see if we got anything back.
            if ( row_match_rs.count() == 1 ):
            
                # found one - update it.
                instance_OUT = row_match_rs[ 0 ]
                print( "Found 1." )
            
            elif ( row_match_rs.count() > 1 ):
            
                # error - what to do?
                instance_OUT = None
                print( "More than one match found" )
            
            else:
            
                # no existing row - create new instance of this class.
                instance_OUT = cls()
                print( "Found 0." )
                
            #-- END check to see if we have an existing row to update. --#
            
        else:
        
            # not updating - create new row.
            instance_OUT = cls()
            print( "Not updating." )
        
        #-- END check to see if updating existing --#
        
        return instance_OUT
        
    #-- END method get_instance() --#


    @classmethod
    def lookup_records( cls,
                        original_name_IN = "",
                        original_id_IN = "",
                        start_dt_IN = None,
                        end_dt_IN = None,
                        time_period_type_IN = "",
                        time_period_category_IN = "",
                        time_period_index_IN = -1,
                        *args,
                        **kwargs ):

        '''
        Accepts an original name, origianl ID, start and end datetime, time
           period type, and time period label.  Uses these values to filter
           time-series records.  If you are working with existing time-series
           records created with make_data, to make it more likely you'll get
           correct matches, pass the same values to these parameters that you did
           when you created the data (so same time period type, time period
           category, time period index, start and end date of the period, and
           original ID).
                    
        Parameters:
        - original_name_IN - name of subreddit we are trying to find time-series record(s) for.
        - original_id_IN - name of subreddit we are trying to find time-series record(s) for.
        - start_dt_IN - datetime.datetime instance of date and time on which you want to start deriving time-series data.
        - end_dt_IN - datetime.datetime instance of date and time on which you want to stop deriving time-series data.
        - time_period_type_IN - (optional) time period type value you want stored in each time-series record.  Defaults to empty string.
        - time_period_category_IN - (optional) label to use in labeling.  If set, this is appended to the front of an integer counter that counts up each time period, is stored in time_period_label.  If not set, the integer time period counter is the only thing stored in time period label.
        - time_period_index_IN - (optional) index to keep track of time periods within a category.  Generated values are non-zero, so only included in filter if value is greater than 0.
        '''
        
        # return reference
        rs_OUT = None
        
        # declare variables.
        
        # start out lookup by getting all objects.
        rs_OUT = cls.objects.all()
        
        # for each parameter, check for a non-empty value, if present, filter.
        
        # original name
        if ( ( original_name_IN ) and ( original_name_IN != "" ) ):
        
            rs_OUT = rs_OUT.filter( original_name__iexact = original_name_IN )
        
        #-- END check for subreddit name --#
        
        # original ID
        if ( ( original_id_IN ) and ( original_id_IN != "" ) ):
        
            rs_OUT = rs_OUT.filter( original_id__iexact = original_id_IN )
        
        #-- END check for subreddit reddit ID name --#
        
        # start date
        if ( ( start_dt_IN ) and ( start_dt_IN != None ) ):
        
            rs_OUT = rs_OUT.filter( start_date = start_dt_IN )
        
        #-- END check for start date --#
        
        # end date
        if ( ( end_dt_IN ) and ( end_dt_IN != "" ) ):
        
            rs_OUT = rs_OUT.filter( end_date = end_dt_IN )
        
        #-- END check for end date --#
        
        # time period type
        if ( ( time_period_type_IN ) and ( time_period_type_IN != "" ) ):
        
            rs_OUT = rs_OUT.filter( time_period_type__iexact = time_period_type_IN )
        
        #-- END check for time period type value --#
        
        # time period category
        if ( ( time_period_category_IN ) and ( time_period_category_IN != "" ) ):
        
            rs_OUT = rs_OUT.filter( time_period_category__iexact = time_period_category_IN )
        
        #-- END check for time period category value --#
        
        # time period index
        if ( ( time_period_index_IN ) and ( time_period_index_IN > 0 ) ):
        
            rs_OUT = rs_OUT.filter( time_period_index = time_period_index_IN )
        
        #-- END check for time period index value --#
        
        return rs_OUT

    #-- END class method lookup_records --#
    

    @classmethod
    def process_exception( cls, exception_IN = None, message_IN = "", print_details_IN = True, *args, **kwargs ):
    
        # return reference
        status_OUT = ""
    
        # declare variables
        exception_helper = None
        exception_message = ""
        exception_status = ""

        # Get exception helper class.
        exception_helper = cls.m_exception_handler
                                
        # process the exception
        exception_message = message_IN
        exception_status = exception_helper.process_exception( exception_IN = exception_IN, message_IN = exception_message, print_details_IN = print_details_IN )
        
        # set status to description of exception
        status_OUT = exception_helper.last_exception_details
        
        return status_OUT
        
    #-- END method process_exception() --#
        
        
    #============================================================================
    # instance methods
    #============================================================================


    def __str__(self):
        
        # return reference
        string_OUT = ""
        
        # id?
        if ( ( self.id ) and ( self.id != None ) and ( self.id > 0 ) ):
        
            string_OUT += str( self.id )
        
        #-- END check to see if id --#
        
        # start date?
        if( self.start_date ):
        
            string_OUT += " - " + str( self.start_date )
        
        #-- END check to see if start_date --#

        # end date?
        if( self.end_date ):
        
            string_OUT += " --> " + str( self.end_date )
        
        #-- END check to see if end_date --#
        
        # label.
        if ( self.time_period_label ):
        
            string_OUT += " - " + self.time_period_label
        
        #-- END check to see if time_period_label --#

        # original ID.
        if ( self.original_id ):
        
            string_OUT += " - ID: " + self.original_id
        
        #-- END check to see if original_id --#

        # original name.
        if ( self.original_name ):
        
            string_OUT += " - Name: " + self.original_name
        
        #-- END check to see if original_name --#

        return string_OUT

    #-- END __str__() method --#


#-- END abstract class AbstractTimeSeriesData --#


@python_2_unicode_compatible
class Basic_Time_Series_Data( AbstractTimeSeriesDataModel ):

    #============================================================================
    # Django model fields from parent.
    #============================================================================
    
    #start_date = models.DateTimeField( null = True, blank = True )
    #end_date = models.DateTimeField( null = True, blank = True )
    #time_period_type = models.CharField( max_length = 255, null = True, blank = True ) # - hourly, by minute, etc.
    #filter_type = models.CharField( max_length = 255, null = True, blank = True ) # - place to keep track of different filter types, if you want.  Example: "text_contains"
    #filter_value = models.CharField( max_length = 255, null = True, blank = True )
    #time_period_label = models.CharField( max_length = 255, null = True, blank = True ) # could give each hour, etc. a separate identifier "start+1", "start+2", etc. - not naming _id to start, so you leave room for this to be a separate table.
    #match_value = models.CharField( max_length = 255, null = True, blank = True )


    #============================================================================
    # instance methods
    #============================================================================


    def __str__(self):
        
        # return reference
        string_OUT = ""
        
        # id?
        if ( ( self.id ) and ( self.id != None ) and ( self.id > 0 ) ):
        
            string_OUT += str( self.id )
        
        #-- END check to see if id --#
        
        # start date?
        if( self.start_date ):
        
            string_OUT += " - " + str( self.start_date )
        
        #-- END check to see if start_date --#

        # end date?
        if( self.end_date ):
        
            string_OUT += " --> " + str( self.end_date )
        
        #-- END check to see if end_date --#
        
        # label.
        if ( self.time_period_label ):
        
            string_OUT += " - " + self.time_period_label
        
        #-- END check to see if time_period_label --#

        # original ID.
        if ( self.original_id ):
        
            string_OUT += " - ID: " + self.original_id
        
        #-- END check to see if original_id --#

        # original name.
        if ( self.original_name ):
        
            string_OUT += " - Name: " + self.original_name
        
        #-- END check to see if original_name --#

        return string_OUT

    #-- END __str__() method --#


#-- END abstract class BasicTimeSeriesData --# 