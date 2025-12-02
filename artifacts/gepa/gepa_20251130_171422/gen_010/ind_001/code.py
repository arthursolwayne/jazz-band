
import pretty_midi

# Create a PrettyMIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Define time signature (4/4)
pm.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0)]

# Define key: F minor (F, Gb, Ab, Bb, B, Db, Eb)
# Using 12-TET tuning, we'll map notes accordingly.

# Create instruments
bass_program = pretty_midi.instrument_name_to_program('Double Bass')
bass = pretty_midi.Instrument(program=bass_program)
pm.instruments.append(bass)

piano_program = pretty_midi.instrument_name_to_program('Acoustic Piano')
piano = pretty_midi.Instrument(program=piano_program)
pm.instruments.append(piano)

drums_program = pretty_midi.instrument_name_to_program('Acoustic Drums')
drums = pretty_midi.Instrument(program=drums_program)
pm.instruments.append(drums)

sax_program = pretty_midi.instrument_name_to_program('Soprano Sax')
sax = pretty_midi.Instrument(program=sax_program)
pm.instruments.append(sax)

# BPM = 160 => 1 beat = 0.375 seconds, 1 bar = 1.5 seconds

# 1 bar = 4 beats, 4 bars = 16 beats

# Bar 1: Drums only (build tension, set up the intro)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth

# Time: 0.0 seconds
drum_kick = pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375)
drum_snare = pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125)
drum_hat = pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.375)
drum_hat = pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.75)
drum_hat = pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125)
drum_hat = pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5)
drums.notes.extend([drum_kick, drum_snare, drum_hat])

# Bar 2: Everyone comes in
# Time: 1.5 seconds

# Bass: walking line, chromatic approaches, no repeated notes
# Fm: F, Gb, Ab, Bb, B, Db, Eb
# Root movement: F → Gb → Ab → Bb

# Use F minor scale: F, Gb, Ab, Bb, B, Db, Eb
# Create a walking line (chromatic approach to each chord)

# Bar 2: Fm7 (F, Ab, Bb, Db)
# Walking line: F → Gb → Ab → Bb (chromatic approach to F)

bass_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875),  # F (Ab)
    pretty_midi.Note(velocity=100, pitch=69, start=1.875, end=2.25),  # Gb (Ab)
    pretty_midi.Note(velocity=100, pitch=70, start=2.25, end=2.625),  # Ab (Ab)
    pretty_midi.Note(velocity=100, pitch=71, start=2.625, end=3.0),   # Bb (Ab)
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4 (beat 2 and 4 of Bar 2 and Bar 3)

# Bar 2: Fm7
# F, Ab, Bb, Db
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=70, start=1.5, end=1.875),  # Ab
    pretty_midi.Note(velocity=100, pitch=74, start=1.5, end=1.875),  # Bb
    pretty_midi.Note(velocity=100, pitch=68, start=1.5, end=1.875),  # Db

    # On beat 2
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.625),  # F
    pretty_midi.Note(velocity=100, pitch=70, start=2.25, end=2.625),  # Ab
    pretty_midi.Note(velocity=100, pitch=74, start=2.25, end=2.625),  # Bb
    pretty_midi.Note(velocity=100, pitch=68, start=2.25, end=2.625),  # Db
]
piano.notes.extend(piano_notes)

# Bar 3: Gbm7 (Gb, Bb, Db, Eb)
# Walking line: Gb → Ab → Bb → Db (chromatic approach to Gb)

bass_notes = [
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375),  # Gb
    pretty_midi.Note(velocity=100, pitch=70, start=3.375, end=3.75),  # Ab
    pretty_midi.Note(velocity=100, pitch=71, start=3.75, end=4.125),  # Bb
    pretty_midi.Note(velocity=100, pitch=72, start=4.125, end=4.5),   # Db
]
bass.notes.extend(bass_notes)

# Piano: Gbm7 (Gb, Bb, Db, Eb)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375),  # Gb
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.375),  # Db
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375),  # Eb

    # On beat 2
    pretty_midi.Note(velocity=100, pitch=69, start=3.75, end=4.125),  # Gb
    pretty_midi.Note(velocity=100, pitch=71, start=3.75, end=4.125),  # Bb
    pretty_midi.Note(velocity=100, pitch=72, start=3.75, end=4.125),  # Db
    pretty_midi.Note(velocity=100, pitch=71, start=3.75, end=4.125),  # Eb
]
piano.notes.extend(piano_notes)

