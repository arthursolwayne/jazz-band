
import pretty_midi

# Create a new PrettyMIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Create instruments
bass_program = pretty_midi.instrument_name_to_program('Double Bass')
piano_program = pretty_midi.instrument_name_to_program('Acoustic Piano')
sax_program = pretty_midi.instrument_name_to_program('Tenor Saxophone')
drums_program = pretty_midi.instrument_name_to_program('Acoustic Grand Piano')  # MIDI uses piano for drums

# Add instruments
bass = pretty_midi.Instrument(program=bass_program)
piano = pretty_midi.Instrument(program=piano_program)
sax = pretty_midi.Instrument(program=sax_program)
drums = pretty_midi.Instrument(program=drums_program, is_drum=True)

pm.instruments = [bass, piano, sax, drums]

# Define time per bar in seconds
bar_duration = 1.5  # 160 BPM = 60 / 160 = 0.375 seconds per beat, 4 beats per bar = 1.5s
beat = 0.375

# Define D major key
D_major = [2, 4, 7, 9, 11, 14, 16]  # D, F#, A, B, C#, F, G

# -----------------------------
# DRUMS: Bar 1 (only)
# -----------------------------
# Kick on 1 and 3, snare on 2 and 4, hihat on every 8th
for i in range(0, 4):
    # Kick on 1 and 3
    if i == 0 or i == 2:
        note = pretty_midi.Note(
            velocity=80,
            pitch=36,  # Kick
            start=i * beat,
            end=i * beat + 0.25
        )
        drums.notes.append(note)
    # Snare on 2 and 4
    if i == 1 or i == 3:
        note = pretty_midi.Note(
            velocity=85,
            pitch=38,  # Snare
            start=i * beat,
            end=i * beat + 0.25
        )
        drums.notes.append(note)
    # Hihat on every 8th
    for j in range(2):
        note = pretty_midi.Note(
            velocity=60,
            pitch=42,  # Hihat
            start=(i * 2 + j) * beat / 2,
            end=(i * 2 + j) * beat / 2 + 0.1
        )
        drums.notes.append(note)

# -----------------------------
# BASS: Bars 2–4
# -----------------------------
# Walking bass line in D major
# D -> F# -> G -> A -> B -> D -> F# -> G
# Add chromatic approaches
bass_notes = [
    (pretty_midi.Note(velocity=80, pitch=2, start=bar_duration, end=bar_duration + 0.25)),  # D
    (pretty_midi.Note(velocity=80, pitch=4, start=bar_duration + 0.25, end=bar_duration + 0.5)),  # F#
    (pretty_midi.Note(velocity=80, pitch=3, start=bar_duration + 0.5, end=bar_duration + 0.75)),  # Gb (chromatic)
    (pretty_midi.Note(velocity=80, pitch=5, start=bar_duration + 0.75, end=bar_duration + 1.0)),  # G
    (pretty_midi.Note(velocity=80, pitch=7, start=bar_duration + 1.0, end=bar_duration + 1.25)),  # A
    (pretty_midi.Note(velocity=80, pitch=9, start=bar_duration + 1.25, end=bar_duration + 1.5)),  # B
    (pretty_midi.Note(velocity=80, pitch=4, start=bar_duration + 1.5, end=bar_duration + 1.75)),  # F#
    (pretty_midi.Note(velocity=80, pitch=3, start=bar_duration + 1.75, end=bar_duration + 2.0)),  # Gb
    (pretty_midi.Note(velocity=80, pitch=5, start=bar_duration + 2.0, end=bar_duration + 2.25)),  # G
    (pretty_midi.Note(velocity=80, pitch=2, start=bar_duration + 2.25, end=bar_duration + 2.5)),  # D
    (pretty_midi.Note(velocity=80, pitch=4, start=bar_duration + 2.5, end=bar_duration + 2.75)),  # F#
    (pretty_midi.Note(velocity=80, pitch=3, start=bar_duration + 2.75, end=bar_duration + 3.0)),  # Gb
    (pretty_midi.Note(velocity=80, pitch=5, start=bar_duration + 3.0, end=bar_duration + 3.25)),  # G
    (pretty_midi.Note(velocity=80, pitch=7, start=bar_duration + 3.25, end=bar_duration + 3.5)),  # A
    (pretty_midi.Note(velocity=80, pitch=9, start=bar_duration + 3.5, end=bar_duration + 3.75)),  # B
    (pretty_midi.Note(velocity=80, pitch=2, start=bar_duration + 3.75, end=bar_duration + 4.0)),  # D
]

for note in bass_notes:
    bass.notes.append(note)

# -----------------------------
# PIANO: Bars 2–4
# -----------------------------
# Comp on 2 and 4
# D7 chords: D A C# F
# 7th chords, comp at 2 and 4 of each bar

for bar in range(2, 4 + 1):
    start_time = bar * bar_duration
    for beat_index in [1, 3]:  # 2nd and 4th beat
        note_start = start_time + beat_index * beat
        # D7 chord: D (2), A (7), C# (4), F (5)
        for pitch in [2, 7, 4, 5]:
            note = pretty_midi.Note(
                velocity=80,
                pitch=pitch,
                start=note_start,
                end=note_start + 0.25
            )
            piano.notes.append(note)

# -----------------------------
# SAX: Bars 2–4
# -----------------------------
# Questioning motif: D - F# - G - rest (hanging)
# Start on D (2), F# (4), G (5), then rest
# Make it sing, not a run

sax_notes = [
    pretty_midi.Note(velocity=100, pitch=2, start=bar_duration, end=bar_duration + 0.25),   # D
    pretty_midi.Note(velocity=100, pitch=4, start=bar_duration + 0.25, end=bar_duration + 0.5),  # F#
    pretty_midi.Note(velocity=100, pitch=5, start=bar_duration + 0.5, end=bar_duration + 0.75),  # G
    # Leave it hanging — rest on the last beat
]

for note in sax_notes:
    sax.notes.append(note)

# -----------------------------
# DRUMS: Bars 2–4
# -----------------------------
# Kick on 1 and 3, snare on 2 and 4, hihat on every 8th

for i in range(0, 4):
    # Kick on 1 and 3
    if i == 0 or i == 2:
        note = pretty_midi.Note(
            velocity=80,
            pitch=36,  # Kick
            start=bar_duration + i * beat,
            end=bar_duration + i * beat + 0.25
        )
        drums.notes.append(note)
    # Snare on 2 and 4
    if i == 1 or i == 3:
        note = pretty_midi.Note(
            velocity=85,
            pitch=38,  # Snare
            start=bar_duration + i * beat,
            end=bar_duration + i * beat + 0.25
        )
        drums.notes.append(note)
    # Hihat on every 8th
    for j in range(2):
        note = pretty_midi.Note(
            velocity=60,
            pitch=42,  # Hihat
            start=bar_duration + (i * 2 + j) * beat / 2,
            end=bar_duration + (i * 2 + j) * beat / 2 + 0.1
        )
        drums.notes.append(note)

# Save the MIDI file
pm.write('jazz_intro.mid')

print("MIDI file saved as 'jazz_intro.mid'")
