
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.375),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),  # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),  # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking bass line in D
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875), # D
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.25), # Eb
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.625), # F
    pretty_midi.Note(velocity=100, pitch=71, start=2.625, end=3.0), # G
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.375), # G#
    pretty_midi.Note(velocity=100, pitch=69, start=3.375, end=3.75), # F
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.125), # Eb
    pretty_midi.Note(velocity=100, pitch=65, start=4.125, end=4.5), # D
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875), # B
    pretty_midi.Note(velocity=100, pitch=64, start=4.875, end=5.25), # C
    pretty_midi.Note(velocity=100, pitch=65, start=5.25, end=5.625), # D
    pretty_midi.Note(velocity=100, pitch=67, start=5.625, end=6.0), # Eb
]
bass.notes.extend(bass_notes)

# Diane: 7th chords comp on 2 and 4
piano_notes = [
    # Bar 2: D7
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875), # D
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=1.875), # G
    pretty_midi.Note(velocity=100, pitch=74, start=1.5, end=1.875), # B
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=1.875), # D
    # Bar 3: D7
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625), # D
    pretty_midi.Note(velocity=100, pitch=72, start=2.25, end=2.625), # G
    pretty_midi.Note(velocity=100, pitch=74, start=2.25, end=2.625), # B
    pretty_midi.Note(velocity=100, pitch=76, start=2.25, end=2.625), # D
    # Bar 4: D7
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375), # D
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.375), # G
    pretty_midi.Note(velocity=100, pitch=74, start=3.0, end=3.375), # B
    pretty_midi.Note(velocity=100, pitch=76, start=3.0, end=3.375), # D
    # Bar 4: D7
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875), # D
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=4.875), # G
    pretty_midi.Note(velocity=100, pitch=74, start=4.5, end=4.875), # B
    pretty_midi.Note(velocity=100, pitch=76, start=4.5, end=4.875), # D
]
piano.notes.extend(piano_notes)

# Dante: Tenor sax melody
sax_notes = [
    # Bar 2: Start the motif
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875), # D
    pretty_midi.Note(velocity=100, pitch=69, start=1.875, end=2.25), # E
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625), # D
    # Bar 3: Build it
    pretty_midi.Note(velocity=100, pitch=71, start=2.625, end=3.0), # G
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.375), # G#
    pretty_midi.Note(velocity=100, pitch=71, start=3.375, end=3.75), # G
    # Bar 4: The cry
    pretty_midi.Note(velocity=100, pitch=69, start=3.75, end=4.125), # E
    pretty_midi.Note(velocity=100, pitch=71, start=4.125, end=4.5), # G
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=4.875), # G#
    pretty_midi.Note(velocity=100, pitch=71, start=4.875, end=5.25), # G
    pretty_midi.Note(velocity=100, pitch=69, start=5.25, end=5.625), # E
    pretty_midi.Note(velocity=100, pitch=67, start=5.625, end=6.0), # D
]
sax.notes.extend(sax_notes)

# Drums for bars 2-4
drum_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.25), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.625), # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.625), # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=2.625, end=3.0),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0),  # Hihat on 4
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.375),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=42, start=3.375, end=3.75), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125), # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=4.125), # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=4.125, end=4.5),  # Hihat on 4
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=4.875),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=42, start=4.875, end=5.25), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625), # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=5.625), # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=6.0),  # Hihat on 4
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("waynes_intro.mid")
