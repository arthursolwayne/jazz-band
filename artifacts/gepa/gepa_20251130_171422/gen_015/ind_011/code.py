
import pretty_midi

# Create a new PrettyMIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Define key: D minor
key = 'Dm'

# Define time signature: 4/4
pm.time_signature_changes = [pretty_midi.TimeSignature(numerator=4, denominator=4, time=0.0)]

# Define instruments
# 1. Drums (Little Ray)
# 2. Bass (Marcus)
# 3. Piano (Diane)
# 4. Tenor Sax (Dante)

# ============= DRUMS =============
drum_program = pretty_midi.instrument_name_to_program('Acoustic Grand Piano')
drum_instrument = pretty_midi.Instrument(program=drum_program)

# Kick on 1 and 3, snare on 2 and 4, hihat every eighth
# Bar length = 6 seconds, 160 BPM = 0.375 seconds per beat

# Bar 1: Only hihat on every eighth
for i in range(8):
    note = pretty_midi.Note(
        velocity=64,
        pitch=pretty_midi.note_name_to_number('C'),
        start=i * 0.375,
        end=(i + 1) * 0.375
    )
    drum_instrument.notes.append(note)

pm.instruments.append(drum_instrument)

# ============= BASS (Marcus) =============
bass_program = pretty_midi.instrument_name_to_program('Fretless Bass')
bass_instrument = pretty_midi.Instrument(program=bass_program)

# Walking line, chromatic, never the same note twice
# Bar 2:
notes = [pretty_midi.note_name_to_number('D'), pretty_midi.note_name_to_number('E'), pretty_midi.note_name_to_number('F'), pretty_midi.note_name_to_number('F#')]
for i, note in enumerate(notes):
    bass_note = pretty_midi.Note(
        velocity=64,
        pitch=note,
        start=i * 0.375 + 1.5,  # Bar 2 starts at 1.5s
        end=(i + 1) * 0.375 + 1.5
    )
    bass_instrument.notes.append(bass_note)

# Bar 3:
notes = [pretty_midi.note_name_to_number('G'), pretty_midi.note_name_to_number('A'), pretty_midi.note_name_to_number('Bb'), pretty_midi.note_name_to_number('B')]
for i, note in enumerate(notes):
    bass_note = pretty_midi.Note(
        velocity=64,
        pitch=note,
        start=i * 0.375 + 3.0,  # Bar 3 starts at 3.0s
        end=(i + 1) * 0.375 + 3.0
    )
    bass_instrument.notes.append(bass_note)

# Bar 4:
notes = [pretty_midi.note_name_to_number('C'), pretty_midi.note_name_to_number('D'), pretty_midi.note_name_to_number('E'), pretty_midi.note_name_to_number('F')]
for i, note in enumerate(notes):
    bass_note = pretty_midi.Note(
        velocity=64,
        pitch=note,
        start=i * 0.375 + 4.5,  # Bar 4 starts at 4.5s
        end=(i + 1) * 0.375 + 4.5
    )
    bass_instrument.notes.append(bass_note)

pm.instruments.append(bass_instrument)

# ============= PIANO (Diane) =============
piano_program = pretty_midi.instrument_name_to_program('Acoustic Grand Piano')
piano_instrument = pretty_midi.Instrument(program=piano_program)

# Comp on 2 and 4 — 7th chords
# Bar 2: Dm7
notes = [pretty_midi.note_name_to_number('D'), pretty_midi.note_name_to_number('F'), pretty_midi.note_name_to_number('A'), pretty_midi.note_name_to_number('C')]
for note in notes:
    piano_note = pretty_midi.Note(
        velocity=80,
        pitch=note,
        start=2.0,  # On beat 2
        end=2.0 + 0.375
    )
    piano_instrument.notes.append(piano_note)

# Bar 3: Gm7
notes = [pretty_midi.note_name_to_number('G'), pretty_midi.note_name_to_number('Bb'), pretty_midi.note_name_to_number('D'), pretty_midi.note_name_to_number('F')]
for note in notes:
    piano_note = pretty_midi.Note(
        velocity=80,
        pitch=note,
        start=3.5,  # On beat 2 of bar 3
        end=3.5 + 0.375
    )
    piano_instrument.notes.append(piano_note)

# Bar 4: Cm7
notes = [pretty_midi.note_name_to_number('C'), pretty_midi.note_name_to_number('Eb'), pretty_midi.note_name_to_number('G'), pretty_midi.note_name_to_number('Bb')]
for note in notes:
    piano_note = pretty_midi.Note(
        velocity=80,
        pitch=note,
        start=5.0,  # On beat 2 of bar 4
        end=5.0 + 0.375
    )
    piano_instrument.notes.append(piano_note)

pm.instruments.append(piano_instrument)

# ============= TENOR SAX (Dante) =============
sax_program = pretty_midi.instrument_name_to_program('Tenor Saxophone')
sax_instrument = pretty_midi.Instrument(program=sax_program)

# Motif: D, F, G, Bb — short, searching, unresolved
# Start at 1.5s (bar 2)
notes = [
    pretty_midi.Note(velocity=100, pitch=pretty_midi.note_name_to_number('D'), start=1.5, end=1.75),
    pretty_midi.Note(velocity=100, pitch=pretty_midi.note_name_to_number('F'), start=2.0, end=2.25),
    pretty_midi.Note(velocity=100, pitch=pretty_midi.note_name_to_number('G'), start=2.5, end=2.75),
    pretty_midi.Note(velocity=100, pitch=pretty_midi.note_name_to_number('Bb'), start=3.0, end=3.25)
]

for note in notes:
    sax_instrument.notes.append(note)

pm.instruments.append(sax_instrument)

# Save the MIDI file
pm.write("jazz_intro_dminor.mid")
