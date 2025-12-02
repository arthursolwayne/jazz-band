
import pretty_midi

# Create a new PrettyMIDI object
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Set the time signature to 4/4
midi.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0)]

# Set the key signature to F major (no sharps or flats)
midi.key_signature_changes = [pretty_midi.KeySignature(0, 0, 0)]  # F major

# Define the tempo (160 BPM)
midi.tempo_changes = [pretty_midi.TempoChange(160, 0)]

# Create instruments
drums_program = pretty_midi.instrument_name_to_program('Acoustic Drum Kit')
bass_program = pretty_midi.instrument_name_to_program('Double Bass')
piano_program = pretty_midi.instrument_name_to_program('Electric Piano 1')
sax_program = pretty_midi.instrument_name_to_program('Tenor Saxophone')

drums = pretty_midi.Instrument(program=drums_program)
bass = pretty_midi.Instrument(program=bass_program)
piano = pretty_midi.Instrument(program=piano_program)
sax = pretty_midi.Instrument(program=sax_program)

# Add instruments to MIDI
midi.instruments = [drums, bass, piano, sax]

# Time per bar (160 BPM = 60 / 160 = 0.375 seconds per beat, 4/4 time = 1.5 seconds per bar)
bar_length = 1.5
note_duration = 0.375  # 1/4 note at 160 BPM

# -----------------------------
# DRUMS (Little Ray) - Bars 1-4
# -----------------------------
# Bar 1: Kick on 1 and 3, snare on 2 and 4
if bar_length >= 1.5:
    # Bar 1
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375))  # Kick on 1
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125))  # Snare on 2
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5))  # Kick on 3

# Bar 2: Kick on 1 and 3, snare on 2 and 4, hihat on all eighths
for i in range(0, 2):
    time = i * bar_length
    # Kick on 1
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.375))
    # Snare on 2
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=time + 0.75, end=time + 1.125))
    # Kick on 3
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=time + 1.125, end=time + 1.5))
    # Hihat on every eighth
    for j in range(0, 8):
        drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=time + (j * 0.375), end=time + (j * 0.375) + 0.125))

# -----------------------------
# BASS (Marcus) - Bars 2-4
# -----------------------------
# Walking line in F major, chromatic approach on the 3rd
# Notes: F, G, A, Bb, C, D, E, F

# Bar 2: F -> Gb (chromatic approach to G)
bass.notes.append(pretty_midi.Note(velocity=90, pitch=70, start=1.5, end=1.875))  # F
bass.notes.append(pretty_midi.Note(velocity=90, pitch=68, start=1.875, end=2.25))  # Gb

# Bar 3: G -> Ab (chromatic approach to A)
bass.notes.append(pretty_midi.Note(velocity=90, pitch=71, start=2.25, end=2.625))  # G
bass.notes.append(pretty_midi.Note(velocity=90, pitch=69, start=2.625, end=3.0))  # Ab

# Bar 4: A -> Bb (chromatic approach to Bb)
bass.notes.append(pretty_midi.Note(velocity=90, pitch=72, start=3.0, end=3.375))  # A
bass.notes.append(pretty_midi.Note(velocity=90, pitch=70, start=3.375, end=3.75))  # Bb

# -----------------------------
# PIANO (Diane) - Bars 2-4
# -----------------------------
# Comp on 2 and 4, 7th chords
# F7: F, A, C, E
# B7: B, D#, F#, A

# Bar 2: F7 on beat 2
piano.notes.append(pretty_midi.Note(velocity=95, pitch=70, start=1.875, end=2.25))  # F
piano.notes.append(pretty_midi.Note(velocity=95, pitch=74, start=1.875, end=2.25))  # A
piano.notes.append(pretty_midi.Note(velocity=95, pitch=76, start=1.875, end=2.25))  # C
piano.notes.append(pretty_midi.Note(velocity=95, pitch=79, start=1.875, end=2.25))  # E

# Bar 3: B7 on beat 4
piano.notes.append(pretty_midi.Note(velocity=95, pitch=76, start=3.375, end=3.75))  # B
piano.notes.append(pretty_midi.Note(velocity=95, pitch=80, start=3.375, end=3.75))  # D#
piano.notes.append(pretty_midi.Note(velocity=95, pitch=82, start=3.375, end=3.75))  # F#
piano.notes.append(pretty_midi.Note(velocity=95, pitch=85, start=3.375, end=3.75))  # A

# Bar 4: F7 again
piano.notes.append(pretty_midi.Note(velocity=95, pitch=70, start=3.75, end=4.125))  # F
piano.notes.append(pretty_midi.Note(velocity=95, pitch=74, start=3.75, end=4.125))  # A
piano.notes.append(pretty_midi.Note(velocity=95, pitch=76, start=3.75, end=4.125))  # C
piano.notes.append(pretty_midi.Note(velocity=95, pitch=79, start=3.75, end=4.125))  # E

# -----------------------------
# SAX (You) - Bars 2-4
# -----------------------------
# Short motif: F, Bb, F, G (rhythmic and tension/resolution)
# Bar 2: F (beat 1), Bb (beat 2), F (beat 3), G (beat 4)

# Bar 2
sax.notes.append(pretty_midi.Note(velocity=100, pitch=70, start=1.5, end=1.875))  # F
sax.notes.append(pretty_midi.Note(velocity=100, pitch=74, start=1.875, end=2.25))  # Bb
sax.notes.append(pretty_midi.Note(velocity=100, pitch=70, start=2.25, end=2.625))  # F
sax.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=2.625, end=3.0))  # G

# Bar 3: Repeat the motif with a slight variation in rhythm
sax.notes.append(pretty_midi.Note(velocity=100, pitch=70, start=2.625, end=2.875))  # F (shorter)
sax.notes.append(pretty_midi.Note(velocity=100, pitch=74, start=2.875, end=3.25))  # Bb
sax.notes.append(pretty_midi.Note(velocity=100, pitch=70, start=3.25, end=3.5))  # F (shorter)
sax.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=3.5, end=3.75))  # G (shorter)

# Write the MIDI file to disk
midi.write("dante_intro.mid")

print("MIDI file created: 'dante_intro.mid'")
