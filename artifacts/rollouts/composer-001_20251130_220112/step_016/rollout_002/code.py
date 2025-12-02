
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
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
# Sax: Dm7 motif - D, F, Bb, C, D (one short motif)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.6875),  # D
    pretty_midi.Note(velocity=110, pitch=65, start=1.6875, end=1.875), # F
    pretty_midi.Note(velocity=110, pitch=60, start=1.875, end=2.0625), # Bb
    pretty_midi.Note(velocity=110, pitch=64, start=2.0625, end=2.25), # C
    pretty_midi.Note(velocity=110, pitch=62, start=2.25, end=2.4375), # D
]
sax.notes.extend(sax_notes)

# Bass: Walking line in Dm, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=40, start=1.5, end=1.6875),  # D
    pretty_midi.Note(velocity=80, pitch=41, start=1.6875, end=1.875), # Eb
    pretty_midi.Note(velocity=80, pitch=39, start=1.875, end=2.0625), # C
    pretty_midi.Note(velocity=80, pitch=42, start=2.0625, end=2.25),  # F
    pretty_midi.Note(velocity=80, pitch=40, start=2.25, end=2.4375),  # D
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.6875),  # D
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.6875),  # Bb
    pretty_midi.Note(velocity=90, pitch=70, start=1.5, end=1.6875),  # F
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=1.6875),  # E
    # 2nd beat: comp
    pretty_midi.Note(velocity=80, pitch=62, start=1.875, end=2.0625),  # D
    pretty_midi.Note(velocity=80, pitch=67, start=1.875, end=2.0625),  # Bb
    pretty_midi.Note(velocity=80, pitch=71, start=1.875, end=2.0625),  # G
    pretty_midi.Note(velocity=80, pitch=69, start=1.875, end=2.0625),  # E
    # 4th beat: comp
    pretty_midi.Note(velocity=80, pitch=62, start=2.625, end=2.8125),  # D
    pretty_midi.Note(velocity=80, pitch=67, start=2.625, end=2.8125),  # Bb
    pretty_midi.Note(velocity=80, pitch=71, start=2.625, end=2.8125),  # G
    pretty_midi.Note(velocity=80, pitch=69, start=2.625, end=2.8125),  # E
]
piano.notes.extend(piano_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Drums
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=3.875),
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.0),
    # Hihat
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=3.5625, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=3.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.9375, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.3125, end=4.5),
]
drums.notes.extend(drum_notes)

# Sax: Repeat motif with variation
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=3.0, end=3.1875),  # D
    pretty_midi.Note(velocity=110, pitch=65, start=3.1875, end=3.375), # F
    pretty_midi.Note(velocity=110, pitch=60, start=3.375, end=3.5625), # Bb
    pretty_midi.Note(velocity=110, pitch=64, start=3.5625, end=3.75), # C
    pretty_midi.Note(velocity=110, pitch=62, start=3.75, end=3.9375), # D
    pretty_midi.Note(velocity=110, pitch=65, start=3.9375, end=4.125), # F
    pretty_midi.Note(velocity=110, pitch=60, start=4.125, end=4.3125), # Bb
    pretty_midi.Note(velocity=110, pitch=62, start=4.3125, end=4.5), # D
]
sax.notes.extend(sax_notes)

