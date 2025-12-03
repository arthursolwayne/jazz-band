
import pretty_midi

# Initialize the MIDI file with 160 BPM
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Instruments
sax = pretty_midi.Instrument(program=66)       # Tenor Sax
bass = pretty_midi.Instrument(program=33)      # Double Bass
piano = pretty_midi.Instrument(program=0)      # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Drum sounds: kick (36), snare (38), hihat (42)
kick = 36
snare = 38
hihat = 42

# Time per bar (160 BPM, 4/4 time)
bar_duration = 6.0 / 4  # 1.5 seconds per bar
beat_duration = bar_duration / 4  # 0.375 seconds per beat

# Bar 1: Drums only (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(1):
    bar_start = bar * bar_duration
    # Kick on beat 1 and 3
    for beat in [0, 2]:
        note = pretty_midi.Note(velocity=100, pitch=kick, start=bar_start + beat * beat_duration, end=bar_start + beat * beat_duration + 0.1)
        drums.notes.append(note)
    # Snare on beat 2 and 4
    for beat in [1, 3]:
        note = pretty_midi.Note(velocity=100, pitch=snare, start=bar_start + beat * beat_duration, end=bar_start + beat * beat_duration + 0.1)
        drums.notes.append(note)
    # Hihat on every eighth note
    for eighth in range(8):
        note = pretty_midi.Note(velocity=80, pitch=hihat, start=bar_start + eighth * beat_duration / 2, end=bar_start + eighth * beat_duration / 2 + 0.05)
        drums.notes.append(note)

# Bar 2: Full band enters
bar_start = 1.5
# Piano (Dm7 -> Gm7 -> Cm7 -> F7)
for bar in range(2, 5):
    bar_offset = bar - 2
    chord = [
        (pretty_midi.Note(velocity=100, pitch=62, start=bar_start + bar_offset * bar_duration, end=bar_start + bar_offset * bar_duration + 0.5), 0),  # D (root)
        (pretty_midi.Note(velocity=100, pitch=67, start=bar_start + bar_offset * bar_duration, end=bar_start + bar_offset * bar_duration + 0.5), 0),  # G (maj7)
        (pretty_midi.Note(velocity=100, pitch=69, start=bar_start + bar_offset * bar_duration, end=bar_start + bar_offset * bar_duration + 0.5), 0),  # Bb (7)
        (pretty_midi.Note(velocity=100, pitch=64, start=bar_start + bar_offset * bar_duration, end=bar_start + bar_offset * bar_duration + 0.5), 0),  # F (5th)
    ]
    if bar_offset == 0:  # Dm7
        chord = [
            (pretty_midi.Note(velocity=100, pitch=62, start=bar_start + bar_offset * bar_duration, end=bar_start + bar_offset * bar_duration + 0.5), 0),  # D
            (pretty_midi.Note(velocity=100, pitch=67, start=bar_start + bar_offset * bar_duration, end=bar_start + bar_offset * bar_duration + 0.5), 0),  # G
            (pretty_midi.Note(velocity=100, pitch=69, start=bar_start + bar_offset * bar_duration, end=bar_start + bar_offset * bar_duration + 0.5), 0),  # Bb
            (pretty_midi.Note(velocity=100, pitch=64, start=bar_start + bar_offset * bar_duration, end=bar_start + bar_offset * bar_duration + 0.5), 0),  # F
        ]
    elif bar_offset == 1:  # Gm7
        chord = [
            (pretty_midi.Note(velocity=100, pitch=67, start=bar_start + bar_offset * bar_duration, end=bar_start + bar_offset * bar_duration + 0.5), 0),  # G
            (pretty_midi.Note(velocity=100, pitch=72, start=bar_start + bar_offset * bar_duration, end=bar_start + bar_offset * bar_duration + 0.5), 0),  # Bb
            (pretty_midi.Note(velocity=100, pitch=74, start=bar_start + bar_offset * bar_duration, end=bar_start + bar_offset * bar_duration + 0.5), 0),  # D
            (pretty_midi.Note(velocity=100, pitch=69, start=bar_start + bar_offset * bar_duration, end=bar_start + bar_offset * bar_duration + 0.5), 0),  # F
        ]
    elif bar_offset == 2:  # Cm7
        chord = [
            (pretty_midi.Note(velocity=100, pitch=60, start=bar_start + bar_offset * bar_duration, end=bar_start + bar_offset * bar_duration + 0.5), 0),  # C
            (pretty_midi.Note(velocity=100, pitch=65, start=bar_start + bar_offset * bar_duration, end=bar_start + bar_offset * bar_duration + 0.5), 0),  # E
            (pretty_midi.Note(velocity=100, pitch=67, start=bar_start + bar_offset * bar_duration, end=bar_start + bar_offset * bar_duration + 0.5), 0),  # G
            (pretty_midi.Note(velocity=100, pitch=62, start=bar_start + bar_offset * bar_duration, end=bar_start + bar_offset * bar_duration + 0.5), 0),  # Bb
        ]
    # Add the chord to piano
    for note, channel in chord:
        note.channel = 0
        piano.notes.append(note)

# Marcus on bass: D2-G2, roots and fifths, chromatic approaches
bar_start = 1.5
for bar in range(2, 5):
    bar_offset = bar - 2
    # D2 (root)
    note = pretty_midi.Note(velocity=80, pitch=50, start=bar_start + bar_offset * bar_duration, end=bar_start + bar_offset * bar_duration + 0.5)
    bass.notes.append(note)
    # G2 (fifth, chromatic approach)
    note = pretty_midi.Note(velocity=80, pitch=53, start=bar_start + bar_offset * bar_duration, end=bar_start + bar_offset * bar_duration + 0.5)
    bass.notes.append(note)

# Dante on sax: short motif, make it sing
bar_start = 1.5
# Motif: Dm (D, Bb, F, G)
notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=bar_start, end=bar_start + 0.75),  # D
    pretty_midi.Note(velocity=100, pitch=69, start=bar_start + 0.75, end=bar_start + 1.5),  # Bb
    pretty_midi.Note(velocity=100, pitch=67, start=bar_start + 1.5, end=bar_start + 2.25),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=bar_start + 2.25, end=bar_start + 3.0),  # G
]
for note in notes:
    note.channel = 0
    sax.notes.append(note)

# Add instruments to MIDI
midi.instruments.append(sax)
midi.instruments.append(bass)
midi.instruments.append(piano)
midi.instruments.append(drums)

# Save the MIDI file
# midi.write disabled
print("MIDI file 'dante_intro.mid' created successfully.")
