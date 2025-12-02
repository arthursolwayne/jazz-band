
import pretty_midi
import numpy as np

# Initialize the MIDI file
midi = pretty_midi.PrettyMIDI()
midi.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0)]
midi.tempo_changes = [pretty_midi.TempoChange(160, 0)]

# Create instruments
drums_program = pretty_midi.instrument_name_to_program('Acoustic Drums')
bass_program = pretty_midi.instrument_name_to_program('Fretless Bass')
piano_program = pretty_midi.instrument_name_to_program('Electric Piano 1')
sax_program = pretty_midi.instrument_name_to_program('Tenor Saxophone')

drums = pretty_midi.Instrument(program=drums_program)
bass = pretty_midi.Instrument(program=bass_program)
piano = pretty_midi.Instrument(program=piano_program)
sax = pretty_midi.Instrument(program=sax_program)

# Add instruments to MIDI
midi.instruments = [drums, bass, piano, sax]

# BPM = 160, 4/4 time
# 6 seconds = 4 bars
# Each bar = 1.5 seconds, beat = 0.375 seconds

#----------------------
# DRUMS: Little Ray (Bars 1-4)
#----------------------
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
def add_drums():
    for bar in range(4):
        for beat in range(4):
            time = bar * 1.5 + beat * 0.375
            # Kick on beat 0 and 2
            if beat == 0 or beat == 2:
                drums.notes.append(pretty_midi.Note(100, 36, time, time + 0.125))
            # Snare on beat 1 and 3
            if beat == 1 or beat == 3:
                drums.notes.append(pretty_midi.Note(100, 38, time, time + 0.125))
            # Hihat on every eighth
            for eighth in range(2):
                hihat_time = time + eighth * 0.1875
                drums.notes.append(pretty_midi.Note(100, 42, hihat_time, hihat_time + 0.0625))

add_drums()

#----------------------
# BASS: Marcus (Bars 1-4)
#----------------------
# Walking bass line, chromatic approaches, no repeated notes
def add_bass():
    # Start on D (note 62)
    current_note = 62
    for bar in range(4):
        for beat in range(4):
            time = bar * 1.5 + beat * 0.375
            # Use a chromatic line with varied motion
            if beat == 0:
                # Root or chromatic approach
                if bar == 0:
                    current_note = 62
                else:
                    current_note = (current_note + 1) % 12 + 60
            elif beat == 1:
                # Upper neighbor
                current_note = (current_note + 2) % 12 + 60
            elif beat == 2:
                # Root or chromatic
                current_note = (current_note - 1) % 12 + 60
            elif beat == 3:
                # Passing tone or chromatic
                current_note = (current_note + 1) % 12 + 60
            bass.notes.append(pretty_midi.Note(100, current_note, time, time + 0.25))

add_bass()

#----------------------
# PIANO: Diane (Bars 1-4)
#----------------------
# 7th chords on 2 and 4, comp with emotion
def add_piano():
    D7 = [62, 66, 69, 71]  # D7
    F7 = [65, 69, 72, 74]  # F7
    G7 = [67, 71, 74, 76]  # G7
    A7 = [69, 73, 76, 78]  # A7

    chords = [D7, F7, G7, A7]
    for bar in range(4):
        for beat in range(4):
            time = bar * 1.5 + beat * 0.375
            if beat == 1 or beat == 3:
                chord = chords[bar % 4]
                for note in chord:
                    piano.notes.append(pretty_midi.Note(100, note, time, time + 0.25))
            else:
                # Add some color with suspended or altered notes
                if bar == 0 and beat == 0:
                    piano.notes.append(pretty_midi.Note(100, 64, time, time + 0.25))  # E (suspended)
                elif bar == 1 and beat == 2:
                    piano.notes.append(pretty_midi.Note(100, 70, time, time + 0.25))  # Bb (altered)

add_piano()

#----------------------
# SAX: Dante (Bars 1-4)
#----------------------
# Short motif: D (62), F# (66), G (67), D (62) — a question
def add_sax():
    # Bar 1: Just the first note
    sax.notes.append(pretty_midi.Note(100, 62, 0.0, 0.375))
    # Bar 2: Add the motif
    for i, note in enumerate([62, 66, 67, 62]):
        time = 1.5 + i * 0.375
        sax.notes.append(pretty_midi.Note(100, note, time, time + 0.375))
    # Bar 3: Let it hang (rest)
    # Bar 4: Come back and finish the motif
    for i, note in enumerate([62, 66, 67, 62]):
        time = 3.0 + i * 0.375
        sax.notes.append(pretty_midi.Note(100, note, time, time + 0.375))

add_sax()

#----------------------
# Write MIDI file
#----------------------
midi.write("dante_intro.mid")
print("MIDI file written: 'dante_intro.mid'")
