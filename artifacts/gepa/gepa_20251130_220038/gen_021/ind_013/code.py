
import pretty_midi

# Initialize the MIDI file
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Instruments
sax = pretty_midi.Instrument(program=66)       # Tenor sax
bass = pretty_midi.Instrument(program=33)      # Double bass
piano = pretty_midi.Instrument(program=0)      # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Drum notes: kick (36), snare (38), hihat (42)
drums_notes = {
    'kick': 36,
    'snare': 38,
    'hihat': 42
}

# Bar duration in seconds (160 BPM, 4/4 time): 60 / 160 = 0.375s per beat, 1.5s per bar
bar_length = 1.5
beat_length = 0.375

# Bar 1: Drums only (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for i in range(0, int(1.5 / beat_length) + 1):
    if i % 2 == 0:  # Kick on 1 and 3
        note = pretty_midi.Note(velocity=100, pitch=drums_notes['kick'], start=i * beat_length, end=(i + 1) * beat_length)
        drums.notes.append(note)
    if i % 2 == 1:  # Snare on 2 and 4
        note = pretty_midi.Note(velocity=100, pitch=drums_notes['snare'], start=i * beat_length, end=(i + 1) * beat_length)
        drums.notes.append(note)
    # Hihat on every eighth
    note = pretty_midi.Note(velocity=80, pitch=drums_notes['hihat'], start=i * beat_length, end=(i + 1) * beat_length)
    drums.notes.append(note)

# Bar 2 (1.5 - 3.0s): Full quartet
# Bass: Walking line in Dm with chromatic approaches
bass_notes = [
    (pretty_midi.Note(velocity=80, pitch=71, start=1.5, end=1.875)),  # D
    (pretty_midi.Note(velocity=80, pitch=70, start=1.875, end=2.25)),  # C
    (pretty_midi.Note(velocity=80, pitch=69, start=2.25, end=2.625)),  # Bb
    (pretty_midi.Note(velocity=80, pitch=68, start=2.625, end=3.0)),  # A
    (pretty_midi.Note(velocity=80, pitch=67, start=3.0, end=3.375)),  # G
    (pretty_midi.Note(velocity=80, pitch=68, start=3.375, end=3.75)),  # A
    (pretty_midi.Note(velocity=80, pitch=69, start=3.75, end=4.125)),  # Bb
    (pretty_midi.Note(velocity=80, pitch=71, start=4.125, end=4.5)),  # D
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4, comping
piano_notes = [
    # Bar 2: Dm7 (D, F, A, C)
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=90, pitch=64, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.875),  # A
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=1.875),  # C
    # Bar 3: Dm7 (D, F, A, C)
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=90, pitch=64, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.375),  # A
    pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=3.375),  # C
    # Bar 4: Dm7 (D, F, A, C)
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=90, pitch=64, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=4.875),  # A
    pretty_midi.Note(velocity=90, pitch=69, start=4.5, end=4.875),  # C
]
piano.notes.extend(piano_notes)

# Sax: One short motif – start it, leave it hanging, come back
# Dm7 scale: D, Eb, F, G, A, Bb, C, D
# Motif: D, F, A, C (Dm7) — played over 4 eighth notes
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=110, pitch=64, start=1.875, end=2.25),  # F
    pretty_midi.Note(velocity=110, pitch=67, start=2.25, end=2.625),  # A
    pretty_midi.Note(velocity=110, pitch=69, start=2.625, end=3.0),  # C
    pretty_midi.Note(velocity=110, pitch=62, start=3.0, end=3.375),  # D (return)
    pretty_midi.Note(velocity=110, pitch=64, start=3.375, end=3.75),  # F
    pretty_midi.Note(velocity=110, pitch=67, start=3.75, end=4.125),  # A
    pretty_midi.Note(velocity=110, pitch=69, start=4.125, end=4.5),  # C
]
sax.notes.extend(sax_notes)

# Drums for Bars 2-4
# Same pattern: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for i in range(0, int(4.5 / beat_length) + 1):
    if 1.5 <= i * beat_length < 4.5:
        if i % 2 == 0:
            note = pretty_midi.Note(velocity=100, pitch=drums_notes['kick'], start=i * beat_length, end=(i + 1) * beat_length)
            drums.notes.append(note)
        if i % 2 == 1:
            note = pretty_midi.Note(velocity=100, pitch=drums_notes['snare'], start=i * beat_length, end=(i + 1) * beat_length)
            drums.notes.append(note)
        note = pretty_midi.Note(velocity=80, pitch=drums_notes['hihat'], start=i * beat_length, end=(i + 1) * beat_length)
        drums.notes.append(note)

# Add all instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