# Bar 4: Abm7 (Ab, Bb, Db, Eb)
# Walking line: Ab → Bb → Db → Eb (chromatic approach to Ab)

bass_notes = [
    pretty_midi.Note(velocity=100, pitch=70, start=4.5, end=4.875),  # Ab
    pretty_midi.Note(velocity=100, pitch=71, start=4.875, end=5.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=72, start=5.25, end=5.625),  # Db
    pretty_midi.Note(velocity=100, pitch=71, start=5.625, end=6.0),   # Eb
]
bass.notes.extend(bass_notes)

# Piano: Abm7 (Ab, Bb, Db, Eb)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=70, start=4.5, end=4.875),  # Ab
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.875),  # Bb
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=4.875),  # Db
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.875),  # Eb

    # On beat 2
    pretty_midi.Note(velocity=100, pitch=70, start=5.25, end=5.625),  # Ab
    pretty_midi.Note(velocity=100, pitch=71, start=5.25, end=5.625),  # Bb
    pretty_midi.Note(velocity=100, pitch=72, start=5.25, end=5.625),  # Db
    pretty_midi.Note(velocity=100, pitch=71, start=5.25, end=5.625),  # Eb
]
piano.notes.extend(piano_notes)

# Sax: 4-bar motif, start strong, leave it hanging, then finish it

# Time: 1.5 seconds (Bar 2)

# Motif: F (71), Ab (70), Bb (71), Gb (69)
# (This is a chromatic descent: F → Gb → Ab → Bb → F, but only 3 notes to start)

# Bar 2, beat 1: F (71)
sax_note = pretty_midi.Note(velocity=110, pitch=71, start=1.5, end=1.875)
sax.notes.append(sax_note)

# Bar 2, beat 2: Ab (70)
sax_note = pretty_midi.Note(velocity=110, pitch=70, start=2.25, end=2.625)
sax.notes.append(sax_note)

# Bar 2, beat 3: Bb (71)
sax_note = pretty_midi.Note(velocity=110, pitch=71, start=2.625, end=3.0)
sax.notes.append(sax_note)

# Bar 2, beat 4: Gb (69) – leave it hanging
sax_note = pretty_midi.Note(velocity=110, pitch=69, start=3.0, end=3.375)
sax.notes.append(sax_note)

# Bar 3, beat 1: F (71) – come back and finish the motif
sax_note = pretty_midi.Note(velocity=110, pitch=71, start=3.375, end=3.75)
sax.notes.append(sax_note)

# Bar 3, beat 2: Ab (70)
sax_note = pretty_midi.Note(velocity=110, pitch=70, start=3.75, end=4.125)
sax.notes.append(sax_note)

# Bar 3, beat 3: Bb (71)
sax_note = pretty_midi.Note(velocity=110, pitch=71, start=4.125, end=4.5)
sax.notes.append(sax_note)

# Bar 3, beat 4: Gb (69) – leave it hanging again
sax_note = pretty_midi.Note(velocity=110, pitch=69, start=4.5, end=4.875)
sax.notes.append(sax_note)

# Bar 4, beat 1: F (71) – complete the motif
sax_note = pretty_midi.Note(velocity=110, pitch=71, start=4.875, end=5.25)
sax.notes.append(sax_note)

# Bar 4, beat 2: Ab (70)
sax_note = pretty_midi.Note(velocity=110, pitch=70, start=5.25, end=5.625)
sax.notes.append(sax_note)

# Bar 4, beat 3: Bb (71)
sax_note = pretty_midi.Note(velocity=110, pitch=71, start=5.625, end=6.0)
sax.notes.append(sax_note)

# Add the drum fill for the end of bar 4
# Time: 5.625 to 6.0 — eighth note fill
drum_hat = pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=6.0)
drums.notes.append(drum_hat)

# Save the MIDI file
pm.write("intro_4_bar_Fm.mid")
