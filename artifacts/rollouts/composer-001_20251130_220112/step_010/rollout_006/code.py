
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
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=90, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=90, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.3125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bar 2: Everyone in. Sax starts motif (1.5 - 3.0s)
# Sax: Fm7 -> Ab7 -> Bb7 -> Eb7 (modeled as melody)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.6875),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=1.6875, end=1.875), # Ab
    pretty_midi.Note(velocity=100, pitch=69, start=1.875, end=2.0),   # Bb
    pretty_midi.Note(velocity=100, pitch=60, start=2.0, end=2.1875),  # Eb
    pretty_midi.Note(velocity=100, pitch=64, start=2.1875, end=2.375),# F
    pretty_midi.Note(velocity=100, pitch=67, start=2.375, end=2.5625),# Ab
    pretty_midi.Note(velocity=100, pitch=69, start=2.5625, end=2.75), # Bb
    pretty_midi.Note(velocity=100, pitch=60, start=2.75, end=3.0),    # Eb
]
sax.notes.extend(sax_notes)

# Bass: Walking line in Fm (chromatic approaches)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=48, start=1.5, end=1.75), # F
    pretty_midi.Note(velocity=80, pitch=49, start=1.75, end=2.0), # F#
    pretty_midi.Note(velocity=80, pitch=47, start=2.0, end=2.25), # E
    pretty_midi.Note(velocity=80, pitch=45, start=2.25, end=2.5), # D
    pretty_midi.Note(velocity=80, pitch=46, start=2.5, end=2.75), # D#
    pretty_midi.Note(velocity=80, pitch=44, start=2.75, end=3.0), # C
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 2: Fm7 on 2 (start=1.75)
    pretty_midi.Note(velocity=90, pitch=48, start=1.75, end=2.0), # F
    pretty_midi.Note(velocity=90, pitch=60, start=1.75, end=2.0), # Eb
    pretty_midi.Note(velocity=90, pitch=59, start=1.75, end=2.0), # D
    pretty_midi.Note(velocity=90, pitch=52, start=1.75, end=2.0), # Ab
    # Bar 3: Ab7 on 2 (start=3.0)
    pretty_midi.Note(velocity=90, pitch=60, start=3.0, end=3.25), # Ab
    pretty_midi.Note(velocity=90, pitch=72, start=3.0, end=3.25), # G
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.25), # Gb
    pretty_midi.Note(velocity=90, pitch=64, start=3.0, end=3.25), # C
    # Bar 4: Bb7 on 2 (start=4.5)
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=4.75), # Bb
    pretty_midi.Note(velocity=90, pitch=74, start=4.5, end=4.75), # A
    pretty_midi.Note(velocity=90, pitch=73, start=4.5, end=4.75), # Ab
    pretty_midi.Note(velocity=90, pitch=65, start=4.5, end=4.75), # D
    # Bar 4: Eb7 on 4 (start=5.25)
    pretty_midi.Note(velocity=90, pitch=60, start=5.25, end=5.5), # Eb
    pretty_midi.Note(velocity=90, pitch=72, start=5.25, end=5.5), # G
    pretty_midi.Note(velocity=90, pitch=71, start=5.25, end=5.5), # Gb
    pretty_midi.Note(velocity=90, pitch=64, start=5.25, end=5.5), # C
]
piano.notes.extend(piano_notes)

# Bar 3: Drums (3.0 - 4.5s)
# Kick on 1 and 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=3.75, end=3.875),
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0),
    # Hihat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=90, pitch=42, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=90, pitch=42, start=3.5625, end=3.75),
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=3.9375),
    pretty_midi.Note(velocity=90, pitch=42, start=3.9375, end=4.125),
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.3125),
    pretty_midi.Note(velocity=90, pitch=42, start=4.3125, end=4.5),
]
drums.notes.extend(drum_notes)

# Bar 4: Drums (4.5 - 6.0s)
# Kick on 1 and 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=5.25, end=5.375),
    pretty_midi.Note(velocity=110, pitch=38, start=6.25, end=6.5),
    # Hihat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.6875),
    pretty_midi.Note(velocity=90, pitch=42, start=4.6875, end=4.875),
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.0625),
    pretty_midi.Note(velocity=90, pitch=42, start=5.0625, end=5.25),
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.4375),
    pretty_midi.Note(velocity=90, pitch=42, start=5.4375, end=5.625),
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=5.8125),
    pretty_midi.Note(velocity=90, pitch=42, start=5.8125, end=6.0),
]
drums.notes.extend(drum_notes)

# Bar 4: Sax ends motif (4.5 - 6.0s)
# Repeat the motif again to close the phrase
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.6875),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=4.6875, end=4.875), # Ab
    pretty_midi.Note(velocity=100, pitch=69, start=4.875, end=5.0),   # Bb
    pretty_midi.Note(velocity=100, pitch=60, start=5.0, end=5.1875),  # Eb
    pretty_midi.Note(velocity=100, pitch=64, start=5.1875, end=5.375),# F
    pretty_midi.Note(velocity=100, pitch=67, start=5.375, end=5.5625),# Ab
    pretty_midi.Note(velocity=100, pitch=69, start=5.5625, end=5.75), # Bb
    pretty_midi.Note(velocity=100, pitch=60, start=5.75, end=6.0),    # Eb
]
sax.notes.extend(sax_notes)

# Bar 4: Bass (4.5 - 6.0s)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=48, start=4.5, end=4.75), # F
    pretty_midi.Note(velocity=80, pitch=49, start=4.75, end=5.0), # F#
    pretty_midi.Note(velocity=80, pitch=47, start=5.0, end=5.25), # E
    pretty_midi.Note(velocity=80, pitch=45, start=5.25, end=5.5), # D
    pretty_midi.Note(velocity=80, pitch=46, start=5.5, end=5.75), # D#
    pretty_midi.Note(velocity=80, pitch=44, start=5.75, end=6.0), # C
]
bass.notes.extend(bass_notes)

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_russo_intro.mid")
