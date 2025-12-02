
import pretty_midi
import numpy as np

# Create a PrettyMIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Time signature: 4/4
pm.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0)]

# Key: D major (key number 2)
pm.key_signature_changes = [pretty_midi.KeySignature(2, 0)]

# Define the tempo (160 BPM)
pm.tempo_changes = [pretty_midi.TempoChange(160, 0)]

# Define the time per bar (1.5 seconds)
time_per_bar = 1.5
time_per_beat = time_per_bar / 4

# Create instruments
sax_program = pretty_midi.programs.Program(64, 0)  # Tenor sax
bass_program = pretty_midi.programs.Program(33, 0)  # Double bass
piano_program = pretty_midi.programs.Program(0, 0)  # Acoustic piano
drum_program = pretty_midi.programs.Program(128, 0)  # Drums

sax_instrument = pretty_midi.Instrument(program=sax_program)
bass_instrument = pretty_midi.Instrument(program=bass_program)
piano_instrument = pretty_midi.Instrument(program=piano_program)
drum_instrument = pretty_midi.Instrument(program=drum_program)

pm.instruments = [sax_instrument, bass_instrument, piano_instrument, drum_instrument]

# DRUMS: Little Ray - Full and rhythmic
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth

for bar in range(4):
    for beat in range(4):
        time = bar * time_per_bar + beat * time_per_beat
        if beat in [0, 2]:  # Kick on 1 and 3
            drum_instrument.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.1))
        if beat in [1, 3]:  # Snare on 2 and 4
            drum_instrument.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.1))
        # Hi-hats on every eighth
        for eighth in range(2):
            hi_hat_time = time + eighth * time_per_beat / 2
            drum_instrument.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=hi_hat_time, end=hi_hat_time + 0.05))

# BASS: Marcus - Walking line with chromatic tension

def bass_note(bar, beat):
    # D major scale: D E F# G A B C#
    # Chromatic approaches:
    # D -> D# -> E (chromatic approach)
    # G -> G# -> A (chromatic approach)
    # A -> A# -> B (chromatic approach)
    # C# -> D (chromatic approach)
    # We'll use chromatic passing tones between chord tones
    # Bar 1: D -> D# -> E (approach E)
    # Bar 2: F# -> G -> G#
    # Bar 3: A -> A# -> B
    # Bar 4: C# -> D
    if bar == 0:
        if beat == 0:
            return 62  # D
        elif beat == 1:
            return 63  # D#
        elif beat == 2:
            return 64  # E
        elif beat == 3:
            return 64  # E
    elif bar == 1:
        if beat == 0:
            return 66  # F#
        elif beat == 1:
            return 67  # G
        elif beat == 2:
            return 68  # G#
        elif beat == 3:
            return 68  # G#
    elif bar == 2:
        if beat == 0:
            return 69  # A
        elif beat == 1:
            return 70  # A#
        elif beat == 2:
            return 71  # B
        elif beat == 3:
            return 71  # B
    elif bar == 3:
        if beat == 0:
            return 72  # C#
        elif beat == 1:
            return 72  # C#
        elif beat == 2:
            return 74  # D
        elif beat == 3:
            return 74  # D

for bar in range(4):
    for beat in range(4):
        time = bar * time_per_bar + beat * time_per_beat
        note_number = bass_note(bar, beat)
        # Bass plays on the downbeats and offbeats with slight syncopation
        if beat in [0, 1, 2, 3]:
            bass_instrument.notes.append(pretty_midi.Note(velocity=80, pitch=note_number, start=time, end=time + 0.25))

# PIANO: Diane - 7th chords on 2 and 4, sparse and punchy

def piano_chord(bar):
    # D7 = D F# A C#
    # G7 = G B D F
    # A7 = A C# E G
    # B7 = B D# F# A
    if bar == 0:
        return [62, 66, 69, 72]  # D7
    elif bar == 1:
        return [67, 71, 62, 65]  # G7
    elif bar == 2:
        return [69, 73, 71, 67]  # A7
    elif bar == 3:
        return [71, 75, 77, 79]  # B7

for bar in range(4):
    chord = piano_chord(bar)
    # Play chord on 2 and 4
    if bar % 2 == 0:  # even bars (0, 2) have chords on 2 and 4
        for beat in [1, 3]:
            time = bar * time_per_bar + beat * time_per_beat
            for note in chord:
                piano_instrument.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.2))
    else:  # odd bars (1, 3), chords on 2 and 4
        for beat in [1, 3]:
            time = bar * time_per_bar + beat * time_per_beat
            for note in chord:
                piano_instrument.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.2))

# SAX: You — concise, expressive, memorable. One motif, start, leave it hanging, return and finish.

# Motif: D -> F# -> E -> D (4 notes), each on quarter note
# Start on bar 0, beat 0
# Bar 0: D (62) quarter
# Bar 1: F# (66) quarter
# Bar 2: E (64) quarter
# Bar 3: D (62) quarter

# But make it more expressive: staggered, with a rest in bar 1

# Bar 0 beat 0: D (62) quarter
# Bar 1 beat 0: rest
# Bar 1 beat 1: F# (66) quarter
# Bar 2 beat 1: E (64) quarter
# Bar 3 beat 1: D (62) quarter

for bar in range(4):
    for beat in range(4):
        time = bar * time_per_bar + beat * time_per_beat
        if bar == 0 and beat == 0:
            sax_instrument.notes.append(pretty_midi.Note(velocity=110, pitch=62, start=time, end=time + 0.5))
        elif bar == 1 and beat == 1:
            sax_instrument.notes.append(pretty_midi.Note(velocity=110, pitch=66, start=time, end=time + 0.5))
        elif bar == 2 and beat == 1:
            sax_instrument.notes.append(pretty_midi.Note(velocity=110, pitch=64, start=time, end=time + 0.5))
        elif bar == 3 and beat == 1:
            sax_instrument.notes.append(pretty_midi.Note(velocity=110, pitch=62, start=time, end=time + 0.5))

# Save the MIDI file
pm.write("dante_intro.mid")