# Bass: Walking line in Dm, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=40, start=3.0, end=3.1875),  # D
    pretty_midi.Note(velocity=80, pitch=41, start=3.1875, end=3.375), # Eb
    pretty_midi.Note(velocity=80, pitch=39, start=3.375, end=3.5625), # C
    pretty_midi.Note(velocity=80, pitch=42, start=3.5625, end=3.75),  # F
    pretty_midi.Note(velocity=80, pitch=40, start=3.75, end=3.9375),  # D
    pretty_midi.Note(velocity=80, pitch=41, start=3.9375, end=4.125), # Eb
    pretty_midi.Note(velocity=80, pitch=39, start=4.125, end=4.3125), # C
    pretty_midi.Note(velocity=80, pitch=42, start=4.3125, end=4.5),  # F
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.1875),  # D
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.1875),  # Bb
    pretty_midi.Note(velocity=90, pitch=70, start=3.0, end=3.1875),  # F
    pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=3.1875),  # E
    # 2nd beat: comp
    pretty_midi.Note(velocity=80, pitch=62, start=3.75, end=3.9375),  # D
    pretty_midi.Note(velocity=80, pitch=67, start=3.75, end=3.9375),  # Bb
    pretty_midi.Note(velocity=80, pitch=71, start=3.75, end=3.9375),  # G
    pretty_midi.Note(velocity=80, pitch=69, start=3.75, end=3.9375),  # E
    # 4th beat: comp
    pretty_midi.Note(velocity=80, pitch=62, start=4.875, end=5.0625),  # D
    pretty_midi.Note(velocity=80, pitch=67, start=4.875, end=5.0625),  # Bb
    pretty_midi.Note(velocity=80, pitch=71, start=4.875, end=5.0625),  # G
    pretty_midi.Note(velocity=80, pitch=69, start=4.875, end=5.0625),  # E
]
piano.notes.extend(piano_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Drums
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.375),
    pretty_midi.Note(velocity=100, pitch=38, start=6.375, end=6.5),
    # Hihat
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.6875, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.0625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.0625, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.4375),
    pretty_midi.Note(velocity=80, pitch=42, start=5.4375, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=5.8125),
    pretty_midi.Note(velocity=80, pitch=42, start=5.8125, end=6.0),
]
drums.notes.extend(drum_notes)

# Sax: Complete the motif, leave it hanging
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.6875),  # D
    pretty_midi.Note(velocity=110, pitch=65, start=4.6875, end=4.875), # F
    pretty_midi.Note(velocity=110, pitch=60, start=4.875, end=5.0625), # Bb
    pretty_midi.Note(velocity=110, pitch=64, start=5.0625, end=5.25), # C
    pretty_midi.Note(velocity=110, pitch=62, start=5.25, end=5.4375), # D
    pretty_midi.Note(velocity=110, pitch=65, start=5.4375, end=5.625), # F
    pretty_midi.Note(velocity=110, pitch=60, start=5.625, end=5.8125), # Bb
    pretty_midi.Note(velocity=110, pitch=62, start=5.8125, end=6.0), # D
]
sax.notes.extend(sax_notes)

# Bass: Walking line in Dm, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=40, start=4.5, end=4.6875),  # D
    pretty_midi.Note(velocity=80, pitch=41, start=4.6875, end=4.875), # Eb
    pretty_midi.Note(velocity=80, pitch=39, start=4.875, end=5.0625), # C
    pretty_midi.Note(velocity=80, pitch=42, start=5.0625, end=5.25),  # F
    pretty_midi.Note(velocity=80, pitch=40, start=5.25, end=5.4375),  # D
    pretty_midi.Note(velocity=80, pitch=41, start=5.4375, end=5.625), # Eb
    pretty_midi.Note(velocity=80, pitch=39, start=5.625, end=5.8125), # C
    pretty_midi.Note(velocity=80, pitch=42, start=5.8125, end=6.0),  # F
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=4.6875),  # D
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=4.6875),  # Bb
    pretty_midi.Note(velocity=90, pitch=70, start=4.5, end=4.6875),  # F
    pretty_midi.Note(velocity=90, pitch=69, start=4.5, end=4.6875),  # E
    # 2nd beat: comp
    pretty_midi.Note(velocity=80, pitch=62, start=5.25, end=5.4375),  # D
    pretty_midi.Note(velocity=80, pitch=67, start=5.25, end=5.4375),  # Bb
    pretty_midi.Note(velocity=80, pitch=71, start=5.25, end=5.4375),  # G
    pretty_midi.Note(velocity=80, pitch=69, start=5.25, end=5.4375),  # E
    # 4th beat: comp
    pretty_midi.Note(velocity=80, pitch=62, start=6.375, end=6.5625),  # D
    pretty_midi.Note(velocity=80, pitch=67, start=6.375, end=6.5625),  # Bb
    pretty_midi.Note(velocity=80, pitch=71, start=6.375, end=6.5625),  # G
    pretty_midi.Note(velocity=80, pitch=69, start=6.375, end=6.5625),  # E
]
piano.notes.extend(piano_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write('dante_intro.mid')
