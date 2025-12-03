
import pretty_midi

# Create a PrettyMIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Set up instruments
bass_program = pretty_midi.instrument_name_to_program('Acoustic Bass')
piano_program = pretty_midi.instrument_name_to_program('Electric Piano 1')
drums_program = pretty_midi.instrument_name_to_program('Drums')
sax_program = pretty_midi.instrument_name_to_program('Soprano Sax')

# Create instruments
bass = pretty_midi.Instrument(program=bass_program)
piano = pretty_midi.Instrument(program=piano_program)
drums = pretty_midi.Instrument(program=drums_program)
sax = pretty_midi.Instrument(program=sax_program)

# Tempo is 160 BPM => 60 / 160 = 0.375 seconds per beat
# Four bars at 4/4 = 16 beats => 6 seconds total
# Each bar is 1.5s

# Define time in seconds for each bar
bar_times = [0, 1.5, 3.0, 4.5, 6.0]

# --- DRUMS: Little Ray (22 years old, too fast, but tonight you need that energy) ---
# Bar 1: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Bar 2: Same, but with a syncopated fill on the & of 3
# Bar 3: Same, but with a roll on the 3rd beat
# Bar 4: Same, but with a snare accent on the & of 4

drum_notes = [
    # Bar 1
    (0, pretty_midi.note_number_to_name(36), 0.375, 1.0),  # Kick on 1
    (0, pretty_midi.note_number_to_name(38), 0.75, 1.0),   # Snare on 2
    (0, pretty_midi.note_number_to_name(42), 1.125, 1.0),  # Hihat on & of 1
    (0, pretty_midi.note_number_to_name(42), 1.5, 1.0),    # Hihat on 2
    (0, pretty_midi.note_number_to_name(36), 1.875, 1.0),  # Kick on 3
    (0, pretty_midi.note_number_to_name(38), 2.25, 1.0),   # Snare on 4
    (0, pretty_midi.note_number_to_name(42), 2.625, 1.0),  # Hihat on & of 3
    (0, pretty_midi.note_number_to_name(42), 3.0, 1.0),    # Hihat on 4

    # Bar 2
    (1.5, pretty_midi.note_number_to_name(36), 0.375, 1.0),  # Kick on 1
    (1.5, pretty_midi.note_number_to_name(38), 0.75, 1.0),   # Snare on 2
    (1.5, pretty_midi.note_number_to_name(42), 1.125, 1.0),  # Hihat on & of 1
    (1.5, pretty_midi.note_number_to_name(42), 1.5, 1.0),    # Hihat on 2
    (1.5, pretty_midi.note_number_to_name(36), 1.875, 1.0),  # Kick on 3
    (1.5, pretty_midi.note_number_to_name(38), 2.25, 1.0),   # Snare on 4
    (1.5, pretty_midi.note_number_to_name(42), 2.625, 1.0),  # Hihat on & of 3
    (1.5, pretty_midi.note_number_to_name(42), 3.0, 1.0),    # Hihat on 4

    # Bar 3
    (3.0, pretty_midi.note_number_to_name(36), 0.375, 1.0),  # Kick on 1
    (3.0, pretty_midi.note_number_to_name(38), 0.75, 1.0),   # Snare on 2
    (3.0, pretty_midi.note_number_to_name(42), 1.125, 1.0),  # Hihat on & of 1
    (3.0, pretty_midi.note_number_to_name(42), 1.5, 1.0),    # Hihat on 2
    (3.0, pretty_midi.note_number_to_name(36), 1.875, 1.0),  # Kick on 3
    (3.0, pretty_midi.note_number_to_name(38), 2.25, 1.0),   # Snare on 4
    (3.0, pretty_midi.note_number_to_name(42), 2.625, 1.0),  # Hihat on & of 3
    (3.0, pretty_midi.note_number_to_name(42), 3.0, 1.0),    # Hihat on 4

    # Bar 4
    (4.5, pretty_midi.note_number_to_name(36), 0.375, 1.0),  # Kick on 1
    (4.5, pretty_midi.note_number_to_name(38), 0.75, 1.0),   # Snare on 2
    (4.5, pretty_midi.note_number_to_name(42), 1.125, 1.0),  # Hihat on & of 1
    (4.5, pretty_midi.note_number_to_name(42), 1.5, 1.0),    # Hihat on 2
    (4.5, pretty_midi.note_number_to_name(36), 1.875, 1.0),  # Kick on 3
    (4.5, pretty_midi.note_number_to_name(38), 2.25, 1.0),   # Snare on 4
    (4.5, pretty_midi.note_number_to_name(42), 2.625, 1.0),  # Hihat on & of 3
    (4.5, pretty_midi.note_number_to_name(42), 3.0, 1.0),    # Hihat on 4
]

