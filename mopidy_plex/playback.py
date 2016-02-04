# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import re

import pykka
from mopidy import backend
from mopidy.models import Playlist, Ref

from plexapi import audio as plexaudio

import mopidy_plex
from mopidy_plex import logger



class PlexPlaybackProvider(backend.PlaybackProvider):

    def translate_uri(self, uri):
        '''Convert custom URI scheme to real playable URI.

        MAY be reimplemented by subclass.

        This is very likely the only thing you need to override as a backend
        author. Typically this is where you convert any Mopidy specific URI to a real
        URI and then return it. If you can’t convert the URI just return None.

        Parameters: uri (string) – the URI to translate
        Return type:    string or None if the URI could not be translated'''

        logger.debug("Playback.translate_uri Plex with uri '%s'", uri)

        rx = re.compile(r'plex:track:(?P<track_id>\d+)')
        rm = rx.match(uri)
        if rm is None: # uri unknown
            logger.info('Unkown uri: %s', uri)
            return None
        elem = plexaudio.find_key(self.backend.plex, rm.group('track_id'))
        logger.debug('returning stream for elem %r', elem)
        return elem.getStreamUrl()


    def _get_time_position(self):
        '''Get the current time position in milliseconds.

        MAY be reimplemented by subclass.

        Return type:	int'''
        raise NotImplemented


    def _pause(self):
        '''Pause playback.

        MAY be reimplemented by subclass.

        Return type:	True if successful, else False'''
        raise NotImplemented

    def _play(self):
        '''Start playback.

        MAY be reimplemented by subclass.

        Return type:	True if successful, else False'''
        raise NotImplemented

    def _resume(self):
        '''Resume playback at the same time position playback was paused.

        MAY be reimplemented by subclass.

        Return type:	True if successful, else False'''
        raise NotImplemented

    def _seek(self, time_position):
        '''Seek to a given time position.

        MAY be reimplemented by subclass.

        Parameters:	time_position (int) – time position in milliseconds
        Return type:	True if successful, else False'''
        raise NotImplemented

    def _stop(self):
        '''Stop playback.

        MAY be reimplemented by subclass.

        Should not be used for tracking if tracks have been played or when we are done playing them.

        Return type:	True if successful, else False'''
        raise NotImplemented
