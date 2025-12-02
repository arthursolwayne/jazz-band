
import pretty_midi

# Create a new PrettyMIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Set the time signature (4/4)
pm.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0.0)]

# Set the key signature (F major, no sharps/flats)
pm.key_signature_changes = [pretty_midi.KeySignature(0, 0.0)]

# Define the note values and time in seconds
note_length = 0.375  # 1 beat at 160 BPM
bar_length = 1.5    # 4 beats per bar at 160 BPM
time = 0.0

# Add instruments
# 1. Drums (Little Ray)
drums_program = pretty_midi.instrument_name_to_program('Acoustic Grand Piano')
drums = pretty_midi.Instrument(program=drums_program)
pm.instruments.append(drums)

# 2. Bass (Marcus)
bass_program = pretty_midi.instrument_name_to_program('Double Bass')
bass = pretty_midi.Instrument(program=bass_program)
pm.instruments.append(bass)

# 3. Piano (Diane)
piano_program = pretty_midi.instrument_name_to_program('Electric Piano 1')
piano = pretty_midi.Instrument(program=piano_program)
pm.instruments.append(piano)

# 4. Tenor Sax (You)
sax_program = pretty_midi.instrument_name_to_program('Tenor Saxophone')
sax = pretty_midi.Instrument(program=sax_program)
pm.instruments.append(sax)

# --- Bar 1: Little Ray (Drums) alone ---
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth

# Kick on 1 and 3
drums.notes.append(pretty_midi.Note(velocity=80, pitch=36, start=0.0, end=0.375))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=36, start=1.125, end=1.5))

# Snare on 2 and 4
drums.notes.append(pretty_midi.Note(velocity=90, pitch=38, start=0.375, end=0.75))
drums.notes.append(pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875))

# Hi-hat on every eighth
for t in [0.0, 0.375, 0.75, 1.125, 1.5, 1.875]:
    drums.notes.append(pretty_midi.Note(velocity=60, pitch=42, start=t, end=t + 0.1875))

time = 1.5  # End of Bar 1

# --- Bar 2: Everyone comes in. Tenor Sax takes the melody ---
# Melody: F - Bb - C - D (F major scale, but with a twist)
# Notes: F (0.0), Bb (0.375), C (0.75), D (1.125)

# Tenor Sax (You)
sax.notes.append(pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.5 + 0.375))  # F
sax.notes.append(pretty_midi.Note(velocity=100, pitch=60, start=1.875, end=1.875 + 0.375))  # Bb
sax.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.25 + 0.375))  # C
sax.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=2.625, end=2.625 + 0.375))  # D

# Marcus (Bass) - Walking line, chromatic approach
# F - E - D - C - Bb - B - C - D
bass.notes.append(pretty_midi.Note(velocity=80, pitch=44, start=1.5, end=1.875))  # F
bass.notes.append(pretty_midi.Note(velocity=80, pitch=43, start=1.875, end=2.25))  # E
bass.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625))  # D
bass.notes.append(pretty_midi.Note(velocity=80, pitch=41, start=2.625, end=3.0))  # C

# Diane (Piano) - Comp on 2 and 4 with 7th chords
# F7 on beat 2
piano.notes.append(pretty_midi.Note(velocity=90, pitch=64, start=1.875, end=2.25))  # F
piano.notes.append(pretty_midi.Note(velocity=90, pitch=69, start=1.875, end=2.25))  # Bb
piano.notes.append(pretty_midi.Note(velocity=90, pitch=71, start=1.875, end=2.25))  # D
piano.notes.append(pretty_midi.Note(velocity=90, pitch=72, start=1.875, end=2.25))  # F7

# F7 on beat 4
piano.notes.append(pretty_midi.Note(velocity=90, pitch=64, start=3.0, end=3.375))  # F
piano.notes.append(pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=3.375))  # Bb
piano.notes.append(pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.375))  # D
piano.notes.append(pretty_midi.Note(velocity=90, pitch=72, start=3.0, end=3.375))  # F7

# --- Bar 3: Tenor Sax leaves it hanging, a question ---
# Tenor Sax: D (1.5), C (1.875), Bb (2.25), D (2.625) — but don't resolve

