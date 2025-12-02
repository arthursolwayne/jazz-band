
import pretty_midi

# Create a new Pretty MIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Set the time signature (4/4)
pm.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0)]

# Set the key signature — F minor (1 flat)
pm.key_signature_changes = [pretty_midi.KeySignature(5, 0)]  # 5 = F minor

# Instrument: Drums (Little Ray)
drum_program = pretty_midi.instrument_name_to_program('Acoustic Grand Piano')
drum_instrument = pretty_midi.Instrument(program=drum_program)

# Instrument: Bass (Marcus)
bass_program = pretty_midi.instrument_name_to_program('Double Bass')
bass_instrument = pretty_midi.Instrument(program=bass_program)

# Instrument: Piano (Diane)
piano_program = pretty_midi.instrument_name_to_program('Acoustic Grand Piano')
piano_instrument = pretty_midi.Instrument(program=piano_program)

# Instrument: Tenor Sax (You)
sax_program = pretty_midi.instrument_name_to_program('Tenor Saxophone')
sax_instrument = pretty_midi.Instrument(program=sax_program)

# Define the time in seconds per beat
bpm = 160
seconds_per_beat = 60.0 / bpm

# Start times per bar:
bar_start_times = [0.0, seconds_per_beat * 4, seconds_per_beat * 8, seconds_per_beat * 12]

# --- DRUMS: Little Ray (Bar 1: Kick on 1 and 3, snare on 2 and 4, hihat every eighth)

# Bar 1
drum_notes = [
    # Kick on 1 and 3
    (pretty_midi.note_number_to_name(36), bar_start_times[0] + 0.0, 0.25),
    (pretty_midi.note_number_to_name(36), bar_start_times[0] + 1.5, 0.25),
    # Snare on 2 and 4
    (pretty_midi.note_number_to_name(38), bar_start_times[0] + 0.75, 0.25),
    (pretty_midi.note_number_to_name(38), bar_start_times[0] + 2.25, 0.25),
    # Hihat every eighth
    (pretty_midi.note_number_to_name(42), bar_start_times[0] + 0.0, 0.125),
    (pretty_midi.note_number_to_name(42), bar_start_times[0] + 0.125, 0.125),
    (pretty_midi.note_number_to_name(42), bar_start_times[0] + 0.25, 0.125),
    (pretty_midi.note_number_to_name(42), bar_start_times[0] + 0.375, 0.125),
    (pretty_midi.note_number_to_name(42), bar_start_times[0] + 0.5, 0.125),
    (pretty_midi.note_number_to_name(42), bar_start_times[0] + 0.625, 0.125),
    (pretty_midi.note_number_to_name(42), bar_start_times[0] + 0.75, 0.125),
    (pretty_midi.note_number_to_name(42), bar_start_times[0] + 0.875, 0.125),
    (pretty_midi.note_number_to_name(42), bar_start_times[0] + 1.0, 0.125),
    (pretty_midi.note_number_to_name(42), bar_start_times[0] + 1.125, 0.125),
    (pretty_midi.note_number_to_name(42), bar_start_times[0] + 1.25, 0.125),
    (pretty_midi.note_number_to_name(42), bar_start_times[0] + 1.375, 0.125),
    (pretty_midi.note_number_to_name(42), bar_start_times[0] + 1.5, 0.125),
    (pretty_midi.note_number_to_name(42), bar_start_times[0] + 1.625, 0.125),
    (pretty_midi.note_number_to_name(42), bar_start_times[0] + 1.75, 0.125),
    (pretty_midi.note_number_to_name(42), bar_start_times[0] + 1.875, 0.125),
    (pretty_midi.note_number_to_name(42), bar_start_times[0] + 2.0, 0.125),
    (pretty_midi.note_number_to_name(42), bar_start_times[0] + 2.125, 0.125),
    (pretty_midi.note_number_to_name(42), bar_start_times[0] + 2.25, 0.125),
    (pretty_midi.note_number_to_name(42), bar_start_times[0] + 2.375, 0.125),
    (pretty_midi.note_number_to_name(42), bar_start_times[0] + 2.5, 0.125),
]

# Convert notes to MIDI numbers
for note_name, start, duration in drum_notes:
    note_number = pretty_midi.note_name_to_number(note_name)
    drum_instrument.notes.append(pretty_midi.Note(velocity=100, pitch=note_number, start=start, end=start + duration))

pm.instruments.append(drum_instrument)

# --- BASS: Marcus (Walking line in Fm, chromatic approaches)

