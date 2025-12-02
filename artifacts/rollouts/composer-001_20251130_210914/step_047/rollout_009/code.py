
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# ONLY drums here. No piano, bass, or sax until bar 2.
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.3125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax melody
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.6875),  # F
    pretty_midi.Note(velocity=100, pitch=66, start=1.6875, end=1.875), # A
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.0),   # Bb
    pretty_midi.Note(velocity=100, pitch=62, start=2.0, end=2.1875),  # F
]
sax.notes.extend(sax_notes)

# Bass line (walking)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=48, start=1.5, end=1.6875),  # F
    pretty_midi.Note(velocity=80, pitch=50, start=1.6875, end=1.875), # G
    pretty_midi.Note(velocity=80, pitch=47, start=1.875, end=2.0),   # E
    pretty_midi.Note(velocity=80, pitch=52, start=2.0, end=2.1875),  # A
]
bass.notes.extend(bass_notes)

# Piano chords (7th chords, comp on 2 and 4)
piano_notes = [
    # Bar 2: 2nd beat
    pretty_midi.Note(velocity=90, pitch=62, start=1.875, end=2.0),  # F7
    pretty_midi.Note(velocity=80, pitch=67, start=1.875, end=2.0),
    pretty_midi.Note(velocity=80, pitch=69, start=1.875, end=2.0),
    pretty_midi.Note(velocity=80, pitch=71, start=1.875, end=2.0),
    # Bar 3: 2nd beat
    pretty_midi.Note(velocity=90, pitch=62, start=2.875, end=3.0),
    pretty_midi.Note(velocity=80, pitch=67, start=2.875, end=3.0),
    pretty_midi.Note(velocity=80, pitch=69, start=2.875, end=3.0),
    pretty_midi.Note(velocity=80, pitch=71, start=2.875, end=3.0),
    # Bar 4: 2nd beat
    pretty_midi.Note(velocity=90, pitch=62, start=3.875, end=4.0),
    pretty_midi.Note(velocity=80, pitch=67, start=3.875, end=4.0),
    pretty_midi.Note(velocity=80, pitch=69, start=3.875, end=4.0),
    pretty_midi.Note(velocity=80, pitch=71, start=3.875, end=4.0),
]
piano.notes.extend(piano_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax melody (repeat and resolve)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.1875),  # F
    pretty_midi.Note(velocity=100, pitch=66, start=3.1875, end=3.375), # A
    pretty_midi.Note(velocity=100, pitch=67, start=3.375, end=3.5625), # Bb
    pretty_midi.Note(velocity=100, pitch=62, start=3.5625, end=3.75),  # F
]
sax.notes.extend(sax_notes)

# Bass line (walking)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=62, start=3.0, end=3.1875),  # F
    pretty_midi.Note(velocity=80, pitch=64, start=3.1875, end=3.375), # G
    pretty_midi.Note(velocity=80, pitch=60, start=3.375, end=3.5625), # E
    pretty_midi.Note(velocity=80, pitch=65, start=3.5625, end=3.75),  # A
]
bass.notes.extend(bass_notes)

# Piano chords (7th chords, comp on 2 and 4)
piano_notes = [
    # Bar 3: 2nd beat
    pretty_midi.Note(velocity=90, pitch=62, start=3.875, end=4.0),  # F7
    pretty_midi.Note(velocity=80, pitch=67, start=3.875, end=4.0),
    pretty_midi.Note(velocity=80, pitch=69, start=3.875, end=4.0),
    pretty_midi.Note(velocity=80, pitch=71, start=3.875, end=4.0),
    # Bar 4: 2nd beat
    pretty_midi.Note(velocity=90, pitch=62, start=4.875, end=5.0),
    pretty_midi.Note(velocity=80, pitch=67, start=4.875, end=5.0),
    pretty_midi.Note(velocity=80, pitch=69, start=4.875, end=5.0),
    pretty_midi.Note(velocity=80, pitch=71, start=4.875, end=5.0),
]
piano.notes.extend(piano_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax melody (resolve)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.6875),  # F
    pretty_midi.Note(velocity=100, pitch=66, start=4.6875, end=4.875), # A
    pretty_midi.Note(velocity=100, pitch=67, start=4.875, end=5.0),   # Bb
    pretty_midi.Note(velocity=100, pitch=62, start=5.0, end=5.1875),  # F
]
sax.notes.extend(sax_notes)

# Bass line (walking)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=62, start=4.5, end=4.6875),  # F
    pretty_midi.Note(velocity=80, pitch=64, start=4.6875, end=4.875), # G
    pretty_midi.Note(velocity=80, pitch=60, start=4.875, end=5.0),   # E
    pretty_midi.Note(velocity=80, pitch=65, start=5.0, end=5.1875),  # A
]
bass.notes.extend(bass_notes)

# Piano chords (7th chords, comp on 2 and 4)
piano_notes = [
    # Bar 4: 2nd beat
    pretty_midi.Note(velocity=90, pitch=62, start=5.875, end=6.0),  # F7
    pretty_midi.Note(velocity=80, pitch=67, start=5.875, end=6.0),
    pretty_midi.Note(velocity=80, pitch=69, start=5.875, end=6.0),
    pretty_midi.Note(velocity=80, pitch=71, start=5.875, end=6.0),
]
piano.notes.extend(piano_notes)

# Drums for bars 2-4
# Bar 2: kick=1.5, snare=2.0, hihat every eighth
for i in range(2):
    drum_notes = [
        pretty_midi.Note(velocity=100, pitch=36, start=1.5 + i*1.5, end=1.5 + i*1.5 + 0.375),
        pretty_midi.Note(velocity=110, pitch=38, start=2.0 + i*1.5, end=2.0 + i*1.5 + 0.125),
    ]
    for j in range(8):
        pretty_midi.Note(velocity=80, pitch=42, start=1.5 + i*1.5 + j*0.1875, end=1.5 + i*1.5 + j*0.1875 + 0.1875)
    drums.notes.extend(drum_notes)

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