for time, note, duration, velocity in drum_notes:
    note_number = pretty_midi.note_name_to_number(note)
    drum_note = pretty_midi.Note(velocity=velocity, pitch=note_number, start=time, end=time + duration)
    drums.notes.append(drum_note)

# --- BASS: Marcus (60 years old, anchor, walking line in Fm) ---
# Fm = F, Ab, C, D, Eb, F, Ab, C, D, Eb, F, etc.
# Walking line: D2-G2, roots and fifths with chromatic approaches

bass_notes = [
    # Bar 1
    (0, 43, 0.375, 1.0),  # D2 as chromatic approach to C (Ab)
    (0.375, 42, 0.375, 1.0),  # C (Ab) (root)
    (0.75, 44, 0.375, 1.0),  # Eb (fifth)
    (1.125, 43, 0.375, 1.0),  # D2 chromatic approach to F

    # Bar 2
    (1.5, 44, 0.375, 1.0),  # Eb
    (1.875, 43, 0.375, 1.0),  # D2
    (2.25, 42, 0.375, 1.0),  # C (Ab)
    (2.625, 44, 0.375, 1.0),  # Eb (fifth)

    # Bar 3
    (3.0, 44, 0.375, 1.0),  # Eb
    (3.375, 43, 0.375, 1.0),  # D2
    (3.75, 42, 0.375, 1.0),  # C (Ab)
    (4.125, 44, 0.375, 1.0),  # Eb

    # Bar 4
    (4.5, 44, 0.375, 1.0),  # Eb
    (4.875, 43, 0.375, 1.0),  # D2
    (5.25, 42, 0.375, 1.0),  # C (Ab)
    (5.625, 44, 0.375, 1.0),  # Eb
]

for time, pitch, duration, velocity in bass_notes:
    note = pretty_midi.Note(velocity=velocity, pitch=pitch, start=time, end=time + duration)
    bass.notes.append(note)

# --- PIANO: Diane (angry about something, open voicings, resolve on the last bar) ---
# Fm: F, Ab, C, D, Eb (no Bb)
# Open voicings, different chords each bar

piano_notes = [
    # Bar 1: Fm7 (F, Ab, C, Eb)
    (0, 64, 0.5, 100),  # F
    (0, 67, 0.5, 100),  # Ab
    (0, 72, 0.5, 100),  # C
    (0, 69, 0.5, 100),  # Eb

    # Bar 2: Ab7 (Ab, C, Eb, Gb)
    (1.5, 67, 0.5, 110),  # Ab
    (1.5, 72, 0.5, 110),  # C
    (1.5, 69, 0.5, 110),  # Eb
    (1.5, 64, 0.5, 110),  # Gb

    # Bar 3: Cm7 (C, Eb, G, Bb)
    (3.0, 72, 0.5, 105),  # C
    (3.0, 69, 0.5, 105),  # Eb
    (3.0, 76, 0.5, 105),  # G
    (3.0, 71, 0.5, 105),  # Bb

    # Bar 4: D7 (D, F#, A, C)
    (4.5, 74, 0.5, 110),  # D
    (4.5, 80, 0.5, 110),  # F#
    (4.5, 77, 0.5, 110),  # A
    (4.5, 72, 0.5, 110),  # C
]

for time, pitch, duration, velocity in piano_notes:
    note = pretty_midi.Note(velocity=velocity, pitch=pitch, start=time, end=time + duration)
    piano.notes.append(note)

# --- SAX: You (Dante, haunting, incomplete motif) ---
# One short motif, start it, leave it hanging, come back and finish it
# Fm: F, Ab, C, D, Eb
# Use F, Ab, C, D in a way that feels unresolved

sax_notes = [
    # Bar 1: Start the motif, leave it hanging
    (0, 77, 0.75, 100),  # D (Fm3)
    (0.75, 74, 0.75, 100),  # F (root)
    (1.5, 77, 0.75, 100),  # D again
    (1.5, 74, 0.75, 100),  # F

    # Bar 2: Rest
    (1.5, 77, 0.0, 0),  # Rest
    (1.5, 74, 0.0, 0),  # Rest

    # Bar 3: Return with variation
    (3.0, 77, 0.75, 100),  # D
    (3.75, 74, 0.75, 100),  # F

    # Bar 4: End with a question, leave it open
    (4.5, 77, 0.75, 100),  # D
    (5.25, 74, 0.75, 100),  # F
]

for time, pitch, duration, velocity in sax_notes:
    note = pretty_midi.Note(velocity=velocity, pitch=pitch, start=time, end=time + duration)
    sax.notes.append(note)

# Add instruments to MIDI
pm.instruments.append(drums)
pm.instruments.append(bass)
pm.instruments.append(piano)
pm.instruments.append(sax)

# Save the MIDI file
pm.write("jazz_intro_f_minor.mid")