# Fm scale: F, Gb, Ab, A, Bb, C, Db
# Let's build a chromatic walking line in Fm, starting from F
bass_notes = [
    # Bar 1
    (48, bar_start_times[0], 0.25),  # F
    (50, bar_start_times[0] + 0.25, 0.25),  # Gb
    (47, bar_start_times[0] + 0.5, 0.25),  # E (chromatic approach to F)
    (48, bar_start_times[0] + 0.75, 0.25),  # F

    # Bar 2
    (49, bar_start_times[1], 0.25),  # G (chromatic)
    (47, bar_start_times[1] + 0.25, 0.25),  # Gb (chromatic)
    (45, bar_start_times[1] + 0.5, 0.25),  # E (chromatic)
    (48, bar_start_times[1] + 0.75, 0.25),  # F

    # Bar 3
    (50, bar_start_times[2], 0.25),  # Gb
    (47, bar_start_times[2] + 0.25, 0.25),  # F
    (52, bar_start_times[2] + 0.5, 0.25),  # A
    (48, bar_start_times[2] + 0.75, 0.25),  # F

    # Bar 4
    (45, bar_start_times[3], 0.25),  # E
    (48, bar_start_times[3] + 0.25, 0.25),  # F
    (50, bar_start_times[3] + 0.5, 0.25),  # Gb
    (48, bar_start_times[3] + 0.75, 0.25),  # F
]

for note_number, start, duration in bass_notes:
    bass_instrument.notes.append(pretty_midi.Note(velocity=90, pitch=note_number, start=start, end=start + duration))

pm.instruments.append(bass_instrument)

# --- PIANO: Diane (7th chords, comp on 2 and 4)

piano_notes = [
    # Bar 1
    (57, bar_start_times[0], 0.25),  # C7 (C E G Bb)
    (58, bar_start_times[0] + 0.25, 0.25),  # D7 (D F# A C)
    (57, bar_start_times[0] + 0.5, 0.25),  # C7
    (58, bar_start_times[0] + 0.75, 0.25),  # D7

    # Bar 2
    (57, bar_start_times[1], 0.25),  # C7
    (58, bar_start_times[1] + 0.25, 0.25),  # D7
    (55, bar_start_times[1] + 0.5, 0.25),  # A7 (A C# E G)
    (58, bar_start_times[1] + 0.75, 0.25),  # D7

    # Bar 3
    (55, bar_start_times[2], 0.25),  # A7
    (58, bar_start_times[2] + 0.25, 0.25),  # D7
    (54, bar_start_times[2] + 0.5, 0.25),  # G7 (G B D F)
    (58, bar_start_times[2] + 0.75, 0.25),  # D7

    # Bar 4
    (54, bar_start_times[3], 0.25),  # G7
    (58, bar_start_times[3] + 0.25, 0.25),  # D7
    (57, bar_start_times[3] + 0.5, 0.25),  # C7
    (58, bar_start_times[3] + 0.75, 0.25),  # D7
]

for note_number, start, duration in piano_notes:
    piano_instrument.notes.append(pretty_midi.Note(velocity=95, pitch=note_number, start=start, end=start + duration))

pm.instruments.append(piano_instrument)

# --- SAX: You (Motif in Fm, 4 bars)

# Tenor Sax Motif
# Bar 1: Start with a soft, open F (G in sax is F)
# Bar 2: Let it resolve or build
# Bar 3: Echo with slight variation
# Bar 4: Finish with a return to F, leaving it open

sax_notes = [
    # Bar 1
    (62, bar_start_times[0], 0.375),  # G (F in concert pitch)
    (60, bar_start_times[0] + 0.375, 0.375),  # E
    (62, bar_start_times[0] + 0.75, 0.375),  # G
    (60, bar_start_times[0] + 1.125, 0.375),  # E

    # Bar 2
    (64, bar_start_times[1], 0.375),  # A
    (62, bar_start_times[1] + 0.375, 0.375),  # G
    (64, bar_start_times[1] + 0.75, 0.375),  # A
    (62, bar_start_times[1] + 1.125, 0.375),  # G

    # Bar 3
    (62, bar_start_times[2], 0.375),  # G
    (60, bar_start_times[2] + 0.375, 0.375),  # E
    (62, bar_start_times[2] + 0.75, 0.375),  # G
    (60, bar_start_times[2] + 1.125, 0.375),  # E

    # Bar 4
    (62, bar_start_times[3], 0.375),  # G (ending on F)
    (60, bar_start_times[3] + 0.375, 0.375),  # E
    (62, bar_start_times[3] + 0.75, 0.375),  # G
    (60, bar_start_times[3] + 1.125, 0.375),  # E
]

for note_number, start, duration in sax_notes:
    sax_instrument.notes.append(pretty_midi.Note(velocity=105, pitch=note_number, start=start, end=start + duration))

pm.instruments.append(sax_instrument)

# Save the MIDI file
pm.write("dantes_shot.mid")
print("MIDI file written as 'dantes_shot.mid'")
