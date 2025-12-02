
import pretty_midi
import numpy as np

# Create a new MIDI file
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Set time signature (4/4)
midi.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0)]

# Set key signature (Dm, which is D minor)
# In MIDI, key signature is stored using the KeySignature class
# D minor has one flat (Bb), so key number is 21 (D = 2, minor = 1, 2 + 1*24 = 26? Let's use the correct MIDI key signature code)
# D minor key signature is 21 in MIDI (D = 2, minor = 1, so 21 = 2 + 1*24)
midi.key_signature_changes = [pretty_midi.KeySignature(21, 0)]

# Create instruments
bass_program = pretty_midi.instrument_name_to_program('Acoustic Bass')
piano_program = pretty_midi.instrument_name_to_program('Electric Piano 1')
drums_program = pretty_midi.instrument_name_to_program('Acoustic Drums')
sax_program = pretty_midi.instrument_name_to_program('Tenor Saxophone')

bass = pretty_midi.Instrument(program=bass_program)
piano = pretty_midi.Instrument(program=piano_program)
drums = pretty_midi.Instrument(program=drums_program)
sax = pretty_midi.Instrument(program=sax_program)

midi.instruments = [bass, piano, drums, sax]

# TEMPO = 160 BPM
# 4/4 time
# 1 bar = 1.5 seconds
# 1 beat = 0.375 seconds

# --- DRUMS: Little Ray ---
# Bar 1: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Bar 2-4: Same pattern, but with subtle space on 1st beat of bar 2, and a fill at the end of bar 4

# Define the drum pattern
def create_drums(bar_start, kick_notes, snare_notes, hihat_notes):
    for i, note in enumerate(kick_notes):
        time = bar_start + (i * 0.375)
        drum_note = pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.15)
        drums.notes.append(drum_note)

    for i, note in enumerate(snare_notes):
        time = bar_start + (i * 0.375)
        drum_note = pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.15)
        drums.notes.append(drum_note)

    for i, note in enumerate(hihat_notes):
        time = bar_start + (i * 0.1875)
        drum_note = pretty_midi.Note(velocity=60, pitch=note, start=time, end=time + 0.1)
        drums.notes.append(drum_note)

# Bar 1
create_drums(0.0, [36], [38], [42, 42, 42, 42, 42, 42, 42, 42])  # Kick on 1,3 | Snare on 2,4 | Hihat every 8th

# Bar 2
create_drums(1.5, [36], [38], [42, 42, 42, 42, 42, 42, 42, 42])

# Bar 3
create_drums(3.0, [36], [38], [42, 42, 42, 42, 42, 42, 42, 42])

# Bar 4
create_drums(4.5, [36], [38], [42, 42, 42, 42, 42, 42, 42, 42])

# --- BASS: Marcus ---
# Walking line in Dm: D, F, G, Bb, D, F, G, Bb, D, F, G, Bb, D, F, G, Bb
# Chromatic approach to each chord
# Bar 1: Walk down from Bb to D (chromatic descending)
# Bars 2-4: Play Dm7 walking line with chromatic approaches

def create_bass_line(start_time, notes):
    for i, pitch in enumerate(notes):
        time = start_time + (i * 0.375)
        note = pretty_midi.Note(velocity=80, pitch=pitch, start=time, end=time + 0.25)
        bass.notes.append(note)

# Bar 1: Chromatic descent from Bb to D
create_bass_line(0.0, [71, 70, 69, 68, 67, 66, 65, 64, 62])  # Bb, A, Ab, G, Gb, F, E, Eb, D

# Bars 2-4: Dm7 walking line with chromatic approaches
# Dm7: D, F, G, C (but in this case, we'll do the walking line with chromatic steps)
# Walk: D, Eb, F, G, Ab, Bb, B, C, D, C, B, Bb, A, G, F, Eb
create_bass_line(1.5, [62, 63, 65, 67, 68, 70, 71, 72, 62, 72, 71, 70, 69, 67, 65, 63])

# --- PIANO: Diane ---
# Comp on 2 and 4 with Dm7 chords
# Use 7th chords with dynamic contrast and avoid predictability

def create_piano_notes(start_time, chords, velocities):
    for i, (chord, velocity) in enumerate(zip(chords, velocities)):
        for pitch in chord:
            time = start_time + (i * 0.0)  # Chord on the beat
            note = pretty_midi.Note(velocity=velocity, pitch=pitch, start=time, end=time + 0.5)
            piano.notes.append(note)

# Bar 1: Dm7 (D, F, G, C) on beat 2 and 4
create_piano_notes(0.75, [[62, 65, 67, 72]], [90])
create_piano_notes(2.25, [[62, 65, 67, 72]], [90])

# Bar 2: Dm7 on beat 2 and 4
create_piano_notes(1.75, [[62, 65, 67, 72]], [90])
create_piano_notes(3.25, [[62, 65, 67, 72]], [90])

# Bar 3: Dm7 on beat 2 and 4
create_piano_notes(2.75, [[62, 65, 67, 72]], [90])
create_piano_notes(4.25, [[62, 65, 67, 72]], [90])

# Bar 4: Dm7 on beat 2 and 4
create_piano_notes(3.75, [[62, 65, 67, 72]], [90])
create_piano_notes(5.25, [[62, 65, 67, 72]], [90])

# --- SAX: Dante ---
# One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Dm scale: D, Eb, F, G, A, Bb, C, D
# Motif: D, Eb, F, G, (rest) G, F, Eb, D (sings, then resolves)

def create_sax_line(start_time, notes):
    for i, pitch in enumerate(notes):
        time = start_time + (i * 0.375)
        if pitch != -1:  # -1 represents a rest
            note = pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + 0.25)
            sax.notes.append(note)
        else:
            # Let's just let the silence be
            pass

# Bar 1: Play the first four notes of the motif (D, Eb, F, G)
create_sax_line(0.0, [62, 63, 65, 67])

# Bar 2: Rest on first beat, then play the resolution (G, F, Eb, D)
create_sax_line(1.5, [-1, 67, 65, 63, 62])

# Save the MIDI file
midi.write("dante_intro.mid")
