
import pretty_midi

# Create a PrettyMIDI object with a tempo of 160 BPM (160 beats per minute)
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Define time signatures: 4/4
time_signature = pretty_midi.TimeSignature(numerator=4, denominator=4, time=0.0)
pm.time_signature_changes = [time_signature]

# Define key signature: D minor (key number 1 for D minor)
key_signature = pretty_midi.KeySignature(key_number=1, time=0.0)
pm.key_signature_changes = [key_signature]

# Helper function to convert beat to seconds
def beat_to_sec(beats):
    return beats / (pm.initial_tempo / 60)

# Create instruments
# Drums
drums_program = pretty_midi.instrument_name_to_program('Acoustic Grand Piano')
drums = pretty_midi.Instrument(program=drums_program, is_drum=True)
pm.instruments.append(drums)

# Bass
bass_program = pretty_midi.instrument_name_to_program('Fretless Bass')
bass = pretty_midi.Instrument(program=bass_program)
pm.instruments.append(bass)

# Piano
piano_program = pretty_midi.instrument_name_to_program('Electric Piano 1')
piano = pretty_midi.Instrument(program=piano_program)
pm.instruments.append(piano)

# Tenor Sax (MIDI program: 64)
sax_program = pretty_midi.instrument_name_to_program('Tenor Saxophone')
sax = pretty_midi.Instrument(program=sax_program)
pm.instruments.append(sax)

# -----------------------------
# DRUMS: Bar 1 (0.0 to 1.5 seconds)
# Kick on 1 & 3, Snare on 2 & 4, Hihat on every eighth
# Bar is 1.5 seconds, 4 beats = 6.0 seconds total

# Bar 1: only hihat
for i in range(8):  # 8 eighth notes per bar
    note = pretty_midi.Note(
        velocity=80,
        pitch=42,  # Closed hihat (MIDI 42)
        start=beat_to_sec(i / 8),
        end=beat_to_sec((i + 1) / 8)
    )
    drums.notes.append(note)

# Bar 2: Kick on 1 & 3, Snare on 2 & 4, Hihat on every eighth
for i in range(8):
    # Hihat
    note = pretty_midi.Note(
        velocity=80,
        pitch=42,
        start=beat_to_sec(i / 8 + 1.5),
        end=beat_to_sec((i + 1) / 8 + 1.5)
    )
    drums.notes.append(note)

    # Kick on beat 1 (i=0) and 3 (i=2)
    if i == 0 or i == 2:
        note = pretty_midi.Note(
            velocity=100,
            pitch=36,  # Kick drum (MIDI 36)
            start=beat_to_sec(i / 8 + 1.5),
            end=beat_to_sec((i + 1) / 8 + 1.5)
        )
        drums.notes.append(note)

    # Snare on beat 2 (i=1) and 4 (i=3)
    if i == 1 or i == 3:
        note = pretty_midi.Note(
            velocity=110,
            pitch=38,  # Snare drum (MIDI 38)
            start=beat_to_sec(i / 8 + 1.5),
            end=beat_to_sec((i + 1) / 8 + 1.5)
        )
        drums.notes.append(note)

# Bar 3 and 4 (same as Bar 2, continued)
for i in range(8):
    # Hihat
    note = pretty_midi.Note(
        velocity=80,
        pitch=42,
        start=beat_to_sec(i / 8 + 3.0),
        end=beat_to_sec((i + 1) / 8 + 3.0)
    )
    drums.notes.append(note)

    # Kick on beat 1 (i=0) and 3 (i=2)
    if i == 0 or i == 2:
        note = pretty_midi.Note(
            velocity=100,
            pitch=36,
            start=beat_to_sec(i / 8 + 3.0),
            end=beat_to_sec((i + 1) / 8 + 3.0)
        )
        drums.notes.append(note)

    # Snare on beat 2 (i=1) and 4 (i=3)
    if i == 1 or i == 3:
        note = pretty_midi.Note(
            velocity=110,
            pitch=38,
            start=beat_to_sec(i / 8 + 3.0),
            end=beat_to_sec((i + 1) / 8 + 3.0)
        )
        drums.notes.append(note)

# -----------------------------
# BASS: Bar 1-4, walking line in D minor (D2-G2, MIDI 38-43)

# Root note D2 (MIDI 38)
# Fifths: A2 (MIDI 43)
# Chromatic approaches: C#2 (MIDI 37), E2 (MIDI 40)

# Bar 1
bass_notes = [
    (38, 0.0, 0.375),   # D2 on beat 1
    (37, 0.375, 0.75),  # C#2 on & of 1
    (38, 0.75, 1.125),  # D2 on beat 2
    (43, 1.125, 1.5),   # A2 on & of 2
]