# Tenor Sax (You)
sax.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.375))  # D
sax.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=3.375, end=3.75))  # C
sax.notes.append(pretty_midi.Note(velocity=100, pitch=60, start=3.75, end=4.125))  # Bb
sax.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=4.125, end=4.5))  # D

# Marcus (Bass) - Walking line (cont)
bass.notes.append(pretty_midi.Note(velocity=80, pitch=60, start=3.0, end=3.375))  # Bb
bass.notes.append(pretty_midi.Note(velocity=80, pitch=62, start=3.375, end=3.75))  # B
bass.notes.append(pretty_midi.Note(velocity=80, pitch=64, start=3.75, end=4.125))  # C
bass.notes.append(pretty_midi.Note(velocity=80, pitch=65, start=4.125, end=4.5))  # D

# Diane (Piano) - Comp on 2 and 4 (F7 again)
# F7 on beat 2
piano.notes.append(pretty_midi.Note(velocity=90, pitch=64, start=3.375, end=3.75))  # F
piano.notes.append(pretty_midi.Note(velocity=90, pitch=69, start=3.375, end=3.75))  # Bb
piano.notes.append(pretty_midi.Note(velocity=90, pitch=71, start=3.375, end=3.75))  # D
piano.notes.append(pretty_midi.Note(velocity=90, pitch=72, start=3.375, end=3.75))  # F7

# F7 on beat 4
piano.notes.append(pretty_midi.Note(velocity=90, pitch=64, start=4.5, end=4.875))  # F
piano.notes.append(pretty_midi.Note(velocity=90, pitch=69, start=4.5, end=4.875))  # Bb
piano.notes.append(pretty_midi.Note(velocity=90, pitch=71, start=4.5, end=4.875))  # D
piano.notes.append(pretty_midi.Note(velocity=90, pitch=72, start=4.5, end=4.875))  # F7

# --- Bar 4: End with a question, not a statement ---
# Tenor Sax: D (3.0), C (3.375), Bb (3.75), B (4.125) — ends on a suspension

# Tenor Sax (You)
sax.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.875))  # D
sax.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=4.875, end=5.25))  # C
sax.notes.append(pretty_midi.Note(velocity=100, pitch=60, start=5.25, end=5.625))  # Bb
sax.notes.append(pretty_midi.Note(velocity=100, pitch=61, start=5.625, end=6.0))  # B (suspension)

# Marcus (Bass) - Walking line (cont)
bass.notes.append(pretty_midi.Note(velocity=80, pitch=67, start=4.5, end=4.875))  # E
bass.notes.append(pretty_midi.Note(velocity=80, pitch=69, start=4.875, end=5.25))  # F
bass.notes.append(pretty_midi.Note(velocity=80, pitch=71, start=5.25, end=5.625))  # G
bass.notes.append(pretty_midi.Note(velocity=80, pitch=72, start=5.625, end=6.0))  # G# (chromatic lead)

# Diane (Piano) - Comp on 2 and 4 (F7 again)
# F7 on beat 2
piano.notes.append(pretty_midi.Note(velocity=90, pitch=64, start=4.875, end=5.25))  # F
piano.notes.append(pretty_midi.Note(velocity=90, pitch=69, start=4.875, end=5.25))  # Bb
piano.notes.append(pretty_midi.Note(velocity=90, pitch=71, start=4.875, end=5.25))  # D
piano.notes.append(pretty_midi.Note(velocity=90, pitch=72, start=4.875, end=5.25))  # F7

# F7 on beat 4
piano.notes.append(pretty_midi.Note(velocity=90, pitch=64, start=6.0, end=6.375))  # F
piano.notes.append(pretty_midi.Note(velocity=90, pitch=69, start=6.0, end=6.375))  # Bb
piano.notes.append(pretty_midi.Note(velocity=90, pitch=71, start=6.0, end=6.375))  # D
piano.notes.append(pretty_midi.Note(velocity=90, pitch=72, start=6.0, end=6.375))  # F7

# Save the MIDI file
pm.write("intro_wayne.mid")