for pitch, start, end in bass_notes:
    note = pretty_midi.Note(velocity=80, pitch=pitch, start=start, end=end)
    bass.notes.append(note)

# Bar 2
bass_notes = [
    (43, 1.5, 1.875),   # A2 on beat 1
    (40, 1.875, 2.25),  # E2 on & of 1
    (43, 2.25, 2.625),  # A2 on beat 2
    (38, 2.625, 3.0),   # D2 on & of 2
]

for pitch, start, end in bass_notes:
    note = pretty_midi.Note(velocity=80, pitch=pitch, start=start, end=end)
    bass.notes.append(note)

# Bar 3
bass_notes = [
    (38, 3.0, 3.375),   # D2 on beat 1
    (37, 3.375, 3.75),  # C#2 on & of 1
    (38, 3.75, 4.125),  # D2 on beat 2
    (43, 4.125, 4.5),   # A2 on & of 2
]

for pitch, start, end in bass_notes:
    note = pretty_midi.Note(velocity=80, pitch=pitch, start=start, end=end)
    bass.notes.append(note)

# Bar 4
bass_notes = [
    (43, 4.5, 4.875),   # A2 on beat 1
    (40, 4.875, 5.25),  # E2 on & of 1
    (43, 5.25, 5.625),  # A2 on beat 2
    (38, 5.625, 6.0),   # D2 on & of 2
]

for pitch, start, end in bass_notes:
    note = pretty_midi.Note(velocity=80, pitch=pitch, start=start, end=end)
    bass.notes.append(note)

# -----------------------------
# PIANO: Open voicings, one chord per bar, resolve on the last bar

# Bar 1: Dm7 (D - F - A - C)
# Open voicing: D (MIDI 62), F (65), A (69), C (60) (spaced out)
# Start on beat 2 (0.75s)
note = pretty_midi.Note(velocity=90, pitch=62, start=0.75, end=1.5)
piano.notes.append(note)
note = pretty_midi.Note(velocity=90, pitch=65, start=0.75, end=1.5)
piano.notes.append(note)
note = pretty_midi.Note(velocity=90, pitch=69, start=0.75, end=1.5)
piano.notes.append(note)
note = pretty_midi.Note(velocity=90, pitch=60, start=0.75, end=1.5)
piano.notes.append(note)

# Bar 2: Gm7 (G - Bb - D - F)
# Open voicing: G (67), Bb (70), D (62), F (65)
note = pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=2.25)
piano.notes.append(note)
note = pretty_midi.Note(velocity=90, pitch=70, start=1.5, end=2.25)
piano.notes.append(note)
note = pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=2.25)
piano.notes.append(note)
note = pretty_midi.Note(velocity=90, pitch=65, start=1.5, end=2.25)
piano.notes.append(note)

# Bar 3: Cm7 (C - Eb - G - Bb)
# Open voicing: C (60), Eb (64), G (67), Bb (70)
note = pretty_midi.Note(velocity=90, pitch=60, start=3.0, end=3.75)
piano.notes.append(note)
note = pretty_midi.Note(velocity=90, pitch=64, start=3.0, end=3.75)
piano.notes.append(note)
note = pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.75)
piano.notes.append(note)
note = pretty_midi.Note(velocity=90, pitch=70, start=3.0, end=3.75)
piano.notes.append(note)

# Bar 4: Dm7 (D - F - A - C), resolution
note = pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=6.0)
piano.notes.append(note)
note = pretty_midi.Note(velocity=90, pitch=65, start=4.5, end=6.0)
piano.notes.append(note)
note = pretty_midi.Note(velocity=90, pitch=69, start=4.5, end=6.0)
piano.notes.append(note)
note = pretty_midi.Note(velocity=90, pitch=60, start=4.5, end=6.0)
piano.notes.append(note)

# -----------------------------
# SAX: Tenor sax motif — one phrase, start it, leave it hanging, come back

# Sax motif: D (62) - F (65) - A (69) - D (62), syncopated start
# Bar 1: 0.75s (beat 2) starts the motif

# First note: D (62) on beat 2 (0.75s)
note = pretty_midi.Note(velocity=100, pitch=62, start=0.75, end=1.0)
sax.notes.append(note)

# Second note: F (65) on beat 2 & (1.125s)
note = pretty_midi.Note(velocity=100, pitch=65, start=1.125, end=1.375)
sax.notes.append(note)

# Third note: A (69) on beat 3 (1.5s)
note = pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.75)
sax.notes.append(note)

# Final note: D (62) on beat 4 (2.25s)
note = pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.5)
sax.notes.append(note)

# Leave it hanging — no resolution, just the question

# End the piece at 6.0 seconds (4 bars)
pm.write('jazz_intro.mid')
print("MIDI file written: jazz_intro.mid")
